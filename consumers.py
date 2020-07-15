# Import Stuff here
#========================================================
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
import datetime
import dash_auth
import bs4
from requests import get
from bs4 import BeautifulSoup
from random import randint # for random integer value
from dash.dependencies import Input, Output, State
from datetime import date, timedelta # to get date today
from web3 import Web3
from dash.exceptions import PreventUpdate

#========================================================
# Stylish stuff here
#========================================================
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)

CONTENT_STYLE = {
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

RB_LOGO = "https://raw.githubusercontent.com/MKallun/Rice-in-a-Block/master/108155783_584586912419739_2665953725697700139_n%20(2).png"

# Blockchain stuff here
#========================================================

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]


abi = json.loads('[{"inputs":[{"internalType":"string","name":"_UserName","type":"string"}],"name":"Login","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_UserName","type":"string"},{"internalType":"string","name":"_Password","type":"string"}],"name":"Register","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_Manufacturer","type":"string"},{"internalType":"string","name":"_Brand","type":"string"},{"internalType":"string","name":"_Area","type":"string"},{"internalType":"string","name":"_Status","type":"string"},{"internalType":"string","name":"_StatusRecieved","type":"string"},{"internalType":"uint256","name":"_StatusWeight","type":"uint256"},{"internalType":"uint256","name":"_Date","type":"uint256"},{"internalType":"uint256","name":"_Year","type":"uint256"},{"internalType":"uint256","name":"_Month","type":"uint256"},{"internalType":"uint256","name":"_Day","type":"uint256"},{"internalType":"uint256","name":"_Weight","type":"uint256"},{"internalType":"uint256","name":"_Price","type":"uint256"}],"name":"enterRiceInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getArea","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getBrand","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getDay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getManu","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getMonth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatus","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusRecieved","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getStatusWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTransID","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_StoreId","type":"uint256"}],"name":"getYear","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"newcount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"transactionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

# needs to be changed to match address in remix solidity
address = web3.toChecksumAddress("0xF5Aeb9F211522A8eeAD06A1c105DeceCbB8339a2")

contract = web3.eth.contract(address=address, abi=abi)



# this is the dataframwe



# Webpage stuff
#========================================================

# Navbar
#========================================================
buttons = dbc.Row(
    [
        dbc.Col(
            dbc.Button("AREA GRAPH", href="/page-1", id="page-1-link"),
            width="auto",
        ),
        dbc.Col(
            dbc.Button("DATE GRAPH", href="/page-3", id="page-3-link"),
            width="auto",
        ),
        dbc.Col(
            dbc.Button("LIST", href="/page-2", id="page-2-link"),
            width="auto",
        ),
        dbc.Col(
            dbc.Button("NEWS", href="/page-4", id="page-4-link"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)


navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=RB_LOGO, height="50px")),
                ],

                align="center",
                no_gutters=True,
            ),
            href="#",
        ),
        dbc.Collapse(buttons, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
)
#========================================================
# Graph
#========================================================

Graph1 = html.Div(
    [
        html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div(dcc.Graph(id='live-update-date'))),
                ]
            ),
        ]
        )
]
)

Graph2 = html.Div(
    [
        html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div(dcc.Graph(id='live-update-area'))),
                ]
            ),
        ]
        )
]
)


#========================================================
# Table
#========================================================
Table1 = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(" "))),
        dbc.Row(
            [
                #dbc.Col(html.Div(" "), width=1),
                dbc.Col(html.Div(dcc.Graph(id='live-update-table'))),
                #dbc.Col(html.Div(" "), width=1),
            ]
        ),
    ]
)

