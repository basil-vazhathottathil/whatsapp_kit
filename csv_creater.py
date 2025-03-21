import pandas as pd

# enter the your numbers here
numbers=[] 

#converting to dataframe
df=pd.DataFrame({'Phone':numbers})

# Change this line to add country code without +
df["Phone"] = df["Phone"].apply(lambda x: f"91{x.strip()}")

#assign names ,because the pywhatkit needs it 
df["Name"] = [f"Person{i+1}" for i in range(len(df))]

#to save to csv
df.to_csv("contacts.csv", index=False)
print('yep its done')