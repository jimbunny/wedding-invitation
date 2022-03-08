import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'home',
    meta: {
      index: 1
    },
    component: () => import(/* webpackChunkName: "home" */ '../views/Home.vue'),
  },
  {
    path: '/works/:id',
    name: 'works',
    meta: {
      index: 1
    },
    component: () => import(/* webpackChunkName: "works" */ '../views/Works.vue'),
  },
  {
    path: '/about',
    name: 'about',
    meta: {
      index: 2
    },
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/404',
    name: '404',
    meta: {
      index: 1
    },
    component: () => import(/* webpackChunkName: "404" */ '../views/404.vue'),
  },
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
