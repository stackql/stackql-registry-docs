---
title: vip_swap
hide_title: false
hide_table_of_contents: false
keywords:
  - vip_swap
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
<tr><td><b>Name</b></td><td><code>vip_swap</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vip_swap</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Swap resource properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VipSwap_Get` | `SELECT` | `groupName, resourceName, singletonResource, subscriptionId` | Gets the SwapResource which identifies the slot type for the specified cloud service. The slot type on a cloud service can either be Staging or Production |
| `VipSwap_List` | `SELECT` | `groupName, resourceName, subscriptionId` | Gets the list of SwapResource which identifies the slot type for the specified cloud service. The slot type on a cloud service can either be Staging or Production |
| `VipSwap_Create` | `INSERT` | `groupName, resourceName, singletonResource, subscriptionId` | Performs vip swap operation on swappable cloud services. |
