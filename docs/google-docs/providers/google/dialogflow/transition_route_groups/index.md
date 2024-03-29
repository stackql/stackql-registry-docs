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
| `name` | `string` | The unique identifier of the transition route group. TransitionRouteGroups.CreateTransitionRouteGroup populates the name automatically. Format: `projects//locations//agents//flows//transitionRouteGroups/` . |
| `transitionRoutes` | `array` | Transition routes associated with the TransitionRouteGroup. |
| `displayName` | `string` | Required. The human-readable name of the transition route group, unique within the flow. The display name can be no longer than 30 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_flows_transition_route_groups_get` | `SELECT` | `agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId` | Retrieves the specified TransitionRouteGroup. |
| `projects_locations_agents_flows_transition_route_groups_list` | `SELECT` | `agentsId, flowsId, locationsId, projectsId` | Returns the list of all transition route groups in the specified flow. |
| `projects_locations_agents_transition_route_groups_get` | `SELECT` | `agentsId, locationsId, projectsId, transitionRouteGroupsId` | Retrieves the specified TransitionRouteGroup. |
| `projects_locations_agents_transition_route_groups_list` | `SELECT` | `agentsId, locationsId, projectsId` | Returns the list of all transition route groups in the specified flow. |
| `projects_locations_agents_flows_transition_route_groups_create` | `INSERT` | `agentsId, flowsId, locationsId, projectsId` | Creates an TransitionRouteGroup in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_transition_route_groups_create` | `INSERT` | `agentsId, locationsId, projectsId` | Creates an TransitionRouteGroup in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_transition_route_groups_delete` | `DELETE` | `agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId` | Deletes the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_transition_route_groups_delete` | `DELETE` | `agentsId, locationsId, projectsId, transitionRouteGroupsId` | Deletes the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `_projects_locations_agents_flows_transition_route_groups_list` | `EXEC` | `agentsId, flowsId, locationsId, projectsId` | Returns the list of all transition route groups in the specified flow. |
| `_projects_locations_agents_transition_route_groups_list` | `EXEC` | `agentsId, locationsId, projectsId` | Returns the list of all transition route groups in the specified flow. |
| `projects_locations_agents_flows_transition_route_groups_patch` | `EXEC` | `agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId` | Updates the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_transition_route_groups_patch` | `EXEC` | `agentsId, locationsId, projectsId, transitionRouteGroupsId` | Updates the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
