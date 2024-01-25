---
title: licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.licenses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a License Profile. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `licenseName, resourceGroupName, subscriptionId` | Retrieves information about the view of a license. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | The operation to get all licenses of a non-Azure machine |
| `list_by_subscription` | `SELECT` | `subscriptionId` | The operation to get all licenses of a non-Azure machine |
| `create_or_update` | `INSERT` | `licenseName, resourceGroupName, subscriptionId` | The operation to create or update a license. |
| `delete` | `DELETE` | `licenseName, resourceGroupName, subscriptionId` | The operation to delete a license. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | The operation to get all licenses of a non-Azure machine |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | The operation to get all licenses of a non-Azure machine |
| `update` | `EXEC` | `licenseName, resourceGroupName, subscriptionId` | The operation to update a license. |
| `validate_license` | `EXEC` | `subscriptionId` | The operation to validate a license. |
