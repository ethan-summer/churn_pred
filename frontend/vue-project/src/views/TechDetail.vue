<template>
    <div class="container mt-5 justify-content-center align-items-center" >
      <nav aria-label="breadcrumb"style="margin-top: 180px;" >
        <ol class="breadcrumb">
          <li class="breadcrumb-item" ><router-link to="/frontend-implementation">回退</router-link></li>
          <li class="breadcrumb-item active" aria-current="page">{{ techDetail2.subtitle || 'Detail' }}</li>
        </ol>
      </nav>
      <div class="row">
        <div class="col-md-6">
          <img :src="techDetail2.imgSrc" class="img-fluid" :alt="techDetail2.title" />
        </div>
        <div class="col-md-6">
          <h2>{{ techDetail2.subtitle }}</h2>
          <p>{{ techDetail2.description }}</p>
          <!-- 如果需要"Learn More"按钮，确保链接是有效的 -->
          <!-- <router-link :to="techDetail2.detailLink" class="btn btn-primary">Learn More</router-link> -->
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { computed } from 'vue';
  import { useRoute } from 'vue-router';

  export default {
    setup() {
      const route2 = useRoute();
      const portfolioItems2 =[
  {
    "title": "前端",
    "subtitle": "HTML介绍",
    "imgSrc": "/static/assets/img/portfolio/html.png",
    "detailLink": "/html/",
    "filter": "filter-html",
    "description": "HTML（Hypertext Markup Language）是一种用于构建网页和网络应用程序的基础性语言。它提供了网页内容的结构化描述，通过使用标签（tags）定义不同的元素，如文本、图像、链接等。这些标签能够指示浏览器如何展示页面内容以及如何与用户交互。HTML是一种基于标记的语言，这意味着它使用起来相对简单，并且具有广泛的应用范围。"
  },
  {
    "title": "前端",
    "subtitle": "CSS",
    "imgSrc": "/static/assets/img/portfolio/css.png",
    "detailLink": "/css/",
    "filter": "filter-css",
    "description": "CSS（Cascading Style Sheets，层叠样式表）是一种用于定义HTML元素外观和布局的样式语言。它为开发人员提供了丰富的控制能力，使他们能够改变网页的外观，包括颜色、字体、间距、尺寸和动画等方面，从而增强用户体验和网页的可视吸引力。\nCSS的工作原理是通过将样式规则应用于HTML元素，以改变它们的外观和布局。样式规则通常由一个选择器和一组声明组成。选择器用于指定要应用样式的HTML元素，而声明则定义了要应用的具体样式属性及其值。例如，可以通过以下CSS规则将段落文本颜色设置为红色："
  },
  {
    "title": "前端",
    "subtitle": "javascript",
    "imgSrc": "/static/assets/img/portfolio/js.png",
    "detailLink": "/js/",
    "filter": "filter-js",
    "description": "JavaScript 是一种高级的、解释型的编程语言，广泛用于网页开发中。作为网页交互的关键，JavaScript 能够在用户浏览器上实现各种复杂的特性，包括但不限于动态内容更新、表单验证、交互式地图、动画效果、游戏开发以及与服务器的异步通信等。\nJavaScript 最初设计用于在网页中添加简单的交互功能，例如验证表单输入或创建简单的动画效果。随着技术的发展和浏览器性能的提升，JavaScript 的功能也不断扩展和增强。现在，它已经成为了一种强大而多才多艺的编程语言，可以实现几乎任何在浏览器中需要的功能。"
  },
  {
    "title": "前端",
    "subtitle": "vue",
    "imgSrc": "/static/assets/img/portfolio/vue.png",
    "detailLink": "/vue/",
    "filter": "filter-vue",
    "description": "Vue.js 是一个渐进式JavaScript框架，专注于构建用户界面。它的设计理念是渐进式的，意味着你可以逐步地将它应用到项目中，无论是小型的交互组件还是大型的单页面应用（SPA）。\nVue.js 的易用性是它备受欢迎的主要原因之一。它的API直观、简洁，使得开发者能够迅速上手并高效开发。与此同时，Vue.js 也提供了丰富的功能，包括数据绑定、组件化、路由管理、状态管理等，为构建复杂的交互式界面提供了便利。"
  },
  {
    "title": "前端",
    "subtitle": "nodejs",
    "imgSrc": "/static/assets/img/portfolio/nodejs.png",
    "detailLink": "/nodejs/",
    "filter": "filter-js",
    "description": "Node.js 是一款强大的开源、跨平台的 JavaScript 运行时环境，它的出现彻底改变了 JavaScript 的应用范围。传统上，JavaScript 主要用于网页前端开发，但随着 Node.js 的兴起，开发者们可以将 JavaScript 应用于服务器端编程，实现了前后端统一的 JavaScript 开发模式。 \nNode.js 的核心是基于 Chrome V8 引擎构建的 JavaScript 运行时环境，它提供了丰富的库和模块，使得开发者能够轻松进行文件操作、网络请求、数据库访问等各种后端功能。Node.js 的事件驱动和非阻塞 I/O 的特性使得它非常适合处理高并发的网络应用，如 Web 服务器、实时通信应用、API 服务等。"
  },
  {
    "title": "前端样式库",
    "subtitle": "bootstrap",
    "imgSrc": "/static/assets/img/portfolio/bootstrap.png",
    "detailLink": "/bootstrap/",
    "filter": "filter-css",
    "description": "Bootstrap 是一个流行的开源前端框架，旨在帮助开发者快速构建现代化、响应式的网页和网络应用。该框架提供了一整套设计好的HTML、CSS和JavaScript组件，涵盖了网页开发中常见的各种需求，包括导航栏、按钮、表单、模态框等。\n通过使用Bootstrap，开发者可以轻松地创建具有一致性和美观性的用户界面，无需从头编写大量的样式和布局代码。Bootstrap 提供了一套现成的样式和组件，具有良好的可定制性，开发者可以根据项目需求进行自定义和扩展。"
  },
  {
    "title": "前端样式库",
    "subtitle": "aos",
    "imgSrc": "/static/assets/img/portfolio/aos.png",
    "detailLink": "/aos/",
    "filter": "filter-js",
    "description": "AOS（Animate On Scroll）是一个轻量级的JavaScript库，专门用于在滚动时添加滚动动画效果。通过使用AOS，开发者可以轻松地为网页元素添加在滚动至视图区域时出现的动画效果，从而增强用户体验和界面的互动性。/n这个库的工作原理很简单：当用户滚动页面时，AOS会监测每个元素是否进入了浏览器窗口的可视区域。一旦元素进入可视区域，AOS会根据预先设定的动画效果，对该元素进行相应的动画处理，例如淡入、滑入、旋转等。"
  }
];

  
      const techDetail2 = computed(() => {
        const techId = route2.path.match(/\/detail\/(.+?)\/?$/)[1];
        console.log(techId);
        const path2 = route2.path;
        return portfolioItems2.find(item => item.detailLink.endsWith(`/${techId}/`)) || { title: '', subtitle: '', imgSrc: '' };
      });
  
      return { techDetail2 };
    }
  };
  </script>
  
  <style scoped>
  /* 你的样式 */
  </style>
  