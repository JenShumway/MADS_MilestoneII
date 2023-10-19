# This file has functions that map World Bank or OECD codes to indicator names and long definition or additional information

# This file could also support data from other datasets besides the World Bank and OECD if the CSV style match

# In order to  use other data sets, the mapping csv file for that data set should have the following columns:
# indicator_code, indicator_name, definition_or_additional_info

# indicator_code column will have the codes. 
# For example OECD might have the code:
# ADMRASTH_M_TOTAL_15_AS_STD_RATE_MPOP

# And the World Bank might have the code:
# SH.ANM.NPRG.ZS


# indicator_name has the meaningful, succinct name of the code. 
# For example, the World Bank might have a value of:
# Prevalence of anemia among children (% of children ages 6-59 months)

# The OECD might have a value of Asthma hospital admission



# definition_or_additional_info has either the full definition from the World Bank or additional information from the OECD
# For example, the World Bank might have a value of:
# Prevalence of anemia among children (% of children ages 6-59 months)

# The OECD might have a value of Asthma hospital admission


# Why these functions? World Bank and OECD codes can seem very cryptic. These functions map the codes to either the indicator name,
# definition or additional info

# get the name of the indicator from the code
def get_indicator_name_from_code(code, mapping_df):
    # print(f"indicator code is {code}")
    indicator_name_series = mapping_df[mapping_df['indicator_code'] == code]['indicator_name']
    try:
        indicator_name = indicator_name_series.values[0]
    except:
        # print(f'this code {code} may be missing a name')
        indicator_name = None

    return indicator_name

# get either the full definition (World Bank) or additional information (OECD)
def get_indicator_definition_or_additional_info_from_code(code, mapping_df):
    indicator_definition_series = mapping_df[mapping_df['indicator_code'] == code]['definition_or_additional_info']
    try:
        indicator_definition_or_additional_info = indicator_definition_series.values[0]
    except:
        # print(f'this code {code} may be missing a definition or additional info')
        indicator_definition_or_additional_info = None
    
    return indicator_definition_or_additional_info