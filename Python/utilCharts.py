# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns


# Plot bar chart. Option to highlight selected x values
def plotBar(aXValues, aYValues, aDF, aSave=False, 
            aSaveName='', aXLabel='', aYLabel='', aTitle='',
            aXGrid=True, aYGrid=False, aFormatYlabel=True,
            aYLabelFormat="{:,}", aXLabelRotation=0,
            aBottomSpacing=0.25, aHighlightSelectedXValues=False,
            aSelectedXValuesToHighlight=None,
            aXTickLabelsOn=True,
            aUseLimit=False, aLimit=[0,100]):
    fig, ax = plt.subplots()
    x=aDF[aXValues]
    #sns.barplot(x=x, y=aDF[aYValues]) # color=clrs)
    if aHighlightSelectedXValues:
        clrs = ['lightgray' if (x not in aSelectedXValuesToHighlight) else 'red' for x in aDF[aXValues]]
        sns.barplot(x=x, y=aDF[aYValues], palette=clrs) # color=clrs)
    else:
        sns.barplot(x=x, y=aDF[aYValues]) # color=clrs)
    #sns.barplot(aXValues, aYValues, data=aDF)
    fig.set_size_inches(12, 8)
    ax.set_xlabel(aXLabel)
    ax.xaxis.grid(aXGrid)
    ax.yaxis.grid(aYGrid)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=aXLabelRotation, fontsize=10)
    plt.gcf().subplots_adjust(bottom=aBottomSpacing)
    if (aXTickLabelsOn==False):
        ax.get_xaxis().set_ticklabels([])
    ax.set_ylabel(aYLabel, fontsize=10)
    ax.set_title(aTitle, fontsize=20)
    if aUseLimit:
        plt.ylim(aLimit)
    if aFormatYlabel:
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
    if aSave:
        fig.savefig(aSaveName)

# Plot bar chart side by side
def plotBarGrouped(aDF, aSave=False, 
                   aSaveName='', aXLabel='', aYLabel='', aTitle='',
                   aXGrid=True, aYGrid=False, aFormatYlabel=True,
                   aYLabelFormat="{:,}", aXLabelRotation=30,
                   aBottomSpacing=0.25, aHighlightSelectedXValue=False,
                   aSelectedXValueToHighlight='',
                   aAnnotateEndX=0, aAnnotateEndY=0,
                   aAnnotateStartX=0, aAnnotateStartY=0,
                   aXTickLabelsOn=True,
                   aUseLimit=False, aLimit=[0,20000],
                   aUseWidth=False, aWidth=0.8,
                   aStyle='seaborn-colorblind',
                   aTitleFontSize=18, aOtherFontSize=10,):
    fig, ax = plt.subplots()
    plt.style.use(aStyle)
    plt.gcf().subplots_adjust(bottom=aBottomSpacing)
    if aUseWidth:
        myplot=aDF.plot(kind='bar', stacked=False,
                        figsize=(12,8), rot=aXLabelRotation, fontsize=9, width=aWidth)
    else:
        myplot=aDF.plot(kind='bar', stacked=False,
                        figsize=(12,8), rot=aXLabelRotation, fontsize=9)
    myplot.yaxis.grid(aYGrid)
    myplot.xaxis.grid(aXGrid)
    myplot.set_ylabel(aYLabel, fontsize=aOtherFontSize)
    if (aFormatYlabel):
        myplot.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
    myplot.set_title(aTitle , fontsize=aTitleFontSize)
    myplot.set_xlabel(aXLabel, fontsize=aOtherFontSize)
    if (aXTickLabelsOn==False):
        myplot.get_xaxis().set_ticklabels([])
    fig = myplot.get_figure()
    if (aHighlightSelectedXValue):
        plt.annotate(aSelectedXValueToHighlight,
                     ha = 'center', va = 'bottom',
                     xytext = (aAnnotateStartX, aAnnotateStartY),
                     xy = (aAnnotateEndX, aAnnotateEndY),
                     arrowprops = { 'facecolor' : 'black', 'shrink' : 0.05 })
    aShowLegend = True
    aProportionForLegend = 0.2
    if (aShowLegend):
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * (1-aProportionForLegend), box.height])
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=10)
    if aUseLimit:
        plt.ylim(aLimit)
    plt.tight_layout()
    plt.show()
    if aSave:
        fig.savefig(aSaveName)


