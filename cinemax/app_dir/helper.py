
# converts stored arrar data back to its original multidimensional array
def to_array(pass_data):
    data = to_string_list(pass_data)
    data = reshape(data, (16, 20))
    return data

# converts a strings to a corresponding list of strings
def to_string_list(data):
    data = data.replace("{", "")
    data = data.replace("}", "")
    data = data.split(",")
    return data

# converts a one-dimensional array to a multi-dimensional array
def reshape(data, shape):
    if len(data) == (shape[0] * shape[1]):
        shape_delimeter = [(max - shape[1], max) for max in range(shape[1],
         len(data) + 1, shape[1])]
        data = [data[min:max] for min, max in shape_delimeter]
        return data
    return data


def get_vvip():
    vvip = [(i, j) for i in range(2) for j in range(20) if(j < 4 or j > 14)]
    for i in range(2, 6):
        for j in range(20):
            vvip.append((i, j))
    return vvip

# returns the siiting positions of the twin seats
def get_twin():
    twin = list()
    for i in range(2):
        for j in range(0, 20, 2):
            if(j > 3 and j < 14):
                twin.append([(i,j), (i, j + 1)])

    return twin

def get_vip():
    return [(i, j) for i in range(6, 12) for j in range(20)]

def get_economy():
    return [(i, j) for i in range(12, 16) for j in range(20)]

def rows():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
   'M', 'N', 'O', 'P']

def columns():
    return  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        18, 19, 20]

def twin_seats():
    twin_keys = ['A5&A6','A7&A8','A9&A10','A11&A12','A13&A14',
        'B5&B6','B7&B8','B9&B10','B11&B12','B13&B14']
    twin = get_twin()
    return dict(zip(twin_keys, twin))

def vvip_seats():
    vvip_keys = ['A1', 'A2', 'A3', 'A4', 'A16', 'A17', 'A18', 'A19','A20',
        'B1', 'B2', 'B3', 'B4', 'B16', 'B17', 'B18', 'B19','B20',
        'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10',
        'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20',
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10',
        'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20'
        'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
        'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20'
        'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
        'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20']
    vvip = get_vvip()
    return dict(zip(vvip_keys, vvip))

def vip_seats():
    vip_keys = ['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10',
        'G11','G12','G13','G14','G15','G16','G17','G18','G19','G20',
        'H1','H2','H3','H4','H5','H6','H7','H8','H9','H10',
        'H11','H12','H13','H14','H15','H16','H17','H18','H19','H20',
        'I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
        'I11','I12','I13','I14','I15','I16','I17','I18','I19','I20',
        'J1','J2','J3','J4','J5','J6','J7','J8','J9','J10',
        'J11','J12','J13','J14','J15','J16','J17','J18','J19','J20',
        'K1','K2','K3','K4','K5','K6','K7','K8','K9','K10',
        'K11','K12','K13','K14','K15','K16','K17','K18','K19','K20',
        'L1','L2','L3','L4','L5','L6','L7','L8','L9','L10',
        'L11','L12','L13','L14','L15','L16','L17','L18','L19','L20']
    vip = get_vip()
    return dict(zip(vip_keys, vip))

def economy_seats():
    economy_keys = ['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10',
        'M11','M12','M13','M14','M15','M16','M17','M18','M19','M20',
        'N1','N2','N3','N4','N5','N6','N7','N8','N9','N10',
        'N11','N12','N13','N14','N15','N16','N17','N18','N19','N20',
        'O1','O2','O3','O4','O5','O6','O7','O8','O9','O10',
        'O11','O12','O13','O14','O15','O16','O17','O18','O19','O20',
        'P1','P2','P3','P4','P5','P6','P7','P8','P9','P10',
        'P11','P12','P13','P14','P15','P16','P17','P18','P19','P20']
    economy = get_economy()
    return dict(zip(economy_keys, economy))

def get_positions(keys, twin=False, vvip=False, vip=False, economy=False):
    if twin:
        twins = twin_seats()
        twin_pos = [twins[key] for key in keys]
        print(twin_pos)
        return twin_pos

    elif vvip:
        vv = vvip_seats()
        return [vv[key] for key in keys]

    elif vip:
        v = vip_seats()
        return [v[key] for key in keys]

    elif economy:
        econ = economy_seats()
        return [econ[key] for key in keys]

def seat_prices():
    f = open("cinemax/app_dir/prices.txt")
    f = f.read()
    f = f.replace("economy:", "")
    f = f.replace("vvip:", "")
    f = f.replace("vip:", "")
    f = f.replace("twin:", "")
    f = f.split("\n")
    twin, econ, vvip, vip, nan = f
    lis = [twin, econ, vvip, vip]
    lis = [int(value) for value in lis]
    return lis
