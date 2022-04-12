"""
CGCNN-like embeddings using continuous values instead of original k-hot.

Properties:
    Group number
    Period number
    Electronegativity
    Covalent radius
    Valence electrons
    First ionization energy
    Electron affinity
    Block
    Atomic Volume

NaN stored for unavaialable parameters.
"""
CONTINUOUS_EMBEDDINGS = {
    0: [
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
    ],
    1: [
        1.0,
        1.0,
        2.1877708435058594,
        31.0,
        1.0,
        13.598434448242188,
        0.754194974899292,
        1.0,
        14.100000381469727,
    ],
    2: [
        18.0,
        1.0,
        1.0,
        28.0,
        2.0,
        24.587387084960938,
        -19.700000762939453,
        1.0,
        31.799999237060547,
    ],
    3: [
        1.0,
        2.0,
        0.04886792600154877,
        128.0,
        1.0,
        5.391714572906494,
        0.6180490255355835,
        1.0,
        13.100000381469727,
    ],
    4: [
        2.0,
        2.0,
        0.1268472671508789,
        96.0,
        2.0,
        9.322698593139648,
        -2.4000000953674316,
        1.0,
        5.0,
    ],
    5: [
        13.0,
        2.0,
        0.25462737679481506,
        84.0,
        3.0,
        8.298019409179688,
        0.27972298860549927,
        2.0,
        4.599999904632568,
    ],
    6: [
        14.0,
        2.0,
        0.42752504348754883,
        73.0,
        4.0,
        11.260295867919922,
        1.2621190547943115,
        2.0,
        5.300000190734863,
    ],
    7: [
        15.0,
        2.0,
        0.5774819254875183,
        71.0,
        5.0,
        14.534130096435547,
        -1.399999976158142,
        2.0,
        17.299999237060547,
    ],
    8: [
        16.0,
        2.0,
        0.9416494369506836,
        66.0,
        6.0,
        13.618054389953613,
        1.461113452911377,
        2.0,
        14.0,
    ],
    9: [
        17.0,
        2.0,
        1.017681360244751,
        57.0,
        7.0,
        17.422819137573242,
        3.4011898040771484,
        2.0,
        17.100000381469727,
    ],
    10: [
        18.0,
        2.0,
        1.0,
        58.0,
        8.0,
        21.56454086303711,
        -3.0,
        2.0,
        16.799999237060547,
    ],
    11: [
        1.0,
        3.0,
        0.09459763765335083,
        166.0,
        1.0,
        5.1390767097473145,
        0.5479260087013245,
        1.0,
        23.700000762939453,
    ],
    12: [
        2.0,
        3.0,
        0.15242105722427368,
        141.0,
        2.0,
        7.64623498916626,
        -3.0,
        1.0,
        14.0,
    ],
    13: [
        13.0,
        3.0,
        0.2360926866531372,
        121.0,
        3.0,
        5.9857683181762695,
        0.43283000588417053,
        2.0,
        10.0,
    ],
    14: [
        14.0,
        3.0,
        0.3468157947063446,
        111.0,
        4.0,
        8.15168285369873,
        1.3895211219787598,
        2.0,
        12.100000381469727,
    ],
    15: [
        15.0,
        3.0,
        0.45102688670158386,
        107.0,
        5.0,
        10.486685752868652,
        0.7466070055961609,
        2.0,
        17.0,
    ],
    16: [
        16.0,
        3.0,
        0.6397251486778259,
        105.0,
        6.0,
        10.360010147094727,
        2.077104091644287,
        2.0,
        15.5,
    ],
    17: [
        17.0,
        3.0,
        0.8123772740364075,
        102.0,
        7.0,
        12.967630386352539,
        3.612725019454956,
        2.0,
        18.700000762939453,
    ],
    18: [
        18.0,
        3.0,
        1.0,
        106.0,
        8.0,
        15.759611129760742,
        -11.5,
        2.0,
        24.200000762939453,
    ],
    19: [
        1.0,
        4.0,
        0.12183826416730881,
        203.0,
        1.0,
        4.340663433074951,
        0.5014700293540955,
        1.0,
        45.29999923706055,
    ],
    20: [
        2.0,
        4.0,
        0.1901577115058899,
        176.0,
        2.0,
        6.113155364990234,
        0.024550000205636024,
        1.0,
        29.899999618530273,
    ],
    21: [
        3.0,
        4.0,
        0.3038673996925354,
        170.0,
        3.0,
        6.561490058898926,
        0.18799999356269836,
        3.0,
        15.0,
    ],
    22: [
        4.0,
        4.0,
        0.4055461883544922,
        160.0,
        4.0,
        6.828120231628418,
        0.07900000363588333,
        3.0,
        10.600000381469727,
    ],
    23: [
        5.0,
        4.0,
        0.4388898015022278,
        153.0,
        5.0,
        6.746187210083008,
        0.5249999761581421,
        3.0,
        8.350000381469727,
    ],
    24: [
        6.0,
        4.0,
        0.6017723083496094,
        139.0,
        6.0,
        6.766510009765625,
        0.6660000085830688,
        3.0,
        7.230000019073486,
    ],
    25: [
        7.0,
        4.0,
        0.6707264184951782,
        150.0,
        7.0,
        7.434018135070801,
        -3.0,
        3.0,
        7.389999866485596,
    ],
    26: [
        8.0,
        4.0,
        0.748727023601532,
        142.0,
        8.0,
        7.902467727661133,
        0.1509999930858612,
        3.0,
        7.099999904632568,
    ],
    27: [
        9.0,
        4.0,
        0.8832423686981201,
        138.0,
        9.0,
        7.881010055541992,
        0.6622564792633057,
        3.0,
        6.699999809265137,
    ],
    28: [
        10.0,
        4.0,
        0.9377039670944214,
        124.0,
        10.0,
        7.639876842498779,
        1.156000018119812,
        3.0,
        6.599999904632568,
    ],
    29: [
        11.0,
        4.0,
        0.9175541996955872,
        132.0,
        11.0,
        7.726379871368408,
        1.2350000143051147,
        3.0,
        7.099999904632568,
    ],
    30: [
        12.0,
        4.0,
        0.8100876808166504,
        122.0,
        12.0,
        9.39419937133789,
        -3.0,
        3.0,
        9.199999809265137,
    ],
    31: [
        13.0,
        4.0,
        0.7205410003662109,
        122.0,
        3.0,
        5.999301910400391,
        0.4300000071525574,
        2.0,
        11.800000190734863,
    ],
    32: [
        14.0,
        4.0,
        0.8001470565795898,
        120.0,
        4.0,
        7.899435043334961,
        1.2327120304107666,
        2.0,
        13.600000381469727,
    ],
    33: [
        15.0,
        4.0,
        0.825337290763855,
        119.0,
        5.0,
        9.788999557495117,
        0.8040000200271606,
        2.0,
        13.100000381469727,
    ],
    34: [
        16.0,
        4.0,
        0.9659121036529541,
        120.0,
        6.0,
        9.752391815185547,
        2.020669937133789,
        2.0,
        16.5,
    ],
    35: [
        17.0,
        4.0,
        1.0490256547927856,
        120.0,
        7.0,
        11.813810348510742,
        3.3635880947113037,
        2.0,
        23.5,
    ],
    36: [
        18.0,
        4.0,
        1.0,
        116.0,
        8.0,
        13.999605178833008,
        -3.0,
        2.0,
        32.20000076293945,
    ],
    37: [
        1.0,
        5.0,
        0.1764136552810669,
        220.0,
        1.0,
        4.177127838134766,
        0.4859200119972229,
        1.0,
        55.900001525878906,
    ],
    38: [
        2.0,
        5.0,
        0.26317858695983887,
        195.0,
        2.0,
        5.694867134094238,
        0.04800000041723251,
        1.0,
        33.70000076293945,
    ],
    39: [
        3.0,
        5.0,
        0.39239412546157837,
        190.0,
        3.0,
        6.217259883880615,
        0.3070000112056732,
        3.0,
        19.799999237060547,
    ],
    40: [
        4.0,
        5.0,
        0.4744466543197632,
        175.0,
        4.0,
        6.633900165557861,
        0.4259999990463257,
        3.0,
        14.100000381469727,
    ],
    41: [
        5.0,
        5.0,
        0.5561695098876953,
        164.0,
        5.0,
        6.75885009765625,
        0.9174060225486755,
        3.0,
        10.800000190734863,
    ],
    42: [
        6.0,
        5.0,
        0.6852949857711792,
        154.0,
        6.0,
        7.092430114746094,
        0.7480000257492065,
        3.0,
        9.399999618530273,
    ],
    43: [
        7.0,
        5.0,
        0.8753613233566284,
        147.0,
        7.0,
        7.119380950927734,
        0.550000011920929,
        3.0,
        8.5,
    ],
    44: [
        8.0,
        5.0,
        0.9579373002052307,
        146.0,
        8.0,
        7.360499858856201,
        1.0499999523162842,
        3.0,
        8.300000190734863,
    ],
    45: [
        9.0,
        5.0,
        0.9761914610862732,
        142.0,
        9.0,
        7.458899974822998,
        1.1369999647140503,
        3.0,
        8.300000190734863,
    ],
    46: [
        10.0,
        5.0,
        1.1242631673812866,
        139.0,
        12.0,
        8.336859703063965,
        0.5619999766349792,
        3.0,
        8.899999618530273,
    ],
    47: [
        11.0,
        5.0,
        0.9437955021858215,
        145.0,
        11.0,
        7.576233863830566,
        1.3020000457763672,
        3.0,
        10.300000190734863,
    ],
    48: [
        12.0,
        5.0,
        0.8015620112419128,
        144.0,
        12.0,
        8.99382209777832,
        -3.0,
        3.0,
        13.100000381469727,
    ],
    49: [
        13.0,
        5.0,
        0.7172747254371643,
        142.0,
        3.0,
        5.786355018615723,
        0.30000001192092896,
        2.0,
        15.699999809265137,
    ],
    50: [
        14.0,
        5.0,
        0.7622796893119812,
        139.0,
        4.0,
        7.343916893005371,
        1.1120669841766357,
        2.0,
        16.299999237060547,
    ],
    51: [
        15.0,
        5.0,
        0.7762722373008728,
        139.0,
        5.0,
        8.608388900756836,
        1.0460000038146973,
        2.0,
        18.399999618530273,
    ],
    52: [
        16.0,
        5.0,
        0.8622506260871887,
        138.0,
        6.0,
        9.009659767150879,
        1.9708759784698486,
        2.0,
        20.5,
    ],
    53: [
        17.0,
        5.0,
        0.9386428594589233,
        139.0,
        7.0,
        10.45125961303711,
        3.0590367317199707,
        2.0,
        25.700000762939453,
    ],
    54: [
        18.0,
        5.0,
        1.0,
        140.0,
        8.0,
        12.129842758178711,
        -0.0560000017285347,
        2.0,
        42.900001525878906,
    ],
    55: [
        1.0,
        6.0,
        0.18145304918289185,
        244.0,
        1.0,
        3.8939056396484375,
        0.47162601351737976,
        1.0,
        70.0,
    ],
    56: [
        2.0,
        6.0,
        0.3032951354980469,
        215.0,
        2.0,
        5.211664199829102,
        0.14462000131607056,
        1.0,
        39.0,
    ],
    57: [
        3.0,
        6.0,
        0.39465051889419556,
        207.0,
        3.0,
        5.576900005340576,
        0.4699999988079071,
        3.0,
        22.5,
    ],
    58: [
        4.0,
        6.0,
        0.5356179475784302,
        204.0,
        2.0,
        5.538599967956543,
        0.6499999761581421,
        4.0,
        21.0,
    ],
    59: [
        5.0,
        6.0,
        0.4288040101528168,
        203.0,
        2.0,
        5.4730000495910645,
        0.9620000123977661,
        4.0,
        20.799999237060547,
    ],
    60: [
        6.0,
        6.0,
        0.44721803069114685,
        201.0,
        2.0,
        5.525000095367432,
        1.9160000085830688,
        4.0,
        20.600000381469727,
    ],
    61: [
        7.0,
        6.0,
        0.4585537314414978,
        199.0,
        2.0,
        5.581999778747559,
        -3.0,
        4.0,
        20.229999542236328,
    ],
    62: [
        8.0,
        6.0,
        0.47021451592445374,
        198.0,
        2.0,
        5.643710136413574,
        -3.0,
        4.0,
        19.899999618530273,
    ],
    63: [
        9.0,
        6.0,
        0.5085079669952393,
        198.0,
        2.0,
        5.670384883880615,
        0.8640000224113464,
        4.0,
        28.899999618530273,
    ],
    64: [
        10.0,
        6.0,
        0.5033860206604004,
        196.0,
        2.0,
        6.149796009063721,
        -3.0,
        4.0,
        19.899999618530273,
    ],
    65: [
        11.0,
        6.0,
        0.5163695216178894,
        194.0,
        2.0,
        5.863800048828125,
        1.1649999618530273,
        4.0,
        19.200000762939453,
    ],
    66: [
        12.0,
        6.0,
        0.5297338366508484,
        192.0,
        2.0,
        5.939050197601318,
        0.35199999809265137,
        4.0,
        19.0,
    ],
    67: [
        13.0,
        6.0,
        0.5434919595718384,
        192.0,
        2.0,
        6.021500110626221,
        -3.0,
        4.0,
        18.700000762939453,
    ],
    68: [
        14.0,
        6.0,
        0.5576573014259338,
        189.0,
        2.0,
        6.107699871063232,
        -3.0,
        4.0,
        18.399999618530273,
    ],
    69: [
        15.0,
        6.0,
        0.5722439289093018,
        190.0,
        2.0,
        6.184309959411621,
        1.0290000438690186,
        4.0,
        18.100000381469727,
    ],
    70: [
        16.0,
        6.0,
        0.517667829990387,
        187.0,
        2.0,
        6.254159927368164,
        -0.019999999552965164,
        4.0,
        24.799999237060547,
    ],
    71: [
        17.0,
        6.0,
        0.6027398109436035,
        187.0,
        2.0,
        5.425870895385742,
        0.3400000035762787,
        4.0,
        17.799999237060547,
    ],
    72: [
        4.0,
        6.0,
        0.7352124452590942,
        175.0,
        4.0,
        6.825069904327393,
        0.014000000432133675,
        3.0,
        13.600000381469727,
    ],
    73: [
        5.0,
        6.0,
        0.8358832001686096,
        170.0,
        5.0,
        7.549570083618164,
        0.32199999690055847,
        3.0,
        10.899999618530273,
    ],
    74: [
        6.0,
        6.0,
        1.0192831754684448,
        162.0,
        6.0,
        7.864029884338379,
        0.8162599802017212,
        3.0,
        9.529999732971191,
    ],
    75: [
        7.0,
        6.0,
        1.1745918989181519,
        151.0,
        7.0,
        7.83351993560791,
        0.15000000596046448,
        3.0,
        8.850000381469727,
    ],
    76: [
        8.0,
        6.0,
        1.2392759323120117,
        144.0,
        8.0,
        8.43822956085205,
        1.100000023841858,
        3.0,
        8.430000305175781,
    ],
    77: [
        9.0,
        6.0,
        1.4759982824325562,
        141.0,
        9.0,
        8.967020034790039,
        1.5637999773025513,
        3.0,
        8.539999961853027,
    ],
    78: [
        10.0,
        6.0,
        1.4510095119476318,
        136.0,
        10.0,
        8.958829879760742,
        2.128000020980835,
        3.0,
        9.100000381469727,
    ],
    79: [
        11.0,
        6.0,
        1.4267007112503052,
        136.0,
        11.0,
        9.225552558898926,
        2.3086299896240234,
        3.0,
        10.199999809265137,
    ],
    80: [
        12.0,
        6.0,
        1.1647894382476807,
        132.0,
        12.0,
        10.437503814697266,
        -3.0,
        3.0,
        14.800000190734863,
    ],
    81: [
        13.0,
        6.0,
        0.924509584903717,
        145.0,
        3.0,
        6.1082868576049805,
        0.37700000405311584,
        2.0,
        17.200000762939453,
    ],
    82: [
        14.0,
        6.0,
        0.9313225746154785,
        146.0,
        4.0,
        7.416679382324219,
        0.3567431569099426,
        2.0,
        18.299999237060547,
    ],
    83: [
        15.0,
        6.0,
        0.8136501312255859,
        148.0,
        5.0,
        7.285515785217285,
        0.9423620104789734,
        2.0,
        21.299999237060547,
    ],
    84: [
        16.0,
        6.0,
        0.9256306886672974,
        140.0,
        6.0,
        8.413999557495117,
        1.899999976158142,
        2.0,
        22.700000762939453,
    ],
    85: [
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
    ],
    86: [18.0, 6.0, 1.0, 150.0, 8.0, 10.748499870300293, -3.0, 2.0, 50.5],
    87: [
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
    ],
    88: [
        2.0,
        7.0,
        0.3596253991127014,
        221.0,
        2.0,
        5.27842378616333,
        0.10000000149011612,
        1.0,
        45.0,
    ],
    89: [
        3.0,
        7.0,
        0.4583164155483246,
        215.0,
        3.0,
        5.380226135253906,
        0.3499999940395355,
        3.0,
        22.540000915527344,
    ],
    90: [
        4.0,
        7.0,
        0.5557018518447876,
        206.0,
        2.0,
        6.306700229644775,
        -3.0,
        4.0,
        19.799999237060547,
    ],
    91: [
        5.0,
        7.0,
        0.623065710067749,
        200.0,
        2.0,
        5.889999866485596,
        -3.0,
        4.0,
        15.0,
    ],
    92: [
        6.0,
        7.0,
        0.6181179881095886,
        196.0,
        2.0,
        6.194049835205078,
        -3.0,
        4.0,
        12.5,
    ],
    93: [
        7.0,
        7.0,
        0.6132539510726929,
        190.0,
        2.0,
        6.265500068664551,
        -3.0,
        4.0,
        21.100000381469727,
    ],
    94: [
        8.0,
        7.0,
        0.6084716320037842,
        187.0,
        2.0,
        6.0258002281188965,
        -3.0,
        4.0,
        12.289999961853027,
    ],
    95: [
        9.0,
        7.0,
        0.6834156513214111,
        180.0,
        2.0,
        5.973800182342529,
        -3.0,
        4.0,
        20.799999237060547,
    ],
    96: [
        10.0,
        7.0,
        0.6900094747543335,
        169.0,
        2.0,
        5.991399765014648,
        -3.0,
        4.0,
        18.280000686645508,
    ],
    97: [
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
    ],
    98: [
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
    ],
    99: [
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
    ],
    100: [
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
        float("NaN"),
    ],
}