# Plot bar stacked chart
# Can specify colors, fontsize, bottom margin spacing, limits,
# highlighted bar with arrow
def plotBarStacked(aXValues, aYValues, aDF, aSave=False, 
                   aSaveName='', aXLabel='', aYLabel='', aTitle='',
                   aXGrid=True, aYGrid=True, aFormatYlabel=True,
                   aYLabelFormat="{:,}", aXLabelRotation=30,
                   aBottomSpacing=0.25, aHighlightSelectedXValue=False,
                   aSelectedXValueToHighlight='',
                   aAnnotateEndX=0, aAnnotateEndY=0,
                   aAnnotateStartX=0, aAnnotateStartY=0,
                   aXTickLabelsOn=True,
                   aUseLimit=False, aLimit=[0,20000],
                   aStyle='seaborn-muted',
                   aColors='kr',
                   aUseColors=False,
                   aBarWidth=0.90,
                   aLabelFontSize=9):
    fig, ax = plt.subplots()
    plt.style.use(aStyle)
    plt.gcf().subplots_adjust(bottom=aBottomSpacing)
    if aUseColors:
        myplot=aDF.plot(kind='bar', stacked=True, x=aXValues, width=aBarWidth,
                        figsize=(12,8), rot=aXLabelRotation, fontsize=aLabelFontSize, color=aColors)
    else:
        myplot=aDF.plot(kind='bar', stacked=True, x=aXValues, width=aBarWidth,
                        figsize=(12,8), rot=aXLabelRotation, fontsize=aLabelFontSize)
    myplot.yaxis.grid(aYGrid)
    myplot.xaxis.grid(aXGrid)
    myplot.set_ylabel(aYLabel, fontsize=18)
    if (aFormatYlabel):
        myplot.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
    myplot.set_title(aTitle , fontsize=18)
    myplot.set_xlabel(aXLabel)
    if (aXTickLabelsOn==False):
        myplot.get_xaxis().set_ticklabels([])
    fig = myplot.get_figure()
    if (aHighlightSelectedXValue):
        plt.annotate(aSelectedXValueToHighlight,
                     ha = 'center', va = 'bottom',
                     xytext = (aAnnotateStartX, aAnnotateStartY),
                     xy = (aAnnotateEndX, aAnnotateEndY),
                     arrowprops = { 'facecolor' : 'black', 'shrink' : 0.05 })
    aShowLegend = True
    aProportionForLegend = 0.2
    if (aShowLegend):
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * (1-aProportionForLegend), box.height])
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=aLabelFontSize)
    if aUseLimit:
        plt.ylim(aLimit)
    plt.tight_layout()
    plt.show()
    if aSave:
        fig.savefig(aSaveName)


# Plot a Stacked Grouped Bar Chart
# Input: a list of [groupName, dataFrame] elements
# The dataFrame should have data for a stacked bar chart
def plotBarStackedGrouped(aXValues, aData, aSave=True, 
                          aSaveName='ReportsAutoGenerated/BarStackedGrouped.png', aXLabel='', aYLabel='', aTitle='',
                          aFormatYlabel=True, aYGrid=True,
                          aYLabelFormat="${:,}", aXLabelRotation=30,
                          aBottomSpacing=0.25,
                          aUseLimit=False, aLimit=[0,20000],
                          aBarWidth=0.90, aPlotWidth=20, aPlotHeight=8,
                          aProportionForLegend=0.1,
                          aTitleFontSize=16, aOtherFontSize=10,
                          aStyle='seaborn-colorblind',
                          aColors='kr',
                          aUseColors=False):
    plt.style.use(aStyle)
    plt.gcf().subplots_adjust(bottom=aBottomSpacing)
    #Set up the subgroups
    numGroups = len(aData)
    fig, axes = plt.subplots(nrows=1, ncols=numGroups, sharey=True)
    w = aPlotWidth
    h = aPlotHeight
    barWidth = aBarWidth
    i = 0
    for d in aData:
        if aUseColors:
            myPlot = (aData[i][1]).plot(ax=axes[i], kind='bar', stacked=True, x=aXValues,
                         figsize=(w,h), 
                         width=barWidth,
                         rot=aXLabelRotation, fontsize=aOtherFontSize,
                         legend=False, color=aColors)
        else:
            myPlot = (aData[i][1]).plot(ax=axes[i], kind='bar', stacked=True, x=aXValues,
                         figsize=(w,h), 
                         width=barWidth,
                         rot=aXLabelRotation, fontsize=aOtherFontSize,
                         legend=False)
        myPlot.set_xlabel(aData[i][0], fontsize=aOtherFontSize)    
        myPlot.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
        myPlot.yaxis.grid(aYGrid)
        myPlot.tick_params(axis='y', labelsize=aOtherFontSize)
        i = i + 1
    
    i = 0
    for d in aData:
        box = axes[i].get_position()
        print(box.x0)
        axes[i].set_position([box.x0 - box.x0 * aProportionForLegend * 1, 
            box.y0, box.width * (1-aProportionForLegend), box.height])
        i = i + 1

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=aOtherFontSize)
    fig.suptitle(aTitle, fontsize=aTitleFontSize)
    if aSave:
        fig.savefig(aSaveName)
        
        
