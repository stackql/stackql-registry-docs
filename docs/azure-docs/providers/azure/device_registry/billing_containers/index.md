---
title: billing_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_containers
  - device_registry
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

Creates, updates, deletes, gets or lists a <code>billing_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.billing_containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_billing_containers', value: 'view', },
        { label: 'billing_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billingContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource ETag |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource ETag |
| <CopyableCode code="properties" /> | `object` | Defines the billingContainer properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingContainerName, subscriptionId" /> | Get a BillingContainer |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List BillingContainer resources by subscription ID |

## `SELECT` examples

List BillingContainer resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_billing_containers', value: 'view', },
        { label: 'billing_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
billingContainerName,
etag,
provisioning_state,
subscriptionId
FROM azure.device_registry.vw_billing_containers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.device_registry.billing_containers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

