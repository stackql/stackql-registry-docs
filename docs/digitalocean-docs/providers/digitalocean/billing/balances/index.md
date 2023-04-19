---
title: balances
hide_title: false
hide_table_of_contents: false
keywords:
  - balances
  - billing
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>balances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.billing.balances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `account_balance` | `string` | Current balance of the customer's most recent billing activity.  Does not reflect `month_to_date_usage`. |
| `generated_at` | `string` | The time at which balances were most recently generated. |
| `month_to_date_balance` | `string` | Balance as of the `generated_at` time.  This value includes the `account_balance` and `month_to_date_usage`. |
| `month_to_date_usage` | `string` | Amount used in the current billing period as of the `generated_at` time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `balance_get` | `SELECT` |  |
