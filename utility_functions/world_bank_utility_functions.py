# This file has functions that map World Bank codes to definitions and names

# get the feature name of a given World Bank indicator
# Why? World Bank codes can seem very cryptic. This will give a full name to the code. If you want a full definition,
# see the function get_world_bank_indicator_definition_from_code below
def get_world_bank_indicator_name_from_code(world_bank_code, mapping_df):
    # print(f"World Bank Code {world_bank_code}")
    # print("Inside get_world_bank_indicator_name_from_code function!")
    indicator_name_series = mapping_df[mapping_df['indicator_code'] == world_bank_code]['indicator_name']
    try:
        indicator_name = indicator_name_series.values[0]
    except:
        # print(f'this code {world_bank_code} may be missing a name')
        indicator_name = None

    return indicator_name

# get the full definition of a World Bank indicator from the code
def get_world_bank_indicator_definition_from_code(world_bank_code, mapping_df):
    # print("Inside get_world_bank_indicator_definition_from_code function!")
    indicator_definition_series = mapping_df[mapping_df['indicator_code'] == world_bank_code]['long_definition']
    try:
        indicator_definition = indicator_definition_series.values[0]
    except:
        # print(f'this code {world_bank_code} may be missing a definition')
        indicator_definition = None

    return indicator_definition