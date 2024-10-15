---
title: transactions_by_invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - transactions_by_invoices
  - billing
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>transactions_by_invoices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transactions_by_invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.transactions_by_invoices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A transaction. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName, invoiceName" /> | Lists the transactions for an invoice. Transactions include purchases, refunds and Azure usage charges. |

## `SELECT` examples

Lists the transactions for an invoice. Transactions include purchases, refunds and Azure usage charges.


```sql
SELECT
properties,
tags
FROM azure.billing.transactions_by_invoices
WHERE billingAccountName = '{{ billingAccountName }}'
AND invoiceName = '{{ invoiceName }}';
```