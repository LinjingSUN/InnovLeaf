import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'


// import store - pinia
import { createPinia } from 'pinia'

// import router
import router from './router/router'

// import elment-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'


// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}


<<<<<<< HEAD
app.config.globalProperties.$http = axios
axios.defaults.baseURL = 'http://127.0.0.1:5000/'

axios.interceptors.request.use(
  config => {
    if (sessionStorage.getItem('token')) {
      config.headers.token = sessionStorage.getItem('token')
    }
    return config
  }
)


=======
>>>>>>> fc9ac2973cd0b8e79b2808ce97897e121f36e5a4
import './global.css'
createApp(App).use(router).use(createPinia()).use(ElementPlus).use(vuetify).mount('#app')