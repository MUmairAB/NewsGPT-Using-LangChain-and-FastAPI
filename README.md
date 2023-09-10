# NewsGPT Using LangChain and FastAPI

![GitHub stars](https://img.shields.io/github/stars/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI?style=flat-square)
![GitHub forks](https://img.shields.io/github/forks/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI?style=flat-square)

This repository contains an implementation of NewsGPT, a news summarization model, using **LangChain** and **FastAPI**. This model is production-ready and can seamlessly function as a standalone application or be seamlessly integrated into other applications. Through this project, you have the capability to produce concise summaries of news articles, providing you with the primary highlights of each article.

## Table of Contents

- [1. Introduction](#introduction)
- [2. Installation](#installation)
- [3. Usage](#usage)
- [4. API Endpoints](#api-endpoints)
- [5. Screenshots of the Working App](#screenshots)
- [6. License](#license)
- [7. Contributions](#contributions)

## 1. Introduction <a name="introduction"></a>

NewsGPT is a powerful language model that can generate coherent and contextually relevant summaries of news articles. This project leverages LangChain, a state-of-the-art language model, and FastAPI, a modern web framework, to create an API for generating news articles on-the-fly. It employs [BART Large CNN](https://huggingface.co/facebook/bart-large-cnn) model as LLM. Additionally, it extends support for seamless integration with **OpenAI's ChatGPT**.

## 2. Installation <a name="installation"></a>

Before you begin, ensure you have Python 3.9+ installed on your system. You can then set up the project as follows:

#### 2.1 Clone the repository:

   ```bash
   git clone https://github.com/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI.git
   cd NewsGPT-Using-LangChain-and-FastAPI
   ```

#### 2.2 Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

#### 2.3 Replace your own HuggingFace **Access Key** in **secret_key.py** file.

## 3. Usage <a name="usage"></a>
To use NewsGPT, follow these steps:

#### 3.1 Step 1:

If you are running the code in Google Colab, then proceed to the next step. But if you are running the code on your local computer, then make the following changes in **NewsGPT Code** file.

   **A)** Remove the following code from the file.
   ```
   #The following code is necessary to run the FastAPI app in Colab
   # But if you are running it locally, then you can un-comment the following
   app.add_middleware(
       CORSMiddleware,
       allow_origins=['*'],
       allow_credentials=True,
       allow_methods=['*'],
       allow_headers=['*'],
   )
   ```

   **B)** Replace the following code:

   ```
   #Run the FastAPI app on local server
   import nest_asyncio
   from pyngrok import ngrok
   import uvicorn

   ngrok_tunnel = ngrok.connect(8000)
   print('Public URL:', ngrok_tunnel.public_url)
   nest_asyncio.apply()
   uvicorn.run(app, port=8000)
   ```

   with

   ```
   import uvicorn
   uviconr.run(app="NewsGPT Code:app",
               host="127.0.0.1",
               port=8000,
               reload=True)
   ```

#### 3.2 Step 2

**A)** Start the FastAPI web server:

   ```
   python 'NewsGPT Code.py'
   ```

**B)** Open your web browser and navigate to http://localhost:8000/docs to access the Swagger documentation and try out the API endpoints.

**C)** Use the API endpoints to generate news article summaries programmatically.

## 4. API Endpoints <a name="api-endpoints"></a>

#### 4.1 /summary:
Generate summarised news articles by providing the article's URL as input prompts. For detailed information on how to use each endpoint, refer to the Swagger documentation available at **http://localhost:8000/docs**.

## 5. Screenshots of the Working App <a name="screenshots"></a>

Following are the snaps of the running app.

#### 5.1 Using the NewsGPT app in a web browser.

<img src="https://github.com/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI/blob/main/Images%20of%20the%20Working%20APP/Using%20the%20custom%20function%20of%20FastAPI.png?raw=true" >

#### 5.2 Using the NewsGPT app from the GitBash terminal using the [Bash Script](https://github.com/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI/blob/main/bash_code.sh)

<img src="https://github.com/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI/blob/main/Images%20of%20the%20Working%20APP/Accessing%20the%20NewsGPT's%20FastAPI%20from%20GitBash.png?raw=true" >

#### 5.3 Using the NewsGPT app from local IDE using [Python Script](https://github.com/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI/blob/main/Use%20NewsGPT%20from%20IDE.py).

<img src="https://github.com/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI/blob/main/Images%20of%20the%20Working%20APP/Using%20NewsGPT%20API%20from%20local%20IDE.png?raw=true" >
 

## 6. License <a name="license"></a>
This project is licensed under the MIT License. Feel free to use, modify, and distribute this code for your own purposes.

## 7. Contributions <a name="contributions"></a>

Thank you for using NewsGPT-Using-LangChain-and-FastAPI! If you have any questions or encounter any issues, please don't hesitate to [create an issue](https://github.com/MUmairAB/NewsGPT-Using-LangChain-and-FastAPI/issues).
