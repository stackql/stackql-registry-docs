---
title: management_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - management_policies
  - storage
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
<tr><td><b>Name</b></td><td><code>management_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.management_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The Storage Account ManagementPolicy properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagementPolicies_Get` | `SELECT` | `accountName, managementPolicyName, resourceGroupName, subscriptionId` | Gets the managementpolicy associated with the specified storage account. |
| `ManagementPolicies_CreateOrUpdate` | `INSERT` | `accountName, managementPolicyName, resourceGroupName, subscriptionId` | Sets the managementpolicy to the specified storage account. |
| `ManagementPolicies_Delete` | `DELETE` | `accountName, managementPolicyName, resourceGroupName, subscriptionId` | Deletes the managementpolicy associated with the specified storage account. |
