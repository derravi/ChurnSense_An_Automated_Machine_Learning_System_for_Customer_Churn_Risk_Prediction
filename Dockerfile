FROM python:3.13.7

RUN mkdir -p customer_churn_prediction

WORKDIR /automated_customer_churn_risk_prediction_machine_learning_system

COPY . /automated_customer_churn_risk_prediction_machine_learning_system

RUN pip install -r requirements.txt

ENV PORT=800

EXPOSE 8000

CMD ["uvicorn","api:app","--host","0.0.0.0","--port","8000"]