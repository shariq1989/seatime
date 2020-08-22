import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader
import VueApexCharts from 'vue-apexcharts'

Vue.config.productionTip = false
Vue.component('apexchart', VueApexCharts)

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
