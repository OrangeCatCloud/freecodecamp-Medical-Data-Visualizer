import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')


# 2
df['overweight'] = (df['weight']/np.power(df['height']/100,2) > 25).astype(int)

# 3
df['gluc'].loc[df.gluc == 1] -= 1
df['gluc'].loc[df.gluc > 1] = 1
df['cholesterol'].loc[df.cholesterol == 1] -= 1
df['cholesterol'].loc[df.cholesterol > 1] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    #df_cat.rename(columns = {"value": "Total"}, inplace = True)
    df_cat['Total'] = df_cat.groupby(['cardio','variable','value'])['value'].transform('count')
    
    #fig, (ax1,ax2) = plt.subplots((1,2))

    # 6
    #df_cat = None
    df_cat['Total'] = df_cat.groupby(['cardio','variable','value'])['value'].transform('count')

    # 7



    # 8
    fig = sns.catplot(data = df_cat, x = "variable", y = "Total", col = "cardio", kind = "bar", hue = "value")


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    a1 = df['height'] <= df['height'].quantile(0.025)
    a2 = df['height'] >= df['height'].quantile(0.975)
    a3 = df['weight'] <= df['weight'].quantile(0.025)
    a4 = df['weight'] >= df['weight'].quantile(0.975)
    a5 = a1 | a2 | a3 | a4

    df_heat = df.drop(df[a5].index)
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.tri(len(corr),k=-1) != 1



    # 14
    fig, ax = plt.subplots(figsize = (12,12))

    # 15
    ax = sns.heatmap(corr, annot = corr, fmt = '.1f', mask = mask, linewidths = 2, 
                     linecolor = 'white', square = True, center = 0, cmap = 'seismic',
                     cbar_kws = {'shrink' : 0.5})


    # 16
    fig.savefig('heatmap.png')
    return fig
