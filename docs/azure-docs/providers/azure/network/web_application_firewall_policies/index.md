---
title: web_application_firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - web_application_firewall_policies
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
<tr><td><b>Name</b></td><td><code>web_application_firewall_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.web_application_firewall_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Defines web application firewall policy properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebApplicationFirewallPolicies_Get` | `SELECT` | `policyName, resourceGroupName, subscriptionId` | Retrieve protection policy with specified name within a resource group. |
| `WebApplicationFirewallPolicies_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the protection policies within a resource group. |
| `WebApplicationFirewallPolicies_ListAll` | `SELECT` | `subscriptionId` | Gets all the WAF policies in a subscription. |
| `WebApplicationFirewallPolicies_CreateOrUpdate` | `INSERT` | `policyName, resourceGroupName, subscriptionId` | Creates or update policy with specified rule set name within a resource group. |
| `WebApplicationFirewallPolicies_Delete` | `DELETE` | `policyName, resourceGroupName, subscriptionId` | Deletes Policy. |
