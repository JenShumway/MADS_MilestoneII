# mapping world bank codes to definitions
import pandas as pd

mapping_world_bank_to_names_and_definitions_df = pd.read_csv('../WorldBankDatasets/Cleaned/World_Bank_Indicator_Definition_Info.csv',
                                                             delimiter='\t')

# get the feature name of a given World Bank indicator
# Why? World Bank codes can seem very cryptic. This will give a full name to the code. If you want a full definition,
# see the function get_world_bank_indicator_definition_from_code below
def get_world_bank_indicator_name_from_code(world_bank_code, mapping_df=mapping_world_bank_to_names_and_definitions_df):
    # print(f"World Bank Code {world_bank_code}")
    indicator_name_series = mapping_df[mapping_df['indicator_code'] == world_bank_code]['indicator_name']

    try:
        indicator_name = indicator_name_series.values[0]
    except:
        # print(f'this code {world_bank_code} may be missing a name')
        indicator_name = None

    return indicator_name

# get the full definition of a World Bank indicator from the code
def get_world_bank_indicator_definition_from_code(world_bank_code, mapping_df=mapping_world_bank_to_names_and_definitions_df):
    indicator_definition_series = mapping_df[mapping_df['indicator_code'] == world_bank_code]['long_definition']
    # indicator_definition = ''
    try:
        indicator_definition = indicator_definition_series.values[0]
    except:
        # print(f'this code {world_bank_code} may be missing a definition')
        indicator_definition = None

    return indicator_definition