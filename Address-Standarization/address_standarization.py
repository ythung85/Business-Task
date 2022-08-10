# Loading package
import pandas as pd
import numpy as np

# Import testing data
test = pd.read_csv('street.csv')
test.head()

# Creating mapping Dict
common_abbre = {'apartment' :'apt',
'#' : 'apt',
'avenue' : 'ave',
'boulevard' : 'blvd',
'building' : 'bldg',
'center' : 'ctr',
'circle' : 'cir',
'court' : 'ct',
'drive' : 'dr',
'east': 'e',
'expressway' : 'expy',
'extension' : 'ext',
'fort' : 'ft',
'freeway' : 'fwy',
'height': 'hts',
'highway' : 'hwy',
'island' : 'is',
'junction' : 'jct',
'lane' : 'ln',
'mount' : 'mt',
'north' : 'n',
'northeast' : 'ne',
'northwest' : 'nw',
'parkway':'pky',
'place' : 'pl',
'post office' : 'po',
'road' : 'rd',
'rural delivery' : 'rdR',
'rural route' : 'rr',
'saint' : 'st',
'south' : 's',
'southeast' : 'se',
'southwest' : 'sw',
'spring' : 'spg',
'square' : 'sq',
'street' : 'st',
'suite' : 'ste',
'terrace' : 'ter',
'turnpike' : 'tpke',
'west' : 'w',
'box' : 'box'}

Number = {'first':'1st',
'second':'2nd',
'third' :'3rd',
'fourth':'4th',
'fifth' :'5th',
'sixth':'6th',
'seventh':'7th',
'eighth':'8th',
'ninth':'9th',
'tenth':'10th',
'eleventh':'11th',
'twelfth':'12th',
'thirteenth':'13th',
'fourteenth':'14th',
'fifteenth':'15th',
'sixteenth':'16th',
'seventeenth':'17th',
'eighteenth':'18th',
'nineteenth':'19th',
'twentieth':'20th',
'twenty-first':'21st',
'twenty-second':'22nd',
'twenty-third':'23rd',
'twenty-fourth':'24th',
'thirtieth':'30th'}



# self-defined function (address standarization)
def address_standard(df, Dict1, Dict2):
    ## format ##
    # number + name + (ave/ blvd/ Ct/ Dr/ St/ Ste/ Rd)
    res = []
    for st in df['Address']:
        sep = st.split(' ')
        if len(sep) <= 1:
            res.append('** missing address type **')
            continue
        
        if sep[0].isnumeric() is False:
            lower = list(map(lambda x: x.lower(), sep))
            if 'box' in lower or 'po' in lower:
                res.append(' '.join(sep))
                continue
            elif '-' in sep[0]:
                pass
            else:
                res.append('** entity name **')
                continue
        
        
        if sep[-1].isnumeric():
            if sep[-2] == '#' and sep[-3] == 'apt':
                sep.pop(-2)
            Object = sep[-2].lower()
            if Object in Dict1.keys():
                sep[-2] = Dict1[Object]
            if Object in Dict1.values():
                sep[-2] = sep[-2].lower()
                pass
            else:
                if sep[0].isnumeric() and len(sep) > 1:
                    if sep[-2] == '#' and sep[-1].isnumeric():
                        sep[-2] = common_abbre[sep[-2]]
                    else:
                        sep = list(map(lambda x: x.lower(), sep))
                    if sep[-1] in common_abbre.values():
                        sep.pop(-1)
                        
                    res.append(' '.join(sep))
                    continue
        else:
            Object = sep[-1].lower()
            if Object in Dict1.keys():
                sep[-1] = Dict1[Object]
            elif Object in Dict1.values():
                sep[-1] = sep[-1].lower()
            else:
                if sep[0].isnumeric() and len(sep) > 1:
                    if sep[-2] == '#' and sep[-1].isnumeric():
                        sep[-2] = common_abbre[sep[-2]]
                    else:
                        sep = list(map(lambda x: x.lower(), sep))
                    if sep[-1] in common_abbre.values():
                        sep.pop(-1)
                    res.append(' '.join(sep))
                    continue
        ## above works
        
        for i in range(1, len(sep)-1):
            Object = sep[i].lower()
            if Object in Dict1.keys():
                sep[i] = Dict1[Object]
            if Object in Dict1.values():
                sep[i] = sep[i].lower()
                pass
            else:
                sep[i] = sep[i].lower()
                
            if Object in Dict2.keys():
                sep[i] = Dict2[Object]
            
        if sep[-1] in common_abbre.values():
            sep.pop(-1)
        
        res.append(' '.join(sep))
    df['correct_address'] = res
    
    return df


# Display clean data
result = address_standard(test, common_abbre, Number)
result.to_csv('result.csv')
result.head()




