import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/model-introduction',
      name: 'model-introduction',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/services',
      name: 'services',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Services.vue')
    },
    {
      path: '/frontend-implementation',
      name: 'frontend-implementation',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FrontendImplementation.vue')
    },
    {
      path: '/backend-implementation',
      name: 'backend-implementation',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/BackendImplementation.vue')
    },
    {
      path: '/detail/:tech',
      name: 'TechDetail2',
      component: () => import('../views/TechDetail.vue'),
      props: true, // 允许我们将路由参数作为props传递给TechDetail组件
    },
    {
      path: '/detailBackend/:tech',
      name: 'TechDetail',
      component: () => import('../views/TechDetailBackEnd.vue'),
      props: true, // 允许我们将路由参数作为props传递给TechDetail组件
    },
    
  ]
})

export default router
