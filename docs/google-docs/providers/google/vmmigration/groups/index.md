---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - vmmigration
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
<tr><td><b>Id</b></td><td><code>google.vmmigration.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The Group name. |
| `description` | `string` | User-provided description of the group. |
| `displayName` | `string` | Display name is a user defined name for this group which can be updated. |
| `migrationTargetType` | `string` | Immutable. The target type of this group. |
| `updateTime` | `string` | Output only. The update time timestamp. |
| `createTime` | `string` | Output only. The create time timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `groupsId, locationsId, projectsId` | Gets details of a single Group. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Groups in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Group in a given project and location. |
| `delete` | `DELETE` | `groupsId, locationsId, projectsId` | Deletes a single Group. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Groups in a given project and location. |
| `patch` | `EXEC` | `groupsId, locationsId, projectsId` | Updates the parameters of a single Group. |
