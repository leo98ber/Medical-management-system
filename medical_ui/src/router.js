import Vue from "vue";
import VueRouter from 'vue-router'
// import App from './App.vue'
import ListDoctors from "@/components/Doctors/ListDoctors.vue";

Vue.use(VueRouter)

const routes = [
   {
    path: "/doctors",
    name: "ListDoctors",
    component: ListDoctors
  },
  //  {
  //   path: "/",
  //   name: "App",
  //   component: App
  // },


];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;