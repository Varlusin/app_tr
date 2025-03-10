from ast import main
from shapely import Point, Polygon

SITY_LIST = [
    {
        "id": 1,
        "sity": "Gyumri",
        "sity_en": "Gyumri",
        "sity_ru": "Гюмри",
        "sity_hy": "Գյումրի",
        "geometry": Polygon([ (43.8150, 40.7735), (43.8080, 40.8183), (43.8139624, 40.8237450), (43.8195298, 40.8330391), (43.8352, 40.8329), (43.8832, 40.8156), (43.87099, 40.7868), (43.8680, 40.77975), (43.8670476, 40.7769898), (43.8704714, 40.7724497), (43.8593, 40.7398), (43.8276, 40.7521), (43.8244, 40.76305), (43.8248, 40.7650), (43.8150, 40.7735),]),
    },
    {
        "id": 2,
        "sity": "Azatan",
        "sity_en": "Azatan",
        "sity_hy": "Ազատան",
        "sity_ru": "Азатан",
        "geometry": Polygon([ (43.8300, 40.7355), (43.8305, 40.7312), (43.8376, 40.7200), (43.8396, 40.7135), (43.8328, 40.7098), (43.8257, 40.7072), (43.8185, 40.7201), (43.8177, 40.7309), (43.8238, 40.7356), (43.8274, 40.7369), (43.8300, 40.7355),]),
    },
    {
        "id": 3,
        "sity": "Akhuryan",
        "sity_en": "Akhuryan",
        "sity_ru": "Ахурян",
        "sity_hy": "Ախուրյան",
        "geometry": Polygon([ (43.8670476, 40.7769898), (43.8704714, 40.7724497), (43.9129, 40.7691), (43.9121, 40.7843), (43.8914, 40.7874), (43.87099, 40.7868), (43.8680, 40.77975), (43.8670476, 40.7769898),]),
    },
    {
        "id": 4,
        "sity": "Maisyan",
        "sity_en": "Maisyan",
        "sity_ru": "Маисян",
        "sity_hy": "Մայիսյան",
        "geometry": Polygon([ (43.8271, 40.8538), (43.8485, 40.8522), (43.8470, 40.8415), (43.8251, 40.8427), (43.8271, 40.8538),]),
    },
    {
        "id": 5,
        "sity": "Marmashen",
        "sity_en": "Marmashen",
        "sity_ru": "Мармашен",
        "sity_hy": "Մարմաշեն",
        "geometry": Polygon([ (43.7770, 40.8447), (43.7907, 40.8369), (43.7796, 40.8281), (43.7726, 40.8365), (43.7706, 40.8402), (43.7770, 40.8447),]),
    },
    {
        "id": 6,
        "sity": "Hatsik",
        "sity_en": "Hatsik",
        "sity_ru": "Ацик",
        "sity_hy": "Հացիկ",
        "geometry": Polygon([ (43.8660, 40.8506), (43.8830, 40.8487), (43.8785, 40.8373), (43.8661, 40.8394), (43.8660, 40.8506),]),
    },
    {
        "id": 7,
        "sity": "Arevik",
        "sity_en": "Arevik",
        "sity_ru": "Аревик",
        "sity_hy": "Արևիկ",
        "geometry": Polygon([ (43.9066, 40.7496), (43.9108, 40.7343), (43.9070, 40.7325), (43.8940, 40.7452), (43.9001, 40.7489), (43.9050, 40.7500), (43.9066, 40.7496),]),
    },
    {
        "id": 8,
        "sity": "Arapi",
        "sity_en": "Arapi",
        "sity_ru": "Арапи",
        "sity_hy": "Առափի",
        "geometry": Polygon([ (43.8066, 40.7935), (43.8100, 40.7896), (43.8120, 40.7798), (43.8092, 40.7736), (43.8060, 40.7725), (43.8042, 40.7768), (43.8013, 40.7801), (43.8005, 40.7877), (43.8066, 40.7935),]),
    },
    {
        "id": 9,
        "sity": "Shirak",
        "sity_en": "Shirak",
        "sity_ru": "Ширак",
        "sity_hy": "Շիրակ",
        "geometry": Polygon([ (43.9075, 40.8440), (43.9132, 40.8444), (43.9203, 40.8417), (43.9241, 40.8414), (43.9249, 40.8391), (43.9122, 40.8326), (43.9056, 40.8379), (43.9075, 40.8440), ]),
    },
    {
        "id": 10,
        "sity": "Voskehask",
        "sity_en": "Voskehask",
        "sity_ru": "Воскеаск",
        "sity_hy": "Ոսկեհասկ",
        "geometry": Polygon([ (43.7695, 40.7724), (43.7786, 40.7747), (43.7869, 40.7529), (43.7703, 40.7532), (43.7679, 40.7681), (43.7695, 40.7724),]),
    },
    {
        "id": 11,
        "sity": "Akhurik",
        "sity_en": "Akhurik",
        "sity_ru": "Ахурик",
        "sity_hy": "Ախուրիկ",
        "geometry": Polygon([ (43.7689, 40.7509), (43.7836, 40.7511), (43.7889, 40.7486), (43.7857, 40.7434), (43.7783, 40.7347), (43.7702, 40.7337), (43.7639, 40.7384), (43.7689, 40.7509),]),
    },
    {
        "id": 12,
        "sity": "Gharibjanyan",
        "sity_en": "Gharibjanyan",
        "sity_ru": "Гарибджанян",
        "sity_hy": "Ղարիբջանյան",
        "geometry": Polygon([ (43.7981, 40.7457), (43.8075, 40.7463), (43.8092, 40.7381), (43.7911, 40.7361), (43.7906, 40.7393), (43.7981, 40.7457),]),
    },
    {
        "id": 13,
        "sity": "Getk",
        "sity_en": "Getk",
        "sity_ru": "Гетк",
        "sity_hy": "Գետք",
        "geometry": Polygon([ (43.7926, 40.7283), (43.7857, 40.7226), (43.7804, 40.7225), (43.7817, 40.7293), (43.7899, 40.7338), (43.7911, 40.7334), (43.7926, 40.7283),]),
    },
]

