---
title: trusted_access_role_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - trusted_access_role_bindings
  - aks
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
<tr><td><b>Name</b></td><td><code>trusted_access_role_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aks.trusted_access_role_bindings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties for trusted access role binding |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId, trustedAccessRoleBindingName` |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId, trustedAccessRoleBindingName, data__properties` |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId, trustedAccessRoleBindingName` |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |
