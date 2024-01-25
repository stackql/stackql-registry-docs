---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
  - data_replication
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
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_replication.policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id of the resource. |
| `name` | `string` | Gets or sets the name of the resource. |
| `properties` | `object` | Policy model properties. |
| `systemData` | `object` | System data required to be defined for Azure resources. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyName, resourceGroupName, subscriptionId, vaultName` | Gets the details of the policy. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Gets the list of policies in the given vault. |
| `create` | `INSERT` | `policyName, resourceGroupName, subscriptionId, vaultName, data__properties` | Creates the policy. |
| `delete` | `DELETE` | `policyName, resourceGroupName, subscriptionId, vaultName` | Removes the policy. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Gets the list of policies in the given vault. |
