// src/router.js
import HelloWorld from '@/components/HelloWorld.vue'
import UserSetting from '@/views/SettingPage.vue'
import StoryPreview from '@/views/StoryPreviewPage.vue'
import { createRouter, createWebHistory } from 'vue-router'


// define your routes here
const routes = [
    { 
        path: '/', 
        name: 'index', 
        component: HelloWorld
    }, {
        path: '/setting',
        name: 'UserSetting',
        component: UserSetting
    }, {
        path: '/history',
        name: 'StoryPreview',
        component: StoryPreview
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router