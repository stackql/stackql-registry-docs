---
title: available_balances
hide_title: false
hide_table_of_contents: false
keywords:
  - available_balances
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

Creates, updates, deletes, gets or lists a <code>available_balances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_balances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.available_balances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_available_balances', value: 'view', },
        { label: 'available_balances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="amount" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="payments_on_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="total_payments_on_account" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Available Credit or Payment on Account Balance. The credit balance can be used to settle due or past due invoices. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | The Available Credit or Payment on Account Balance for a billing account. The credit balance can be used to settle due or past due invoices and is supported for billing accounts with agreement type Microsoft Customer Agreement. The payment on account balance is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Online Services Program. |
| <CopyableCode code="get_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | The Available Credit or Payment on Account Balance for a billing profile. The credit balance can be used to settle due or past due invoices and is supported for billing accounts with agreement type Microsoft Customer Agreement. The payment on account balance is supported for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

The Available Credit or Payment on Account Balance for a billing account. The credit balance can be used to settle due or past due invoices and is supported for billing accounts with agreement type Microsoft Customer Agreement. The payment on account balance is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Online Services Program.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_available_balances', value: 'view', },
        { label: 'available_balances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
amount,
billingAccountName,
billingProfileName,
payments_on_account,
tags,
total_payments_on_account
FROM azure.billing.vw_available_balances
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.available_balances
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