# Plot box plot
def plotBox(dataDF=None, aXValues='', aYValues='',
            aSave=False, aSaveName='', aTitle='',
            aYLabel='',
            aXAxisGrid=False, aYAxisGrid=False):
    if dataDF is None:
        return
    fig, ax = plt.subplots()
    sns.boxplot(aXValues, aYValues, data=dataDF)
    fig.set_size_inches(12, 8)
    ax.set_xlabel('')
    ax.yaxis.grid(aYAxisGrid)
    ax.xaxis.grid(aXAxisGrid)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=45, fontsize=12)
    plt.gcf().subplots_adjust(bottom=0.30)
    ax.set_ylabel(aYLabel, fontsize=16)
    ax.set_title(aTitle, fontsize=18)
    if aSave:
        fig.savefig(aSaveName)


# Plot histogram
def plotHistogram(aVector, aSave=False, aSaveName='', aXLabel='',
                  aYLabel='', aTitle='', aXLabelFormat='{:,}',
                  aUseXLabelFormat=True,
                  aOverlayBoxplot=True, aOverlayMean=True, aBins=20,
                  aStyle='seaborn-colorblind',
                  aXGrid=False, aYGrid=False):
    plt.style.use(aStyle)
    fig = plt.figure(figsize = [16, 12])
    ax1 = fig.add_subplot(1,1,1)
    ax = sns.distplot(aVector, hist=True, kde=False, 
                 bins=aBins, color = 'blue',
                 hist_kws={'edgecolor':'black'})
    ax.xaxis.grid(aXGrid)
    ax.yaxis.grid(aYGrid)
    if (aOverlayBoxplot):
        ax2 = ax1.twinx()
        sns.boxplot(x=aVector, ax=ax2)
        ax2.set(ylim=(-.5, 10))
    if (aOverlayMean):
        plt.axvline(aVector.mean(), color='k', linestyle='dashed', linewidth=3)
    ax.set_title(aTitle, fontsize=20)
    ax.set_xlabel(aXLabel, fontsize=16)
    ax.set_ylabel(aYLabel, fontsize=16)
    if aUseXLabelFormat:
        ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aXLabelFormat.format(int(x))))
    if aSave:
        fig.savefig(aSaveName)
        

# General func to plot line chart
def plotLine(aPlotDF, aX, aY, aTitle, aXTitle, aYTitle,
             aSaveFilename, aYLabelFormat="${:,}",
             aShowLegend=True, aProportionForLegend=0.2,
             aLineWidth=5, aStyle='seaborn-dark',
             aXTickLabelsOn=True,
             aXLabelRotation=30,
             aXGrid=True, aYGrid=True,
             aUseLimit=False, aLimit=[0,20000],
             aLabelFontSize=12):
    fig, ax = plt.subplots()
    plt.style.use(aStyle)
    chartTitle = aTitle
    # create a color palette
    palette = plt.get_cmap('tab20')
    i = 0
    for y in aY:
        plt.plot(aPlotDF[aX], aPlotDF[y], marker='', color=palette(i), linewidth=aLineWidth, alpha=0.9, label=y)
        i = i + 1
    # Add the highlighted schools and legend
    fig.set_size_inches(12, 8)
    ax.set_xlabel(aXTitle, fontsize=16)
    if (aXTickLabelsOn==False):
        ax.get_xaxis().set_ticklabels([])
    plt.xticks(rotation=aXLabelRotation)
    ax.set_ylabel(aYTitle, fontsize=16)
    #ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
    ax.yaxis.grid(aYGrid)
    ax.xaxis.grid(aXGrid)
    if aUseLimit:
        plt.ylim(aLimit)
    if (aShowLegend):
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * (1-aProportionForLegend), box.height])
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=aLabelFontSize)
    #ax.set_xlim(0, 100)
    ax.set_title(chartTitle, fontsize=20)
    # Save plot
    saveFileName = (aSaveFilename)
    fig.savefig(saveFileName)


