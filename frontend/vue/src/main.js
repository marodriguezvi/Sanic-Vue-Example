import Vue from 'vue'
import VueResource from 'vue-resource';
import App from './App.vue'

/* To extend functionality */
Vue.use(VueResource);

/* Define global route */
//Vue.http.options.root = 'http://localhost:8000'

new Vue({
  el: '#app',
  render: h => h(App)
})
