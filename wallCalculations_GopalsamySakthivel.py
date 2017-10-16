def WallCalc(wallLayersSeries,wallLayersParallel,fractionInsulation,Matlib):
    ConvectionLayers=['InsideConv','outerConvWinter']
    totalSeriesRes=0.000
    for everyL in wallLayersSeries:
        if(everyL['length']==Material_Library[everyL['material']]['length']):
            i=Material_Library[everyL['material']]['R']
        else:
            i=Material_Library[everyL['material']]['R']*(everyL['length']/Material_Library[everyL['material']]['length'])
        totalSeriesRes+=i
    for a in ConvectionLayers:
        totalSeriesRes+=Material_Library[a]['R']
    R=0.00
    z=0.00
    for every in wallLayersParallel:
        if(every['length']==Material_Library[every['material']]['length']):
            j=Material_Library[every['material']]['R']
        else:
            j=Material_Library[every['material']]['R']*(every['length']/Material_Library[every['material']]['length'])
        y=totalSeriesRes+j
        z=(1/(y))
        if(every['material']=='glassfiber'):
            R+=(fractionInsulation*z)
        else:
            R+=((1-fractionInsulation)*z)
    return R

def doorcalc(door):
    ConvectionLayers=['InsideConv','outerConvWinter']
    Door_R=0.00
    for a in ConvectionLayers:
        Door_R+=Material_Library[a]['R']
    for everyL in door:
        if(everyL['length']==Material_Library[everyL['material']]['length']):
            i=Material_Library[everyL['material']]['R']
        else:
            i=Material_Library[everyL['material']]['R']*(everyL['length']/Material_Library[everyL['material']]['length'])
        Door_R+=i
    Door_U=(1.00/Door_R)
    return Door_U