#========================================================
# webscraping
# this gets selected value from URL, in this case URL being rappler 
# and getting values for headlin, date of publish, preview and link
# then adds it to a dataframe 
try:
    url = 'https://agriculture.einnews.com/search/rice+philippines/?search%5B%5D=news&search%5B%5D=press&order=relevance'
    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    bs4.BeautifulSoup
    movie_containers = html_soup.find_all('div', class_ = 'article-content')
            

    headlines = []
    dates = []
    previews = []
    links = []

    for container in movie_containers:

        headline = container.h3.a.text
        headlines.append(headline)

        date1 = str(container.div.find('span', class_ = 'date').text)
        dates.append(date1)

        preview = preview = container.p.text
        previews.append(preview)

        link = container.find('a')['href'].lstrip('https://agriculture.einnews.com/article/')
        links.append(link)
        print(links)


    #================================================================
    # creates 2 dataframe
    # this is dataframe containing all headline and links 
    headline_df = pd.DataFrame({
            'headline': headlines,
            'link': links
            })
    headline_df['link'] = 'http://agriculture.einnews.com/article/' + headline_df['link'].astype(str)  

    # this is dataframe containing all dates and previews
    info_df = pd.DataFrame({
            'date': dates,
            'preview': previews,
    })



    # this calls the table function and passes headline_df to add hyperlink to headline

    table_header = [
        html.Thead(html.Tr([html.Th("Headline",colSpan=1), html.Th("Date",colSpan=3)]))
    ]

    row1 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[0]['headline'],href=headline_df.iloc[0]['link'])))), html.Td(info_df.iloc[0]['date'])])
    row2 = html.Tr([html.Td(info_df.iloc[0]['preview']), html.Td(" ")])

    row3 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[1]['headline'],href=headline_df.iloc[1]['link'])))), html.Td(info_df.iloc[1]['date'])])
    row4 = html.Tr([html.Td(info_df.iloc[1]['preview']), html.Td(" ")])

    row5 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[2]['headline'],href=headline_df.iloc[2]['link'])))), html.Td(info_df.iloc[2]['date'])])
    row6 = html.Tr([html.Td(info_df.iloc[2]['preview']), html.Td(" ")])

    row7 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[3]['headline'],href=headline_df.iloc[3]['link'])))), html.Td(info_df.iloc[3]['date'])])
    row8 = html.Tr([html.Td(info_df.iloc[3]['preview']), html.Td(" ")])

    row9 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[4]['headline'],href=headline_df.iloc[4]['link'])))), html.Td(info_df.iloc[4]['date'])])
    row10 = html.Tr([html.Td(info_df.iloc[4]['preview']), html.Td(" ")])

    row11 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[5]['headline'],href=headline_df.iloc[5]['link'])))), html.Td(info_df.iloc[5]['date'])])
    row12 = html.Tr([html.Td(info_df.iloc[5]['preview']), html.Td(" ")])

    row13 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[6]['headline'],href=headline_df.iloc[6]['link'])))), html.Td(info_df.iloc[6]['date'])])
    row14 = html.Tr([html.Td(info_df.iloc[6]['preview']), html.Td(" ")])

    row15 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[7]['headline'],href=headline_df.iloc[7]['link'])))), html.Td(info_df.iloc[7]['date'])])
    row16 = html.Tr([html.Td(info_df.iloc[7]['preview']), html.Td(" ")])

    row17 = html.Tr([html.Td(html.H4(html.B(html.A(headline_df.iloc[8]['headline'],href=headline_df.iloc[8]['link'])))), html.Td(info_df.iloc[8]['date'])])
    row18 = html.Tr([html.Td(info_df.iloc[8]['preview']), html.Td(" ")])

    spacer = html.Tr([html.Td(" "), html.Td(" ")])

    table_body = [html.Tbody([row1, row2, spacer, row3, row4, spacer, row5, row6, spacer, row7, row8, spacer, row9, row10, spacer, row11, row12, spacer, row13, row14, spacer, row15, row16, spacer, row17, row18])]

    table3 = dbc.Table(table_header + table_body, borderless=True)
    Table2 = html.Div(
        [
            dbc.Row(dbc.Col(html.Div(" "))),
            dbc.Row(
                [
                    dbc.Col(html.Div(" "), width=2),
                    dbc.Col(html.Div(table3), width=8),
                    dbc.Col(html.Div(" "), width=2),
                ]
            ),
        ]
    )
