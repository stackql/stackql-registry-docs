---
title: virtual_network_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_rules
  - data_lake_store
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
<tr><td><b>Name</b></td><td><code>virtual_network_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_store.virtual_network_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The virtual network rule properties. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualNetworkRules_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId, virtualNetworkRuleName` | Gets the specified Data Lake Store virtual network rule. |
| `VirtualNetworkRules_ListByAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists the Data Lake Store virtual network rules within the specified Data Lake Store account. |
| `VirtualNetworkRules_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId, virtualNetworkRuleName, data__properties` | Creates or updates the specified virtual network rule. During update, the virtual network rule with the specified name will be replaced with this new virtual network rule. |
| `VirtualNetworkRules_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId, virtualNetworkRuleName` | Deletes the specified virtual network rule from the specified Data Lake Store account. |
| `VirtualNetworkRules_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId, virtualNetworkRuleName` | Updates the specified virtual network rule. |
