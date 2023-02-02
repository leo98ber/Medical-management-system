
<template>

    <div class="container h-100">
      <div class="row h-100 justify-content-center align-items-center">
        <div class="col-sm-12 col-md-5 col-lg-5 pt-2 pl-5 pr-5 pb-5" id="auth-container">
          <h1 style="text-align: center">Login</h1>


      <form @submit="onSubmit">
        <div class="row">
        <div class="col">
          <div class="card">
            <b-card-body>
                <div class="form-group row">
                  <label for="email" class="col-lg-3 col-form-label">Email</label>
                  <div class="pt-1 pb-3 col-sm-6">
                    <input type="text" placeholder="Introduce email" name="email" class="form-control" v-model.trim="form.email">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="title" class="col-lg-3 col-form-label">Password</label>
                  <div class="pt-10 pb-3 col-lg-6">
                    <input type="text" placeholder="Introduce password" name="password" class="form-control" v-model.trim="form.password">
                  </div>
                </div>
              <button class="btn btn-primary btn-block mt-5" type="submit">Register</button>
        </b-card-body>
        </div>
          </div>
            </div>

    </form>
           <form method="GET" action="/signup">
              <button :to="{name:'CreateUserSignUp'}" class="btn btn-secondary btn-secondary btn-block mt-3" type="submit">Signup</button>
          </form>
    </div>
      </div>
        </div>





</template>

<script>
  // import axios from 'axios'
  import axios from "axios";
  import swal from "sweetalert";

  export default {
    data () {
      return {
        form:{
          email: '',
          password: '',

        }
      }
    },

    methods: {
      onSubmit(evt){
        evt.preventDefault()

      const path = `http://0.0.0.0:8000/users/login/`
        axios.post(path, this.form).then((response) =>{
          this.form.email = response.data.email
          this.form.password = response.data.password
          console.log(response.data)
          localStorage.setItem('user', JSON.stringify(response.data))

          location.href = '/'

        }).catch((error)=>{
          console.log(error)
          swal({
                icon: 'error',
                title: 'Error',
                text: 'Invalid username or password',
              })
        })
      },
    },

    created() {
    }
    }
</script>
