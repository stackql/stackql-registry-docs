---
title: billing_account_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_account_policies
  - subscription
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

Creates, updates, deletes, gets or lists a <code>billing_account_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_account_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.billing_account_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_billing_account_policies', value: 'view', },
        { label: 'billing_account_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified ID for the policy. |
| <CopyableCode code="name" /> | `text` | Policy name. |
| <CopyableCode code="allow_transfers" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountId" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_tenants" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID for the policy. |
| <CopyableCode code="name" /> | `string` | Policy name. |
| <CopyableCode code="properties" /> | `object` | Put billing account policies response properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountId" /> | Get Billing Account Policy. |

## `SELECT` examples

Get Billing Account Policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_billing_account_policies', value: 'view', },
        { label: 'billing_account_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allow_transfers,
billingAccountId,
service_tenants,
system_data,
type
FROM azure.subscription.vw_billing_account_policies
WHERE billingAccountId = '{{ billingAccountId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.subscription.billing_account_policies
WHERE billingAccountId = '{{ billingAccountId }}';
```
</TabItem></Tabs>

