---
title: quota_request_status
hide_title: false
hide_table_of_contents: false
keywords:
  - quota_request_status
  - reservations
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

Creates, updates, deletes, gets or lists a <code>quota_request_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quota_request_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.quota_request_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quota_request_status', value: 'view', },
        { label: 'quota_request_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Quota request ID. |
| <CopyableCode code="name" /> | `text` | Quota request name. |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="message" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_submit_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Quota request ID. |
| <CopyableCode code="name" /> | `string` | Quota request name. |
| <CopyableCode code="properties" /> | `object` | The details of quota request. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, location, providerId, subscriptionId" /> | For the specified Azure region (location), get the details and status of the quota request by the quota request ID for the resources of the resource provider. The PUT request for the quota (service limit) returns a response with the requestId parameter. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, providerId, subscriptionId" /> | For the specified Azure region (location), subscription, and resource provider, get the history of the quota requests for the past year. To select specific quota requests, use the oData filter. |

## `SELECT` examples

For the specified Azure region (location), subscription, and resource provider, get the history of the quota requests for the past year. To select specific quota requests, use the oData filter.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quota_request_status', value: 'view', },
        { label: 'quota_request_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
message,
providerId,
provisioning_state,
request_submit_time,
subscriptionId,
type,
value
FROM azure.reservations.vw_quota_request_status
WHERE location = '{{ location }}'
AND providerId = '{{ providerId }}'
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
FROM azure.reservations.quota_request_status
WHERE location = '{{ location }}'
AND providerId = '{{ providerId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

