---
title: balances
hide_title: false
hide_table_of_contents: false
keywords:
  - balances
  - billing
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>balances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>balances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.billing.balances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_balance" /> | `string` | Current balance of the customer's most recent billing activity. Does not reflect `month_to_date_usage`. |
| <CopyableCode code="generated_at" /> | `string` | The time at which balances were most recently generated. |
| <CopyableCode code="month_to_date_balance" /> | `string` | Balance as of the `generated_at` time. This value includes the `account_balance` and `month_to_date_usage`. |
| <CopyableCode code="month_to_date_usage" /> | `string` | Amount used in the current billing period as of the `generated_at` time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="balance_get" /> | `SELECT` | <CopyableCode code="" /> | To retrieve the balances on a customer's account, send a GET request to `/v2/customers/my/balance`. |

## `SELECT` examples

To retrieve the balances on a customer's account, send a GET request to `/v2/customers/my/balance`.


```sql
SELECT
account_balance,
generated_at,
month_to_date_balance,
month_to_date_usage
FROM digitalocean.billing.balances
;
```