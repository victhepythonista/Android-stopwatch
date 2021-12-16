

def GetWidgetRoot(widget):
    # try to find the parent widget of
    # the provided widget
    parent = None
    current_root =widget
    root_found =  False

    while not root_found:
        print('...finding root widget for : {current_root}')
        try:
            test_root = current_root.parent
            if test_root:
                current_root = test_root
            break
        except AttributeError:
            print('attribute error !')
        else:
            raise
            break

        return current_root


def AddWidgets(parent, children):
    for child in children:
        widget.add_widget(child)

def FinalizeTimeUnit(value, unit_length = 2):
    test_value = str(value)
    while True:
        if len(test_value) < unit_length:
            test_value = '0' + test_value
            continue
        break
    return test_value

def GetDecimal(num, length = 2):
    #assert isinstance(num,float)
    num_str= str(num)
    if '.' in num_str:
        ind = num_str.index('.')
        res =  num_str[(ind+1):]
        if len(res) >= length:
            return res[:2]
        else: return ('0' + res)
    return '00'

def PrettifyTime(raw_time):
    hours =  int(raw_time//3600)
    minutes = int(raw_time//60)
    seconds =  int(raw_time%60)
    micro_seconds =  GetDecimal(raw_time)

    hours = FinalizeTimeUnit(hours)
    minutes = FinalizeTimeUnit(minutes)
    seconds = FinalizeTimeUnit(seconds)
    micro_seconds = FinalizeTimeUnit(micro_seconds)
    result = f"{hours}:{minutes}:{seconds}:{micro_seconds}"
    while result[0:3] == '00:' and len(result) > 5:
        result = result[3:]
    return result

if __name__ == '__main__':
    print(PrettifyTime(2332))
    print(GetDecimal(20.2))
