#### How to use this repo

* to run ubuntu api server use vagrant up in / of repo
* to build python container run docker built . -t <image_tag> in Image folder 
* to run python container run docker run -it -p 8000:8000 <image_tag>
* consul api is available in http://172.16.17.20:8500, python api service available in http://localhost:8000
