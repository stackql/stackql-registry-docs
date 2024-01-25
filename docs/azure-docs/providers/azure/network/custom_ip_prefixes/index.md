---
title: custom_ip_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_ip_prefixes
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
<tr><td><b>Name</b></td><td><code>custom_ip_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.custom_ip_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Custom IP prefix properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `zones` | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customIpPrefixName, resourceGroupName, subscriptionId` | Gets the specified custom IP prefix in a specified resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all custom IP prefixes in a resource group. |
| `create_or_update` | `INSERT` | `customIpPrefixName, resourceGroupName, subscriptionId` | Creates or updates a custom IP prefix. |
| `delete` | `DELETE` | `customIpPrefixName, resourceGroupName, subscriptionId` | Deletes the specified custom IP prefix. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all custom IP prefixes in a resource group. |
