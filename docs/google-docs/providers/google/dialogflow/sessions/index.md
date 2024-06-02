---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - dialogflow
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dialogflow.sessions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_environments_sessions_detect_intent" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId, sessionsId" /> | Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries. Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). |
| <CopyableCode code="projects_locations_agents_environments_sessions_fulfill_intent" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId, sessionsId" /> | Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined. |
| <CopyableCode code="projects_locations_agents_environments_sessions_match_intent" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId, sessionsId" /> | Returns preliminary intent match results, doesn't change the session status. |
| <CopyableCode code="projects_locations_agents_environments_sessions_server_streaming_detect_intent" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId, sessionsId" /> | Processes a natural language query and returns structured, actionable data as a result through server-side streaming. Server-side streaming allows Dialogflow to send [partial responses](https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) earlier in a single request. |
| <CopyableCode code="projects_locations_agents_sessions_detect_intent" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId, sessionsId" /> | Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries. Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). |
| <CopyableCode code="projects_locations_agents_sessions_fulfill_intent" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId, sessionsId" /> | Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined. |
| <CopyableCode code="projects_locations_agents_sessions_match_intent" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId, sessionsId" /> | Returns preliminary intent match results, doesn't change the session status. |
| <CopyableCode code="projects_locations_agents_sessions_server_streaming_detect_intent" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId, sessionsId" /> | Processes a natural language query and returns structured, actionable data as a result through server-side streaming. Server-side streaming allows Dialogflow to send [partial responses](https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) earlier in a single request. |
| <CopyableCode code="projects_locations_agents_sessions_submit_answer_feedback" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId, sessionsId" /> | Updates the feedback received from the user for a single turn of the bot response. |
