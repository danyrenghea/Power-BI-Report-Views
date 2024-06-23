First Phyton visual
1.	import matplotlib.pyplot as plt
2.	 
3.	plt.plot(dataset.course,dataset.prep_time,'go')
4.	plt.xlabel('course type')
5.	plt.ylabel('prep time')
6.	 
7.	plt.show()
Violin plot:
1.	# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 
2.	 
3.	# dataset = pandas.DataFrame(prep_time, cook_time)
4.	# dataset = dataset.drop_duplicates()
5.	 
6.	# Paste or type your script code here:
7.	import matplotlib.pyplot as plt
8.	import seaborn as sns
9.	 
10.	sns.violinplot(x=dataset["course"],y=dataset["prep_time"],palette="Blues")
11.	 
12.	plt.show()
Pair plot:
1.	# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 
2.	 
3.	# dataset = pandas.DataFrame(prep_time, cook_time)
4.	# dataset = dataset.drop_duplicates()
5.	 
6.	# Paste or type your script code here:
7.	import matplotlib.pyplot as plt
8.	import seaborn as sns
9.	 
10.	sns.pairplot(dataset)
11.	 
12.	plt.show()

Overlapping ridge plots:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()

sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
# Create the data
rs = dataset.cook_time
x = dataset.prep_time
g = dataset.region
df = pd.DataFrame(dict(x=x, g=g))
# Initialize the FacetGrid object
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="g", hue="g", aspect=15, height=.5, palette=pal)
 
# Draw the densities in a few steps
g.map(sns.kdeplot, "x",
bw_adjust=.5, clip_on=False,
fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw_adjust=.5)
g.map(plt.axhline, y=0, lw=2, clip_on=False)
# Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
 ax = plt.gca()
 ax.text(0, .2, label, fontweight="bold", color=color,
 ha="left", va="center", transform=ax.transAxes)
 g.map(label, "x")
 # Set the subplots to overlap
g.fig.subplots_adjust(hspace=-.25)
 # Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[],ylabel = "")
g.despine(bottom=True, left=True)
 plt.show()

TextBlob as
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
def get_sentiment(text):
    #obtain polarity
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return 0
dataset['Review Text'].astype(str)
dataset['Sentiment']=dataset['Review Text'].apply(get_sentiment)



