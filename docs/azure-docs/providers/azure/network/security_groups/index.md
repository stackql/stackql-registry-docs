---
title: security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - security_groups
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
<tr><td><b>Name</b></td><td><code>security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.security_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Network Security Group resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Gets the specified network security group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all network security groups in a resource group. |
| `create_or_update` | `INSERT` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Creates or updates a network security group in the specified resource group. |
| `delete` | `DELETE` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Deletes the specified network security group. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all network security groups in a resource group. |
