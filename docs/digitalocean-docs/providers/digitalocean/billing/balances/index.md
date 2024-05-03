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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>balances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.billing.balances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_balance" /> | `string` | Current balance of the customer's most recent billing activity.  Does not reflect `month_to_date_usage`. |
| <CopyableCode code="generated_at" /> | `string` | The time at which balances were most recently generated. |
| <CopyableCode code="month_to_date_balance" /> | `string` | Balance as of the `generated_at` time.  This value includes the `account_balance` and `month_to_date_usage`. |
| <CopyableCode code="month_to_date_usage" /> | `string` | Amount used in the current billing period as of the `generated_at` time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="balance_get" /> | `SELECT` |  |