except:
    card_content = [
        dbc.CardHeader("Site Error"),
        dbc.CardBody(
            [
                html.H5("Site Error", className="card-title"),
                html.P(
                    "There are some issues loading https://agriculture.einnews.com, our source of rice related news",
                    className="card-text",
                ),
            ]
        ),
    ]

    cards = dbc.Row(
        [dbc.Col(dbc.Card(card_content, color="dark", outline=True))]
    )
    Table2 = html.Div(
        [
            dbc.Row(dbc.Col(html.Div(" "))),
            dbc.Row(
                [
                    dbc.Col(html.Div(" "), width=2),
                    dbc.Col(html.Div(cards), width=8),
                    dbc.Col(html.Div(" "), width=2),
                ]
            ),
        ]
    )
#========================================================

content = html.Div(id="page-content", style=CONTENT_STYLE)
emp = html.Div(dbc.Row(html.Div("CURRENTLY NOT AVAILABLE!"),align="center"))
app.layout = html.Div([
    dcc.Location(id="url"), 
    navbar, 
    html.Div(" "),
    html.Div([
        dbc.Row(
            [
                dbc.Col(html.Div(" "), align="start", width=3),
                dbc.Col(html.Div("This program is just the prototype version of the actual program that the developers have imagined."), align="center", width=8),
                dbc.Col(html.Div(dcc.Interval(
                        id='interval-component',
                        interval = 30*1000,
                        n_intervals=0
                    ))),
                dbc.Col(html.Div(" "), align="end"),
            ],
        ),
        dbc.Row(
            dbc.Col(html.Div(id='live-update-time'),width={"size": 1, "offset": 1}),
        ),
        dbc.Row([
            dbc.Col(html.Div(content)),
        ])
    ]),
    ])

@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):

    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    elif pathname == "/page-2":
        return False, True, False
    elif pathname == "/page-3":
        return False, False, True
    return [pathname == f"/page-{i}" for i in range(1, 4)]
#=============================================================================================
@app.callback(
        Output("page-content", "children"),
    [
        Input("url", "pathname")
    ],
    )
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return Graph2
    elif pathname == "/page-2":
        return Table1

    elif pathname == "/page-3":
        return Graph1

    elif pathname == "/page-4":
        return Table2

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
#=======================================================================
@app.callback(
    Output('live-update-time','children'),
    [Input('interval-component','n_intervals')]
)
def update_time(n):
    dates = datetime.date.today()
    f"{dates.month:02d}" #format to keep the month double digit e.g. 01 for january
    f"{dates.day:02d}" #format to keep the day double digit e.g. 01
    datey = str(dates.year)
    dated = str(dates.day)
    #print("O")
    return [
        html.Span('Date: {} {}, {}'.format(dates.strftime("%B"), dated, datey))
    ]

