<template>
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <h2>Edit User</h2>
      </div>
    </div>
      <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-body">
              <form @onSubmit="onSubmit">

                <div class="form-group row">
                  <label for="first_name" class="col-sm-2 col-form-label">First Name</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Introduce first name" name="first_name" class="form-control">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="title" class="col-sm-2 col-form-label">Last Name</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Introduce last name" name="last_name" class="form-control">
                  </div>
                </div>


                <div class="form-group row">
                  <label for="title" class="col-sm-2 col-form-label">Email</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Introduce last name" name="last_name" class="form-control">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="phone_number" class="col-sm-2 col-form-label">Phone Number</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Introduce phone number" name="phone_number" class="form-control">
                  </div>
                </div>

                <div class="rows">
                  <div class="col text-left">
                    <b-button type="submit" variant="primary">Edit</b-button>
                    <b-button type="submit" class="btn-large-space" :to="{name:'ListDoctors'}">Cancel</b-button>
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
  // import axios from 'axios'
  export default {
    name: 'EditUsers',

    // methods: {
    //   getDoctors(){
    //     let url = 'http://0.0.0.0:8000/users/'
    //     axios.put(url).then((response) => {
    //       this.items = response.data
    //     }).catch((error)=>{
    //       console.log("ERROR")
    //       console.log(error)
    //     })
    //   }},
    //
    //   created(){
    //     this.getDoctors()
    //   },
    // data () {
    //   return {
    //     perPage: 10,
    //     currentPage: 1,
    //     fields: ['first_name', 'last_name', 'major', 'center', 'availability'],
    //       // { key: 'first_name', label: 'Name' },
    //
    //     items: [
    //   ]
    //   }
    // },
    // computed: {
    //   rows() {
    //     return this.items.length
    //   }
    // }
    }
</script>
