import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('districts.csv')

df['Total Population'] = df['Male'] + df['Female']
df['Sex ratio'] = (df['Male']/df['Female'])*100
df['Literacy Rate'] = (df['Literate']/df['Total Population'])*100

print(df)

st.sidebar.title('India Map')

state_list = sorted(df['State'].unique())
state_list.insert(0,'Entire India')

state = st.sidebar.selectbox('Select State',state_list)

parameters = ['Total Population','Male', 'Female','Sex ratio', 'Literate','Literacy Rate', 'Total_Power_Parity',
       'Housholds_with_Electric_Lighting', 'Households_with_Internet',
       'Rural_Households', 'Urban_Households']

primary = st.sidebar.selectbox('Select Primary parameter',sorted(parameters))

secondary = st.sidebar.selectbox('Select Secondary parameter',sorted(parameters))

plotbtn = st.sidebar.button('Plot')

if plotbtn:

    if state == 'Entire India':

        st.dataframe(df)

        st.text(primary + " " + secondary)

        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",zoom=5,size=primary,color=secondary,
                          mapbox_style="carto-positron",hover_name='District',size_max=20,width=1500,height=720)

        st.plotly_chart(fig,use_container_width=True)

    else:

        st.text(primary + " " + secondary)

        state_df = df[df['State'] == state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", zoom=5, size=primary, color=secondary,
                                mapbox_style="carto-positron", hover_name='District', size_max=35, width=1200,
                                height=720)

        st.plotly_chart(fig, use_container_width=True)