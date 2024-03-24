from django.http import HttpResponse
import subprocess
import os
import time
#TODO:这个是所谓的访问localhost:8080/predictss路由下就会直接调用 python ./prediction_service/model/main.py --train_file_path ./prediction_service/model/input/internet_service_churn.csv
def predict(request):
    print(f"当前工作目录: {os.getcwd()}")

    script_path = './prediction_service/model/main.py' #这个是模型预测代码放的位置 因为路径原因 必须这么设置
    command = f'python {script_path} --train_file_path ./prediction_service/model/input/internet_service_churn.csv'

    try:
        print("三模型开始预测")
        start_time = time.time()  # 记录开始时间

        # 使用 subprocess.run 执行命令，等待直到命令执行完毕
        result = subprocess.run(command, shell=True, encoding='utf-8', capture_output=True)

        end_time = time.time()  # 记录结束时间
        duration = end_time - start_time  # 计算持续时间
       #然后手动在前端实现进度条  时间就是这里记录的训练所需要的时间
        if result.returncode == 0:
            print(f"Script executed successfully in {duration:.2f} seconds")
            return HttpResponse(f"Script executed successfully in {duration:.2f} seconds", status=201)
        else:
            print(f"Script execution failed after {duration:.2f} seconds")
            return HttpResponse(f"Script execution failed after {duration:.2f} seconds. Error: {result.stderr}", status=500)
    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponse(f"An error occurred: {e}", status=500)
#展示图片的视图函数  不用管
from django.http import JsonResponse
import os
from django.conf import settings

def list_images(request):
    directory = os.path.join(settings.BASE_DIR, 'prediction_service', 'model', 'model_performance_output')
    base_url = 'http://localhost:8000/images/'  # 注意根据实际部署情况调整这里的URL
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('.png'))]
    
    # 创建完整的URL列表
    image_urls = [base_url + filename for filename in image_files]
    
    return JsonResponse(image_urls, safe=False)


def list_images_for_single_model(request):
    if request.method == 'POST':
        model = request.POST.get('model')
    
    directory = os.path.join(settings.BASE_DIR, 'prediction_service', 'model', 'model_performance_output')
    base_url = 'http://localhost:8000/images_model/'  # 注意根据实际部署情况调整这里的URL
    if model == 'LogisticRegression':
        image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('LogisticRegression.png'))]
    if model == 'XGBoost':
        image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('XGBoost.png'))]
    if model == 'RandomForest':
        image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(('RandomForest.png'))]
    
    # 创建完整的URL列表
    image_urls = [base_url + filename for filename in image_files]
    
    return JsonResponse(image_urls, safe=False)


def churn_predict_encrypt_for_single_model(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        model = request.POST.get('model')

    script_path = './prediction_service/model/main.py'
    command = f'python {script_path} --test_file_path ./prediction_service/model/input_test/churn_test.csv --key {key} --model {model} --encrypt_data'
    
    base_url = 'http://localhost:8000/encrypt_and_decrypt/'
    pred_result = base_url  + 'churn_test_encrypt.csv'
    
    return JsonResponse(pred_result, safe=False)

def churn_predict_decrypt(request):
    if request.method == 'POST':
        key = request.POST.get('key')

    script_path = './prediction_service/model/main.py'
    command = f'python {script_path} --encrypt_file_path ./prediction_service/model/input_test/churn_test_encrypt.csv --key {key}  --decrypt_data'
    
    base_url = 'http://localhost:8000/encrypt_and_decrypt/'
    pred_result = base_url  + 'churn_test_encrypt_to_encrypt.csv'
    
    return JsonResponse(pred_result, safe=False)



 
    
    
    
    
