---
title: transition_route_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - transition_route_groups
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
<tr><td><b>Name</b></td><td><code>transition_route_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.transition_route_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `transitionRouteGroups` | `array` | The list of transition route groups. There will be a maximum number of items returned based on the page_size field in the request. The list may in some cases be empty or contain fewer entries than page_size even if this isn't the last page. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_flows_transition_route_groups_get` | `SELECT` | `agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId` | Retrieves the specified TransitionRouteGroup. |
| `projects_locations_agents_flows_transition_route_groups_list` | `SELECT` | `agentsId, flowsId, locationsId, projectsId` | Returns the list of all transition route groups in the specified flow. |
| `projects_locations_agents_flows_transition_route_groups_create` | `INSERT` | `agentsId, flowsId, locationsId, projectsId` | Creates an TransitionRouteGroup in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_transition_route_groups_delete` | `DELETE` | `agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId` | Deletes the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_transition_route_groups_patch` | `EXEC` | `agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId` | Updates the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
