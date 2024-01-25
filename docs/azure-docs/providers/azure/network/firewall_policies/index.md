---
title: firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policies
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
<tr><td><b>Name</b></td><td><code>firewall_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.firewall_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Firewall Policy definition. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `firewallPolicyName, resourceGroupName, subscriptionId` | Gets the specified Firewall Policy. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Firewall Policies in a resource group. |
| `create_or_update` | `INSERT` | `firewallPolicyName, resourceGroupName, subscriptionId` | Creates or updates the specified Firewall Policy. |
| `delete` | `DELETE` | `firewallPolicyName, resourceGroupName, subscriptionId` | Deletes the specified Firewall Policy. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Firewall Policies in a resource group. |
