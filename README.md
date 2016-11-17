  ![coollogo_com-9082891](https://cloud.githubusercontent.com/assets/9820374/20377032/e2ec1a56-acc6-11e6-8e9c-72c72f49b7fa.png)

# 2CNUrl
This repo is some python scripts for replace image url to qiniu url.

demo:
![](https://raw.githubusercontent.com/jhonny-me/replaceImage/master/demo/demo.gif)

## Requirements

Before using following scripts, you should create a qiniu account and a bucket for configure.You should implement the *accessKey*,*secretkey*,*bucket_url*,*bucket* in ```uploadToQiniu.py``` file.

## magic.py

You can use this script for replacing all the image url to qiniu url automatically.

**param**: file name(should be a markdown file)

The script will name all image resource using file name's md5 hash value + '_image_' + order number,eg:

image names for image in ```20160925_为慈善事业贡献你的代码.md``` should be ```d8563544010dd4bff9c497f47729292e_image_0.jpg``` 

demo:

```
☁  replaceImage [master] ⚡ python magic.py 20160925_为慈善事业贡献你的代码.md
```

the output will overwirte this file using qiniu url.

## replaceToCNUrl.py

You can use this script for replace single image url to qiniu url.

**param**: image url required

**param**: custom resource name

If you provide a custom reource name, image uploaded to qiniu will be name using provided, otherwise will use the name in original url, eg:

generated qiniu url for ```python replaceToCNUrl.py http://images.51cto.com/files/uploadimg/20100630/104906665.jpg``` will be ```balabala.bkt.clouddn.com/104906665.jpg```, and ```balabala.bkt.clouddn.com/custom_name.jpg``` for ```python replaceToCNUrl.py http://images.51cto.com/files/uploadimg/20100630/104906665.jpg custom_name.jpg```

demo:

```
./replaceToCNUrl.py http://images.51cto.com/files/uploadimg/20100630/104906665.jpg
```

## Todo

- [ ] optimize image before upload to qiniu
- [ ] fail logs

##License

**MIT**
