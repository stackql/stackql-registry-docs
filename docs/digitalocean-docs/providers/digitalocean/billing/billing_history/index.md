---
title: billing_history
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_history
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

Creates, updates, deletes, gets or lists a <code>billing_history</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.billing.billing_history" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Description of the billing history entry. |
| <CopyableCode code="amount" /> | `string` | Amount of the billing history entry. |
| <CopyableCode code="date" /> | `string` | Time the billing history entry occurred. |
| <CopyableCode code="invoice_id" /> | `string` | ID of the invoice associated with the billing history entry, if applicable. |
| <CopyableCode code="invoice_uuid" /> | `string` | UUID of the invoice associated with the billing history entry, if applicable. |
| <CopyableCode code="type" /> | `string` | Type of billing history entry. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_history_list" /> | `SELECT` | <CopyableCode code="" /> | To retrieve a list of all billing history entries, send a GET request to `/v2/customers/my/billing_history`. |

## `SELECT` examples

To retrieve a list of all billing history entries, send a GET request to `/v2/customers/my/billing_history`.


```sql
SELECT
description,
amount,
date,
invoice_id,
invoice_uuid,
type
FROM digitalocean.billing.billing_history
;
```