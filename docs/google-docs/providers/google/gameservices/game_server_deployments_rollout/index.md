---
title: game_server_deployments_rollout
hide_title: false
hide_table_of_contents: false
keywords:
  - game_server_deployments_rollout
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
<tr><td><b>Name</b></td><td><code>game_server_deployments_rollout</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gameservices.game_server_deployments_rollout</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the game server deployment rollout, in the following form: `projects/{project}/locations/{locationId}/gameServerDeployments/{deploymentId}/rollout`. For example, `projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout`. |
| `updateTime` | `string` | Output only. The last-modified time. |
| `createTime` | `string` | Output only. The creation time. |
| `defaultGameServerConfig` | `string` | The default game server config is applied to all realms unless overridden in the rollout. For example, `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`. |
| `etag` | `string` | ETag of the resource. |
| `gameServerConfigOverrides` | `array` | Contains the game server config rollout overrides. Overrides are processed in the order they are listed. Once a match is found for a realm, the rest of the list is not processed. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_gameServerDeployments_getRollout` | `SELECT` | `gameServerDeploymentsId, locationsId, projectsId` |
