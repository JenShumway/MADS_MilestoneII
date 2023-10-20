import pandas as pd

# Load data
mapping_oecd_to_names_and_additional_info_df = pd.read_csv(
    "../OECD/Cleaned/OECD_Indicator_Definition_Info.csv",
)
mapping_world_bank_to_names_and_definitions_df = pd.read_csv(
    "../WorldBankDatasets/Cleaned/World_Bank_Indicator_Definition_Info.csv",
    delimiter="\t",
)

data_maps = [mapping_oecd_to_names_and_additional_info_df, mapping_world_bank_to_names_and_definitions_df]

# Get the mapping required
def get_mapping(code):
    
    # Check if the mapping contains the code and return if it does
    for map in data_maps:
        if map['indicator_code'].str.contains(code).any():
            return map

# get the name of the indicator from the code
def get_ind_name(code):

    mapping_df = get_mapping(code)

    indicator_name_series = mapping_df[mapping_df["indicator_code"] == code][
        "indicator_name"
    ]
    try:
        indicator_name = indicator_name_series.values[0]
    except:
        # print(f'this code {code} may be missing a name')
        indicator_name = None

    return indicator_name


# get either the full definition (World Bank) or additional information (OECD)
def get_ind_info(code):

    mapping_df = get_mapping(code)

    indicator_definition_series = mapping_df[mapping_df["indicator_code"] == code][
        "definition_or_additional_info"
    ]
    try:
        indicator_definition_or_additional_info = indicator_definition_series.values[0]
    except:
        # print(f'this code {code} may be missing a definition or additional info')
        indicator_definition_or_additional_info = None

    return indicator_definition_or_additional_info
