---
title: game_server_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - game_server_deployments
  - gameservices
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
<tr><td><b>Name</b></td><td><code>game_server_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gameservices.game_server_deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the game server deployment, in the following form: `projects/{project}/locations/{locationId}/gameServerDeployments/{deploymentId}`. For example, `projects/my-project/locations/global/gameServerDeployments/my-deployment`. |
| `description` | `string` | Human readable description of the game server deployment. |
| `labels` | `object` | The labels associated with this game server deployment. Each label is a key-value pair. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `createTime` | `string` | Output only. The creation time. |
| `etag` | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gameServerDeployments_get` | `SELECT` | `gameServerDeploymentsId, locationsId, projectsId` | Gets details of a single game server deployment. |
| `projects_locations_gameServerDeployments_list` | `SELECT` | `locationsId, projectsId` | Lists game server deployments in a given project and location. |
| `projects_locations_gameServerDeployments_create` | `INSERT` | `locationsId, projectsId` | Creates a new game server deployment in a given project and location. |
| `projects_locations_gameServerDeployments_delete` | `DELETE` | `gameServerDeploymentsId, locationsId, projectsId` | Deletes a single game server deployment. |
| `projects_locations_gameServerDeployments_patch` | `EXEC` | `gameServerDeploymentsId, locationsId, projectsId` | Patches a game server deployment. |
| `projects_locations_gameServerDeployments_previewRollout` | `EXEC` | `gameServerDeploymentsId, locationsId, projectsId` | Previews the game server deployment rollout. This API does not mutate the rollout resource. |
| `projects_locations_gameServerDeployments_updateRollout` | `EXEC` | `gameServerDeploymentsId, locationsId, projectsId` | Patches a single game server deployment rollout. The method will not return an error if the update does not affect any existing realms. For example, the following cases will not return an error: * The default_game_server_config is changed but all existing realms use the override. * A non-existing realm is explicitly called out in the game_server_config_overrides field. |
