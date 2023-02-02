<template>
    <div class="container mt-5">
      <div>
        <b-navbar class="fixed-top navbar-expand-lg" toggleable="lg" type="dark" variant="info">
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <b-collapse id="nav-collapse" is-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
              <b-nav-item-dropdown right>
                <!-- Using 'button-content' slot -->
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
          <h2>List Doctors
            <div class="overflow-auto">
              <div class="col-md-12">
                <b-table stripped hover
                         :items="items" :fields="fields"
                         :per-page="perPage"
                         :current-page="currentPage"
                         small>
                </b-table>
              </div>
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="my-table"
                ></b-pagination>
                <p class="mt-3">Current Page: {{ currentPage }}</p>
              </div>
          </h2>
      </div>
    </div>
  </div>
</template>


<script>
  import axios from 'axios'
  export default {
    name: 'ListDoctors',

    methods: {
      getDoctors(){
        console.log("AXIOS")
        let url = 'http://0.0.0.0:8000/doctors/'
        axios.get(url).then((response) => {
          console.log("backend connection")
          console.log(response.data)
          this.items = response.data
        }).catch((error)=>{
          console.log("ERROR")
          console.log(error)
        })
      }},

      created(){
        this.getDoctors()
      },
    data () {
      return {
        perPage: 10,
        currentPage: 1,
        fields: ['first_name', 'last_name', 'major', 'center', 'availability'],
          // { key: 'first_name', label: 'Name' },

        items: [
      ]
      }
    },
    computed: {
      rows() {
        return this.items.length
      }
    }
    }
</script>

<style>

</style>
