---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - area120tables
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.area120tables.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the workspace. Workspace names have the form `workspaces/&#123;workspace&#125;`. |
| `updateTime` | `string` | Time when the workspace was last updated. |
| `createTime` | `string` | Time when the workspace was created. |
| `displayName` | `string` | The human readable title of the workspace. |
| `tables` | `array` | The list of tables in the workspace. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `workspacesId` | Gets a workspace. Returns NOT_FOUND if the workspace does not exist. |
| `list` | `SELECT` |  | Lists workspaces for the user. |
