
import pandas as pd
import string

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

lis=[]
lis=data.split('\n')

df=pd.DataFrame(lis)

df=df[0].str.split(';',expand=True)

df.columns=df.iloc[0]

df=df[1:6]


#Part 1

#Changing Data type to int

df['FlightCodes']=df['FlightCodes'].astype("str").astype("string")

df['FlightCodes']=df['FlightCodes'].replace(to_replace="",value="0")

def dtype(text):
    return int(float(text))

df['FlightCodes']=df['FlightCodes'].apply(lambda x: dtype(x))

df['FlightCodes']

#Incrementing values by 10 - Method 1

for i in range(2,5):
    df['FlightCodes'].loc[i]=df['FlightCodes'].loc[i-1]+10

df['FlightCodes']

#Incrementing values by 10 - Method 2

df['FlightCodes'].loc[2]=df['FlightCodes'].loc[1]+10
df['FlightCodes'].loc[4]=df['FlightCodes'].loc[3]+10

#Part 2

df['To_From']=df['To_From'].str.upper()

df.columns

df[['To','From']]=df.To_From.str.split('_',expand=True)

df

df=df.drop(['To_From'],axis=1)

df


#Part 3

def punct(text):
    for ch in string.punctuation:
        text = text.replace(ch, '')
    return text

df['Airline Code'] = df['Airline Code'].apply(punct)

df
