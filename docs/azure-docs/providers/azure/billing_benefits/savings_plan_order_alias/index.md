---
title: savings_plan_order_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - savings_plan_order_alias
  - billing_benefits
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
<tr><td><b>Name</b></td><td><code>savings_plan_order_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.billing_benefits.savings_plan_order_alias</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `kind` | `string` | Resource provider kind |
| `properties` | `object` | Savings plan properties |
| `sku` | `object` | The SKU to be applied for this resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `savingsPlanOrderAliasName` | Get a savings plan. |
| `create` | `INSERT` | `savingsPlanOrderAliasName, data__sku` | Create a savings plan. Learn more about permissions needed at https://go.microsoft.com/fwlink/?linkid=2215851 |
