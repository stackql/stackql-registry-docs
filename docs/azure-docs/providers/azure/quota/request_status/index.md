---
title: request_status
hide_title: false
hide_table_of_contents: false
keywords:
  - request_status
  - quota
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

Creates, updates, deletes, gets or lists a <code>request_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>request_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.request_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_request_status', value: 'view', },
        { label: 'request_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Quota request ID. |
| <CopyableCode code="name" /> | `text` | Quota request name. |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="message" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_submit_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. "Microsoft.Quota/quotas". |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Quota request ID. |
| <CopyableCode code="name" /> | `string` | Quota request name. |
| <CopyableCode code="properties" /> | `object` | Quota request properties. |
| <CopyableCode code="type" /> | `string` | Resource type. "Microsoft.Quota/quotas". |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, scope" /> | Get the quota request details and status by quota request ID for the resources of the resource provider at a specific location. The quota request ID **id** is returned in the response of the PUT operation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | For the specified scope, get the current quota requests for a one year period ending at the time is made. Use the **oData** filter to select quota requests. |

## `SELECT` examples

For the specified scope, get the current quota requests for a one year period ending at the time is made. Use the **oData** filter to select quota requests.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_request_status', value: 'view', },
        { label: 'request_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
error,
message,
provisioning_state,
request_submit_time,
scope,
type,
value
FROM azure.quota.vw_request_status
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.quota.request_status
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

