---
title: inventory_source_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_source_groups
  - displayvideo
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
<tr><td><b>Name</b></td><td><code>inventory_source_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.inventory_source_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the inventory source group. |
| `displayName` | `string` | Required. The display name of the inventory source group. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `inventorySourceGroupId` | `string` | Output only. The unique ID of the inventory source group. Assigned by the system. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `inventorySourceGroups_get` | `SELECT` | `inventorySourceGroupsId` | Gets an inventory source group. |
| `inventorySourceGroups_list` | `SELECT` |  | Lists inventory source groups that are accessible to the current user. The order is defined by the order_by parameter. |
| `inventorySourceGroups_create` | `INSERT` |  | Creates a new inventory source group. Returns the newly created inventory source group if successful. |
| `inventorySourceGroups_delete` | `DELETE` | `inventorySourceGroupsId` | Deletes an inventory source group. |
| `inventorySourceGroups_patch` | `EXEC` | `inventorySourceGroupId` | Updates an inventory source group. Returns the updated inventory source group if successful. |
