from pydantic import BaseModel, Field
from typing import Literal, Annotated


class ChurnInput(BaseModel):

    gender: Annotated[Literal["male", "female"], Field(..., description="Enter the Gender", examples=["male"])]

    SeniorCitizen: Annotated[Literal["yes", "no"], Field(..., description="Is customer a senior citizen?", examples=["no"])]


    Partner: Annotated[Literal["yes", "no"], Field(..., description="Does customer have a partner?", examples=["yes"])]
    
    Dependents: Annotated[Literal["yes", "no"], Field(..., description="Does customer have dependents?", examples=["no"])]
    
    tenure: Annotated[int, Field(..., ge=0, le=120, description="Tenure in months", examples=[24])]
    
    PhoneService: Annotated[Literal["yes", "no"], Field(..., description="Phone service subscription", examples=["yes"])]
    
    MultipleLines: Annotated[Literal["yes", "no"], Field(..., description="Multiple phone lines subscription", examples=["no"])]
    
    InternetService: Annotated[Literal["dsl", "fiber optic", "no"], Field(..., description="Type of internet service", examples=["fiber optic"])]
    
    OnlineSecurity: Annotated[Literal["yes", "no"], Field(..., description="Online security service", examples=["yes"])]
    
    OnlineBackup: Annotated[Literal["yes", "no"], Field(..., description="Online backup service", examples=["no"])]
    
    DeviceProtection: Annotated[Literal["yes", "no"], Field(..., description="Device protection service", examples=["yes"])]
    
    TechSupport: Annotated[Literal["yes", "no"], Field(..., description="Tech support service", examples=["no"])]
    
    StreamingTV: Annotated[Literal["yes", "no"], Field(..., description="Streaming TV subscription", examples=["yes"])]
    
    StreamingMovies: Annotated[Literal["yes", "no"], Field(..., description="Streaming Movies subscription", examples=["yes"])]
    
    Contract: Annotated[Literal["month-to-month", "one year", "two year"], Field(..., description="Type of contract", 
    examples=["one year"])]
    
    PaperlessBilling: Annotated[Literal["yes", "no"], Field(..., description="Paperless billing enabled?", examples=["yes"])]
    
    PaymentMethod: Annotated[Literal["electronic check", "mailed check", "bank transfer", "credit card"], Field(..., 
    description="Payment method type", examples=["credit card"])]
    
    MonthlyCharges: Annotated[float, Field(..., gt=0, description="Monthly charges amount", examples=[79.85])]
    
    TotalCharges: Annotated[float, Field(..., ge=0, description="Total charges amount", examples=[1916.40])]