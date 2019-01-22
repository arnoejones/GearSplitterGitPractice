import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import WranglerRatiosLookup, Calculate

app = dash.Dash()

jeep_model_list = []
for key, value in WranglerRatiosLookup.jeep_model_dict().items():
    jeep_model_list.append({'label': key, 'value': value})

diff_list = []
for diff in WranglerRatiosLookup.wrangler_diff_ratios():
    diff_list.append({'label': str(diff) + ':1', 'value': diff})

app.layout = html.Div([
    dcc.Input(id='mph-in',
              value=70,
              debounce=True,
              type='float'
              ), ' Enter MPH',
    html.Div(id='mph-out'),

    dcc.Input(id='rpm-in',
              value=2666,
              debounce=True,
              type='float'
              ), ' Enter RPM',
    html.Div(id='rpm-out'),

    dcc.Dropdown(
        id="jeep-dropdown-id",
        options=jeep_model_list,
        value='jk_2012', ),
    html.Div(id='jeep-model-div'),

    dcc.RadioItems(
        id='tranny_id',
        options=[{'label': 'Automatic', 'value': 'auto'},
                 {'label': ' Manual', 'value': 'manual'}],
        value='auto'), 'Transmission Type',
    html.Div(id='tranny-div'),

    # html.H4("Rubicon?"),
    dcc.RadioItems(
        id='rubi-id',
        options=[{'label': 'Yes', 'value': True},
                 {'label': 'No', 'value': False}],
        value=True), 'Rubicon Transfer Case?',
    html.Div(id='rubi-div'),

    # html.H4("Transfer Case:"),
    dcc.RadioItems(
        id='tcase_id',
        options=[{'label': ' Engaged ', 'value': True},
                 {'label': 'Not Engaged', 'value': False}],
        value=False), 'Transfer Case Engaged?',
    html.Div(id='tcase-div'),

    dcc.Dropdown(id="diff-ratio-id",
                 options=diff_list,
                 value=4.56), 'Differential Ratio',
    html.Div(id='diff-ratio-div'),

    html.Button(id='submit-button',
                n_clicks=0,
                children='Calculate Tire Diameter',
                style={'fontSize': 24}),
    html.H1(id='number-out')
])

# just some values to initialize the dictionary
numbers_dict = {'mph': 70,
                'rpm': 2666,
                'jeep_model': 'jk_2012',
                'transmissionType': 'auto',
                'rubicon': True,
                'fourLowEngaged': False,
                'differentialGearRatio': 4.56,
                'gearSelected': 5}


@app.callback(Output('diff-ratio-div', 'children'),
              [Input('diff-ratio-id', 'value')])
def commit_diff_ratio(diff_ratio):
    numbers_dict['differentialGearRatio'] = float(diff_ratio)


@app.callback(Output('mph-out', 'children'),
              [Input('mph-in', 'value')])
def commit_mph(mph_value):
    numbers_dict['mph'] = float(mph_value)


@app.callback(Output('rpm-out', 'children'),
              [Input('rpm-in', 'value')])
def commit_rpm(rpm_value):
    numbers_dict['rpm'] = float(rpm_value)


@app.callback(Output(component_id='jeep-model-div', component_property='children'),
              [Input(component_id='jeep-dropdown-id', component_property='value')])
def jeep_model_callback(jeep_model_input_value):
    numbers_dict['jeep_model'] = jeep_model_input_value


@app.callback(Output(component_id='tranny-div', component_property='children'),
              [Input(component_id='tranny_id', component_property='value')])
def tranny_callback(tranny_input_value):
    numbers_dict['transmissionType'] = tranny_input_value


@app.callback(Output(component_id='rubi-div', component_property='children'),
              [Input(component_id='rubi-id', component_property='value')])
def rubicon_callback(rubicon_input_value):
    numbers_dict['rubicon'] = rubicon_input_value


@app.callback(Output(component_id='tcase-div', component_property='children'),
              [Input(component_id='tcase_id', component_property='value')])
def tcase_callback(tcase_input_value):
    numbers_dict['fourLowEngaged'] = tcase_input_value


@app.callback(Output('number-out', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('mph-in', 'value')])
def display_tire_size(some_number, some_value):
    # number = numbers_dict['mph'] * numbers_dict['rpm']
    # return number
    gear_ratios = []
    # --- determine which transmission list to use ---
    # --- automatic transmisions ---
    if numbers_dict['jeep_model'] == 'jk_2012' and numbers_dict['transmissionType'] == 'auto':
        gear_ratios = WranglerRatiosLookup.jk_2012_auto_trans_ratios()
    if numbers_dict['jeep_model'] == 'jk_2007' and numbers_dict['transmissionType'] == 'auto':
        gear_ratios = WranglerRatiosLookup.jk_2007_auto_trans_ratios()
    if numbers_dict['jeep_model'] == 'jl' and numbers_dict['transmissionType'] == 'auto':
        gear_ratios = WranglerRatiosLookup.jl_automatic_trans_ratios()

    # --- manual transmissions ---
    if numbers_dict['jeep_model'] == 'jk_2012' and numbers_dict['transmissionType'] == 'manual':
        gear_ratios = WranglerRatiosLookup.jk_2012_manual_trans_ratios()
    if numbers_dict['jeep_model'] == 'jk_2007' and numbers_dict['transmissionType'] == 'manual':
        gear_ratios = WranglerRatiosLookup.jk_2007_manual_trans_ratios()
    if numbers_dict['jeep_model'] == 'jl' and numbers_dict['transmissionType'] == 'manual':
        gear_ratios = WranglerRatiosLookup.jl_manual_trans_ratios()

    # --- Determine transfer case ratio ---
    if numbers_dict['fourLowEngaged'] is True and numbers_dict['rubicon'] is True:
        transfercase_final_value = 4  # rubicon
    elif numbers_dict['fourLowEngaged'] is True and numbers_dict['rubicon'] is False:
        transfercase_final_value = 2.76  # non-rubicon
    else:
        transfercase_final_value = 1  # not engaged, so 1:1

    return float("{0:.2f}".format(Calculate.JeepGearSplitter.calculateTireDiameter(mph=numbers_dict['mph'],
                                                                                   rpm=numbers_dict['rpm'],
                                                                                   tranny_gear=gear_ratios[-1],
                                                                                   tcase=transfercase_final_value,
                                                                                   diff=numbers_dict[
                                                                                       'differentialGearRatio'])))


if __name__ == '__main__':
    app.run_server()
