def choose_topic(candidate, curriculum):

    # Missions the candidate passed
    passed = []

    for mission in candidate["missions"]:
        if mission.get("passed") is True:
            passed.append(mission["day"])

    # Find first passed topic in curriculum
    for day in curriculum["days"]:
        if day["day"] in passed:
            return day

    # fallback
    return curriculum["days"][0]