<template>
    <div class="container mt-5 justify-content-center align-items-center" >
      <nav aria-label="breadcrumb"style="margin-top: 180px;" >
        <ol class="breadcrumb">
          <li class="breadcrumb-item" ><router-link to="/frontend-implementation">回退</router-link></li>
          <li class="breadcrumb-item active" aria-current="page">{{ techDetail.subtitle || 'Detail' }}</li>
        </ol>
      </nav>
      <div class="row">
        <div class="col-md-6">
          <img :src="techDetail.imgSrc" class="img-fluid" :alt="techDetail.title" />
        </div>
        <div class="col-md-6">
          <h2>{{ techDetail.subtitle }}</h2>
          <p>{{ techDetail.description }}</p>
          <!-- 如果需要"Learn More"按钮，确保链接是有效的 -->
          <!-- <router-link :to="techDetail.detailLink" class="btn btn-primary">Learn More</router-link> -->
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { computed } from 'vue';
  import { useRoute } from 'vue-router';

  export default {
    setup() {
      const route = useRoute();
      const portfolioItems =[
          { title: "后端", subtitle: "django", imgSrc: "/static/assets/img/portfolio/django.png", detailLink: "/django/", filter: "filter-django",description: "Django 是一个开源的 Python Web 框架，旨在提供一个简单、快速开发的平台，使开发者能够轻松构建高效、可扩展的 Web 应用。它采用了 MTV（模型-模板-视图）的设计模式，将数据模型、用户界面和业务逻辑进行了清晰的分离，使得代码结构更加清晰和易于维护。 \nDjango 提供了一整套工具和库，包括 ORM（对象关系映射）、表单处理、认证系统、会话管理等，可以满足大部分 Web 应用的需求。它还自带了一个功能强大的管理后台，可以快速生成管理界面，用于管理应用中的数据模型，极大地简化了管理员的工作。" },
          {
    title: "后端",
    subtitle: "random-forest",
    imgSrc: "/static/assets/img/portfolio/random-forest.png",
    detailLink: "/random-forest/",
    filter: "filter-algor",
    description: "本人实现了随机森林模型的训练和优化过程。首先，它读取了一个CSV文件，对数据进行预处理和准备。然后，通过划分训练集和测试集，使用随机森林模型进行训练。在训练过程中，对每棵树的AUC值进行了计算，并根据阈值筛选出重要的决策树。接着，使用KMeans算法对这些重要的决策树进行聚类，并选择了聚类中心对应的决策树，进一步优化了随机森林模型。最后，使用改进后的模型进行预测，并返回预测结果。"
},

        
{ title: "后端",
subtitle: "logic",
imgSrc: "/static/assets/img/portfolio/logic.png",
detailLink: "/logic/",
filter: "filter-algor",
description: "本人实现了一个逻辑回归模型的训练和测试过程，具体功能包括：实现了逻辑回归的梯度下降算法，包括随机梯度下降和小批量梯度下降。提供了对训练数据和测试数据进行预处理的函数，包括数据加载、缺失值填充和特征标准化等。实现了逻辑回归模型的训练函数，通过梯度下降算法更新模型参数，并保存训练过程中的权重。实现了对测试数据进行预测的函数，加载训练得到的权重，对测试数据进行预测，并返回预测结果。提供了对预测结果进行写回和解码的功能，将预测结果写回到测试数据中并保存，以及解码加密的数据文件。"
},
{ 
  title: "后端", 
  subtitle: "xgboost", 
  imgSrc: "/static/assets/img/portfolio/xgboost.png", 
  detailLink: "/xgboost/", 
  filter: "filter-algor",
  description: "本人使用XGBoost进行二分类任务的训练和测试。主要功能包括：通过 pandas 读取 CSV 文件，填充缺失值，将数据集划分为训练集和测试集。使用 XGBoost 提供的 DMatrix 格式转换训练集和测试集数据。定义了自定义的损失函数 `log_loss_with_penalties` 和评估函数 `custom_eval_metric`，并利用 XGBoost 的 train 函数进行模型训练。在训练过程中，设置了早停策略以避免过拟合。最后，利用训练好的模型进行预测，并将预测结果转换为二分类标签。该代码还包含了计算准确率、F1 分数、绘制 ROC 曲线和输出混淆矩阵等功能，但这些功能目前是被注释掉的。"
},
{
title: "后端",
subtitle: "DES加密",
imgSrc: "/static/assets/img/portfolio/des.png",
detailLink: "/des/",
filter: "filter-algor" ,
description: "这段代码展示了一个简单而有效的数据加密和解密工具。作者使用 Python 编写了 DES 加密算法和相应的加密和解密函数，以及用于处理 CSV 文件的功能。首先定义了一个 DES 加密算法所需的密钥，然后实现了 DES 加密和解密函数，采用了电子密码本（ECB）模式。接着，作者实现了对 CSV 文件中指定列的加密和解密功能，使用了 pandas 库读取和写入 CSV 文件，并结合 DES 加密算法对数据进行加密和解密。最后，通过命令行接口提供了对加密列进行解密的功能。整体来说，这段代码简单易懂，展示了作者在数据加密领域的一些基本技能和实现能力。"
},
       ];

  
      const techDetail = computed(() => {
        const techId = route.path.match(/\/detailBackend\/(.+?)\/?$/)[1];
        console.log(techId);
        const path = route.path;
        return portfolioItems.find(item => item.detailLink.endsWith(`/${techId}/`)) || { title: '', subtitle: '', imgSrc: '' };
      });
  
      return { techDetail };
    }
  };
  </script>
  
  <style scoped>
  /* 你的样式 */
  </style>
  