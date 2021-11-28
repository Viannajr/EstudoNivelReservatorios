import pandas as pd
import numpy as np
import matplotlib.pylab as plt

j = 1
for i in range(2000, 2021):
    
    uRl = 'https://ons-dl-prod-opendata.s3.amazonaws.com/dataset/ear_subsistema_di/EAR_DIARIO_SUBSISTEMA_' + str(i) + '.csv'
    df = pd.read_csv(uRl, sep = ';')

    df.columns = ['id_subsistema', 'nome_subsistema', 'data_medição', 'ear_max_mwmes', 'ear_dia_mwmes', 'ear_percentual']
    df['data_medição'] = pd.to_datetime(df['data_medição'])
    plt.figure(j)
    plt.plot(df.loc[df['id_subsistema'] == 'SE', ['ear_percentual']].reset_index(drop=True))
    plt.plot(df.loc[df['id_subsistema'] == 'NE', ['ear_percentual']].reset_index(drop=True))
    plt.plot(df.loc[df['id_subsistema'] == 'S', ['ear_percentual']].reset_index(drop=True))
    plt.plot(df.loc[df['id_subsistema'] == 'N', ['ear_percentual']].reset_index(drop=True))
    
    plt.xlabel("Dia do ano")
    plt.ylabel("Nível dos Reservatórios (%)")
    plt.title("Nível Percetual dos Reservatorios - Ano" + str(i))
    plt.grid(True)
    plt.legend(['SE', 'NE', 'S', 'N'])
    j = j + 1
    
    #show the figure
    plt.savefig('nivelReservatorio'+str(i)+'.pdf')
    plt.close()