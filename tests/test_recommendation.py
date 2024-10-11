from app.models.recommendation import get_recommendations

def test_get_recommendations():
    user_id = 1
    recommendations = get_recommendations(user_id)
    assert len(recommendations) > 0
