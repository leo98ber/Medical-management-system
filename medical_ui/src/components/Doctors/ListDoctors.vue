<template>
  <v-container class="px-10 px-md-10 mt-3" fluid>
        <div class="tables-basic mt-3">
<!--    <v-row>-->

      <h2 align="center">Doctors available</h2>
      <v-col cols="12">

            <v-card class="mx-auto mt-5" max-width="10000">
              <v-data-table
                :headers="headers"
                :items="doctors"
                fixed-header
                :items-per-page="10">
              </v-data-table>
            </v-card>
      </v-col>
<!--    </v-row>-->
          </div>
  </v-container>
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
          this.doctors = response.data
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
        doctors: [],
        headers: [

        { text: 'Name', value: 'first_name'},
        { text: 'Last Name', value: 'last_name' },
        {text: 'Major', value: 'major'},
        { text: 'Center', value: 'center' },
        { text: 'Availability', value: 'availability' },
      ]
      }
    },


      // filterOnlyCapsText (value, search) {
      //   return value != null &&
      //     search != null &&
      //     typeof value === 'string' &&
      //     value.toString().toLocaleUpperCase().indexOf(search) !== -1
      // },
    }
</script>

<style>

</style>