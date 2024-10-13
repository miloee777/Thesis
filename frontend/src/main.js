import NuadPlaDukInfo from '@/components/NuadPlaDukInfo.vue'
import PhakPodNaInfo from '@/components/PhakPodNaInfo.vue'
import YaKhaoNokInfo from '@/components/YaKhaoNokInfo.vue'
import YaKokSaiInfo from '@/components/YaKokSaiInfo.vue'
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import DetectionPage from './components/DetectionPage.vue'
import HomePage from './components/HomePage.vue'

// กำหนดค่า routes ที่นี่
const routes = [
  { 
    path: '/', 
    name: 'Home', 
    component: HomePage },

  { 
    path: '/detection', 
    name: 'Detection', 
    component: DetectionPage },

  {
    path: '/Nuad-PlaDuk-Info',
    name: 'NuadPlaDukInfo',
    component: NuadPlaDukInfo,
  },

  { path: '/ya-kok-sai-info', 
    name: 'YaKokSaiInfo',
    component: YaKokSaiInfo },

 {  path: '/ya-khao-nok-info',
    name: 'YaKhaoNokInfo', 
    component: YaKhaoNokInfo },

 {  path: '/phak-pod-na-info', 
    name: 'phak-pod-na-info', 
    component: PhakPodNaInfo },
]

// ใช้ค่า routes ในการสร้าง router
const router = createRouter({
  history: createWebHistory(),
  routes
})

// สร้างแอปและใช้ router
createApp(App).use(router).mount('#app')