# Plot line chart for multiple DFs
# General func to plot line chart
def plotLineMulti(aPlotDF, aX, aY, aTitle, aXTitle, aYTitle,
             aSaveFilename, aYLabelFormat="${:,}",
             aShowLegend=True, aProportionForLegend=0.2,
             aLineWidth=5, aStyle='seaborn-dark',
             aXTickLabelsOn=True,
             aXLabelRotation=30,
             aXGrid=True, aYGrid=True,
             aUseLimit=False, aLimit=[0,20000],
             aLabelFontSize=12):
    fig, ax = plt.subplots()
    plt.style.use(aStyle)
    chartTitle = aTitle
    # create a color palette
    palette = plt.get_cmap('tab20')
    iDF = 0
    i=0
    for df in aPlotDF:
        iX=aX[iDF]
        iY=aY[iDF]
        for y in iY:
            plt.plot(df[iX], df[y], marker='', color=palette(i), linewidth=aLineWidth, alpha=0.9, label=y)
            i=i+1
        iDF = iDF + 1
    fig.set_size_inches(12, 8)
    ax.set_xlabel(aXTitle, fontsize=16)
    if (aXTickLabelsOn==False):
        ax.get_xaxis().set_ticklabels([])
    plt.xticks(rotation=aXLabelRotation)
    ax.set_ylabel(aYTitle, fontsize=16)
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
    ax.yaxis.grid(aYGrid)
    ax.xaxis.grid(aXGrid)
    if aUseLimit:
        plt.ylim(aLimit)
    if (aShowLegend):
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * (1-aProportionForLegend), box.height])
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=aLabelFontSize)
    ax.set_title(chartTitle, fontsize=20)
    # Save plot
    saveFileName = (aSaveFilename)
    fig.savefig(saveFileName)
    plt.close(fig)


# General func to plot scatter
# Options: highlighting with legend, circle size, curve fit 
def plotScatter(aPlotDF, aX, aY, aHighlightList, aHighlightCol, aTitle='', 
                aXTitle='', aYTitle='',
                aSaveFilename='ReportsAutoGenerated/Scatter.png', 
                aLegendLocation=2, aCurveFitOrder=2,
                aIncludeFittedCurve=True, aYLabelFormat="${:,}",
                aShowLegend=True, aProportionForLegend=0.2,
                aUseLimit=False, aLimit=[0,20000],
                aFormatYLabel=True,
                aXLabelFormat='${:,}', aFormatXLabel=False,
                aUseCircleSize=False, aCircleSizeCol=None,
                aLegendFont=10, aTitleFont=20):
    fig, ax = plt.subplots()
    # Get the school year string
    chartTitle = aTitle
    circleSize=80
    if aUseCircleSize:
        aPlotDF = aPlotDF.sort_values(by=aX)
        circleSize = aPlotDF[aCircleSizeCol]
    sns.regplot(y=aY,
                x=aX,
                data=aPlotDF,
                scatter_kws={'s': circleSize, 'alpha':0.2}, fit_reg=aIncludeFittedCurve,
                order=aCurveFitOrder, ci=None, truncate=True)
    # Add the highlighted schools and legend
    colorSelection = ['b','g','r','c','m', 'orange', 'k']
    colorSelectionSize = len(colorSelection)
    shapeSelection = ['o','v', '^', '<', '>', 's', 'p', 'P','*', 'h', 'H', '+', 'x', 'X', 'D', 'd', '1', '2', '3', '4', '8', ]
    shapeSelectionSize = len(shapeSelection)
    for i in range(len(aHighlightList)):
        highlightItem = aHighlightList[i]
        highlightItemData = aPlotDF.loc[aPlotDF[aHighlightCol] == highlightItem]
        sns.regplot(y=highlightItemData[aY],
                    x=highlightItemData[aX],
                    fit_reg=False,
                    marker=shapeSelection[ (int(i / colorSelectionSize) % shapeSelectionSize)],
                    color=colorSelection[i%colorSelectionSize], label=highlightItem, 
                    scatter_kws={'s': 150, 'alpha':1.0})
    fig.set_size_inches(12, 8)
    ax.set_xlabel(aXTitle, fontsize=16)
    ax.set_ylabel(aYTitle, fontsize=16)
    if aFormatXLabel:
        ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aXLabelFormat.format(int(x))))
    if aFormatYLabel:
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
    ax.grid(True)
    if (aShowLegend):
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * (1-aProportionForLegend), box.height])
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=aLegendFont)
    if aUseLimit:
        ax.set_ylim(aLimit)
    ax.set_title(chartTitle, fontsize=aTitleFont)
    # Save plot
    saveFileName = (aSaveFilename)
    fig.savefig(saveFileName)
    plt.close(fig)        


