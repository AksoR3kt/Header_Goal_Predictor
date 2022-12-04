import numpy as np
import pickle
import streamlit as st

#loaded_model = pickle.load(open("C:/Users/akoja/Downloads/header_goals.sav", 'rb'))
loaded_model = pickle.load(open("header_goals.sav", 'rb'))


def header_prediction(input_data, comment):
    input_array = np.asarray(input_data)

    input_array_reshaped = input_array.reshape(1, -1)

    prediction = loaded_model.predict(input_array_reshaped)

    rounded_pred = round(prediction[0])

    return f'{comment} predicted header goal count: {rounded_pred}'

def main():
    st.title('Header goal prediction APP')

    predictor = ''

    valids =[5, 13, 16, 3, 12, 8, 7, 7, 10, 9, 6, 10, 4, 3, 13, 15,
             5, 10, 9, 12, 10, 5, 8, 6, 7, 13, 4, 15, 10, 7, 8, 1, 6, 7, 9, 13, 6, 3, 9]

    teams = ["AFC Bournemouth",
    "Arsenal",
    "Aston Villa",
    "Birmingham City",
    "Blackburn Rovers",
    "Blackpool",
    "Bolton Wanderers",
    "Brighton and Hove Albion",
    "Burnley",
    "Cardiff City",
    "Charlton Athletic",
    "Chelsea",
    "Crystal Palace",
    "Derby County",
    "Everton",
    "Fulham",
    "Huddersfield Town",
    "Hull City",
    "Leicester City",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Middlesbrough",
    "Newcastle United",
    "Norwich City",
    "Portsmouth",
    "Queens Park Rangers",
    "Reading",
    "Sheffield United",
    "Southampton",
    "Stoke City",
    "Sunderland",
    "Swansea City",
    "Tottenham Hotspur",
    "Watford",
    "West Bromwich Albion",
    "West Ham United",
    "Wigan Athletic",
    "Wolverhampton Wanderers"]

    comments = [ "Season 2016-17",
                 "Arsene Wenger's last season",
                 "Season 2007-08",
                 "Season 2009-10",
                 "Season 2007-08",
                 "Last season in the Premier League 2010-11",
                 "Season 2011-12",
                 "Season 2017-18",
                 "Season 2017-18",
                 "Season 2008-09",
                 "Season 2008-09",
                 "Jose Mourinho in the house",
                 "Season 2013-14",
                 "Season 2009-10",
                 "Season 2012-13",
                 "Season 2010-11",
                 "Season 2014-15",
                 "Season 2010-11",
                 "Season 2012-13",
                 "Jurgen Klopp debut season",
                 "More oil, more fun",
                 "Worst season, worst team",
                 "Season 2014-15",
                 "Just shooting the woodwork",
                 "TEEMO PUKKI",
                 "Season 2006-07",
                 "Season 2007-08",
                 "Season 2006-07",
                 "Season 2014-15",
                 "Season 2017-18",
                 "Shaqiri carry",
                 "No headers 'till we die",
                 "Season 2014-15",
                 "Season 2010-11",
                 "Chickens",
                 "Season 2006-07",
                 "Season 2014-15",
                 "Season 2017-18",
                 "Season 2010-11",
                 "Season 2017-18"]

    datas = [[55, 452, 160, 19, 7, 0, 51, 5, 53, 51, 628, 193, 31],
             [74, 594, 234, 17, 4, 1, 68, 7, 89, 117, 572, 225, 57],
             [71, 511, 182, 11, 6, 5, 55, 16, 115, 30, 932, 229, 39],
             [38, 452, 155, 7, 2, 4, 30, 8, 98, 124, 736, 186, 39],
             [52, 478, 155, 5, 5, 3, 43, 9, 142, 84, 911, 205, 39],
             [55, 531, 161, 11, 7, 3, 44, 11, 97, 75, 836, 183, 46],
             [46, 495, 163, 8, 5, 0, 40, 6, 55, 101, 769, 210, 25],
             [34, 384, 119, 8, 5, 0, 30, 4, 98, 32, 680, 163, 30],
             [36, 378, 128, 9, 0, 1, 32, 4, 100, 18, 707, 167, 22],
             [32, 418, 124, 10, 1, 0, 28, 4, 81, 35, 792, 196, 30],
             [34, 418, 133, 11, 4, 1, 27, 7, 96, 84, 750, 178, 39],
             [73, 564, 210, 15, 4, 1, 66, 7, 75, 73, 682, 226, 40],
             [45, 476, 151, 8, 8, 1, 39, 6, 56, 30, 703, 210, 55],
             [20, 376, 116, 7, 0, 0, 15, 5, 103, 29, 804, 158, 39],
             [55, 633, 207, 13, 2, 1, 44, 11, 100, 54, 989, 257, 67],
             [49, 547, 172, 10, 2, 2, 42, 7, 100, 119, 865, 191, 38],
             [28, 362, 109, 8, 2, 0, 27, 1, 67, 26, 765, 165, 21],
             [38, 427, 132, 16, 2, 1, 30, 8, 86, 22, 853, 160, 31],
             [56, 423, 149, 8, 5, 1, 49, 7, 92, 63, 744, 203, 35],
             [63, 629, 202, 16, 2, 1, 48, 15, 91, 75, 780, 265, 36],
             [102, 673, 238, 19, 6, 5, 86, 16, 59, 120, 892, 283, 59],
             [49, 430, 144, 9, 3, 1, 44, 5, 75, 43, 786, 228, 28],
             [27, 351, 100, 6, 2, 0, 26, 1, 51, 37, 722, 141, 19],
             [56, 489, 154, 19, 2, 3, 44, 12, 97, 97, 730, 171, 27],
             [28, 467, 148, 15, 1, 1, 19, 9, 48, 58, 818, 197, 37],
             [45, 525, 186, 9, 2, 0, 32, 13, 141, 84, 783, 247, 39],
             [30, 500, 146, 9, 1, 0, 18, 12, 108, 50, 683, 170, 32],
             [52, 419, 132, 8, 3, 0, 42, 10, 87, 84, 1067, 280, 39],
             [32, 483, 147, 14, 2, 2, 25, 7, 82, 84, 800, 178, 39],
             [37, 450, 145, 15, 3, 1, 34, 3, 73, 56, 800, 227, 37],
             [35, 384, 132, 8, 0, 1, 28, 8, 87, 33, 598, 136, 33],
             [29, 387, 119, 4, 5, 0, 26, 3, 78, 38, 616, 159, 19],
             [42, 441, 136, 14, 5, 3, 35, 7, 82, 46, 725, 163, 31],
             [69, 659, 252, 19, 5, 2, 59, 10, 72, 64, 738, 254, 47],
             [40, 422, 143, 7, 3, 0, 36, 4, 61, 22, 686, 164, 25],
             [53, 506, 170, 15, 5, 0, 46, 7, 100, 30, 778, 202, 39],
             [48, 372, 133, 14, 2, 1, 39, 10, 97, 51, 732, 161, 29],
             [40, 511, 170, 9, 2, 5, 32, 8, 71, 111, 620, 169, 39],
             [40, 473, 152, 10, 3, 0, 37, 3, 82, 30, 999, 205, 29]]

    pred = []

    for i in pred:
        i[0] = datas[i]
        i[1] = comments[i]

    for i in range(39):
        if st.button(teams[i]):
            predictor = header_prediction(datas[i], comments[i])
        f"Valid: {valids[i]}"
        st.success(predictor)

if __name__ == '__main__':
    main()
