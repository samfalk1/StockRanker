# StockRanker

This python code in pandas library has a CSV with 11,700 stocks downloaded from stock screener database.  The code ranks all the stocks by relative rank for 5 common value financial ratios.  The five statistics are: P/E, P/B, P/S, current ratio, and debt:equity ratio.  Then the code sums the score of each stock for each statistic to create a "Composite Value Score".  Then the code ranks all the stocks by the composite value score, so you can get a short list of the best "value" stocks across many statistics.
