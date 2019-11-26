% MATLAB client to test server functions

%% test connection
url = "http://127.0.0.1:5000/hello";
options = weboptions('RequestMethod', 'get');
data = webread(url, options)

%% test POST JSON
url = "http://127.0.0.1:5000/post-json";
data = struct('key1', 'value1', 'key2', ['value2'; 'value3']);
options = weboptions('RequestMethod', 'post', 'ArrayFormat','json');

response = webwrite(url, data, options)
disp(response.data)

%% test POST matrix
data = rand(4, 4)   % send a double matrix
response = webwrite(url, data, options)

% convert back
disp(response.data)