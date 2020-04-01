import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm';
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import firebase from "firebase"
Vue.use(BootstrapVue);

import router from "./router"
import VueRouter from "vue-router";

import * as services from "./services/";
Vue.prototype.$services = services;

Vue.config.productionTip = false


Vue.use(VueRouter)

Vue.config.productionTip = false


var firebaseConfig = {
    apiKey: "AIzaSyBKecVZhU97tuwPX4H8CgSYG0o2tYjEpdY",
    authDomain: "gaia-a65ca.firebaseapp.com",
    databaseURL: "https://gaia-a65ca.firebaseio.com",
    projectId: "gaia-a65ca",
    storageBucket: "gaia-a65ca.appspot.com",
    messagingSenderId: "492925154027",
    appId: "1:492925154027:web:c7938a840ed24f6f0844ae",
    measurementId: "G-KZKQ3P0Y26"
  };

  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();


new Vue({
  render: h => h(App),
  router: router
}).$mount('#app')
