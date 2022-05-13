#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:40:10 2021

@author: sebastian
"""

import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import base64
from textwrap import dedent



image_filename_cr2 = 'logo_footer110.png'
encoded_image_cr2 = base64.b64encode(open(image_filename_cr2, 'rb').read()).decode('ascii')
image_filename_DMC = 'logo_cerro.png'
encoded_image_DMC = base64.b64encode(open(image_filename_DMC, 'rb').read()).decode('ascii')
image_filename_cr2_celeste = 'cr2_celeste.png'
encoded_image_cr2_celeste = base64.b64encode(open(image_filename_cr2_celeste, 'rb').read()).decode('ascii')
image_filename_GWA = 'logo_footer110.png'
encoded_image_GWA = base64.b64encode(open(image_filename_GWA, 'rb').read()).decode('ascii')
image_filename_GWA_center = 'GAW_index.png'
encoded_image_GWA_center = base64.b64encode(open(image_filename_GWA_center, 'rb').read()).decode('ascii')
image_filename_rapa_nui = 'mapa_tres.png'
encoded_image_rapa_nui = base64.b64encode(open(image_filename_rapa_nui, 'rb').read()).decode('ascii')


fig = go.Figure(go.Scattergeo(lat=[-27.16], lon=[-109.43]))
fig.update_geos(projection_type="orthographic", projection_rotation=dict(lon=-80, lat=-30), bgcolor='rgba(0,0,0,0)',
                lataxis_showgrid=True, lonaxis_showgrid=True
                
                  )
fig.update_layout(height=200, margin={"r":0,"t":0,"l":0,"b":0}, 
                  plot_bgcolor='#f6f6f6',
            paper_bgcolor='#f6f6f6')



fig2 = go.Figure(go.Scattergeo(lat=[-30.169], lon=[-70.804]))
fig2.update_geos(projection_type="orthographic", projection_rotation=dict(lon=-80, lat=-30), bgcolor='rgba(0,0,0,0)',
                lataxis_showgrid=True, lonaxis_showgrid=True
                
                  )
fig2.update_layout(height=200, margin={"r":0,"t":0,"l":0,"b":0}, 
                  plot_bgcolor='#f6f6f6',
            paper_bgcolor='#f6f6f6')




###############diccionario con fechas##########################################

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
################################### Configuración Encabezado html.Img(src='data:image/png;base64,{}'.format(encoded_image_GWA_center),style={'height':'400px', 'margin-left':'100px'})Página Web##############    
    html.Div([
        html.Div([html.H2("", style={'font-size':'18pt','color': 'white','font-family': 'Abel', 'font-weight': '200 !important', 'margin-top': '28px', 'margin-left':'10px'})], style={'position':'absolute','display': 'inline-block'}),
             html.A([       
             html.Img(src='data:image/png;base64,{}'.format(encoded_image_cr2), style={'height':'80px'})],href = 'http://www.cr2.cl/', style={'margin-left': '400px', 'position':'absolute'}),
             html.A([     
             html.Img(src='data:image/png;base64,{}'.format(encoded_image_DMC),style = {'height':'80px'})], href='http://www.meteochile.gob.cl/PortalDMC-web', style={'margin-left': '700px', 'position':'absolute'}),
             html.A([     
             html.Img(src='data:image/png;base64,{}'.format(encoded_image_GWA),style = {'height':'80px'})], href='https://www.wmo.int/gaw/', style={'margin-left': '100px', 'position':'absolute'}),
            html.Div([
                html.H2("Language:" , style={'font-size':'15pt','color': 'white', 'margin-top': '0px'})], style={'margin-left': '2050px','display': 'inline-block', 'position':'absolute'}
                )
            ,
            html.Div([
        daq.ToggleSwitch(
                    id='Switch_Lang',
                    className='SwicthLang',
                    value=True,
                    )], style={'backgroundColor':'#1766a0','margin-top':'30px','margin-left': '0px','display': 'inline-block', 'position':'absolute'})
        
    ],
    style={'backgroundColor':'limegreen', 'height':'80px'}),
#####################################################################################    
    html.Div(id='tabs-content', style={'backgroundcolor':'#f6f6f6'})
])    
########################################Contenido Página Web#########################
@app.callback(Output('tabs-content', 'children'),
              Input('Switch_Lang', 'value'))
def Web_Language(Switch_Lang):
#####################################Versión en Ingles###############################    
    if Switch_Lang==True:
        return [html.Div([
             html.Div([
            html.H1("Estación de Alta Montaña Cerro Tres Puntas (Refugio Andino)", style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '28px','color': 'limegreen','backgroundColor': '#f6f6f6'}),
            dcc.Markdown(dedent(f'''
                                El refugio Andino ubicado a 3685 m en los límites de la estación de esquí Valle Nevado, a 25 km de Santiago – Región Metropolitana 33.19”12 °S 70.13”55°W)
                                El Refugio Andino es un proyecto que consiste en medir la meteorología y otros parámetros atmosféricos  cómo la contaminación del aire y el flujo solar en la Cordillera cerca de Santiago.
                                El refugio se instaló en abril 2019 y la estación de meteorología en enero 2020. Un etalametro para medir Carbono negro y un Radiometro Aeronet de Aerosol Optical depth serían instalado cuando las condiciones permita .
                                La información de del Refugio Andino está disponible en forma libre y en tiempo real.
              '''), style={'margin-left':'24px'}),
            html.H1("Financiamiento", style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '28px','color': 'limegreen','backgroundColor': '#f6f6f6'}),
            dcc.Markdown(dedent(f'''
                              El Refugio Andino fue concebido inicialmente como parte del Centro de Ciencia del Clima y la Resiliencia (CR)2, un centro de excelencia FONDAP-CONICYT(15110009) constituido el año 2013 por investigadores de la Universidad de Chile, Universidad de Concepción y Universidad Austral de Chile. 
                              '''), style={'margin-left':'24px'}),
            html.H1("Equipo", style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '28px','color': 'limegreen','backgroundColor': '#f6f6f6'}),
          dcc.Markdown(dedent(f''' 
                                * Roberto Rondanelli (Director del Proyecto, académico DGF y CR2) 
                                * José Miguel Campillo (Instrumentista DGF) 
                                * Zoë Fleming (Investigadora CR2, química atmosférica)
                                * Nicolás Huneeus (Académico DGF y CR2) 
                                * Laura Gallardo (Académico DGF y CR2) 
                                * Francisca Muñoz (Encargada de Datos y Cómputos, CR2) 
                                * Cecilia Montecino (Jefe Administrativa, CR2) 
                                * Susana Bustos (Apoyo en coordinación, CR2) 
                                 
                              '''), style={'margin-left':'24px'}),

            html.H1("Bitácora de funcionamiento", style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '28px','color': 'limegreen','backgroundColor': '#f6f6f6'}),
          dcc.Markdown(dedent(f''' 
                                1. 3 enero 2020 – ingeniería y Proyectos – instalación final de los instrumentos en la torre
                                2. 31 enero 2020 - visita
                                3. 19 febrero 2020 - reparaciones
                                4. 2 septiembre 2020 - visita
                                5. 30 septiembre 2020- visita
                                6. 1 diciembre 2020- cambio de datalogger y enchufar pluviometro
                                7. 28 enero 2021 anticongelante dejado en el pluviometro
                                8. 1 abril arquitectos empezan a poner plataforma

                                 
                              '''), style={'margin-left':'24px'}),

          ],
            style={'color': 'black', 'width':'60%','fontFamily': '"Times New Roman"'
                                                    ,'backgroundColor': '#f6f6f6', 'display': 'inline-block', 'margin-top':'50px', 'border-right': '2px solid #0668a1'}),
                              html.Div([
                                  html.H2(html.A("Cerro tres puntas",href = 'https://rapanui.wayra.cr2.cl/' ), style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '22px','color': 'limegreen','backgroundColor': '#f6f6f6'}),
                                  html.A([       
             html.Img(src='data:image/png;base64,{}'.format(encoded_image_rapa_nui), style={'height':'680px'})],href = 'https://rapanui.wayra.cr2.cl/', style={'margin-left': '50px'}),
                                  
                                  dcc.Markdown(
                                      dedent(f'''
                                             ''')) ,                                      
                                  ], style={'color': 'black', 'width':'40%','fontFamily': '"Times New Roman"'
                                                    ,'backgroundColor': '#f6f6f6','float':'right' ,'display': 'inline-block', 'margin-top':'50px'})
                              
                              ], style={'backgroundColor': '#f6f6f6'})]

#######################################Version en Español ##########################      
    if Switch_Lang==False:
        return [html.Div([
             html.Div([
            html.H1("Global Atmospheric Watch (GAW) stations in Chile", style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '28px','color': 'limegreen','backgroundColor': '#f6f6f6'}),
            dcc.Markdown(dedent(f'''
                The World Meteorological Organization (WMO) established the Global Atmospheric Watch (GAW) program to assess, quantify and provide a basis for predicting changes in atmospheric composition in 1989. Currently,
                the GAW monitoring network consists of 30 fully equipped GAW stations, and ca. 400 regional stations, including contributing stations,
                that collect data on greenhouse gases, aerosols, precipitation chemistry, etc. These data are collected in data centers and made publically available over the internet: https://gawsis.meteoswiss.ch/GAWSIS/#/ 
                '''), style={'margin-left':'24px'})
          ,html.Img(src='data:image/png;base64,{}'.format(encoded_image_GWA_center),style={'height':'400px', 'margin-left':'100px'}),
          dcc.Markdown(dedent(f'''
                              As part of the sub-regional program for the southern cone of South America, three stations were installed in Chile under the auspices of GAW and the Chilean Weather Office (In Spanish Dirección Meteorológica de Chile, DMC) by the mid-1990. Namely, an O3 sounding device on Rapa Nui (27ºS, 109ºW, 51 m a.s.l.); a surface O3 monitor, meteorological and radiation sensors at Cerro Tololo (30ºS, 70ºW, 2200 m a.s.l.); and a multiband radiometer at Valdivia (39.8ºS, 73ºW, 10 m a.s.l.). 
                              Unfortunately, the Valdivia station was destroyed in a fire in the mid-2000. 
                              Cerro Tololo and Rapa Nui have been kept in operation rather continuously since the mid 1990’s, approaching today a 25-year record each. Moreover, Cerro Tololo has been expanded. Presently, methane, carbon dioxide, carbon monoxide, radiation and aerosol monitors are operating there. Publications that have provided analyses of these data are listed below.
                              Principal Investigators: Laura Gallardo (CR2, DGF, Universidad de Chile) and Carmen Vega (DMC)
                              Site manager: Francisca Muñoz (CR2)
                              Data Scientists: Camilo Menares (CR2), Charlie Opazo (CR2, DGF) and Sebastián Villalón (CR2)
                              In this joint platform between the Center for Climate and Resilience Research and the Chilean Weather Office, we present Tololo and Rapa Nui data, and provide statistical analyses including decadal trends. This platform is complementary to designated data providers within GAW.
                '''), style={'margin-left':'24px'}),
                
                html.H1("Papers", style={'text-align': 'center','font-family': 'Abel','font-size': '28px','color': 'limegreen','backgroundColor': '#f6f6f6'}),
                dcc.Markdown(dedent(f'''
                    
                    a) **Rapa Nui**
                    
                             
                    Gallardo, L., Henríquez, A., Thompson, A. M., Rondanelli, R., Carrasco, J., Orfanoz-Cheuquelaf, A., et al. (2016). The first twenty years (1994-2014) of ozone soundings from Rapa Nui (27°S, 109°W, 51m a.s.l.). Tellus, Ser. B Chem. Phys. Meteorol. 68, 29484. doi:10.3402/tellusb.v68.29484.
                    
                    Calderón, J. and Fuenzalida, H. 2014. Radiación ultravioleta en Isla de Pascua: factores climáticos y ozono total. Stratus 2, 8. Revista de la Dirección Meteorológica de Chile. ISSN 0719-4544
                    
                    
                    b) **Tololo**
                
                    Anet, G. J., Steinbacher, M., Gallardo, L., Velásquez Álvarez, A. P., Emmenegger, L., and Buchmann, B. (2017). Surface ozone in the Southern Hemisphere: 20 years of data from a site with a unique setting in El Tololo, Chile. Atmos. Chem. Phys. 17, 6477–6492. doi:10.5194/acp-17-6477-2017.
                    
                    Gallardo, L., Carrasco, J., and Olivares, G. (2000). An analysis of ozone measurements at Cerro Tololo (30°S, 70°W, 2200 m.a.s.l.) in Chile. Tellus, Ser. B Chem. Phys. Meteorol. 52, 50–59. doi:10.3402/tellusb.v52i1.16081.
                    
                    Kalthoff, N., Bischoff-Gauß, I., Fiebig-Wittmaack, M., Fiedler, F., Thürauf, J., Novoa, E., et al. (2002). Mesoscale wind regimes in Chile at 30°S. J. Appl. Meteorol. 41, 953–970. doi:10.1175/1520-0450(2002)041<0953:MWRICA>2.0.CO;2.
                    
                    Rondanelli, R., Gallardo, L., and Garreaud, R. D. (2002). Rapid changes in ozone mixing ratios at Cerro Tololo (30°10′S, 70°48′W, 2200 m) in connection with cutoff lows and deep troughs. J. Geophys. Res. Atmos. 107, ACL 6-1-ACL 6-15. doi:10.1029/2001JD001334.
                        
                    
                    c) **Valdivia**
                    
                    Diaz, S., Camilión, C., Deferrari, G., Fuenzalida, H., Armstrong, R., Booth, C., et al. (2006). Ozone and UV Radiation over Southern South America: Climatology and Anomalies. Photochem. Photobiol. 82, 834–843. doi:https://doi.org/10.1562/2005-09-26-RA-697.

                    Huovinen, P., Gómez, I., and Lovengreen, C. (2006). A Five-year Study of Solar Ultraviolet Radiation in Southern Chile (39° S): Potential Impact on Physiology of Coastal Marine Algae? Photochem. Photobiol. 82, 515–522. doi:https://doi.org/10.1562/2005-07-05-RA-601.

                    Lovengreen, C., Fuenzalida, H., and Villanueva, L. (2000). Ultraviolet solar radiation at Valdivia, Chile (39.8°S). Atmos. Environ. 34, 4051–4061. doi:10.1016/S1352-2310(00)00227-2.
                
               '''), style={'margin-left':'60px'}) ,

          ],
            style={'color': 'black', 'width':'60%','fontFamily': '"Times New Roman"'
                                                    ,'backgroundColor': '#f6f6f6', 'display': 'inline-block', 'margin-top':'50px', 'border-right': '2px solid #0668a1'}),
                              html.Div([
                                  html.H2(html.A("Rapa Nui Dashboard",href = 'https://rapanui.wayra.cr2.cl/' ), style={'margin-left':'10px',
                                                                                     'text-align': 'center','font-family': 'Abel','font-size': '22px','color': 'limegreen','backgroundColor': '#f6f6f6'}),
                                  html.A([       
             html.Img(src='data:image/png;base64,{}'.format(encoded_image_rapa_nui), style={'height':'200px'})],href = 'https://rapanui.wayra.cr2.cl/', style={'margin-left': '50px'}),
                                  
                                  dcc.Markdown(
                                      dedent(f'''
                                             ''')) ,                                      
                                  ], style={'color': 'black', 'width':'40%','fontFamily': '"Times New Roman"'
                                                    ,'backgroundColor': '#f6f6f6','float':'right' ,'display': 'inline-block', 'margin-top':'50px'})
                              
                              ], style={'backgroundColor': '#f6f6f6'})]
if __name__ == '__main__':
    app.run_server(debug=False,host='0.0.0.0', port = 8071)    
