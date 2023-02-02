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
      let  username = user['username']
      const path = `http://0.0.0.0:8000/users/${username}/`
      axios.get(path).then((response) => {
        this.element.username = response.data.username
      }).catch((error) => {
        console.log(error)
      })
    },

  deleteUser(){
        let user = JSON.parse(localStorage.getItem('user'))
        let  username = user['username']
        const path = `http://0.0.0.0:8000/users/${username}/`
              axios.delete(path).then((response) => {
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
