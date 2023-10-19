# This file has functions that map OECD codes to definitions and additional info

# Why? OECD codes can seem very cryptic. These functions either give the full name or additional information about a code.

# get the feature name of an OECD indicator
def get_oecd_indicator_name_from_code(oecd_code, mapping_df):
    # print(f"OECD code is {oecd_code}")
    # print("inside of get_oecd_indicator_name_from_code function")
    indicator_name_series = mapping_df[mapping_df['indicator_code'] == oecd_code]['indicator_name']
    try:
        indicator_name = indicator_name_series.values[0]
    except:
        # print(f'this code {oecd_code} may be missing a name')
        indicator_name = None

    return indicator_name

# get additional information from the OECD code
# for example if the indicator code is ADMRASTH_M_TOTAL_15_AS_STD_RATE_MPOP
# indicator name would be Asthma hospital admission
# and additional_info would be Male, 15 years old and over, Age-sex standardised rate per 100 000 population
def get_oecd_additional_info_from_code(oecd_code, mapping_df):
    # print("inside of get_additional_info_from_oecd_code function")
    indicator_definition_series = mapping_df[mapping_df['indicator_code'] == oecd_code]['additional_info']
    try:
        indicator_definition = indicator_definition_series.values[0]
    except:
        # print(f'this code {oecd_code} may be missing additional info')
        indicator_definition = None

    return indicator_definition

# # testing
# import pandas as pd
# # mapping_oecd_to_names_and_additional_info_df = pd.read_csv('../OECD/Cleaned/OECD_Indicator_Definition_Info.csv',
# mapping_oecd_to_names_and_additional_info_df = pd.read_csv('OECD/Cleaned/OECD_Indicator_Definition_Info.csv',
#                                                              delimiter=',')

# # mapping_oecd_to_names_and_additional_info_df

# get_oecd_additional_info_from_code('ADMRASTH_M_TOTAL_15_AS_STD_RATE_MPOP', mapping_oecd_to_names_and_additional_info_df)
# # get_oecd_additional_info_from_code('ADMRASTH_M_TOTAL_15_AS_STD_RATE_MPOP', mapping_oecd_to_names_and_additional_info_df)