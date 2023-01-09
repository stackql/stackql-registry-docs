---
title: assigned_inventory_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - assigned_inventory_sources
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
<tr><td><b>Name</b></td><td><code>assigned_inventory_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.assigned_inventory_sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `assignedInventorySources` | `array` | The list of assigned inventory sources. This list will be absent if empty. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the page_token field in the subsequent call to `ListAssignedInventorySources` method to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `inventorySourceGroups_assignedInventorySources_list` | `SELECT` | `inventorySourceGroupsId` | Lists inventory sources assigned to an inventory source group. |
| `inventorySourceGroups_assignedInventorySources_create` | `INSERT` | `inventorySourceGroupsId` | Creates an assignment between an inventory source and an inventory source group. |
| `inventorySourceGroups_assignedInventorySources_delete` | `DELETE` | `assignedInventorySourcesId, inventorySourceGroupsId` | Deletes the assignment between an inventory source and an inventory source group. |
| `inventorySourceGroups_assignedInventorySources_bulkEdit` | `EXEC` | `inventorySourceGroupsId` | Bulk edits multiple assignments between inventory sources and a single inventory source group. The operation will delete the assigned inventory sources provided in BulkEditAssignedInventorySourcesRequest.deleted_assigned_inventory_sources and then create the assigned inventory sources provided in BulkEditAssignedInventorySourcesRequest.created_assigned_inventory_sources. |
