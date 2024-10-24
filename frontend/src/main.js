import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createWebHistory, createRouter } from 'vue-router'
import Toast from './components/Toast.vue'

//Import routes
import Home from './views/Home.vue'

const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/about', name: 'about', component: () => import('./views/About.vue') },
    { path: '/contact', name: 'contact', component:  () => import('./views/Contact.vue') },
    { path: '/test', name: 'test', component:  () => import('./components/CameraComponent.vue') },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App)
app.component('Toast', Toast)
app.use(router).mount('#app')
