<template>
    <!-- ======= Portfolio Section ======= -->
    <section id="program" class="portfolio">
         <div class="container" data-aos="fade-up">
   
           <div class="section-title">
             <h2>技术实现</h2>
             <p>前端的技术实现</p>
           </div>
   
           <div class="row" data-aos="fade-up" data-aos-delay="100">
             <div class="col-lg-12 d-flex justify-content-center">
               <ul id="portfolio-flters">
                 <li @click="setFilter('*')" :class="{ 'filter-active': currentFilter === '*' }">全部</li>
                 <li @click="setFilter('filter-html')" :class="{ 'filter-active': currentFilter === 'filter-html' }">HTML</li>
                 <li @click="setFilter('filter-css')" :class="{ 'filter-active': currentFilter === 'filter-css' }">CSS</li>
                 <li @click="setFilter('filter-js')" :class="{ 'filter-active': currentFilter === 'filter-js' }">JavaScript</li>
                 <li @click="setFilter('filter-vue')" :class="{ 'filter-active': currentFilter === 'filter-vue' }">Vue</li>
               </ul>
             </div>
           </div>
   
           <div class="row portfolio-container" data-aos="fade-up" data-aos-delay="200">
             <div v-for="(item, index) in filteredItems" :key="index" class="col-lg-4 col-md-6 portfolio-item" :class="item.filter">
               <div class="portfolio-wrap">
                 <img :src="item.imgSrc" class="img-fluid" :alt="item.title">
                 <div class="portfolio-info">
                   <h4>{{ item.title }}</h4>
                   <p>{{ item.subtitle }}</p>
                   <div class="portfolio-links">
                     <a :href="item.imgSrc" data-gallery="portfolioGallery" class="portfolio-lightbox" :title="item.title"><i class="bx bx-plus"></i></a>
                     <a :href="detail+item.detailLink" target="_blank" title="More Details"><i class="bx bx-link"></i></a>
                   </div>
                 </div>
               </div>
             </div>
           </div>
   
         </div>
       </section><!-- End Portfolio Section -->
   </template>
  
  <script>
  export default {
    data() {
      return {
        detail:'detail',
        currentFilter: '*', // 默认显示所有项目
        portfolioItems: [
          { title: "前端", subtitle: "HTML", imgSrc: "/static/assets/img/portfolio/html.png", detailLink: "/html/", filter: "filter-html" },
          { title: "前端", subtitle: "CSS", imgSrc: "/static/assets/img/portfolio/css.png", detailLink: "/css/", filter: "filter-css" },
          { title: "前端", subtitle: "javascript", imgSrc: "/static/assets/img/portfolio/js.png", detailLink: "/js/", filter: "filter-js" },
          { title: "前端", subtitle: "vue", imgSrc: "/static/assets/img/portfolio/vue.png", detailLink: "/vue/", filter: "filter-vue" },
          { title: "前端", subtitle: "nodejs", imgSrc: "/static/assets/img/portfolio/nodejs.png", detailLink: "/nodejs/", filter: "filter-js" },
          { title: "前端样式库", subtitle: "bootstrap", imgSrc: "/static/assets/img/portfolio/bootstrap.png", detailLink: "/bootstrap/", filter: "filter-css" },
          { title: "前端样式库", subtitle: "aos", imgSrc: "/static/assets/img/portfolio/aos.png", detailLink: "/aos/", filter: "filter-js" },

        ]
      };
    },
    computed: {
      filteredItems() {
        if (this.currentFilter === '*') {
          return this.portfolioItems;
        } else {
          return this.portfolioItems.filter(item => item.filter === this.currentFilter);
        }
      }
    },
    methods: {
      setFilter(filter) {
        this.currentFilter = filter;
      }
    }
  };
  </script>
  
  
  
  <style scoped>
 
  </style>
  