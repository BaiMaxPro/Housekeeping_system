FROM python:3.8
 
WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY . .

EXPOSE 5000

ENV PYTHONPATH=/
 
CMD ["python", "app.py"]
