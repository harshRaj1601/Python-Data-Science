import streamlit as st
import pandas as pd
import plotly.express as px

# UI Configuration

st.set_page_config(
    page_title="Pokemon App",
    page_icon="☠️",
    layout="wide"
)

#load data

@st.cache_data
def load_data():
    return pd.read_csv("Pokemon.csv",index_col="#")

# UI integration

with st.spinner("loading dataset..."):
    df = load_data()
    #st.snow()

st.title("Pokemon Data Analytics")
st.subheader("A simple data app to analyze Pokemon data")

st.sidebar.title("Menu")
choice = st.sidebar.radio("Options", ["View Data","Visualize Data"])
if choice == "View Data":
    st.header("View Dataset")
    st.dataframe(df)
else:
    st.header("Visualization")
    # scol = st.sidebar.radio("Select a column",df.columns)
    # st.write(f"### Visulaizing {scol}")
    # if df[scol].dtype == "object":
    #     total_unique_values = df[scol].nunique()
    #     st.write(f"Total Unique Values: {total_unique_values}")
    # elif df[scol].dtype == "int64":
    #     st.write(f"Min Value: {df[scol].min()}")
    #     st.write(f"Max Value: {df[scol].max()}")
    #     st.write(f"Mean Value: {df[scol].mean()}")
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    num_cols = df.select_dtypes(exclude="object").columns.tolist()
    cat_cols.remove("Name")
    num_cols.remove("Legendary")
    num_cols.remove("Generation")
    cat_cols.append("Generation")
    cat_cols.append("Legendary")

    snum_cols = st.sidebar.selectbox("Select a numeric column", num_cols)
    scat_cols = st.sidebar.selectbox("Select a catagorical column", cat_cols)

    c1, c2 = st.columns(2)

    # visualization

    fig1 = px.histogram(df,x=snum_cols,
                        title=f"Distribution of {snum_cols}")
    
    fig2 = px.pie(df,names=scat_cols,title=f"Distribution of {scat_cols}",hole=0.3)
    
    c1.plotly_chart(fig1)
    c2.plotly_chart(fig2)

    fig3 = px.box(df,x=scat_cols, y=snum_cols, title=f"{snum_cols} by {scat_cols}")
    st.plotly_chart(fig3)

    fig4 = px.treemap(
        df,path=["Generation","Type 1"],
        title="Pokemon type Distribution"
    )

    st.plotly_chart(fig4)