---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The full name of the source. |
| `description` | `string` | Free-text description. |
| `createTime` | `string` | Output only. The timestamp when the source was created. |
| `managed` | `boolean` | If `true`, the source is managed by other service(s). |
| `pendingFrameCount` | `integer` | Output only. Number of frames that are still being processed. |
| `priority` | `integer` | The information confidence of the source. The higher the value, the higher the confidence. |
| `updateTime` | `string` | Output only. The timestamp when the source was last updated. |
| `errorFrameCount` | `integer` | Output only. The number of frames that were reported by the source and contained errors. |
| `state` | `string` | Output only. The state of the source. |
| `type` | `string` | Data source type. |
| `displayName` | `string` | User-friendly display name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, sourcesId` | Gets the details of a source. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the sources in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new source in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, sourcesId` | Deletes a source. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists all the sources in a given project and location. |
| `patch` | `EXEC` | `locationsId, projectsId, sourcesId` | Updates the parameters of a source. |
