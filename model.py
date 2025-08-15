def predict(runs,batting_avg,bowling_avg,economy_rate,wickets):
    predicted_role = None
    if runs >= 4000 and batting_avg >= 35:
        predicted_role = 'Batsman'
    elif bowling_avg < 20 and economy_rate < 5.5 and wickets > 150:
        predicted_role = 'Bowler'
    else:
        predicted_role = 'All-rounder'
    return predicted_role