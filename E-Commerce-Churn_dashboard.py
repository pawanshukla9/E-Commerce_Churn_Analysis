import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#=============================================
#Import Data
#=============================================
df = pd.read_csv('https://raw.githubusercontent.com/pawanshukla9/data/refs/heads/main/e-commerce_churn_clean.csv')


# ============================================
# ORDER DEFINITIONS (IMPORTANT)
# ============================================
QUARTER_ORDER = ["Q1", "Q2", "Q3", "Q4"]
AGE_ORDER = sorted(df["Age_Group"].dropna().unique())
ENGAGEMENT_ORDER = ["Low", "Medium", "High", "Very High"]
VALUE_ORDER = ["Bronze", "Silver", "Gold", "Platinum"]

# ============================================
# FILTER OPTIONS (YOUR VERSION)
# ============================================
country_options = sorted(df["Country"].dropna().unique())
gender_options = sorted(df["Gender"].dropna().unique())
age_options = [x for x in AGE_ORDER if x in df["Age_Group"].dropna().unique()]
quarter_options = [x for x in QUARTER_ORDER if x in df["Signup_Quarter"].dropna().unique()]

#payment_options = sorted(df["Payment_Mode"].dropna().unique())
#engagement_options = [x for x in ENGAGEMENT_ORDER if x in df["Engagement_Tier"].dropna().unique()]
#value_options = [x for x in VALUE_ORDER if x in df["Value_Segment"].dropna().unique()]

# ============================================
# APP
# ============================================
app = dash.Dash(__name__)

# ============================================
# LAYOUT
# ============================================

app.layout = html.Div([

    # =====================================================
    # HEADER
    # =====================================================
    html.Div([

        html.H1(
            "Customer Churn Dashboard",
            style={
                'textAlign': 'center',
                'color': '#FFFFFF',
                'marginBottom': '10px',
                'fontFamily': 'Arial'
            }
        ),

        html.P(
            "Analyze churn behavior across demographics and engagement",
            style={
                'textAlign': 'center',
                'color': '#D3D3D3',
                'fontSize': '18px'
            }
        )

    ], style={
        'backgroundColor': '#2F4F4F',
        'padding': '25px',
        'borderRadius': '12px',
        'marginBottom': '25px'
    }),

    # =====================================================
    # FILTER SECTION
    # =====================================================
    html.Div([

        html.Div([
            html.Label("Country"),
            dcc.Dropdown(
                id='country-filter',
                options=[{'label': c, 'value': c} for c in country_options],
                placeholder="Select Country",
                multi=True
            )
        ], style={'width': '24%'}),

        html.Div([
            html.Label("Quarter"),
            dcc.Dropdown(
                id='quarter-filter',
                options=[{'label': q, 'value': q} for q in quarter_options],
                placeholder="Select Quarter",
                multi=True
            )
        ], style={'width': '24%'}),

        html.Div([
            html.Label("Gender"),
            dcc.Dropdown(
                id='gender-filter',
                options=[{'label': g, 'value': g} for g in gender_options],
                placeholder="Select Gender",
                multi=True
            )
        ], style={'width': '24%'}),

        html.Div([
            html.Label("Age Group"),
            dcc.Dropdown(
                id='age-filter',
                options=[{'label': a, 'value': a} for a in age_options],
                placeholder="Select Age Group",
                multi=True
            )
        ], style={'width': '24%'})

    ], style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'gap': '10px',
        'backgroundColor': '#F8F9FA',
        'padding': '20px',
        'borderRadius': '12px',
        'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)',
        'marginBottom': '30px'
    }),

    # =====================================================
    # KPI SECTION
    # =====================================================
    html.Div([

        html.Div(id='kpi-total', style={
            'backgroundColor': '#FFFFFF',
            'padding': '25px',
            'borderRadius': '12px',
            'width': '30%',
            'textAlign': 'center',
            'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)'
        }),

        html.Div(id='kpi-churn', style={
            'backgroundColor': '#FFFFFF',
            'padding': '25px',
            'borderRadius': '12px',
            'width': '30%',
            'textAlign': 'center',
            'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)'
        }),

        html.Div(id='kpi-ltv', style={
            'backgroundColor': '#FFFFFF',
            'padding': '25px',
            'borderRadius': '12px',
            'width': '30%',
            'textAlign': 'center',
            'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)'
        })

    ], style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'marginBottom': '30px'
    }),

    # =====================================================
    # ROW 1 CHARTS
    # =====================================================
    html.Div([

        html.Div([
            dcc.Graph(id='bar-chart')
        ], style={
            'width': '49%',
            'backgroundColor': '#FFFFFF',
            'padding': '10px',
            'borderRadius': '12px',
            'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)'
        }),

        html.Div([
            dcc.Graph(id='pie-chart')
        ], style={
            'width': '49%',
            'backgroundColor': '#FFFFFF',
            'padding': '10px',
            'borderRadius': '12px',
            'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)'
        })

    ], style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'marginBottom': '30px'
    }),

    # =====================================================
    # LINE CHART
    # =====================================================
    html.Div([

        dcc.Graph(id='quarterly-churn-line')

    ], style={
        'backgroundColor': '#FFFFFF',
        'padding': '10px',
        'borderRadius': '12px',
        'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)',
        'marginBottom': '30px'
    }),

    # =====================================================
    # ROW 2 CHARTS
    # =====================================================
    html.Div([

        html.Div([
            dcc.Graph(id='behavior-subplot')
        ], style={
            'width': '49%',
            'backgroundColor': '#FFFFFF',
            'padding': '10px',
            'borderRadius': '12px',
            'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)'
        }),

        html.Div([
            dcc.Graph(id='heatmap-chart')
        ], style={
            'width': '49%',
            'backgroundColor': '#FFFFFF',
            'padding': '10px',
            'borderRadius': '12px',
            'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)'
        })

    ], style={
        'display': 'flex',
        'justifyContent': 'space-between',
        'marginBottom': '30px'
    })

], style={
    'backgroundColor': '#F4F6F9',
    'padding': '20px',
    'fontFamily': 'Arial'
})

