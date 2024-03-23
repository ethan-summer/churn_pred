<script setup>
import { onMounted } from 'vue';
import AOS from 'aos';
import 'aos/dist/aos.css'; //需要引入 CSS

onMounted(() => {
  AOS.init();
});
</script>


<template>
  <main>
    <div class="container-fluid d-flex flex-column justify-content-center align-items-center" style="min-height: 100vh;">

  <!-- bootstrap流体盒子 -->


    <!-- 中间的文字 -->
  
    <div data-aos="fade-up" data-aos-delay="200" style="margin-top: 30px;">
      <h1 class="title">用户流失分析预测平台</h1>
    </div>

    <!-- 技术卡片 -->
    <div class="tech-cards" data-aos="fade-up" data-aos-delay="400">
      <!-- 示例技术卡片 -->
      <div class="tech-card">Vue.js</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="500">Django</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="600">机器学习</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="700">随机森林算法</div>
      <!-- 添加更多技术卡片 -->
    </div>
     <!-- 技术卡片 -->
     <div class="tech-cards" data-aos="fade-up" data-aos-delay="400">
      <!-- 示例技术卡片 -->
      <div class="tech-card">JavaScript</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="500">css</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="600">逻辑回归</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="700">des加密</div>
      <!-- 添加更多技术卡片 -->
    </div>
    <div class="tech-cards" data-aos="fade-up" data-aos-delay="400">
      <!-- 示例技术卡片 -->
      <div class="tech-card">HTML</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="500">AOS</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="600">bootstrap</div>
      <div class="tech-card" data-aos="fade-up" data-aos-delay="700">Nodejs</div>
      <!-- 添加更多技术卡片 -->
    </div>
  </div>
  </main>
</template>

<style>
/* 小卡片样式 */
.tech-cards {
  
  display: flex;
  justify-content: center;
  gap: 20px; /* 卡片间距 */
  margin-top: 20px; /* 与标题间距 */
}

.tech-card {
  padding: 20px;
  background-color: white;
  border-radius: 40px;
  font-size: 30px;
  /* 卡片样式 */
}
.title{
  background-color: white;
  border-radius: 40px;
  text-align: center;
  font-weight: bolder;
  font-size: 70px;
  padding: 20px;


}



/* 添加以下样式以设置背景图片 */
main {
  background-image: url('/background.png'); /* 假设background.png在public目录根位置 */
  background-size: cover; /* 背景图片覆盖整个元素 */
  background-position: center; /* 背景图片居中显示 */
}


</style>
