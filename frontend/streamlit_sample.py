import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(layout="wide")

# Data
# 実際はAPIから取得
df = pd.read_csv('data/data_sample.csv')
vars_cont = [var for var in df.columns if var.startswith('cont')]

# Layout (Sidebar)
st.sidebar.markdown("Streamlitのテスト。変数を選べ。")
cont_selected_1 = st.sidebar.selectbox('変数その１', vars_cont)
cont_selected_2 = st.sidebar.selectbox('変数その２', vars_cont)
cont_selected_3 = st.sidebar.selectbox('変数その３', vars_cont)

# Continuous Variable Distribution in Content
group_labels = ['target=0', 'target=1']
# 変数その１
li_cont0_1 = df[df['target'] == 0][cont_selected_1].values.tolist()
li_cont1_1 = df[df['target'] == 1][cont_selected_1].values.tolist()
cont_data_1 = [li_cont0_1, li_cont1_1]
fig_cont_1 = ff.create_distplot(cont_data_1, group_labels,
                                show_hist=False,
                                show_rug=False)
fig_cont_1.update_layout(height=300,
                         width=500,
                         margin={'l': 20, 'r': 20, 't': 0, 'b': 0},
                         legend=dict(
                             yanchor="top",
                             y=0.99,
                             xanchor="right",
                             x=0.99)
                         )
# 変数その２
li_cont0_2 = df[df['target'] == 0][cont_selected_2].values.tolist()
li_cont1_2 = df[df['target'] == 1][cont_selected_2].values.tolist()
cont_data_2 = [li_cont0_2, li_cont1_2]
fig_cont_2 = ff.create_distplot(cont_data_2, group_labels,
                                show_hist=False,
                                show_rug=False)
fig_cont_2.update_layout(height=300,
                         width=500,
                         margin={'l': 20, 'r': 20, 't': 0, 'b': 0},
                         legend=dict(
                             yanchor="top",
                             y=0.99,
                             xanchor="right",
                             x=0.99)
                         )

# 変数その３
li_cont0_3 = df[df['target'] == 0][cont_selected_3].values.tolist()
li_cont1_3 = df[df['target'] == 1][cont_selected_3].values.tolist()
cont_data_3 = [li_cont0_3, li_cont1_3]

fig_cont_3 = ff.create_distplot(cont_data_3, group_labels,
                                show_hist=False,
                                show_rug=False)
fig_cont_3.update_layout(height=300,
                         width=1000,
                         margin={'l': 20, 'r': 20, 't': 0, 'b': 0},
                         legend=dict(
                             yanchor="top",
                             y=0.99,
                             xanchor="right",
                             x=0.99)
                         )

# Graph (Pie Chart in Sidebar)
df_target = df[['id', 'target']].groupby('target').count() / len(df)
fig_target = go.Figure(data=[go.Pie(labels=df_target.index,
                                    values=df_target['id'],
                                    hole=.3)])
fig_target.update_layout(showlegend=False,
                         height=400,
                         margin={'l': 20, 'r': 60, 't': 0, 'b': 0})
fig_target.update_traces(textposition='inside', textinfo='label+percent')

# Layout (Content)
left_column, right_column = st.columns(2)
left_column.subheader('変数その１　分布: ' + cont_selected_1)
right_column.subheader('変数その2　分布: ' + cont_selected_2)
left_column.plotly_chart(fig_cont_1)
right_column.plotly_chart(fig_cont_2)
st.subheader('変数その３　分布: ' + cont_selected_3)
st.plotly_chart(fig_cont_3)

st.subheader('targetの分布')
st.plotly_chart(fig_target)
