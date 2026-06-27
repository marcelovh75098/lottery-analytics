from engine.statistics import (
    global_frequency,
    recent_frequency,
    last_seen
)


def build_global_ranking(draws):

    global_freq = global_frequency(draws)

    freq30 = recent_frequency(draws,30)

    freq100 = recent_frequency(draws,100)

    freq200 = recent_frequency(draws,200)

    last = last_seen(draws)

    ranking=[]

    for n in range(1,44):

        score=(

            global_freq.get(n,0)*0.25+

            freq30.get(n,0)*2+

            freq100.get(n,0)*1.5+

            freq200.get(n,0)*1-

            last.get(n,0)*0.15

        )

        ranking.append({

            "number":n,

            "score":round(score,4),

            "historical_count":global_freq.get(n,0),

            "recent30":freq30.get(n,0),

            "recent100":freq100.get(n,0),

            "recent200":freq200.get(n,0),

            "last_seen":last.get(n,0)

        })

    ranking.sort(

        key=lambda x:x["score"],

        reverse=True

    )

    return ranking
