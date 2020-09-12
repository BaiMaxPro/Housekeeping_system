FROM python:3.8
 
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY . /app

EXPOSE 5000
 
CMD ["python", "app.py"]
