<template>

  <b-card-body class="h-100">
        <div class="container h-100">'

        <div class="row h-100 justify-content-center align-items-center">
        <div class="col-sm-12 col-md-5 col-lg-5 pt-2 pl-5 pr-5 pb-5" id="auth-container">
        <h1 style="text-align: center">SignUp</h1>
        <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-body">
              <form @submit="onSubmit">

                <div class="form-group row">
                  <label for="username" class="col-lg-3 col-form-label">Username</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="text" placeholder="Introduce username" name="username" class="form-control" v-model.trim="form.username" minlength="8" maxlength="20" required>
                  </div>
                </div>


                <div class="form-group row">
                  <label for="first_name" class="col-lg-3 col-form-label">First Name</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="text" placeholder="Introduce first name" name="first_name" class="form-control" v-model.trim="form.first_name" minlength="2" maxlength="20">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="title" class="col-lg-3 col-form-label">Last Name</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="text" placeholder="Introduce last name" name="last_name" class="form-control" v-model.trim="form.last_name" minlength="2" maxlength="20">
                  </div>
                </div>


                <div class="form-group row">
                  <label for="title" class="col-lg-3 col-form-label">Email</label>
                  <div class="pt-10 pb-3 col-sm-6">
                    <input type="email" placeholder="Introduce last name" name="email" class="form-control" v-model.trim="form.email" minlength="4" maxlength="50">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="phone_number" class="col-lg-3 col-form-label">Phone Number</label>
                  <div class="pt-10 pb-3 col-lg-6">
                    <input type="text" placeholder="Introduce phone number" name="phone_number" class="form-control" v-model.trim="form.phone_number" minlength="8" maxlength="20">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="password" class="col-lg-3 col-form-label">Password</label>
                  <div class="pt-10 pb-3 col-lg-6">
                    <input type="password" placeholder="Introduce password" name="password" class="form-control" v-model.trim="form.password" minlength="8" maxlength="20">
                  </div>
                </div>


                <div class="form-group row">
                  <label for="password_confirmation" class="col-lg-3 col-form-label">Confirmation</label>
                  <div class="pt-10 pb-3 col-lg-6">
                    <input type="password" placeholder="Introduce confirm your password" name="password_confirmation" class="form-control" v-model.trim="form.password_confirmation">
                  </div>
                </div>

              <button class="btn btn-primary btn-block mt-5" type="submit">Send</button>
              </form>
      </div>
        </div>
          </div>
            </div>
        </div>
        </div>
        </div>
  </b-card-body>
</template>




<script>

  import axios from "axios";
  import swal from "sweetalert";

  export default {
    name: 'CreateUserSignUp',

    data () {
      return {
        form:{
          username: '',
          password: '',
          password_confirmation: '',
          email:'',
          first_name: '',
          last_name: '',
          phone_number: ''

        }
      }
    },

    methods: {
      onSubmit(evt){
        evt.preventDefault()

      console.log(path)
      const path = `http://0.0.0.0:8000/users/signup/`
        console.log(path)
        axios.post(path, this.form).then((response) =>{
          this.form.username = response.data.username
          this.form.password = response.data.password
          this.form.password_confirmation = response.data.password_confirmation
          this.form.first_name = response.data.first_name
          this.form.last_name = response.data.last_name
          this.form.phone_number = response.data.phone_number
          this.form.email = response.data.email
          location.href = '/'

        }).catch((error)=>{
          console.log(error)
          swal({
                icon: 'error',
                title: 'Error',
                text: 'Invalid data to create user',
              })
        })
      },
    },

    created() {
    }
    }
</script>
