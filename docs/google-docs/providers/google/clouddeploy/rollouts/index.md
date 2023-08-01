---
title: rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - rollouts
  - clouddeploy
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
<tr><td><b>Name</b></td><td><code>rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.rollouts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `rollouts` | `array` | The `Rollout` objects. |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Gets details of a single Rollout. |
| `list` | `SELECT` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Lists Rollouts in a given project and location. |
| `create` | `INSERT` | `deliveryPipelinesId, locationsId, projectsId, releasesId` | Creates a new Rollout in a given project and location. |
| `advance` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Advances a Rollout in a given project and location. |
| `approve` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Approves a Rollout. |
| `cancel` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Cancels a Rollout in a given project and location. |
| `ignore_job` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Ignores the specified Job in a Rollout. |
| `retry_job` | `EXEC` | `deliveryPipelinesId, locationsId, projectsId, releasesId, rolloutsId` | Retries the specified Job in a Rollout. |
