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
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Firewall Policy definition. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FirewallPolicies_Get` | `SELECT` | `firewallPolicyName, resourceGroupName, subscriptionId` | Gets the specified Firewall Policy. |
| `FirewallPolicies_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Firewall Policies in a resource group. |
| `FirewallPolicies_ListAll` | `SELECT` | `subscriptionId` | Gets all the Firewall Policies in a subscription. |
| `FirewallPolicies_CreateOrUpdate` | `INSERT` | `firewallPolicyName, resourceGroupName, subscriptionId` | Creates or updates the specified Firewall Policy. |
| `FirewallPolicies_Delete` | `DELETE` | `firewallPolicyName, resourceGroupName, subscriptionId` | Deletes the specified Firewall Policy. |
| `FirewallPolicies_UpdateTags` | `EXEC` | `firewallPolicyName, resourceGroupName, subscriptionId` | Updates tags of a Azure Firewall Policy resource. |
