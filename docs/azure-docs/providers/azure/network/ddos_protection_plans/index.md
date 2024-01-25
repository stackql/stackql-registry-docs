---
title: ddos_protection_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - ddos_protection_plans
  - network
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
<tr><td><b>Name</b></td><td><code>ddos_protection_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.ddos_protection_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | DDoS protection plan properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ddosProtectionPlanName, resourceGroupName, subscriptionId` | Gets information about the specified DDoS protection plan. |
| `list` | `SELECT` | `subscriptionId` | Gets all DDoS protection plans in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the DDoS protection plans in a resource group. |
| `create_or_update` | `INSERT` | `ddosProtectionPlanName, resourceGroupName, subscriptionId` | Creates or updates a DDoS protection plan. |
| `delete` | `DELETE` | `ddosProtectionPlanName, resourceGroupName, subscriptionId` | Deletes the specified DDoS protection plan. |
| `_list` | `EXEC` | `subscriptionId` | Gets all DDoS protection plans in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the DDoS protection plans in a resource group. |
