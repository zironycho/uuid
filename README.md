# UUID Generation app

## Call API
* generate uuid
  * /
* check uuid
  * /{{ uuid }}

## BUILD
```
docker build . -t zironycho/uuid
```

## RUN 
```
docker run --rm -d -p 5000:5000 --name uuid zironycho/uuid
```
