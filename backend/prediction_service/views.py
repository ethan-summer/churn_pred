from django.http import HttpResponse
import subprocess
import os
import time
#TODO:这个是所谓的访问localhost:8080/predictss路由下就会直接调用 python ./prediction_service/model/main.py --train_file_path ./prediction_service/model/input/internet_service_churn.csv
# def predict(request):
#     print(f"当前工作目录: {os.getcwd()}")

#     script_path = './prediction_service/model/main.py' #这个是模型预测代码放的位置 因为路径原因 必须这么设置
#     command = f'python {script_path} --train_file_path ./prediction_service/model/input/internet_service_churn.csv'

#     try:
#         print("三模型开始预测")
#         start_time = time.time()  # 记录开始时间

#         # 使用 subprocess.run 执行命令，等待直到命令执行完毕
#         result = subprocess.run(command, shell=True, encoding='utf-8', capture_output=True)

#         end_time = time.time()  # 记录结束时间
#         duration = end_time - start_time  # 计算持续时间
#        #然后手动在前端实现进度条  时间就是这里记录的训练所需要的时间
#         if result.returncode == 0:
#             print(f"Script executed successfully in {duration:.2f} seconds")
#             return HttpResponse(f"Script executed successfully in {duration:.2f} seconds", status=201)
#         else:
#             print(f"Script execution failed after {duration:.2f} seconds")
#             return HttpResponse(f"Script execution failed after {duration:.2f} seconds. Error: {result.stderr}", status=500)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return HttpResponse(f"An error occurred: {e}", status=500)
# #展示图片的视图函数  不用管
from django.http import JsonResponse
import os
from django.conf import settings

def list_images_compare(request):#获取三模型对比
    directory = os.path.join(settings.BASE_DIR, 'prediction_service', 'model', 'model_performance_output')
    base_url = 'http://localhost:8000/images/'  # 注意根据实际部署情况调整这里的URL
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('.png'))]
    
    # 创建完整的URL列表
    image_urls = [base_url + filename for filename in image_files]
    
    return JsonResponse(image_urls, safe=False)


def ends_with_keyword(filename, keyword):
    """
   获取以keyword结尾的文件名
    """
    filename_without_extension = filename.rsplit('.', 1)[0]
    return filename_without_extension.lower().endswith(keyword.lower())
import json
def list_images(request):
    print('获取图片列表')
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # 解析JSON数据
        model = data.get('model')
    else:
        # 如果不是POST请求，可以选择返回一个错误或者一个空列表
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    print(model)
    directory = os.path.join(settings.BASE_DIR, 'prediction_service', 'model', 'model_performance_output')
    base_url = 'http://localhost:8000/images/'  # 注意根据实际部署情况调整这里的URL
    
    # 初始化image_files以避免UnboundLocalError
    image_files = []

    if model in ['LogisticRegression', 'XGBoost', 'RandomForest']:
        image_files = [
            f for f in os.listdir(directory) 
            if os.path.isfile(os.path.join(directory, f)) and ends_with_keyword(f, model)
        ]
    else:
        image_files = ["accuracy.png","combined_roc.png","confusion_matrix.png","f1.png","precision_recall.png"]
    # 创建完整的URL列表
    image_urls = [base_url + filename for filename in image_files]
    print(image_urls)
    return JsonResponse(image_urls, safe=False)

#注释掉路径不对的代码
# def churn_predict_encrypt_for_single_model(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))  # 解析JSON数据
#         key = data.get('key')
#         model = data.get('model')

#     script_path = './prediction_service/model/main.py'
#     command = f'python {script_path} --test_file_path ./prediction_service/model/input_test/churn_test.csv --key {key} --model {model} --encrypt_data'
    
#     base_url = 'http://localhost:8000/encrypt_and_decrypt/'
#     pred_result = base_url  + 'churn_test_encrypt.csv'
    
#     return JsonResponse(pred_result, safe=False)



def predict(request):
    if request.method == 'POST':
        # 从 request.POST 中获取 'key' 和 'model' 字段
        data = json.loads(request.body.decode('utf-8'))
       
        data2 = data.get('model')
        model =data2.get('model')
        key = data2.get('key')
        # 打印获取到的值以确认
        print(f"Model: {model}")
        print(f"Key: {key}")

        # 其他代码不变...

        script_path = './prediction_service/model/main.py'
        # 确保路径是正确的，这里的路径是硬编码的，你可能需要根据实际情况进行修改
        command = f'python {script_path} --test_file_path ./prediction_service/model/input_test/churn_test.csv --key {key} --model {model} --encrypt_data'
        print("开始执行脚本: " + command)

        try:
            print("开始预测")
            start_time = time.time()  # 记录开始时间

            # 使用 subprocess.run 执行命令
            result = subprocess.run(command, shell=True, encoding='utf-8', capture_output=True)

            end_time = time.time()  # 记录结束时间
            duration = end_time - start_time  # 计算持续时间

            if result.returncode == 0:
                print(f"脚本成功执行，耗时 {duration:.2f} 秒")
                return HttpResponse(f"脚本成功执行，耗时 {duration:.2f} 秒", status=201)
            else:
                print(f"脚本执行失败，耗时 {duration:.2f} 秒")
                return HttpResponse(f"脚本执行失败，耗时 {duration:.2f} 秒。错误信息: {result.stderr}", status=500)
        except Exception as e:
            print(f"发生错误：{e}")
            return HttpResponse(f"发生错误：{e}", status=500)

#解密文件
def churn_predict_decrypt(request):
    if request.method == 'POST':
       
        data = json.loads(request.body.decode('utf-8'))
        key = data.get('key')
        print(key)

    script_path = './prediction_service/model/main.py'
    command = f'python {script_path} --encrypt_file_path prediction_service/model/input_test/churn_test_encrypt.csv --key {key}  --decrypt_data'
    print("开始执行脚本: " + command)

    try:
        print("开始解密")
        start_time = time.time()  # 记录开始时间

        # 使用 subprocess.run 执行命令
        result = subprocess.run(command, shell=True, encoding='utf-8', capture_output=True)
        end_time = time.time()  # 记录结束时间
        duration = end_time - start_time  # 计算持续时间

        if result.returncode == 0:
            print(f"脚本成功执行，耗时 {duration:.2f} 秒")
            return HttpResponse(f"脚本成功执行，耗时 {duration:.2f} 秒", status=201)
        else:
            print(f"脚本执行失败，耗时 {duration:.2f} 秒")
            return HttpResponse(f"脚本执行失败，耗时 {duration:.2f} 秒。错误信息: {result.stderr}", status=500)
    except Exception as e:
        print(f"发生错误：{e}")
        return HttpResponse(f"发生错误：{e}", status=500)



 
    
    
    
    
