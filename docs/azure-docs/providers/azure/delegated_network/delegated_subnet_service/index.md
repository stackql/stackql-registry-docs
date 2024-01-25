---
title: delegated_subnet_service
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_subnet_service
  - delegated_network
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
<tr><td><b>Name</b></td><td><code>delegated_subnet_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.delegated_network.delegated_subnet_service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of delegated subnet |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the DelegatedSubnets resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get all the DelegatedSubnets resources in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all the DelegatedSubnets resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get all the DelegatedSubnets resources in a subscription. |
| `patch_details` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Patch delegated subnet resource |
| `put_details` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Put delegated subnet resource |
