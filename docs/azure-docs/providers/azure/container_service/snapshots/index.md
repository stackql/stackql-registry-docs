---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - container_service
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties used to configure a node pool snapshot. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Snapshots_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
| `Snapshots_List` | `SELECT` | `subscriptionId` |
| `Snapshots_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Snapshots_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` |
| `Snapshots_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` |
| `Snapshots_UpdateTags` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |
