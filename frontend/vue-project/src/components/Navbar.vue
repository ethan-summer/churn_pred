<script setup>

import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
const route = useRoute();//获取当前路由信息

const navigateTo = (path) => {
  router.push(path);
};
</script>



<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand" href="#"><i class="bi bi-bar-chart-fill"></i>  用户流失分析预测平台</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
  <li class="nav-item">
    <a  :class="route.path === '/' ? 'navlinkActive' : 'nav-link'" href="#" @click.prevent="navigateTo('/')">首页</a>
  </li>
  <li class="nav-item">
    <a  :class="route.path === '/model-introduction' ? 'navlinkActive' : 'nav-link'" href="#" @click.prevent="navigateTo('/model-introduction')">模型评估图展示</a>
  </li>
  <li class="nav-item">
    <a :class="route.path === '/services' ? 'navlinkActive' : 'nav-link'" href="#" @click.prevent="navigateTo('/services')">上传服务</a>
  </li>
  <li class="nav-item">
    <a :class="route.path === '/frontend-implementation' ? 'navlinkActive' : 'nav-link'" href="#" @click.prevent="navigateTo('/frontend-implementation')">前端技术实现</a>
  </li>
  <li class="nav-item">
    <a  :class="route.path === '/backend-implementation' ? 'navlinkActive' : 'nav-link'" href="#" @click.prevent="navigateTo('/backend-implementation')">后端技术实现</a>
  </li>

</ul>

    </div>
  </div>
</nav>
</template>

<style>
 /* Custom CSS for Navbar Items Spacing and Centering */
 .navbar-nav {
      margin: 0 auto;
      display: flex;
      justify-content: center;
      gap: 20px; /* Adjust the gap between nav items here */
    }
    @media (max-width: 992px) { /* Adjust based on your breakpoint */
      .navbar-nav {
        flex-direction: column;
        gap: 10px; /* Smaller gap for vertical nav on smaller screens */
      }
    }
  
  .navlinkActive{
  font-weight: bold;
  font-size: x-large;
  color: black;
  text-decoration: none;
}

</style>