@app.callback(
    Output('live-update-date','figure'),
    [Input('interval-component','n_intervals')]
)
def update_time(n):
    dates = datetime.date.today()
    f"{dates.month:02d}" #format to keep the month double digit e.g. 01 for january
    f"{dates.day:02d}" #format to keep the day double digit e.g. 01
    datey = str(dates.year)
    datem = str(dates.month)
    dated = str(dates.day)
    loop = contract.functions.getTransID().call()
    limit = loop + 1
    dfall = pd.DataFrame()   # this is for all the rice info
    for i in range (1, int(limit)):
        if (int(contract.functions.getYear(int(i)).call()) == int(datey)):
            stId = i
            manu = contract.functions.getManu(int(i)).call()
            bran = contract.functions.getBrand(int(i)).call()
            area = contract.functions.getArea(int(i)).call()
            stat = contract.functions.getStatus(int(i)).call() # Status (Delivered / Recieved)
            stRe = contract.functions.getStatusRecieved(int(i)).call()  # StatusRecieved (Damaged / Stolen / Complete)
            stWe = contract.functions.getStatusWeight(int(i)).call()  # StatusWeight (if stRe = Complete : stWe = 0)
            fuldate = str(contract.functions.getDate(int(i)).call())
            year = contract.functions.getYear(int(i)).call()
            mont = contract.functions.getMonth(int(i)).call()
            day = contract.functions.getDay(int(i)).call()
            wght = contract.functions.getWeight(int(i)).call()
            pric = contract.functions.getPrice(int(i)).call()
            rewg = wght-stWe # This is for the remaining weight
            s_datetime = datetime.datetime.strptime(fuldate, '%Y%m%d')
        Rice = {
            'Manufacturer': [manu],
            'Brand': [bran],
            'Area': [area],
            'Status': [stat],
            'StatusRecieved': [stRe],
            'StatusWeight': [stWe],
            'Date': [s_datetime],
            'Year': [year],
            'Month': [mont],
            'Day': [day],
            'Weight': [wght],
            'Price': [pric],
            'RemainingWeight': [rewg]
            }
        dfnew = pd.DataFrame(Rice, columns= ['Manufacturer', 'Brand', 'Area', 'Status', 'StatusRecieved', 'StatusWeight', 'Date', 'Year', 'Month', 'Day', 'Weight', 'Price', 'RemainingWeight'])
        dfall = dfall.append(dfnew, ignore_index=True)
    try:
        jan = int(dfall.loc[dfall['Month'] == 1,'Weight'].sum()) 
        feb = int(dfall.loc[dfall['Month'] == 2,'Weight'].sum()) 
        mar = int(dfall.loc[dfall['Month'] == 3,'Weight'].sum()) 
        apr = int(dfall.loc[dfall['Month'] == 4,'Weight'].sum()) 
        may = int(dfall.loc[dfall['Month'] == 5,'Weight'].sum()) 
        jun = int(dfall.loc[dfall['Month'] == 6,'Weight'].sum()) 
        jul = int(dfall.loc[dfall['Month'] == 7,'Weight'].sum()) 
        aug = int(dfall.loc[dfall['Month'] == 8,'Weight'].sum()) 
        sep = int(dfall.loc[dfall['Month'] == 9,'Weight'].sum()) 
        octo = int(dfall.loc[dfall['Month'] == 10,'Weight'].sum()) 
        nov = int(dfall.loc[dfall['Month'] == 11,'Weight'].sum()) 
        dec = int(dfall.loc[dfall['Month'] == 12,'Weight'].sum()) 
        print("Updating Date Graph...")
    except:
        jan = 0
        feb = 0
        mar = 0
        apr = 0
        may = 0
        jun = 0
        jul = 0
        aug = 0
        sep = 0
        octo = 0 
        nov = 0
        dec = 0
        print("Oh no!")
    Month = {
        'Months' : ['January', 'February','March','April','May','June','July','August','September','October','November','December'],
        'Weight' : [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]
    }
    dfmon = pd.DataFrame(Month, columns=['Weight','Months'])
    datefig = px.bar(dfmon, x="Months", y="Weight", title='Total Rice Weight / Date', color="Months", height=500)
    return datefig

