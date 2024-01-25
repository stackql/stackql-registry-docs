---
title: sim_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sim_groups
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>sim_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.sim_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | SIM group properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, simGroupName, subscriptionId` | Gets information about the specified SIM group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the SIM groups in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all the SIM groups in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, simGroupName, subscriptionId, data__properties` | Creates or updates a SIM group. |
| `delete` | `DELETE` | `resourceGroupName, simGroupName, subscriptionId` | Deletes the specified SIM group. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the SIM groups in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all the SIM groups in a subscription. |
