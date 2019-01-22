import Calculate
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

masterListRpm = []
masterListMph = []
jeep_model = 'jk'

fromCalculate = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model, 3.23, 33.4, 3, 'automatic', True, False)
df = pd.DataFrame(fromCalculate)
df = df.transpose()
df.columns = ['RPM', 'MPH']

# master_list = []
fromCalculate1 = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model, 3.73, 33.4, 3, 'automatic', True, False)
df1 = pd.DataFrame(fromCalculate1)
df1 = df1.transpose()
df1.columns = ['RPM', 'MPH']
# master_list.append(fromCalculate)
# #masterListMph.append(fromCalculate[1])
# # masterListRpm.append(fromCalculate[0])
fromCalculate2 = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model, 4.10, 33.4, 3, 'automatic', True, False)
df2 = pd.DataFrame(fromCalculate2)
df2 = df2.transpose()
df2.columns = ['RPM', 'MPH']

# master_list.append(fromCalculate)
# masterListMph.append(fromCalculate[1])
# masterListRpm.append(fromCalculate[0])
fromCalculate3 = Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model, 4.56, 33.4, 3, 'automatic', True, False)
df3 = pd.DataFrame(fromCalculate3)
df3 = df3.transpose()
df3.columns = ['RPM', 'MPH']
# masterListMph.append(fromCalculate[1])
# masterListRpm.append(fromCalculate[0])
fromCalculate4 = (Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model, 4.88, 33.4, 3, 'automatic', True, False))
df4 = pd.DataFrame(fromCalculate4)
df4 = df4.transpose()
df4.columns = ['RPM', 'MPH']



# masterListMph.append(fromCalculate[1])
# masterListRpm.append(fromCalculate[0])
fromCalculate5 = (Calculate.JeepGearSplitter.calculateSpeedFromRpm(jeep_model, 5.13, 33.4, 3, 'automatic', True, False))
df5 = pd.DataFrame(fromCalculate5)
df5 = df5.transpose()
df5.columns = ['RPM', 'MPH']
# masterListMph.append(fromCalculate[1])
# masterListRpm.append(fromCalculate[0])



# master_list = zip(masterListMph, masterListRpm)
# master_list = list(master_list)
# #master_list = set(master_list)
# get all this stuff into a dataframe
# df = pd.DataFrame(fromCalculate)
# df = df.transpose()
# df.columns = ['RPM', 'MPH']
# print(df)

trace1 = go.Scatter(x=df['RPM'],
                   y=df['MPH'],
                    name = '3.23'
                   )

trace2 = go.Scatter(x = df1['RPM'],
                   y=df1['MPH'],
                    name = '3.23'
                   )

trace3 = go.Scatter(x = df2['RPM'],
                   y=df2['MPH'],
                    name = '4.10'
                   )

trace4 = go.Scatter(x = df3['RPM'],
                   y=df3['MPH'],
                    name = '4.56'
                   )

trace5 = go.Scatter(x = df4['RPM'],
                   y=df4['MPH'],
                    name = '4.88'
                   )

trace6 = go.Scatter(x = df5['RPM'],
                   y=df5['MPH'],
                    name = '5.13'
                   )

data = [trace1, trace2, trace3, trace4, trace5, trace6]

layout = go.Layout(title = "shit bird")
fig = go.Figure(data=data, layout = layout)
pyo.plot(fig)

# jeep_title= 'Jeep {} Gear Splitter'.format(jeep_model.upper())
# labels = ['3.23', '3.73','4,10','4.56','4.88','5.13']
# colors = ['rgb(244, 66, 66)',
#           'rgb(52, 4, 242)',
#           'rgb(2, 252, 239)',
#           'rgb(189,189,189)',
#           'rgb(252, 110, 1)',
#           'rgb(38, 255, 0)',
#           ]
#
# mode_size = [2,2,2,2,2,2]
# line_size = [2,2,2,2,2,2]
# x_data = masterListRpm.copy()
# y_data = masterListMph.copy()
# traces = []
#
# for i in range(0,6):
#     traces.append(go.Scatter(
#         x=x_data[i],
#         y=y_data[i],
#         mode = 'lines+markers', name=labels[i],
#         line=dict(color=colors[i], width=line_size[i]),
#
#         connectgaps=True,
#     ))
#
#     traces.append(go.Scatter(
#         x=[x_data[i][0], x_data[i][11]],
#         y=[y_data[i][0], y_data[i][11]],
#         mode='lines+markers', name = x_data[i][0],
#         marker=dict(color=colors[i], size=mode_size[i])
#     ))
#
# layout = go.Layout(
#     xaxis=dict(
#         showline=True,
#         showgrid=True,
#         showticklabels=True,
#         linecolor='rgb(204,204,204)',
#         linewidth = 1,
#         ticks='outside',
#         tickcolor='rgb(204,204,204)',
#         tickwidth=2,
#         ticklen=5,
#         tickfont=dict(family='Arial',
#             size=12,
#             color='rgb(82, 82, 82)'
#         ),
#     ),
#     yaxis=dict(
#         showgrid=True,
#         zeroline=True,
#         showline=True,
#         showticklabels=True,
#     ),
#     autosize=True,
#     margin=dict(
#         autoexpand=True,
#         # l=250,
#         # r=120,
#         # t=0,
#     ),
#     showlegend=False,
#     title = jeep_title
# )
#
# annotations = []
#
# for y_trace, label, color in zip(y_data, labels, colors):
#     # labeling the left_side of the plot
#     annotations.append(dict(xref='paper', x=0.05, y=y_trace[11],
#                                   xanchor='center', yanchor='middle',
#                                   text=label + ' Gear Ratio',
#                                   font=dict(family='Arial',
#                                             size=16),
#                                   showarrow=False))
#     # labeling the right_side of the plot
#     annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
#                                   xanchor='center', yanchor='middle',
#                                   text='{} Max MPH'.format(y_trace[11]),
#                                   font=dict(family='Arial',
#                                             size=16),
#                                   showarrow=False))
#
#
# layout['annotations'] = annotations
#
# fig = go.Figure(data=traces, layout=layout)
# pyo.plot(fig, filename="deleteme.html")

#
# data = [go.Scatter(x = masterListRpm, y = masterListMph, marker=dict(color="rgb(16,32,77)"))]
#
# layout = go.Layout(,
#                    xaxis = {'title':'RPM'},
#                    yaxis=dict(title='MPH'),
#                    hovermode='closest')
# fig = go.Figure(data = data, layout=layout)
# pyo.plot(fig, filename="deleteme.html")