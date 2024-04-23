import { createApp } from 'vue'
import App from './App.vue'

// import router
import router from './router/router'

// import elment-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

import './global.css'
createApp(App).use(router).use(ElementPlus).mount('#app')