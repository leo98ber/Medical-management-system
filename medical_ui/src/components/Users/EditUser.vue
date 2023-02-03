<template>
  <div class="container">
      <div>
        <b-navbar class="fixed-top navbar-expand-lg" toggleable="lg" type="dark" variant="info">
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <b-collapse id="nav-collapse" is-nav>

            <b-navbar-nav class="ml-auto">
              <b-nav-item-dropdown right>
                <template #button-content>
                  <em>User</em>
                </template>
                <b-dropdown-item :to="{name:'EditUser'}">Profile</b-dropdown-item>
                <b-dropdown-item :to="{name:'Login'}">Sign Out</b-dropdown-item>
              </b-nav-item-dropdown>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
      </div>

    <div class="row">
      <div class="col text-left">
        <h2 class="col-6 pt-3 pb-3">Edit User</h2>
      </div>
    </div>
      <div class="row">
        <div class="col">
          <div class="card">
            <template>
              <b-button :to="{name:'DeleteUser'}" type="submit" class="col-md-2 offset-md-10" variant="danger" size="sm">Delete User</b-button>
            </template>

            <div class="card-body">
              <form @submit="onSubmit">
                <div class="form-group row">
                  <label for="username" class="col-sm-2 col-form-label">Username</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="text" placeholder="Introduce username" name="phone_number" class="form-control" v-model.trim="form.username" minlength="8" maxlength="20" readonly>
                  </div>
                </div>


                <div class="form-group row">
                  <label for="first_name" class="col-sm-2 col-form-label">First Name</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="text" placeholder="Introduce first name" name="first_name" class="form-control" v-model.trim="form.first_name" minlength="2" maxlength="20">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="title" class="col-sm-2 col-form-label">Last Name</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="text" placeholder="Introduce last name" name="last_name" class="form-control" v-model.trim="form.last_name" minlength="2" maxlength="20">
                  </div>
                </div>


                <div class="form-group row">
                  <label for="title" class="col-sm-2 col-form-label">Email</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="email" placeholder="Introduce email" name="email" class="form-control" v-model.trim="form.email" readonly minlength="4" maxlength="50">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="phone_number" class="col-sm-2 col-form-label">Phone Number</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="tel" placeholder="Introduce phone number" name="phone_number" class="form-control" v-model.trim="form.phone_number" minlength="8" maxlength="20">
                  </div>
                </div>

                <div class="rows">
                  <div class="col text-left">
                    <b-button type="submit" class="btn-block mt-5" variant="primary">Edit</b-button>
                    <b-button type="submit" class="btn-block mt-5 btn-large-space" :to="{name:'ListDoctors'}">Cancel</b-button>
                  </div>
                </div>

              </form>
      </div>
        </div>
          </div>
            </div>

  </div>
</template>


<script>
  import axios from 'axios'
  import swal from 'sweetalert'
  import DeleteUser from "./DeleteUser.vue";

  export default {
    name: 'EditUsers',
    computed: {
      DeleteUser() {
        return DeleteUser
      }
    },
    data () {
      return {

        form:{
          'first_name':'',
          'last_name':'',
          'email': '',
          'phone_number': ''
        }
      }
    },

    methods: {
      onSubmit(evt){
        evt.preventDefault()


      let user = JSON.parse(localStorage.getItem('user'))
      let token = ''
      let  username = ''
      if(user){
        token = user['token']
        username = user['username']
      }


      const path = `http://0.0.0.0:8000/users/${username}/`
        axios.put(path, this.form, {headers: {'Authorization': 'Bearer '+token}}).then(async (response) => {
          this.form.first_name = response.data.first_name
          this.form.last_name = response.data.last_name
          this.form.phone_number = response.data.phone_number
          this.form.email = response.data.email

          await swal("User changed successfully", "", "success")
          location.href = '/'

        }).catch((error)=>{
          console.log("ERROR")
          console.log(error)})
          swal({
                icon: 'error',
                title: 'Error',
                text: 'Invalid data to update user',
              })
      },
      getUser (){

      let user = JSON.parse(localStorage.getItem('user'))
      let token = ''
      let  username = ''
      if(user){
        token = user['token']
        username = user['username']
      }

      const path = `http://0.0.0.0:8000/users/${username}/`
        axios.get(path, {headers: {'Authorization': 'Bearer '+token}}).then((response) =>{
          this.form.first_name = response.data.first_name
          this.form.last_name = response.data.last_name
          this.form.phone_number = response.data.phone_number
          this.form.email = response.data.email
          this.form.username = response.data.username
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
    },

    created() {
      this.getUser()
    }
    }
</script>
