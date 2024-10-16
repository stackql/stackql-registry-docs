---
title: management_group_subscriptions_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - management_group_subscriptions_subscriptions
  - management_groups
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

Creates, updates, deletes, gets or lists a <code>management_group_subscriptions_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_group_subscriptions_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.management_groups.management_group_subscriptions_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_group_subscriptions_subscriptions', value: 'view', },
        { label: 'management_group_subscriptions_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The fully qualified ID for the subscription.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000/subscriptions/0000000-0000-0000-0000-000000000001 |
| <CopyableCode code="name" /> | `text` | The stringified id of the subscription. For example, 00000000-0000-0000-0000-000000000000 |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource.  For example, Microsoft.Management/managementGroups/subscriptions |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the subscription.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000/subscriptions/0000000-0000-0000-0000-000000000001 |
| <CopyableCode code="name" /> | `string` | The stringified id of the subscription. For example, 00000000-0000-0000-0000-000000000000 |
| <CopyableCode code="properties" /> | `object` | The generic properties of subscription under a management group. |
| <CopyableCode code="type" /> | `string` | The type of the resource.  For example, Microsoft.Management/managementGroups/subscriptions |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId, subscriptionId" /> | Retrieves details about given subscription which is associated with the management group. |

## `SELECT` examples

Retrieves details about given subscription which is associated with the management group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_group_subscriptions_subscriptions', value: 'view', },
        { label: 'management_group_subscriptions_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
display_name,
groupId,
parent,
state,
subscriptionId,
tenant,
type
FROM azure.management_groups.vw_management_group_subscriptions_subscriptions
WHERE groupId = '{{ groupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.management_groups.management_group_subscriptions_subscriptions
WHERE groupId = '{{ groupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

