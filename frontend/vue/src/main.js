import Vue from 'vue'
import VueResource from 'vue-resource';
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faSyncAlt, faBan } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faSyncAlt, faBan)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

/* To extend functionality */
Vue.use(VueResource);

/* Define global route */
//Vue.http.options.root = 'http://localhost:8000'

new Vue({
  el: '#app',
  render: h => h(App)
})
