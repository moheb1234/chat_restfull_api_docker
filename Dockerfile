FROM python
WORKDIR /user/src/app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt