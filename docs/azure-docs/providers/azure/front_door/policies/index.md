---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - front_door
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.front_door.policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | Gets a unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Defines web application firewall policy properties. |
| `sku` | `object` | The pricing tier of the web application firewall policy. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyName, resourceGroupName, subscriptionId` | Retrieve protection policy with specified name within a resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the protection policies within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all of the protection policies within a subscription. |
| `create_or_update` | `INSERT` | `policyName, resourceGroupName, subscriptionId` | Create or update policy with specified rule set name within a resource group. |
| `delete` | `DELETE` | `policyName, resourceGroupName, subscriptionId` | Deletes Policy |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all of the protection policies within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all of the protection policies within a subscription. |
| `update` | `EXEC` | `policyName, resourceGroupName, subscriptionId` | Patch a specific frontdoor webApplicationFirewall policy for tags update under the specified subscription and resource group. |