# ============================================
# CALLBACK
# ============================================
@app.callback(
    [
        Output('kpi-total', 'children'),
        Output('kpi-churn', 'children'),
        Output('kpi-ltv', 'children'),

        Output('pie-chart', 'figure'),
        Output('bar-chart', 'figure'),
        Output('quarterly-churn-line', 'figure'),
        Output('heatmap-chart', 'figure'),
        Output('behavior-subplot', 'figure')
    ],
    [
        Input('country-filter', 'value'),
        Input('quarter-filter', 'value'),
        Input('gender-filter', 'value'),
        Input('age-filter', 'value')
    ]
)
def update_dashboard(country, quarter, gender, age):

    dff = df.copy()

    if country:
        dff = dff[dff['Country'].isin(country)]
    if quarter:
        dff = dff[dff['Signup_Quarter'].isin(quarter)]
    if gender:
        dff = dff[dff['Gender'].isin(gender)]
    if age:
        dff = dff[dff['Age_Group'].isin(age)]

    # KPIs
    total = len(dff)
    churn_rate = round(dff['Churned'].mean() * 100, 2)
    avg_ltv = round(dff['Lifetime_Value'].mean(), 2)

    kpi1 = html.H3(f"Total Customers: {total}")
    kpi2 = html.H3(f"Churn Rate: {churn_rate}%")
    kpi3 = html.H3(f"Avg Lifetime Value: ${avg_ltv}")

    # PIE
    pie_fig = px.pie(dff, names='Churn_Status', title='Churn Distribution')

    # ENGAGEMENT BAR
    eng = dff.groupby('Engagement_Tier', as_index=False)['Churned'].mean()

    bar_fig = px.bar(
        eng,
        x='Engagement_Tier',
        y='Churned',
        title='Churn Rate by Engagement Tier'
    )

    # QUARTERLY LINE
    quarterly = dff.groupby('Signup_Quarter', as_index=False).agg(
        Total_Customers=('Churned', 'count'),
        Churned_Customers=('Churned', 'sum')
    )

    quarterly['Churn_Rate'] = (quarterly['Churned_Customers'] / quarterly['Total_Customers']) * 100
    quarterly['Retention_Rate'] = 100 - quarterly['Churn_Rate']

    fig_quarterly = go.Figure()
    fig_quarterly.add_trace(go.Scatter(
        x=quarterly['Signup_Quarter'],
        y=quarterly['Churn_Rate'],
        mode='lines+markers',
        name='Churn Rate (%)'
    ))

    fig_quarterly.add_trace(go.Scatter(
        x=quarterly['Signup_Quarter'],
        y=quarterly['Retention_Rate'],
        mode='lines+markers',
        name='Retention Rate (%)'
    ))

    fig_quarterly.update_layout(
        title="Quarterly Churn vs Retention Trend",
        xaxis_title="Signup Quarter",
        yaxis_title="Percentage",
        hovermode="x unified"
    )

    # HEATMAP
    heatmap_data = (
            dff.groupby(["Engagement_Tier", "Value_Segment"], as_index=False)
            .agg(Churn_Rate=("Churned", "mean"), Customers=("Churned", "size"))
        )
    heatmap_data["Churn_Rate"] = heatmap_data["Churn_Rate"] * 100

    heatmap_pivot = heatmap_data.pivot(
        index="Engagement_Tier",
        columns="Value_Segment",
        values="Churn_Rate",
    )

    heatmap_pivot = heatmap_pivot.reindex(
        index=[x for x in ENGAGEMENT_ORDER if x in heatmap_pivot.index],
        columns=[x for x in VALUE_ORDER if x in heatmap_pivot.columns],
    )

    fig_heatmap = px.imshow(
        heatmap_pivot,
        text_auto=".1f",
        aspect="auto",
        title="Churn Rate Heatmap: Engagement Tier vs Value Segment",
        labels=dict(color="Churn Rate %"),
    )
    #fig_heatmap = beautify(fig_heatmap, height=390)


    # SUBPLOTS
    grouped = dff.groupby('Churn_Status', as_index=False)[[
        'Login_Frequency',
        'Session_Duration_Avg',
        'Pages_Per_Session'
    ]].mean()

    fig = make_subplots(
        rows=1,
        cols=3,
        subplot_titles=[
            "Login Frequency",
            "Session Duration",
            "Pages Per Session"
        ]
    )

    fig.add_trace(go.Bar(x=grouped['Churn_Status'], y=grouped['Login_Frequency']), row=1, col=1)
    fig.add_trace(go.Bar(x=grouped['Churn_Status'], y=grouped['Session_Duration_Avg']), row=1, col=2)
    fig.add_trace(go.Bar(x=grouped['Churn_Status'], y=grouped['Pages_Per_Session']), row=1, col=3)

    fig.update_layout(title="Behavior Comparison: Churn vs Retained")

    return (
        kpi1, kpi2, kpi3,
        pie_fig,
        bar_fig,
        fig_quarterly,
        fig_heatmap,
        fig
    )

# ============================================
# RUN SERVER
# ============================================

if __name__ == '__main__':
    app.run(debug=True)