COMUNITY_DATA = [
    {
        "id": 1,
        "geometry": Polygon(
            [
                (43.8355419, 40.7936076),
                (43.8356513, 40.7916763),
                (43.836466, 40.7897871),
                (43.8367802, 40.7894194),
                (43.8369257, 40.7891397),
                (43.8367324, 40.78677),
                (43.834886, 40.7856594),
                (43.8341457, 40.784908),
                (43.8308803, 40.784417),
                (43.8270, 40.777),
                (43.8261, 40.7764),
                (43.8257, 40.7766),
                (43.8232, 40.7766),
                (43.8212, 40.7753),
                (43.8150, 40.7735),
                (43.8248, 40.7650),
                (43.8290, 40.7704),
                (43.8370, 40.7754),
                (43.8384, 40.7746),
                (43.8397, 40.7755),
                (43.8433, 40.7775),
                (43.8426, 40.7781),
                (43.8422, 40.7788),
                (43.8424, 40.7789),
                (43.8434, 40.7792),
                (43.8436, 40.7793),
                (43.8439, 40.7795),
                (43.8441, 40.7797),
                (43.8442, 40.7800),
                (43.84434, 40.7808),
                (43.8455, 40.7873),
                (43.8459, 40.7884),
                (43.84635, 40.79305),
                (43.8355419, 40.7936076),
            ]
        ),
    },
    {
        "id": 2,
        "geometry": Polygon(
            [
                (43.863311, 40.8029465),
                (43.8607303, 40.8052008),
                (43.8603626, 40.8053139),
                (43.8486635, 40.8062964),
                (43.8474827, 40.8070603),
                (43.8330663, 40.8223807),
                (43.8313751, 40.8140095),
                (43.8308556, 40.8114423),
                (43.8340665, 40.8014731),
                (43.8353686, 40.7978253),
                (43.8355419, 40.7936076),
                (43.84635, 40.79305),
                (43.8474783, 40.792988),
                (43.8476348, 40.792943),
                (43.863311, 40.8029465),
            ]
        ),
    },
    {
        "id": 3,
        "geometry": Polygon(
            [
                (43.8313751, 40.8140095),
                (43.8139624, 40.8237450),
                (43.8195298, 40.8330391),
                (43.8352, 40.8329),
                (43.8330663, 40.8223807),
                (43.8313751, 40.8140095),
            ]
        ),
    },
    {
        "id": 4,
        "geometry": Polygon(
            [
                (43.8680, 40.77975),
                (43.8560, 40.77915),
                (43.8557, 40.7792),
                (43.8540, 40.7799),
                (43.8534, 40.78015),
                (43.8529, 40.7803),
                (43.8520, 40.78045),
                (43.8448, 40.7807),
                (43.84434, 40.7808),
                (43.8455, 40.7873),
                (43.8459, 40.7884),
                (43.84635, 40.79305),
                (43.8474783, 40.792988),
                (43.8476348, 40.792943),
                (43.863311, 40.8029465),
                (43.8832, 40.8156),
                (43.8680, 40.77975),
            ]
        ),
    },
    {
        "id": 5,
        "geometry": Polygon(
            [
                (43.8139624, 40.8237450),
                (43.8313751, 40.8140095),
                (43.8308556, 40.8114423),
                (43.8340665, 40.8014731),
                (43.8353686, 40.7978253),
                (43.8355419, 40.7936076),
                (43.8356513, 40.7916763),
                (43.836466, 40.7897871),
                (43.8367802, 40.7894194),
                (43.8369257, 40.7891397),
                (43.8367324, 40.78677),
                (43.834886, 40.7856594),
                (43.8341457, 40.784908),
                (43.8308803, 40.784417),
                (43.8270, 40.777),
                (43.8261, 40.7764),
                (43.8257, 40.7766),
                (43.8232, 40.7766),
                (43.8212, 40.7753),
                (43.8150, 40.7735),
                (43.8080, 40.8183),
                (43.8139624, 40.8237450),
            ]
        ),
    },
    {
        "id": 6,
        "geometry": Polygon(
            [
                (43.8680, 40.77975),
                (43.8560, 40.77915),
                (43.8557, 40.7792),
                (43.8540, 40.7799),
                (43.8534, 40.78015),
                (43.8529, 40.7803),
                (43.8520, 40.78045),
                (43.8448, 40.7807),
                (43.84434, 40.7808),
                (43.8442, 40.7800),
                (43.8441, 40.7797),
                (43.8439, 40.7795),
                (43.8436, 40.7793),
                (43.8434, 40.7792),
                (43.8424, 40.7789),
                (43.8422, 40.7788),
                (43.8426, 40.7781),
                (43.8433, 40.7775),
                (43.8397, 40.7755),
                (43.8384, 40.7746),
                (43.8370, 40.7754),
                (43.8290, 40.7704),
                (43.8248, 40.7650),
                (43.8244, 40.76305),
                (43.8276, 40.7521),
                (43.8593, 40.7398),
                (43.8704714, 40.7724497),
                (43.8670476, 40.7769898),
                (43.8680, 40.77975),
            ]
        ),
    },
    {
        "id": 7,
        "geometry": Polygon(
            [
                (43.8352, 40.8329),
                (43.8832, 40.8156),
                (43.863311, 40.8029465),
                (43.8607303, 40.8052008),
                (43.8603626, 40.8053139),
                (43.8486635, 40.8062964),
                (43.8474827, 40.8070603),
                (43.8330663, 40.8223807),
                (43.8352, 40.8329),
            ]
        ),
    },
]

DONT_AVELABLE = {
    "sor_en": "Sorry, the service is not available at the specified location.",
    "sor_hy": "Կներեք նշված վայրում ծառայությունը հասանելի չէ։",
    "sor_ru": "К сожалению, услуга недоступна по указанному адресу.",
}

SHIRAKI_MARZ = {
    "shirak_en": "Shirak region",
    "shirak_ru": "Ширакская область",
    "shirak_hy": "Շիրակի մարզ",
}

SERVICE_AVAILABLE_SPACE = Polygon(
    [
        (43.7643, 40.8442),
        (43.827, 40.854),
        (43.9263, 40.85),
        (43.9208, 40.7236),
        (43.8257, 40.7064),
        (43.7603, 40.729),
        (43.7643, 40.8442),
    ]
)

if __name__ == "__main__":
    main()
