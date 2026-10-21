from scenariocompass import HistoricalVetting


def test_historical_vetting_fail(historical_vetting_df):

    historical_vetting_df = HistoricalVetting().apply(historical_vetting_df)

    for col in historical_vetting_df.meta.columns:
        if col in [
            "Historical Vetting [SCI 2025]",
            "Historical Vetting|Primary Energy|Gas|2025",
            "Historical Vetting|Primary Energy|Nuclear|2025",
        ]:
            assert historical_vetting_df.meta.iloc[0][col] == "failed"
        else:
            assert historical_vetting_df.meta.iloc[0][col] == "ok"
