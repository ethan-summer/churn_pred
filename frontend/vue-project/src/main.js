// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
// 导入 Bootstrap 和 BootstrapVue CSS 文件（顺序很重要）
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

import router from './router'; // 引入路由配置

createApp(App)
  .use(router) // 使用 router
  .mount('#app');
