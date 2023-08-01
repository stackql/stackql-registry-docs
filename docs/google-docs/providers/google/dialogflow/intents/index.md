---
title: intents
hide_title: false
hide_table_of_contents: false
keywords:
  - intents
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>intents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.intents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `intents` | `array` | The list of intents. There will be a maximum number of items returned based on the page_size field in the request. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_intents_list` | `SELECT` | `agentsId, locationsId, projectsId` | Returns the list of all intents in the specified agent. |
| `projects_locations_agents_intents_create` | `INSERT` | `agentsId, locationsId, projectsId` | Creates an intent in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_intents_delete` | `DELETE` | `agentsId, intentsId, locationsId, projectsId` | Deletes the specified intent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_intents_get` | `EXEC` | `agentsId, intentsId, locationsId, projectsId` | Retrieves the specified intent. |
| `projects_locations_agents_intents_patch` | `EXEC` | `agentsId, intentsId, locationsId, projectsId` | Updates the specified intent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
