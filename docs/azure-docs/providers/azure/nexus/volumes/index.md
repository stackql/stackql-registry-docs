---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - nexus
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.volumes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, volumeName` | Get properties of the provided volume. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of volumes in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of volumes in the provided subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, volumeName, data__extendedLocation, data__properties` | Create a new volume or update the properties of the existing one. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, volumeName` | Delete the provided volume. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of volumes in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of volumes in the provided subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, volumeName` | Update tags associated with the provided volume. |