@app.callback(
    Output('live-update-area','figure'),
    [Input('interval-component','n_intervals')]
)
def update_area(n):
    dates = datetime.date.today()
    f"{dates.month:02d}" #format to keep the month double digit e.g. 01 for january
    f"{dates.day:02d}" #format to keep the day double digit e.g. 01
    datey = str(dates.year)
    datem = str(dates.month)
    dated = str(dates.day)
    loop = contract.functions.getTransID().call()
    limit = loop + 1
    dfall = pd.DataFrame()   # this is for all the rice info
    for i in range (1, int(limit)):
        if (int(contract.functions.getMonth(int(i)).call()) == int(datem) and int(contract.functions.getYear(int(i)).call()) == int(datey)):
            stId = i
            manu = contract.functions.getManu(int(i)).call()
            bran = contract.functions.getBrand(int(i)).call()
            area = contract.functions.getArea(int(i)).call()
            stat = contract.functions.getStatus(int(i)).call() # Status (Delivered / Recieved)
            stRe = contract.functions.getStatusRecieved(int(i)).call()  # StatusRecieved (Damaged / Stolen / Complete)
            stWe = contract.functions.getStatusWeight(int(i)).call()  # StatusWeight (if stRe = Complete : stWe = 0)
            fuldate = str(contract.functions.getDate(int(i)).call())
            year = contract.functions.getYear(int(i)).call()
            mont = contract.functions.getMonth(int(i)).call()
            day = contract.functions.getDay(int(i)).call()
            wght = contract.functions.getWeight(int(i)).call()
            pric = contract.functions.getPrice(int(i)).call()
            rewg = wght-stWe # This is for the remaining weight
            s_datetime = datetime.datetime.strptime(fuldate, '%Y%m%d')
        Rice = {
            'Manufacturer': [manu],
            'Brand': [bran],
            'Area': [area],
            'Status': [stat],
            'StatusRecieved': [stRe],
            'StatusWeight': [stWe],
            'Date': [s_datetime],
            'Year': [year],
            'Month': [mont],
            'Day': [day],
            'Weight': [wght],
            'Price': [pric],
            'RemainingWeight': [rewg]
            }
        dfnew = pd.DataFrame(Rice, columns= ['Manufacturer', 'Brand', 'Area', 'Status', 'StatusRecieved', 'StatusWeight', 'Date', 'Year', 'Month', 'Day', 'Weight', 'Price', 'RemainingWeight'])
        dfall = dfall.append(dfnew, ignore_index=True)
        dfarea = dfall.groupby(['Area', 'Month'])['Weight'].sum()
        #print(dfarea)
    try:
        reg1 = int(dfall.loc[dfall['Area'] == 'REGION I','Weight'].sum()) 
        reg2 = int(dfall.loc[dfall['Area'] == 'REGION II','Weight'].sum()) 
        reg3 = int(dfall.loc[dfall['Area'] == 'REGION III','Weight'].sum()) 
        reg4 = int(dfall.loc[dfall['Area'] == 'REGION IV','Weight'].sum()) 
        reg5 = int(dfall.loc[dfall['Area'] == 'REGION V','Weight'].sum()) 
        reg6 = int(dfall.loc[dfall['Area'] == 'REGION VI','Weight'].sum()) 
        reg7 = int(dfall.loc[dfall['Area'] == 'REGION VII','Weight'].sum()) 
        reg8 = int(dfall.loc[dfall['Area'] == 'REGION VIII','Weight'].sum()) 
        reg9 = int(dfall.loc[dfall['Area'] == 'REGION IX','Weight'].sum()) 
        reg10 = int(dfall.loc[dfall['Area'] == 'REGION X','Weight'].sum()) 
        reg11 = int(dfall.loc[dfall['Area'] == 'REGION XI','Weight'].sum()) 
        reg12 = int(dfall.loc[dfall['Area'] == 'REGION XII','Weight'].sum()) 
        reg13 = int(dfall.loc[dfall['Area'] == 'NCR','Weight'].sum()) 
        reg14 = int(dfall.loc[dfall['Area'] == 'BARMM','Weight'].sum()) 
        reg15 = int(dfall.loc[dfall['Area'] == 'CARAGA','Weight'].sum()) 
        print("Updating Area Graph...")
    except:
        reg1 = 0
        reg2 = 0
        reg3 = 0
        reg4 = 0
        reg5 = 0
        reg6 = 0
        reg7 = 0
        reg8 = 0
        reg9 = 0
        reg10 = 0
        reg11 = 0
        reg12 = 0
        reg13 = 0
        reg14 = 0
        reg15 = 0

    Location = {
        'Location' : ['REGION I','REGION II','REGION III','REGION IV','REGION V','REGION VI','REGION VII','REGION VIII','REGION IX','REGION X','REGION XI','REGION XII','NCR','BARMM','CARAGA'],
        'Weight' : [reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9,reg10,reg11,reg12,reg13,reg14,reg15]
    }

    dfloc = pd.DataFrame(Location,columns=['Weight',  'Location'])
    barfig = px.bar(dfloc, x="Location", y="Weight", title='Total Rice Weight / Region', color="Location", height=500)
    return barfig

