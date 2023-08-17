---
title: entity_types
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_types
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
<tr><td><b>Name</b></td><td><code>entity_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.entity_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The unique identifier of the session entity type. Format: `projects//locations//agents//sessions//entityTypes/` or `projects//locations//agents//environments//sessions//entityTypes/`. If `Environment ID` is not specified, we assume default 'draft' environment. |
| `entities` | `array` | Required. The collection of entities to override or supplement the custom entity type. |
| `entityOverrideMode` | `string` | Required. Indicates whether the additional data should override or supplement the custom entity type definition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_entity_types_get` | `SELECT` | `agentsId, entityTypesId, locationsId, projectsId` | Retrieves the specified entity type. |
| `projects_locations_agents_entity_types_list` | `SELECT` | `agentsId, locationsId, projectsId` | Returns the list of all entity types in the specified agent. |
| `projects_locations_agents_environments_sessions_entity_types_get` | `SELECT` | `agentsId, entityTypesId, environmentsId, locationsId, projectsId, sessionsId` | Retrieves the specified session entity type. |
| `projects_locations_agents_environments_sessions_entity_types_list` | `SELECT` | `agentsId, environmentsId, locationsId, projectsId, sessionsId` | Returns the list of all session entity types in the specified session. |
| `projects_locations_agents_sessions_entity_types_get` | `SELECT` | `agentsId, entityTypesId, locationsId, projectsId, sessionsId` | Retrieves the specified session entity type. |
| `projects_locations_agents_sessions_entity_types_list` | `SELECT` | `agentsId, locationsId, projectsId, sessionsId` | Returns the list of all session entity types in the specified session. |
| `projects_locations_agents_entity_types_create` | `INSERT` | `agentsId, locationsId, projectsId` | Creates an entity type in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_environments_sessions_entity_types_create` | `INSERT` | `agentsId, environmentsId, locationsId, projectsId, sessionsId` | Creates a session entity type. |
| `projects_locations_agents_sessions_entity_types_create` | `INSERT` | `agentsId, locationsId, projectsId, sessionsId` | Creates a session entity type. |
| `projects_locations_agents_entity_types_delete` | `DELETE` | `agentsId, entityTypesId, locationsId, projectsId` | Deletes the specified entity type. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_environments_sessions_entity_types_delete` | `DELETE` | `agentsId, entityTypesId, environmentsId, locationsId, projectsId, sessionsId` | Deletes the specified session entity type. |
| `projects_locations_agents_sessions_entity_types_delete` | `DELETE` | `agentsId, entityTypesId, locationsId, projectsId, sessionsId` | Deletes the specified session entity type. |
| `_projects_locations_agents_entity_types_list` | `EXEC` | `agentsId, locationsId, projectsId` | Returns the list of all entity types in the specified agent. |
| `_projects_locations_agents_environments_sessions_entity_types_list` | `EXEC` | `agentsId, environmentsId, locationsId, projectsId, sessionsId` | Returns the list of all session entity types in the specified session. |
| `_projects_locations_agents_sessions_entity_types_list` | `EXEC` | `agentsId, locationsId, projectsId, sessionsId` | Returns the list of all session entity types in the specified session. |
| `projects_locations_agents_entity_types_patch` | `EXEC` | `agentsId, entityTypesId, locationsId, projectsId` | Updates the specified entity type. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_environments_sessions_entity_types_patch` | `EXEC` | `agentsId, entityTypesId, environmentsId, locationsId, projectsId, sessionsId` | Updates the specified session entity type. |
| `projects_locations_agents_sessions_entity_types_patch` | `EXEC` | `agentsId, entityTypesId, locationsId, projectsId, sessionsId` | Updates the specified session entity type. |
