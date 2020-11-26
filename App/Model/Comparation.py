from DISClib.DataStructures import mapentry

def compareId(id1, id2):
    id2 = mapentry.getKey(id2)
    if (id1 == id2):
        return 0
    elif (id1 > id2):
        return 1
    else:
        return -1

def tripsVal(element1, element2):
    if element1['value'] > element2['value']:
        return True
    return False

def targetVal(element1, element2):
    if element1['weight'] > element2['weight']:
        return True
    return False
