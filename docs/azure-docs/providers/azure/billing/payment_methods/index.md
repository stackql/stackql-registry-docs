---
title: payment_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - payment_methods
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

Creates, updates, deletes, gets or lists a <code>payment_methods</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>payment_methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.payment_methods" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_payment_methods', value: 'view', },
        { label: 'payment_methods', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_holder_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration" /> | `text` | field from the `properties` object |
| <CopyableCode code="family" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_four_digits" /> | `text` | field from the `properties` object |
| <CopyableCode code="logos" /> | `text` | field from the `properties` object |
| <CopyableCode code="paymentMethodName" /> | `text` | field from the `properties` object |
| <CopyableCode code="payment_method" /> | `text` | field from the `properties` object |
| <CopyableCode code="payment_method_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="payment_method_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a payment method link. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, paymentMethodName" /> | Gets a payment method available for a billing account. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="get_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, paymentMethodName" /> | Gets a payment method linked with a billing profile. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="get_by_user" /> | `SELECT` | <CopyableCode code="paymentMethodName" /> | Gets a payment method owned by the caller. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the payment methods available for a billing account. Along with the payment methods owned by the caller, these payment methods can be attached to a billing profile to make payments. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists payment methods attached to a billing profile. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="list_by_user" /> | `SELECT` | <CopyableCode code="" /> | Lists the payment methods owned by the caller. |
| <CopyableCode code="delete_by_user" /> | `DELETE` | <CopyableCode code="paymentMethodName" /> | Deletes a payment method owned by the caller. |

## `SELECT` examples

Lists the payment methods owned by the caller.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_payment_methods', value: 'view', },
        { label: 'payment_methods', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_holder_name,
billingAccountName,
billingProfileName,
display_name,
expiration,
family,
last_four_digits,
logos,
paymentMethodName,
payment_method,
payment_method_id,
payment_method_type,
status,
tags
FROM azure.billing.vw_payment_methods
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.payment_methods
;
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>payment_methods</code> resource.

```sql
/*+ delete */
DELETE FROM azure.billing.payment_methods
WHERE paymentMethodName = '{{ paymentMethodName }}';
```
