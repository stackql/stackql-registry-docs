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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.sessions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_environments_sessions_detectIntent` | `EXEC` | `agentsId, environmentsId, locationsId, projectsId, sessionsId` | Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries. Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). |
| `projects_locations_agents_environments_sessions_fulfillIntent` | `EXEC` | `agentsId, environmentsId, locationsId, projectsId, sessionsId` | Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined. |
| `projects_locations_agents_environments_sessions_matchIntent` | `EXEC` | `agentsId, environmentsId, locationsId, projectsId, sessionsId` | Returns preliminary intent match results, doesn't change the session status. |
| `projects_locations_agents_sessions_detectIntent` | `EXEC` | `agentsId, locationsId, projectsId, sessionsId` | Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries. Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). |
| `projects_locations_agents_sessions_fulfillIntent` | `EXEC` | `agentsId, locationsId, projectsId, sessionsId` | Fulfills a matched intent returned by MatchIntent. Must be called after MatchIntent, with input from MatchIntentResponse. Otherwise, the behavior is undefined. |
| `projects_locations_agents_sessions_matchIntent` | `EXEC` | `agentsId, locationsId, projectsId, sessionsId` | Returns preliminary intent match results, doesn't change the session status. |
