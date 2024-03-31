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
    description: "定义了一个用于构建和优化随机森林模型的函数 random_forest，该函数过程以数据预处理开始，通过读取CSV文件并填充缺失值。然后对特征和标签进行分离，并划分出训练集和测试集。划分时考虑到标签的平衡，使用了分层采样。在初始化随机森林模型后，函数对其进行训练，并计算每棵树的AUC（曲线下面积）值，以衡量单个决策树在训练集上的性能。之后，函数为不同的阈值设定一个范围，并针对这些阈值使用5折分层交叉验证来细致评估随机森林的性能。对于每个阈值，它计算所有决策树平均概率预测结果的AUC和F1分数，从而评估在该阈值下选出的决策树子集的表现。函数进一步利用最优阈值，选择AUC得分超过该阈值的决策树作为精选子集。接着使用K-Means聚类算法对选出的决策树的特征重要性进行聚类，将决策树划分为若干组，并以每组中心的树作为代表。基于这些代表性决策树，构建了一个新的随机森林模型，再次用全部训练数据进行拟合。最后，使用经过优化的随机森林模型在测试集上进行预测，返回这些预测结果、实际测试标签以及预测概率。整体上，这种方法旨在通过调整决策树的子集和执行聚类分析来提升随机森林模型的性能，从而获得更准确和更具泛化能力的分类器。"
},

        
{ title: "后端",
subtitle: "logic",
imgSrc: "/static/assets/img/portfolio/logic.png",
detailLink: "/logic/",
filter: "filter-algor",
description: "本人实现了一个逻辑回归模型的训练和测试过程，这段代码实现了一个逻辑回归模型，通过使用梯度上升算法与多种高级优化技术相结合来提高其性能和泛化能力。在每次迭代中，它采用小批量梯度上升策略以随机方式选择训练数据的子集，这不仅加速了收敛过程，同时也有助于减少内存消耗并增强模型在未知数据上的表现。算法中还应用了自适应学习率调整机制，使得学习率随迭代次数的增加而逐步减小，从而允许模型在逼近最优解时更细致且稳定地进行参数调整。此外，为了抑制过拟合并鼓励权重值保持在较小水平上，算法引入了L2正则化项，该项通过惩罚大权重值有效地控制了模型复杂度。同时，配合AdaGrad算法的应用，它对每个参数都进行了基于历史梯度信息的自适应学习率更新，确保了各参数更新步长的均衡性，特别是当参数空间存在显著差异时。经过若干迭代后，算法输出了一组经过细致调整的权重，可以直接用于新样本的分类预测。整体而言，这个算法充分考虑了算法的收敛速度、模型的泛化能力和避免过拟合的要求，最终实现了一个健壮且高效的逻辑回归分类器。"
},
{ 
  title: "后端", 
  subtitle: "xgboost", 
  imgSrc: "/static/assets/img/portfolio/xgboost.png", 
  detailLink: "/xgboost/", 
  filter: "filter-algor",
  description: "基于XGBoost算法实现的分类模型，其中融入了自定义损失函数和评估指标，以适应特定的业务需求。为了优化我的模型，我定义了一个自定义的对数损失函数 log_loss_with_penalties，它不仅计算了标准的对数损失来衡量预测值与实际标签之间的差异，还引入了两种不同权重的惩罚系数，分别针对两类不同的分类错误。这样设计的目的是为了使得模型能够更加关注那些对业务冲击较大的错误类型，通过调整这些惩罚系数，我可以使模型在训练过程中对某类错误赋予更高的惩罚，以达到业务上的特殊需求。我利用自定义的损失函数和评估指标来训练XGBoost模型。在模型的训练过程中，我使用了 xgb.train 函数，并设置了早停机制，即如果在连续多轮迭代后模型性能没有显著提升，则停止训练，这有助于避免过拟合并节省计算资源。经过训练，模型保存了最优参数，以便未来对新数据进行预测。"
},
{
title: "后端",
subtitle: "DES加密",
imgSrc: "/static/assets/img/portfolio/des.png",
detailLink: "/des/",
filter: "filter-algor" ,
description: "这段代码展示了一个有效的数据加密和解密工具。作者使用 Python 编写了 DES 加密算法和相应的加密和解密函数，以及用于处理 CSV 文件的功能。首先定义了一个 DES 加密算法所需的密钥，然后实现了 DES 加密和解密函数，采用了电子密码本（ECB）模式。接着，作者实现了对 CSV 文件中指定列的加密和解密功能，使用了 pandas 库读取和写入 CSV 文件，并结合 DES 加密算法对数据进行加密和解密。最后，通过命令行接口提供了对加密列进行解密的功能。整体来说，这段代码简单易懂，展示了作者在数据加密领域的一些基本技能和实现能力。"
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
  