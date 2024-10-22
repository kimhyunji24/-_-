# Python 이미지를 기반으로 합니다.
FROM python:3.9-slim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 필요한 파일들을 작업 디렉토리에 복사합니다.
COPY . /app

# 필요한 패키지를 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 포트를 노출합니다.
EXPOSE 8000

# Django 서버를 시작합니다.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]