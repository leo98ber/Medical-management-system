import Vue from 'vue'
import Router from 'vue-router'
import ListDoctors from '@/components/Doctors/ListDoctors.vue';
import EditUser from "../components/Users/EditUser.vue";
import DeleteUser from "../components/Users/DeleteUser.vue";
import CreateUserSignUp from "../components/Users/CreateUserSignUp.vue";
import Login from "../components/Users/Login.vue";



Vue.use(Router)

export default new Router(

  {
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'ListDoctors',
      component: ListDoctors
    },
    {
      path: '/users/edit',
      name: 'EditUser',
      component: EditUser
    },
    {
      path: '/users/delete',
      name: 'DeleteUser',
      component: DeleteUser
    },
    {
      path: '/signup',
      name: 'CreateUserSignUp',
      component: CreateUserSignUp
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },

  ]
})
