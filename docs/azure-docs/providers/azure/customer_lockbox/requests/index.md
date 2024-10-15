---
title: requests
hide_title: false
hide_table_of_contents: false
keywords:
  - requests
  - customer_lockbox
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

Creates, updates, deletes, gets or lists a <code>requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.customer_lockbox.requests" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_requests', value: 'view', },
        { label: 'requests', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The Arm resource id of the Lockbox request. |
| <CopyableCode code="name" /> | `text` | The name of the Lockbox request. |
| <CopyableCode code="access_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="justification" /> | `text` | field from the `properties` object |
| <CopyableCode code="requestId" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_case_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="support_request" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the Lockbox request. |
| <CopyableCode code="workitemsource" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Arm resource id of the Lockbox request. |
| <CopyableCode code="name" /> | `string` | The name of the Lockbox request. |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with a lockbox request. |
| <CopyableCode code="type" /> | `string` | The type of the Lockbox request. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="requestId, subscriptionId" /> | Get Customer Lockbox request |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the Lockbox requests in the given subscription. |

## `SELECT` examples

Lists all of the Lockbox requests in the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_requests', value: 'view', },
        { label: 'requests', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access_level,
created_date_time,
duration,
expiration_date_time,
justification,
requestId,
request_id,
resource_ids,
resource_type,
status,
subscriptionId,
subscription_id,
support_case_url,
support_request,
type,
workitemsource
FROM azure.customer_lockbox.vw_requests
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.customer_lockbox.requests
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