"""
Atomic radii in picometers

NaN stored for unavailable parameters.
"""
ATOMIC_RADII = {
    0: float("NaN"),
    1: 25.0,
    2: 120.0,
    3: 145.0,
    4: 105.0,
    5: 85.0,
    6: 70.0,
    7: 65.0,
    8: 60.0,
    9: 50.0,
    10: 160.0,
    11: 180.0,
    12: 150.0,
    13: 125.0,
    14: 110.0,
    15: 100.0,
    16: 100.0,
    17: 100.0,
    18: 71.0,
    19: 220.0,
    20: 180.0,
    21: 160.0,
    22: 140.0,
    23: 135.0,
    24: 140.0,
    25: 140.0,
    26: 140.0,
    27: 135.0,
    28: 135.0,
    29: 135.0,
    30: 135.0,
    31: 130.0,
    32: 125.0,
    33: 115.0,
    34: 115.0,
    35: 115.0,
    36: float("NaN"),
    37: 235.0,
    38: 200.0,
    39: 180.0,
    40: 155.0,
    41: 145.0,
    42: 145.0,
    43: 135.0,
    44: 130.0,
    45: 135.0,
    46: 140.0,
    47: 160.0,
    48: 155.0,
    49: 155.0,
    50: 145.0,
    51: 145.0,
    52: 140.0,
    53: 140.0,
    54: float("NaN"),
    55: 260.0,
    56: 215.0,
    57: 195.0,
    58: 185.0,
    59: 185.0,
    60: 185.0,
    61: 185.0,
    62: 185.0,
    63: 185.0,
    64: 180.0,
    65: 175.0,
    66: 175.0,
    67: 175.0,
    68: 175.0,
    69: 175.0,
    70: 175.0,
    71: 175.0,
    72: 155.0,
    73: 145.0,
    74: 135.0,
    75: 135.0,
    76: 130.0,
    77: 135.0,
    78: 135.0,
    79: 135.0,
    80: 150.0,
    81: 190.0,
    82: 180.0,
    83: 160.0,
    84: 190.0,
    85: float("NaN"),
    86: float("NaN"),
    87: float("NaN"),
    88: 215.0,
    89: 195.0,
    90: 180.0,
    91: 180.0,
    92: 175.0,
    93: 175.0,
    94: 175.0,
    95: 175.0,
    96: float("NaN"),
    97: float("NaN"),
    98: float("NaN"),
    99: float("NaN"),
    100: float("NaN"),
}