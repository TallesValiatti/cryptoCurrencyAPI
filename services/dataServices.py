import jwt
from flask import Flask
import datetime
from flask import jsonify
from functools import wraps
from flask import request

class DataServices(object):

    #private token
    
    @staticmethod
    def validateData(data):
        if(len(data) != 8):
            return False
        if not all(isinstance(x, float) for x in data):
            return False
        return True
            
    @staticmethod
    def predict(data):
        data = [data]
        print(data)

        return True
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
            var data = new List<double>() { 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0};

            HttpClient req = new HttpClient();
            var body = new
            {
                data = data
            };

            HttpContent content = new StringContent(JsonConvert.SerializeObject(body), System.Text.Encoding.UTF8, "application/json");
            var task = req.PostAsync("http://127.0.0.1:5000/predict?token=" + token, content);
            task.Wait();

            var result = task.Result;

            result.EnsureSuccessStatusCode();

            var task2 = result.Content.ReadAsStringAsync();

            task2.Wait();

            var contentBody = JsonConvert.DeserializeObject<returnPredict>(task2.Result);

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
            var task = req.PostAsync("http://127.0.0.1:5000/auth", content);
            task.Wait();

            var result = task.Result;

            result.EnsureSuccessStatusCode();

            var task2 = result.Content.ReadAsStringAsync();
            task2.Wait();

            var contentBody = JsonConvert.DeserializeObject<returnAuth>(task2.Result);

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