import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import store from './store/index'
// import axios from 'axios'
import vuetify from './plugins/vuetify'

// axios.defaults.baseURL = config.BaseURLApi

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App),
  // store
}).$mount('#app')
