from scenariocompass import HistoricalVetting


def test_historical_vetting_pass(historical_vetting_df):

    historical_vetting_df = HistoricalVetting().apply(historical_vetting_df)

    assert all(historical_vetting_df.meta.iloc[0][historical_validation] == "passed")
    assert all(test_data.meta[historical_validation.criteria_names] == "ok")


def test_historical_vetting_pass(historical_vetting_df):