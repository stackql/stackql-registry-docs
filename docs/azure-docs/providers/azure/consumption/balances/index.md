---
title: balances
hide_title: false
hide_table_of_contents: false
keywords:
  - balances
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
<tr><td><b>Name</b></td><td><code>balances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.consumption.balances</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Balances_GetByBillingAccount` | `EXEC` | `billingAccountId` | Gets the balances for a scope by billingAccountId. Balances are available via this API only for May 1, 2014 or later. |
| `Balances_GetForBillingPeriodByBillingAccount` | `EXEC` | `billingAccountId, billingPeriodName` | Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later. |
