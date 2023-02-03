<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col">
        <h3>Are you sure you want to delete this user?</h3>
        <p>Username: {{this.element.username}}</p>
      <template>
        <b-button v-on:click="deleteUser" type="submit"variant="danger" size="sm">Delete User</b-button>
      </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import swal from 'sweetalert'
export default {


  data(){
    return {
      userId: this.$route.params.userId,
      element: {
        username: ''
      }
    }
  },

  methods: {
    getUser()
    {
      let user = JSON.parse(localStorage.getItem('user'))
      let token = ''
      let  username = ''
      if(user){
        token = user['token']
        username = user['username']
      }
      const path = `http://0.0.0.0:8000/users/${username}/`
      axios.get(path,{headers: {'Authorization': 'Bearer '+token}}).then((response) => {
        this.element.username = response.data.username
      }).catch(async (error) => {
        console.log(error)
        await swal({
          icon: 'error',
          title: 'Error',
          text: "Something was wrong",
        })
        location.href = '/login'

      })
    },

  deleteUser(){
        let user = JSON.parse(localStorage.getItem('user'))
        let token = ''
        let  username = ''
        if(user){
          token = user['token']
          username = user['username']
        }
        const path = `http://0.0.0.0:8000/users/${username}/`
              axios.delete(path, {headers: {'Authorization': 'Bearer '+token}}).then(async (response) => {
                await swal("User was deleted successfully", "", "success")
                location.href = '/login'
              }).catch((error) => {
          console.log(error)
          swal({
                icon: 'error',
                title: 'Error',
                text: 'Unexpected error deleted user',
              })
      })
      }

  },
  created() {
      this.getUser()
    }
}

</script>
