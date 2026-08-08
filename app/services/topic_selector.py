def get_available_topics(candidate, curriculum):

    # Find the curriculum days the candidate has passed
    passed_days = []
    
    for mission in candidate["missions"]:
        if mission.get("passed") is True:
            passed_days.append(mission["day"])
    
    # Get matching curriculum days
    available_topics = []
    
    for day in curriculum["days"]:
        if day["day"] in passed_days:
            available_topics.append(day)
    
    # Fallback if no matching days exist
    if not available_topics:
        available_topics = curriculum["days"]
    
    return available_topics
    
def choose_topic(candidate, curriculum, excluded_days=None):
    
    excluded_days = excluded_days or set()
    
    available_topics = get_available_topics(
        candidate,
        curriculum
    )
    
    # Prefer a topic that hasn't been covered yet
    for topic in available_topics:
    
        if topic["day"] not in excluded_days:
            return topic
    
    # If everything has been covered, fall back to the first topic
    return available_topics[0]