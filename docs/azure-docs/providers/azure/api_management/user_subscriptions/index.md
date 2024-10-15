---
title: user_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_subscriptions
  - api_management
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

Creates, updates, deletes, gets or lists a <code>user_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.user_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_user_subscriptions', value: 'view', },
        { label: 'user_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allow_tracing" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="notification_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="owner_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sid" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="state_comment" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="userId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Subscription details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, userId" /> | Gets the specified Subscription entity associated with a particular user. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, userId" /> | Lists the collection of subscriptions of the specified user. |

## `SELECT` examples

Lists the collection of subscriptions of the specified user.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_user_subscriptions', value: 'view', },
        { label: 'user_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allow_tracing,
created_date,
display_name,
end_date,
expiration_date,
notification_date,
owner_id,
primary_key,
resourceGroupName,
scope,
secondary_key,
serviceName,
sid,
start_date,
state,
state_comment,
subscriptionId,
userId
FROM azure.api_management.vw_user_subscriptions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userId = '{{ userId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.user_subscriptions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userId = '{{ userId }}';
```
</TabItem></Tabs>

