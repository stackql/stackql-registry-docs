---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="customerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="view_charges" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A policy at customer scope. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Get the policies for a billing account of Enterprise Agreement type. |
| <CopyableCode code="get_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="get_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, customerName, policyName" /> | Lists the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="get_by_customer_at_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, customerName" /> | Lists the policies for a customer at billing account scope. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |
| <CopyableCode code="get_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the policies that are managed by the Billing Admin for the defined subscriptions. This is supported for Microsoft Online Services Program, Microsoft Customer Agreement and Microsoft Partner Agreement. |

## `SELECT` examples

Lists the policies that are managed by the Billing Admin for the defined subscriptions. This is supported for Microsoft Online Services Program, Microsoft Customer Agreement and Microsoft Partner Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
billingAccountName,
billingProfileName,
customerName,
policies,
policyName,
provisioning_state,
subscriptionId,
tags,
view_charges
FROM azure.billing.vw_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

