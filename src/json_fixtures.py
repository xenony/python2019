class JSONFixture:

    def create_issue(self, summary, assignee, priority):
        json = {
            "fields": {
                "project":
                    {
                        "key": "WEBINAR"
                    },
                "summary": summary,
                "description": "Creating of an issue",
                "assignee": {"name": assignee},
                "priority": {"name": priority},
                "issuetype": {"name": "Bug"}
            }
        }
        return json

    def search_issue(self, issue_name, start, max_results):
        json = {
            "jql": "summary~" + issue_name,
            "startAt": start,
            "maxResults": max_results
        }
        return json
