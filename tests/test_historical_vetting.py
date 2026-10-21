from scenariocompass import HistoricalVetting


def test_historical_vetting_pass(historical_vetting_df):
    """Assert a historical vetting is passing as expected"""

    historical_vetting = HistoricalVetting()
    obs = historical_vetting.apply(historical_vetting_df)

    assert (obs.meta[historical_vetting.vetting_indicator] == "passed").iloc[0]
    assert (obs.meta[historical_vetting.criteria_names] == "ok").all(axis=1).iloc[0]


def test_historical_vetting_insufficient_reporting(historical_vetting_df):
    """Assert that missing a vetting-variable yields 'insufficient_reporting' and n/a"""

    historical_vetting = HistoricalVetting()
    variable = "Primary Energy|Nuclear"
    obs = historical_vetting.apply(historical_vetting_df.filter(
        variable=variable, keep=False,
    ))

    assert all(
        obs.meta[historical_vetting.vetting_indicator] == "insufficient reporting"
    )

    ok_cols = [col for col in historical_vetting.criteria_names if variable not in col]
    assert (obs.meta[ok_cols] == "ok").all(axis=1).iloc[0]

    # criteria columns where expected variable do not exist are marked as `n/a`
    na_cols = [col for col in historical_vetting.criteria_names if variable in col]
    assert (obs.meta[na_cols].isna()).all(axis=1).iloc[0]
