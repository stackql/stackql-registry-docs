---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the group. |
| `description` | `string` | The description of the resource. |
| `displayName` | `string` | User-friendly display name. |
| `labels` | `object` | Labels as key value pairs. |
| `updateTime` | `string` | Output only. The timestamp when the group was last updated. |
| `createTime` | `string` | Output only. The timestamp when the group was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupsId, locationsId, projectsId` | Gets the details of a group. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all groups in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new group in a given project and location. |
| `delete` | `DELETE` | `groupsId, locationsId, projectsId` | Deletes a group. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists all groups in a given project and location. |
| `patch` | `EXEC` | `groupsId, locationsId, projectsId` | Updates the parameters of a group. |
