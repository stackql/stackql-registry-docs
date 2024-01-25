---
title: cost_allocation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - cost_allocation_rules
  - cost_management
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
<tr><td><b>Name</b></td><td><code>cost_allocation_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.cost_allocation_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure Resource Manager Id for the rule. This is a read ony value. |
| `name` | `string` | Name of the rule. This is a read only value. |
| `properties` | `object` | The properties of a cost allocation rule |
| `type` | `string` | Resource type of the rule. This is a read only value of Microsoft.CostManagement/CostAllocationRule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `billingAccountId, ruleName` | Get a cost allocation rule by rule name and billing account or enterprise enrollment. |
| `list` | `SELECT` | `billingAccountId` | Get the list of all cost allocation rules for a billing account or enterprise enrollment. |
| `create_or_update` | `INSERT` | `billingAccountId, ruleName` | Create/Update a rule to allocate cost between different resources within a billing account or enterprise enrollment. |
| `delete` | `DELETE` | `billingAccountId, ruleName` | Delete cost allocation rule for billing account or enterprise enrollment. |
| `_list` | `EXEC` | `billingAccountId` | Get the list of all cost allocation rules for a billing account or enterprise enrollment. |
| `check_name_availability` | `EXEC` | `billingAccountId` | Checks availability and correctness of a name for a cost allocation rule |
