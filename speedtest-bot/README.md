### Start From Image
* docker pull tlqiao/speedtest_mongodb:v0.1
* docker pull tlqiao/speedtest_bot:v0.1
* docker network create my_network
* docker run --name mongodb -d -p 27017:27017 --network my_network tlqiao/speedtest_mongodb:v0.1
* docker run --name speedtest_bot -d -p 7860:7860 --network my_network -e OPENAI_API_KEY="your own openai api key" OPENAI_BASE_URL="openai base url"  tlqiao/speedtest_bot:v0.1
* visit it with address "http://localhost:7860/"


### Start From local
* Install python 
* Install dependencies.  execute command  "pip install -r requirements.txt"

##### Set openai api key
* Register chatgpt account and get openai api key
* Set Env, Env varible name is "OPENAI_API_KEY"
* Set Env, Env variable name is "OPENAI_BASE_URL"


#### 使用国内大模型编写测试用例
* 如果要使用国内模型编写测试用例，目前工具支持moonshot和zhipu，需要在环境变量中设置如下环境变量：
* Set Env, Env varible name is "MOONSHOT_API_KEY"
* Set Env, Env variable name is "MOONSHOT_BASE_URL"
* Set Env, Env variable name is "ZHIPU_API_KEY"

##### Init Database
* Install mongodb
* create database "speedtest"

##### Start frontend app from source code
* python ./app.py

##### Start backend server from source code
python ./server.py

### APP page 
![image](https://github.com/SpeedTest-AI/speedtest-bot/blob/main/static/home.png)

### How to use the tool to improve test efficiency, see the [video](https://www.bilibili.com/video/BV1zC4y1i7VG/)
* you can use test data in verifydata folder to try the tool