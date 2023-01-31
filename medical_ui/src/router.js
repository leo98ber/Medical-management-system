import Vue from "vue";
import VueRouter from 'vue-router'
import HelloWorld from "@/components/HelloWorld.vue";
import ListDoctors from "@/components/Doctors/ListDoctors.vue";

Vue.use(VueRouter)

const routes = [
   {
    path: "/doctors",
    name: "ListDoctors",
    component: ListDoctors
  },
   {
    path: "/",
    name: "HelloWorld",
    component: HelloWorld
  },


];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;