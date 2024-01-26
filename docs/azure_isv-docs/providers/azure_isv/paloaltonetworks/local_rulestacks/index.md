---
title: local_rulestacks
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rulestacks
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>local_rulestacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.local_rulestacks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The properties of the managed service identities assigned to this resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | PAN Rulestack Describe Object |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `localRulestackName, resourceGroupName, subscriptionId` | Get a LocalRulestackResource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List LocalRulestackResource resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List LocalRulestackResource resources by subscription ID |
| `create_or_update` | `INSERT` | `localRulestackName, resourceGroupName, subscriptionId, data__properties` | Create a LocalRulestackResource |
| `delete` | `DELETE` | `localRulestackName, resourceGroupName, subscriptionId` | Delete a LocalRulestackResource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List LocalRulestackResource resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List LocalRulestackResource resources by subscription ID |
| `commit` | `EXEC` | `localRulestackName, resourceGroupName, subscriptionId` | Commit rulestack configuration |
| `revert` | `EXEC` | `localRulestackName, resourceGroupName, subscriptionId` | Revert rulestack configuration |
| `update` | `EXEC` | `localRulestackName, resourceGroupName, subscriptionId` | Update a LocalRulestackResource |
