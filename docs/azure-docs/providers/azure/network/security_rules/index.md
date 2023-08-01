---
title: security_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_rules
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
<tr><td><b>Name</b></td><td><code>security_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.security_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `type` | `string` | The type of the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Security rule resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityRules_Get` | `SELECT` | `networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId` | Get the specified network security rule. |
| `SecurityRules_List` | `SELECT` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Gets all security rules in a network security group. |
| `SecurityRules_CreateOrUpdate` | `INSERT` | `networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId` | Creates or updates a security rule in the specified network security group. |
| `SecurityRules_Delete` | `DELETE` | `networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId` | Deletes the specified network security rule. |
