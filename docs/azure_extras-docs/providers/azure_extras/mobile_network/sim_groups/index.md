---
title: sim_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sim_groups
  - mobile_network
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.sim_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | SIM group properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SimGroups_Get` | `SELECT` | `resourceGroupName, simGroupName, subscriptionId` | Gets information about the specified SIM group. |
| `SimGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the SIM groups in a resource group. |
| `SimGroups_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all the SIM groups in a subscription. |
| `SimGroups_CreateOrUpdate` | `INSERT` | `resourceGroupName, simGroupName, subscriptionId, data__properties` | Creates or updates a SIM group. |
| `SimGroups_Delete` | `DELETE` | `resourceGroupName, simGroupName, subscriptionId` | Deletes the specified SIM group. |
| `SimGroups_UpdateTags` | `EXEC` | `resourceGroupName, simGroupName, subscriptionId` | Updates SIM group tags. |