# Plot scatter for 2 populations
# General func to plot scatter
# Options: highlighting with legend, circle size, curve fit 
def plotScatterMulti(aPlotDF0, aX0, aY0, aHighlightList0, aHighlightCol0,
                     aPlotDF1, aX1, aY1, aHighlightList1, aHighlightCol1,
                     aColor0='green', aColor1='blue',
                     aLegendTitle0='',
                     aLegendTitle1='',
                     aTitle='', 
                     aXTitle='', aYTitle='',
                     aSaveFilename='ReportsAutoGenerated/Scatter.png', 
                     aLegendLocation=2, aCurveFitOrder=2,
                     aIncludeFittedCurve=True, aYLabelFormat="${:,}",
                     aShowLegend=True, aProportionForLegend=0.2,
                     aUseLimit=False, aLimit=[0,20000],
                     aFormatYLabel=True,
                     aXLabelFormat='${:,}', aFormatXLabel=False,
                     aUseCircleSize=False, aCircleSizeCol=None,
                     aLegendFont=10):
    fig, ax = plt.subplots()
    # Get the school year string
    chartTitle = aTitle
    circleSize0=80
    circleSize1=80
    if aUseCircleSize:
        aPlotDF0 = aPlotDF0.sort_values(by=aX0)
        circleSize0 = aPlotDF0[aCircleSizeCol]
        aPlotDF1 = aPlotDF1.sort_values(by=aX1)
        circleSize1 = aPlotDF1[aCircleSizeCol]
    sns.regplot(y=aY0,
                x=aX0,
                data=aPlotDF0,
                color=aColor0,
                label=aLegendTitle0,
                scatter_kws={'s': circleSize0, 'alpha':0.2}, fit_reg=aIncludeFittedCurve,
                order=aCurveFitOrder, ci=None, truncate=True)
    sns.regplot(y=aY1,
                x=aX1,
                data=aPlotDF1,
                color=aColor1,
                label=aLegendTitle1,
                scatter_kws={'s': circleSize1, 'alpha':0.2}, fit_reg=aIncludeFittedCurve,
                order=aCurveFitOrder, ci=None, truncate=True)
    # Add the highlighted schools and legend
    shapeSelection = ['o','v', '^', '<', '>', 's', 'p', 'P','*', 'h', 'H', '+', 'x', 'X', 'D', 'd', '1', '2', '3', '4', '8', ]
    shapeSelectionSize = len(shapeSelection)
    for i in range(len(aHighlightList0)):
        highlightItem = aHighlightList0[i]
        highlightItemData = aPlotDF0.loc[aPlotDF0[aHighlightCol0] == highlightItem]
        sns.regplot(y=highlightItemData[aY0],
                    x=highlightItemData[aX0],
                    fit_reg=False,
                    #marker=shapeSelection[ (int(i / shapeSelectionSize) % shapeSelectionSize)],
                    #color=colorSelection[i%colorSelectionSize], label=highlightItem, 
                    marker=shapeSelection[ (i%shapeSelectionSize)],
                    color=aColor0, label=highlightItem, 
                    scatter_kws={'s': 150, 'alpha':1.0})
    for i in range(len(aHighlightList1)):
        highlightItem = aHighlightList1[i]
        highlightItemData = aPlotDF1.loc[aPlotDF1[aHighlightCol1] == highlightItem]
        sns.regplot(y=highlightItemData[aY1],
                    x=highlightItemData[aX1],
                    fit_reg=False,
                    marker=shapeSelection[ (i%shapeSelectionSize)],
                    color=aColor1, label=highlightItem,
                    #color=aColor2, # Don't show in legend
                    scatter_kws={'s': 150, 'alpha':1.0})
    fig.set_size_inches(12, 8)
    ax.set_xlabel(aXTitle, fontsize=16)
    ax.set_ylabel(aYTitle, fontsize=16)
    if aFormatXLabel:
        ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aXLabelFormat.format(int(x))))
    if aFormatYLabel:
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: aYLabelFormat.format(int(x))))
    ax.grid(True)
    if (aShowLegend):
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * (1-aProportionForLegend), box.height])
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=aLegendFont)
    if aUseLimit:
        ax.set_ylim(aLimit)
    ax.set_title(chartTitle, fontsize=20)
    # Save plot
    saveFileName = (aSaveFilename)
    fig.savefig(saveFileName)
    plt.close(fig)    



