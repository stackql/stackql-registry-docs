---
title: transactions_transaction_summary_by_invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - transactions_transaction_summary_by_invoices
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

Creates, updates, deletes, gets or lists a <code>transactions_transaction_summary_by_invoices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transactions_transaction_summary_by_invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.transactions_transaction_summary_by_invoices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azureCreditApplied" /> | `number` | The total amount of any Azure credits applied. |
| <CopyableCode code="billingCurrency" /> | `string` | The ISO 4217 code for the currency in which the transactions are billed. |
| <CopyableCode code="consumptionCommitmentDecremented" /> | `number` | The total Microsoft Azure Consumption Commitment (MACC) decrement through the invoice. |
| <CopyableCode code="subTotal" /> | `number` | The total pre-tax charged amount. |
| <CopyableCode code="tax" /> | `number` | The total tax amount applied. |
| <CopyableCode code="total" /> | `number` | The total charges. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, invoiceName" /> | Gets the transaction summary for an invoice. Transactions include purchases, refunds and Azure usage charges. |

## `SELECT` examples

Gets the transaction summary for an invoice. Transactions include purchases, refunds and Azure usage charges.


```sql
SELECT
azureCreditApplied,
billingCurrency,
consumptionCommitmentDecremented,
subTotal,
tax,
total
FROM azure.billing.transactions_transaction_summary_by_invoices
WHERE billingAccountName = '{{ billingAccountName }}'
AND invoiceName = '{{ invoiceName }}';
```