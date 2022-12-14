---
title: aggregated_cost
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregated_cost
  - consumption
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
<tr><td><b>Name</b></td><td><code>aggregated_cost</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.aggregated_cost</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AggregatedCost_GetByManagementGroup` | `EXEC` | `managementGroupId` | Provides the aggregate cost of a management group and all child management groups by current billing period. |
| `AggregatedCost_GetForBillingPeriodByManagementGroup` | `EXEC` | `billingPeriodName, managementGroupId` | Provides the aggregate cost of a management group and all child management groups by specified billing period |
