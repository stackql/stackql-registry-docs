---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - contactcenterinsights
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the view. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/views/&#123;view&#125; |
| `createTime` | `string` | Output only. The time at which this view was created. |
| `displayName` | `string` | The human-readable display name of the view. |
| `updateTime` | `string` | Output only. The most recent time at which the view was updated. |
| `value` | `string` | String with specific view properties, must be non-empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, viewsId` | Gets a view. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists views. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a view. |
| `delete` | `DELETE` | `locationsId, projectsId, viewsId` | Deletes a view. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists views. |
| `patch` | `EXEC` | `locationsId, projectsId, viewsId` | Updates a view. |
