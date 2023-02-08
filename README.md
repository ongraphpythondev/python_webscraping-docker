# Python webscraping with docker
- This project is python webscraping using beautifulsoup.
- It perform webscraping inside docker container.
- It scrap all link url, image url from a given website and list them.

### Files Contains :
- It contains two files :
> - **python file named "main.py"**
> This python file contain all web scraping python script
> - **Dockerfile named "Dockerfile"**
> This Dockerfile contains Docker commands which need to run python script inside docker container.

### Commands :
-  To Build docker container :
```
docker build -t main .
```
- To run python script in docker container :
```
docker run -it main
```


