// src/router.js
// import HelloWorld from '@/components/HelloWorld.vue'
import UserSetting from '@/views/SettingPage.vue'
import StoryPreview from '@/views/StoryPreviewPage.vue'
import GeneratePage from '@/views/GeneratePage.vue'
import { createRouter, createWebHistory } from 'vue-router'


// define your routes here
const routes = [
    { 
        path: '/', 
        name: 'index', 
        component: GeneratePage
    }, {
        path: '/setting',
        name: 'UserSetting',
        component: UserSetting
    }, {
        path: '/history',
        name: 'StoryPreview',
        component: StoryPreview
    },
    { 
        path: '/reading', 
        name: 'Reading',
        component: () => import('@/views/ReadingPage.vue')
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router