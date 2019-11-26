"""
A python client to test server functions
"""

import time
import requests
import json
import numpy as np

url_index = 'http://127.0.0.1:5000/'

def test_connection():
    """
    test connection
    """
    print('*** test connection ***')
    r = requests.get(url_index + 'hello', timeout=2)
    print(r.text)

def test_post_json():
    """
    test POST JSON
    """
    print('*** test POST JSON ***')
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

    r = requests.post(url_index + 'post-json', json=payload)
    print(r.url)
    print(r.text)

def test_post_numpy_array():
    """
    test POST numpy array
    """
    print('*** test POST numpy array ***')
    array = np.random.rand(4, 4)
    payload = json.dumps(array.tolist())    # convert numpy to json

    r = requests.post(url_index + 'post-json', json=payload)
    print(r.url)
    print(r.text)

    # convert back
    data = json.loads(r.text)['data']
    print('Retrived data:\n', np.array(json.loads(data)))

def test_post_numpy_array_stress_test():
    """
    Stress test of sending numpy arrays
    """
    print('*** stress test POST numpy array ***')
    # test large array
    array = np.random.rand(10000, 10)
    print('Sending large array with size: ', array.shape)
    payload = json.dumps(array.tolist())    # convert numpy to json

    time_start = time.time()
    r = requests.post(url_index + 'post-json', json=payload)
    print('Elasped time: ', time.time() - time_start)
    

if __name__ == '__main__':
    test_connection()
    test_post_json()
    test_post_numpy_array()
    test_post_numpy_array_stress_test()