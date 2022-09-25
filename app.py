import pandas as pd
import streamlit as st
import helper
import plotly.express as px

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1517065963912-27f75001ebe2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80");
background-size: cover;
}
[data-testid="stSidebar"]>div:first-child{
background-image: url("https://cdn.pixabay.com/photo/2015/09/06/00/46/yellow-926728_1280.jpg");
background position: center;
background repeat: no repeat;
}
</style>

'''
st.markdown(page_bg_img,unsafe_allow_html=True)


df = pd.read_csv('owid-co2-data.csv')

drop = []
n=0
null = df.isnull().sum()
for i in null:
  if i >20000:
    col = null.index[n]
    drop.append(col)
  n+=1

st.sidebar.title('co2 Analysis')
st.sidebar.image('https://images.unsplash.com/photo-1597165826924-f0e9fb81762e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80')
user_menu = st.sidebar.radio('Select an option',('Overall Analysis','Country Wise Analysis','Global Share Analysis','Per Gdp Analysis'))

if user_menu == 'Overall Analysis':
    st.title('Overall Analysis')
    st.dataframe(df)
    st.subheader('co2 Per Capita Over the years')
    fig = helper.avg_co2(df)
    st.plotly_chart(fig)
    st.subheader('World Population')
    fig = helper.world_population(df)
    st.plotly_chart(fig)
    st.subheader('World Gdp')
    fig = helper.world_gdp(df)
    st.plotly_chart(fig)
    st.subheader("co2 Per Capita Over the years")
    fig = helper.world_co2_per_capita(df)
    st.plotly_chart(fig)
    st.subheader("Share co2 Over the years")
    fig = helper.share_co2(df)
    st.plotly_chart(fig)

elif user_menu=='Country Wise Analysis':
    st.title('Country Wise Analysis')
    country_list = df['country'].sort_values().unique()
    country = st.selectbox('Select Country',country_list)
    df_country = df[df.country==country]
    st.subheader(country+' co2 Over the Years')
    fig = helper.line(df_country,df_country['co2_per_capita'])
    st.plotly_chart(fig)
    st.subheader("Cement co2 in "+country)
    fig = helper.scatter(df_country,df_country['cement_co2_per_capita'],df_country['cement_co2'])
    st.plotly_chart(fig)
    st.subheader("Coal co2 in " + country)
    fig = helper.scatter(df_country, df_country['coal_co2_per_capita'], df_country['coal_co2'])
    st.plotly_chart(fig)
    st.subheader("Gas co2 in " + country)
    fig = helper.scatter(df_country, df_country['gas_co2_per_capita'], df_country['gas_co2'])
    st.plotly_chart(fig)
    st.subheader("Oil co2 in " + country)
    fig = helper.scatter(df_country, df_country['oil_co2_per_capita'], df_country['oil_co2'])
    st.plotly_chart(fig)
    st.subheader("Cumulative co2 in " + country)
    fig = helper.line(df_country,df_country['cumulative_co2'])
    st.plotly_chart(fig)
    st.subheader("Cumulative Cement co2 in " + country)
    fig = helper.line(df_country, df_country['cumulative_cement_co2'])
    st.plotly_chart(fig)
    st.subheader("Cumulative Gas co2 in " + country)
    fig = helper.line(df_country, df_country['cumulative_gas_co2'])
    st.plotly_chart(fig)
    st.subheader("Cumulative Oil co2 in " + country)
    fig = helper.line(df_country, df_country['cumulative_oil_co2'])
    st.plotly_chart(fig)
    st.subheader("Primary Energy Consumption in " + country)
    fig = helper.line(df_country, df_country['primary_energy_consumption'])
    st.plotly_chart(fig)
    st.subheader("Energy Per Capita in " + country)
    fig = helper.line(df_country, df_country['energy_per_capita'])
    st.plotly_chart(fig)


elif user_menu=='Global Share Analysis':
    st.title('Global Share Analysis')
    country_list = df['country'].sort_values().unique()
    country = st.selectbox('Select Country',country_list)
    df_country = df[df.country==country]
    st.subheader("Share Global co2 in " + country)
    fig = helper.scatter(df_country, df_country['share_global_co2'], df_country['co2_per_capita'])
    st.plotly_chart(fig)
    st.subheader("Share Global Cement co2 in " + country)
    fig = helper.scatter(df_country, df_country['share_global_cement_co2'], df_country['cement_co2_per_capita'])
    st.plotly_chart(fig)
    st.subheader("Share Global Coal co2 in " + country)
    fig = helper.scatter(df_country, df_country['share_global_coal_co2'], df_country['coal_co2_per_capita'])
    st.plotly_chart(fig)
    st.subheader("Share Global Gas co2 in " + country)
    fig = helper.scatter(df_country, df_country['share_global_gas_co2'], df_country['gas_co2_per_capita'])
    st.plotly_chart(fig)
    st.subheader("Share Global Oil co2' in " + country)
    fig = helper.scatter(df_country, df_country['share_global_oil_co2'], df_country['oil_co2_per_capita'])
    st.plotly_chart(fig)
    st.subheader("Share Global Cumulative co2 in " + country)
    fig = helper.line(df_country, df_country['share_global_cumulative_co2'])
    st.plotly_chart(fig)
    st.subheader("Share Global Cumulative Cement co2 in " + country)
    fig = helper.line(df_country, df_country['share_global_cumulative_cement_co2'])
    st.plotly_chart(fig)
    st.subheader("Share Global Cumulative Gas co2 in " + country)
    fig = helper.line(df_country, df_country['share_global_cumulative_gas_co2'])
    st.plotly_chart(fig)
    st.subheader("Share Global Cumulative Oil co2 in " + country)
    fig = helper.line(df_country, df_country['share_global_cumulative_oil_co2'])
    st.plotly_chart(fig)

elif user_menu== 'Per Gdp Analysis':
    st.title('Per Gdp Analysis')
    st.subheader("co2 per Gdp")
    fig = helper.co2_per_gdp(df)
    st.plotly_chart(fig)
    st.subheader('Energy Per Gdp')
    fig = helper.energy_per_gdp(df)
    st.plotly_chart(fig)
    country_list = df['country'].sort_values().unique()
    country = st.selectbox('Select Country', country_list)
    df_country = df[df.country == country]
    st.subheader("co2 per Gdp in " + country)
    fig = helper.scatter(df_country, df_country['co2_per_gdp'], df_country['gdp'])
    st.plotly_chart(fig)
    st.subheader("Energy per Gdp in " + country)
    fig = helper.scatter(df_country, df_country['energy_per_gdp'], df_country['gdp'])
    st.plotly_chart(fig)