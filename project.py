#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import pandas as pd


# In[2]:


data=pd.read_excel("C:/Users/fawzy/Desktop/rev/sales.xlsx")
data


# ## we want the total sales by every product

# In[3]:


d1=data['Sales'].groupby(data['Product']).sum().reset_index().sort_values(by='Sales',ascending=True)
d1


# In[4]:


fig1=px.bar(d1,y='Product',x='Sales',title='sum of sales by product')
fig1.show()


# In[5]:


data


# ## sum of discounts by discount band

# In[6]:


d2=data['Discounts'].groupby(data['Discount Band']).sum().reset_index().iloc[0:3,:]
d2


# In[7]:


fig2=px.pie(d2,names='Discount Band',values='Discounts',title="sum of discount by dicount band")
fig2.show()


# In[8]:


data


# ## sum of sales by each country

# In[9]:


d3=data['Sales'].groupby(data['Country']).sum().reset_index()
d3


# In[10]:


def W(df):
    if df['Country']=='Canada':
        return 'CAN'
    elif df['Country']=='France':
        return 'FRA'
    elif df['Country']=='United States of America':
        return 'USA'
    elif df['Country']=='Germany':
        return 'DEU'
    else:
        return 'MEX'
d3['iso_alpha']=d3.apply(W,axis=1)


# In[11]:


d3


# In[12]:


fig3=px.scatter_geo(d3,locations='iso_alpha',projection='orthographic',color='Country',hover_data='Sales',size='Sales',title='sum of sales by country')
fig3.show()


# ## sum of sales by month

# In[13]:


d4=data['Sales'].groupby(data['Date']).sum().reset_index()
d4


# In[14]:


fig4=px.line(d4,x='Date',y='Sales',title='sum of sales by month')
fig4.show()


# ## sum of profits by each month

# In[15]:


d5=data['Profit'].groupby(data['Date']).sum().reset_index()
d5


# In[16]:


fig5=px.line(d5,x='Date',y='Profit',title='sum of Profit by month')
fig5.show()


# ## sum of sales by each segment

# In[17]:


d6=data['Sales'].groupby(data['Segment']).sum().reset_index().sort_values(by='Sales',ascending=False)
d6


# In[18]:


fig6=px.bar(d6,x='Segment',y='Sales',title='sum of sales by Segment')
fig6.show()


# In[19]:


total_sales=round((data['Sales'].sum()/1000000),2)
total_sales


# In[20]:


total_units=round((data['Units Sold'].sum()/100000),2)
total_units


# In[21]:


total_cogs=round((data['COGS'].sum()/1000000),2)
total_cogs


# In[22]:


total_profits=round((data['Profit'].sum()/1000000),2)
total_profits


# In[23]:


profits_percentage=round(((total_profits/total_sales)*100),2)
profits_percentage


# ## installing dash

# In[24]:


pip install dash


# ## importing

# In[25]:


from dash import Dash, html, dcc


# In[ ]:


import dash_bootstrap_components as dbc
app=Dash(__name__)

app.layout=html.Div([
           html.H1("SalesDashboard",style={'text-align':'center'}),
           dbc.Card(dbc.CardBody([html.H4('sum of sales',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{total_sales}M")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'100px'})),
           dbc.Card(dbc.CardBody([html.H4('sum of units sold',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{total_units}M")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'400px'})),
    
           dbc.Card(dbc.CardBody([html.H4('sum of COGS',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{total_cogs}M")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'700px'})),
           dbc.Card(dbc.CardBody([html.H4('sum of profits',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{total_profits}M")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'1000px'})),
           dbc.Card(dbc.CardBody([html.H4('profits%',className='card-title',style={'fontsize':'24px'}),
                                 html.H2(f"{profits_percentage}%")],style={'width':'18rem','position':'absolute',
                                                                   'top':'40px','left':'1300px'})),
    
    
           dcc.Graph(figure=fig2,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'200px','left':'100',
                                                                     'borderRadius':'50px','padding':'10px'}),

           dcc.Graph(figure=fig3,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'200px','left':'700px',
                                                                     'borderRadius':'50px','padding':'10px'}),
           dcc.Graph(figure=fig4,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'200px','left':'1200px',
                                                                     'borderRadius':'50px','padding':'10px'}) ,
           dcc.Graph(figure=fig1,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'500px','left':'100px',
                                                                     'borderRadius':'50px','padding':'10px'}),
           dcc.Graph(figure=fig6,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'500px','left':'700px',
                                                                     'borderRadius':'50px','padding':'10px'}),
           dcc.Graph(figure=fig5,style={'width':'25%','height':'300px','position':'absolute',
                                                                   'top':'500px','left':'1200px',
                                                                     'borderRadius':'50px','padding':'10px'})
    
    
    
    
    
    
    
],style={'backgroundColor':'gold'}
)

if __name__=='__main__':
    app.run(port=8050)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




