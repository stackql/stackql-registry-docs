---
title: policy_policy_for_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_policy_for_tenants
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

Creates, updates, deletes, gets or lists a <code>policy_policy_for_tenants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_policy_for_tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.policy_policy_for_tenants" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policy_policy_for_tenants', value: 'view', },
        { label: 'policy_policy_for_tenants', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Policy Id. |
| <CopyableCode code="name" /> | `text` | Policy name. |
| <CopyableCode code="block_subscriptions_into_tenant" /> | `text` | field from the `properties` object |
| <CopyableCode code="block_subscriptions_leaving_tenant" /> | `text` | field from the `properties` object |
| <CopyableCode code="exempted_principals" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Policy Id. |
| <CopyableCode code="name" /> | `string` | Policy name. |
| <CopyableCode code="properties" /> | `object` | Tenant policy. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Get the subscription tenant policy for the user's tenant. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get the subscription tenant policy for the user's tenant. |

## `SELECT` examples

Get the subscription tenant policy for the user's tenant.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policy_policy_for_tenants', value: 'view', },
        { label: 'policy_policy_for_tenants', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
block_subscriptions_into_tenant,
block_subscriptions_leaving_tenant,
exempted_principals,
policy_id,
system_data,
type
FROM azure.subscription.vw_policy_policy_for_tenants
;
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
FROM azure.subscription.policy_policy_for_tenants
;
```
</TabItem></Tabs>

