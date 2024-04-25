import { createApp } from 'vue'
import App from './App.vue'


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


import './global.css'
createApp(App).use(router).use(createPinia()).use(ElementPlus).use(vuetify).mount('#app')