#=======================================================================

@app.callback(
    Output('live-update-table','figure'),
    [Input('interval-component','n_intervals')]
)
def update_tabble(n):
    loop = contract.functions.getTransID().call()
    limit = loop + 1
    dfall = pd.DataFrame()   # this is for all the rice info
    for i in range (1, int(limit)):
        stId = i
        manu = contract.functions.getManu(int(i)).call()
        bran = contract.functions.getBrand(int(i)).call()
        area = contract.functions.getArea(int(i)).call()
        stat = contract.functions.getStatus(int(i)).call() # Status (Delivered / Recieved)
        stRe = contract.functions.getStatusRecieved(int(i)).call()  # StatusRecieved (Damaged / Stolen / Complete)
        stWe = contract.functions.getStatusWeight(int(i)).call()  # StatusWeight (if stRe = Complete : stWe = 0)
        fuldate = str(contract.functions.getDate(int(i)).call())
        year = contract.functions.getYear(int(i)).call()
        mont = contract.functions.getMonth(int(i)).call()
        day = contract.functions.getDay(int(i)).call()
        wght = contract.functions.getWeight(int(i)).call()
        pric = contract.functions.getPrice(int(i)).call()
        rewg = wght-stWe # This is for the remaining weight
        s_datetime = datetime.datetime.strptime(fuldate, '%Y%m%d')
        Rice = {
            'Manufacturer': [manu],
            'Brand': [bran],
            'Area': [area],
            'Status': [stat],
            'StatusRecieved': [stRe],
            'StatusWeight': [stWe],
            'Date': [s_datetime],
            'Year': [year],
            'Month': [mont],
            'Day': [day],
            'Weight': [wght],
            'Price': [pric],
            'RemainingWeight': [rewg]
            }
        dfnew = pd.DataFrame(Rice, columns= ['Manufacturer', 'Brand', 'Area', 'Status', 'StatusRecieved', 'StatusWeight', 'Date', 'Year', 'Month', 'Day', 'Weight', 'Price', 'RemainingWeight'])
        dfall = dfall.append(dfnew, ignore_index=True)
    try:
        tablefig = go.Figure(data=[go.Table(
            header=dict(
                values=['<b>Date</b>','<b>Area</b>','<b>Manufacturer</b>','<b>Brand</b>','<b>Status</b>','<b>Damaged, Stolen, Complete</b>','<b>Weight(kg)</b>','<b>Weight of Damage</b>','<b>Usable/Sellable Rice(kg)</b>','<b>Price per kg</b>'],
                line_color='darkslategray',
                align=['center'],
                font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[
                    dfall.Date,
                    dfall.Area,
                    dfall.Manufacturer,
                    dfall.Brand,
                    dfall.Status,
                    dfall.StatusRecieved,
                    dfall.Weight,
                    dfall.StatusWeight,
                    dfall.RemainingWeight,
                    dfall.Price
                    ],
                line_color='darkslategray',
                align = ['center'],
                font = dict(color = 'darkslategray', size = 12),
            ),
            )
        ])
        print("Updating Table...")
    except:
            tablefig = go.Figure(data=[go.Table(
            header=dict(
                values=['<b>Date</b>','<b>Area</b>','<b>Manufacturer</b>','<b>Brand</b>','<b>Status</b>','<b>Damaged, Stolen, Complete</b>','<b>Weight(kg)</b>','<b>Weight of Damage</b>','<b>Usable/Sellable Rice(kg)</b>','<b>Price per kg</b>'],
                line_color='darkslategray',
                align=['center'],
                font=dict(color='black', size=12)
            ),
            cells=dict(
                values=[
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None
                    ],
                line_color='darkslategray',
                align = ['center'],
                font = dict(color = 'darkslategray', size = 12),
            ),
            ),
            
        ])
    return tablefig
#=======================================================================
if __name__ == '__main__':
    app.run_server(debug=True)

