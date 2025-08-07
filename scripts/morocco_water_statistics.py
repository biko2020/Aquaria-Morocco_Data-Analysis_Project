import pandas as pd
import numpy as np

# 1. NATIONAL WATER OVERVIEW DATA
national_water_data = {
    'metric': [
        'total_large_dams',
        'total_dam_capacity_bcm',
        'small_medium_dams', 
        'national_dam_filling_rate_percent',
        'agricultural_dam_filling_rate_percent',
        'per_capita_water_availability_m3',
        'water_stress_threshold_m3',
        'total_renewable_freshwater_bcm_yr',
        'groundwater_withdrawals_mcm_yr',
        'groundwater_overexploitation_bcm_yr',
        'agriculture_water_usage_percent',
        'agriculture_gdp_contribution_percent',
        'rainfall_reduction_2024_percent',
        'water_decline_since_1960s_percent'
    ],
    'value': [149, 19.1, 137, 23.17, 28.0, 650, 1000, 2.5, 3170, 4.2, 86, 13, 70, 77],
    'unit': [
        'count', 'billion_m3', 'count', 'percent', 'percent', 'm3_per_capita', 
        'm3_per_capita', 'BCM/yr', 'MCM/yr', 'BCM/yr', 'percent', 'percent', 
        'percent', 'percent'
    ],
    'year': [2024] * 14,
    'source': ['Ministry_Equipment_Water'] * 14,
    'criticality': [
        'medium', 'high', 'low', 'critical', 'critical', 'critical', 
        'reference', 'high', 'high', 'critical', 'high', 'medium', 
        'critical', 'critical'
    ]
}

# 2. REGIONAL DAM PERFORMANCE DATA
regional_dam_data = {
    'basin_name': [
        'Oum_Errabia', 'El_Nahla', 'Chefchaouen', 'Cherif_Al', 
        'El_Kensera', 'Bab_Louta', 'National_Average'
    ],
    'filling_rate_percent': [11.1, 100, 100, 100, 24, 70, 23.17],
    'capacity_million_m3': [553, None, None, None, 54, 23.9, 20000],
    'performance_status': [
        'critical', 'excellent', 'excellent', 'excellent', 
        'poor', 'good', 'critical'
    ],
    'priority_for_awg': ['high', 'low', 'low', 'low', 'high', 'medium', 'high']
}

# 3. GOVERNMENT INVESTMENT DATA
investment_data = {
    'agency': ['Department_of_Water', 'ONEE', 'Desalination_Program'],
    'investment_million_usd': [80, 56, None],
    'purpose': [
        'groundwater_search', 
        'utility_infrastructure', 
        'desalination_plants'
    ],
    'target_production_bcm': [None, None, 1.7],
    'relevance_to_awg': ['medium', 'high', 'competitive_threat']
}

# 4. TIME SERIES DATA (for trend analysis)
water_availability_trend = {
    'year': [1960, 1990, 2020, 2024],
    'per_capita_m3': [2600, 1500, 700, 650],
    'population_millions': [12, 25, 37, 38],  # estimated
    'water_stress_level': ['none', 'low', 'high', 'critical']
}

# Convert to DataFrames for analysis
df_national = pd.DataFrame(national_water_data)
df_regional = pd.DataFrame(regional_dam_data)
df_investment = pd.DataFrame(investment_data)
df_trends = pd.DataFrame(water_availability_trend)

# 5. MARKET OPPORTUNITY SCORING
def calculate_market_opportunity_score(row):
    """Calculate market opportunity score based on water stress indicators"""
    if row['filling_rate_percent'] < 20:
        return 9  # Critical opportunity
    elif row['filling_rate_percent'] < 40:
        return 7  # High opportunity
    elif row['filling_rate_percent'] < 60:
        return 5  # Medium opportunity
    else:
        return 3  # Lower opportunity

df_regional['market_opportunity_score'] = df_regional.apply(calculate_market_opportunity_score, axis=1)

# 6. KEY METRICS FOR AWG MARKET ANALYSIS
awg_market_metrics = {
    'water_crisis_severity': df_national[df_national['metric'] == 'per_capita_water_availability_m3']['value'].iloc[0] / 1000,  # Below threshold ratio
    'infrastructure_failure_rate': 100 - df_national[df_national['metric'] == 'national_dam_filling_rate_percent']['value'].iloc[0],
    'government_investment_ready_usd': 136_000_000,  # 80M + 56M
    'target_regions_count': len(df_regional[df_regional['market_opportunity_score'] >= 7]),
    'agricultural_market_size_percent': df_national[df_national['metric'] == 'agriculture_water_usage_percent']['value'].iloc[0]
}

# 7. EXPORT DATA FOR FURTHER ANALYSIS
def export_morocco_water_data():
    """Export all datasets to CSV for external analysis"""
    df_national.to_csv('morocco_national_water_data.csv', index=False)
    df_regional.to_csv('morocco_regional_dam_data.csv', index=False)
    df_investment.to_csv('morocco_investment_data.csv', index=False)
    df_trends.to_csv('morocco_water_trends.csv', index=False)
    
    # Create summary statistics
    summary_stats = {
        'critical_regions': df_regional[df_regional['market_opportunity_score'] >= 7]['basin_name'].tolist(),
        'average_filling_rate': df_regional['filling_rate_percent'].mean(),
        'total_government_investment': sum(filter(None, investment_data['investment_million_usd'])),
        'water_stress_severity': awg_market_metrics['water_crisis_severity']
    }
    
    return summary_stats

# USAGE EXAMPLES:

# Example 1: Find highest priority regions for AWG deployment
high_priority_regions = df_regional[df_regional['priority_for_awg'] == 'high']
print("High Priority Regions for AWG:")
print(high_priority_regions[['basin_name', 'filling_rate_percent', 'market_opportunity_score']])

# Example 2: Calculate market size indicators
water_stress_population = 38_000_000 * (650/1000)  # Population affected by water stress
print(f"Population affected by water stress: {water_stress_population:,.0f}")

# Example 3: Track government investment opportunities
total_government_budget = sum([x for x in investment_data['investment_million_usd'] if x is not None])
print(f"Total government water investment: ${total_government_budget}M USD")

# Example 4: Identify competitive advantages
traditional_infrastructure_failure = 100 - df_national[df_national['metric'] == 'national_dam_filling_rate_percent']['value'].iloc[0]
print(f"Traditional infrastructure failure rate: {traditional_infrastructure_failure:.1f}%")

# This structured approach allows for:
# - Easy data manipulation and analysis
# - Integration with visualization tools
# - Automated calculations and scoring
# - Export to other formats (CSV, Excel, databases)
# - Version control and data updates
