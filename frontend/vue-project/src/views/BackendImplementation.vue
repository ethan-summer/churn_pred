<template>
    <!-- ======= Portfolio Section ======= -->
    <section id="program" class="portfolio">
         <div class="container" data-aos="fade-up">
   
           <div class="section-title">
             <h2>技术实现</h2>
             <p>后端的技术实现</p>
           </div>
   
           <div class="row" data-aos="fade-up" data-aos-delay="100">
             <div class="col-lg-12 d-flex justify-content-center">
               <ul id="portfolio-flters">
                 <li @click="setFilter('*')" :class="{ 'filter-active': currentFilter === '*' }">全部</li>
                 <li @click="setFilter('filter-django')" :class="{ 'filter-active': currentFilter === 'filter-django' }">Django</li>
                 <li @click="setFilter('filter-algor')" :class="{ 'filter-active': currentFilter === 'filter-algor' }">算法</li>
       

               </ul>
             </div>
           </div>
   
           <div class="row portfolio-container" data-aos="fade-up" data-aos-delay="200">
             <div v-for="(item, index) in filteredItems" :key="index" class="col-lg-4 col-md-6 portfolio-item" :class="item.filter">
               <div class="portfolio-wrap">
                 <img :src="item.imgSrc"  class="img-fluid"  :alt="item.title">
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
        detail:'detailBackend',
        currentFilter: '*', // 默认显示所有项目
        portfolioItems: [
          { title: "后端", subtitle: "django", imgSrc: "/static/assets/img/portfolio/django.png", detailLink: "/django/", filter: "filter-django" },
          { title: "后端", subtitle: "random-forest", imgSrc: "/static/assets/img/portfolio/random-forest.png", detailLink: "/random-forest/", filter: "filter-algor" },
          { title: "后端", subtitle: "logic", imgSrc: "/static/assets/img/portfolio/logic.png", detailLink: "/logic/", filter: "filter-algor" },
          { title: "后端", subtitle: "xgboost", imgSrc: "/static/assets/img/portfolio/xgboost.png", detailLink: "/xgboost/", filter: "filter-algor" },
          { title: "后端", subtitle: "EDS加密", imgSrc: "/static/assets/img/portfolio/des.png", detailLink: "/des/", filter: "filter-algor" },
      

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
  