import jwt
from flask import Flask
import datetime
from flask import jsonify
from functools import wraps
from flask import request
import functools
from tensorflow.keras import layers
import numpy as np
import tensorflow as tf
from tensorflow import keras

class DataServices(object):

    #private token
    dataLen = 11
    
    @staticmethod
    def validateData(data):
        if(len(data) != DataServices.dataLen):
            return False
        if not all(isinstance(x, float) for x in data):
            return False
        return True

    @staticmethod
    def normalize(x):
        x1 = []
        for i in range(len(x)):
            item = x[i]
            mean = np.mean(item)
            #print(mean)
            std = np.std(item)
        # print(std)
            item = (item - mean)/std
        # print(item)
            x1.append(item)
        return np.array(x1)
    @staticmethod
    def predict(data):
        data=[data]
                
        #load model
        model = tf.keras.models.load_model('./model_tensorflow.h5')
        
        #nomalize data
        data = DataServices.normalize(data)
        print(data)
        result = model.predict(data)
        result = int(np.round(result))
        return True if (result == 1) else False
    """
  using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;

namespace estudosGerais
{
    class Program
    {
        public static bool ok = false;
        public static Object obj = new object();
        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    var token = auth();
                    var result = predict(token);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e);
                }
            }
            
            Console.ReadLine();
        }

        public static bool predict(string token)
        {
            var data = new List<double>() { 1080.0, 1100.0, 1000.1, 1000.0, 1010.0, 1000.1, 1000.0, 1090.0, 1105.1, 1140.0, 1140.0 };

            HttpClient req = new HttpClient();
            var body = new
            {
                data = data
            };

            HttpContent content = new StringContent(JsonConvert.SerializeObject(body), System.Text.Encoding.UTF8, "application/json");
            var taskPost = req.PostAsync("http://127.0.0.1:5000/predict?token=" + token, content);
            taskPost.Wait();

            var result = taskPost.Result;

            result.EnsureSuccessStatusCode();

            var taskRead = result.Content.ReadAsStringAsync();

            taskRead.Wait();

            var contentBody = JsonConvert.DeserializeObject<returnPredict>(taskRead.Result);
            
            Console.WriteLine(contentBody.result);
            return contentBody.result;
        }
        public static string auth()
        {  
            HttpClient req = new HttpClient();
            var body = new
            {
                user = "talles",
                password = "123"
            };
            HttpContent content = new StringContent(JsonConvert.SerializeObject(body), System.Text.Encoding.UTF8, "application/json");
            var taskPost = req.PostAsync("http://127.0.0.1:5000/auth", content);
            taskPost.Wait();

            var result = taskPost.Result;

            result.EnsureSuccessStatusCode();

            var taskRead = result.Content.ReadAsStringAsync();
            taskRead.Wait();

            var contentBody = JsonConvert.DeserializeObject<returnAuth>(taskRead.Result);

            return contentBody.token;
        }
    }

    class returnAuth
    {
        public string exp{ get; set; }
        public string message { get; set; }
        public string token { get; set; }
    }
    class returnPredict
    {
        public bool result { get; set; }
    }
}


    """