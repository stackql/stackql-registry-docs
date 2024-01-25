---
title: hybrid_use_benefit
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_use_benefit
  - software_plan
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
<tr><td><b>Name</b></td><td><code>hybrid_use_benefit</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.software_plan.hybrid_use_benefit</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `etag` | `integer` | Indicates the revision of the hybrid use benefit |
| `properties` | `object` | Hybrid use benefit properties |
| `sku` | `object` | The SKU to be applied for this resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `planId, scope` | Gets a given plan ID |
| `list` | `SELECT` | `scope` | Get all hybrid use benefits associated with an ARM resource. |
| `create` | `INSERT` | `planId, scope, data__sku` | Create a new hybrid use benefit under a given scope |
| `delete` | `DELETE` | `planId, scope` | Deletes a given plan ID |
| `_list` | `EXEC` | `scope` | Get all hybrid use benefits associated with an ARM resource. |
| `update` | `EXEC` | `planId, scope, data__sku` | Updates an existing hybrid use benefit |
