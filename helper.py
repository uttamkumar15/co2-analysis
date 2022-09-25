import plotly.express as px

def avg_co2(df):
    co2_con = df.dropna()
    fig = px.histogram(co2_con, x='country', y='co2_per_capita', histfunc='avg', color='country')
    fig.update_layout(xaxis={'categoryorder': 'total descending'})
    return fig

def world_co2_per_capita(df):
    co2_ani = df.sort_values(by='year')
    fig = px.choropleth(co2_ani, locations='country',
                        locationmode="country names", color='co2_per_capita', animation_frame='year')
    return fig

def world_population(df):
    co2_ani = df.sort_values(by='year')
    fig = px.choropleth(co2_ani, locations='country',
                        locationmode="country names", color='population', animation_frame='year')
    return fig

def world_gdp(df):
    co2_ani = df.sort_values(by='year')
    fig = px.choropleth(co2_ani, locations='country',
                        locationmode="country names", color='gdp', animation_frame='year')
    return fig

def share_co2(df):
    co2_ani = df.sort_values(by='year')
    fig = px.choropleth(co2_ani, locations='country',
                        locationmode="country names", color='share_global_co2', animation_frame='year')
    return fig

def co2_per_gdp(df):
    co2_ani = df.sort_values(by='year')
    fig = px.choropleth(co2_ani, locations='country',
                        locationmode="country names", color='co2_per_gdp', animation_frame='year')
    return fig

def energy_per_gdp(df):
    co2_ani = df.sort_values(by='year')
    fig = px.choropleth(co2_ani, locations='country',
                        locationmode="country names", color='energy_per_gdp', animation_frame='year')
    return fig


def line(df,a):
    fig = px.line(x=df['year'], y=a, data_frame=df)
    return fig

def scatter(df,a,b):
    fig = px.scatter(x=df['year'],y=a,data_frame=df,color= b)
    return fig
