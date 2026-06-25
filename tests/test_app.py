from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    email = "newstudent@mergington.edu"

    signup_response = client.post(
        f"/activities/Chess Club/signup?email={email}"
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        f"/activities/Chess Club/signup?email={email}"
    )

    assert unregister_response.status_code == 200
    assert unregister_response.json()["message"] == f"Unregistered {email} from Chess Club"

    activities_response = client.get("/activities")
    activity = activities_response.json()["Chess Club"]
    assert email not in activity["participants"]
