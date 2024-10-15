---
title: alerts_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_histories
  - alerts_management
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

Creates, updates, deletes, gets or lists a <code>alerts_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alerts_histories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts_histories', value: 'view', },
        { label: 'alerts_histories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="alertId" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="modifications" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Properties of the alert modification item. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | Get the history of an alert, which captures any monitor condition changes (Fired/Resolved) and alert state changes (New/Acknowledged/Closed). |

## `SELECT` examples

Get the history of an alert, which captures any monitor condition changes (Fired/Resolved) and alert state changes (New/Acknowledged/Closed).

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts_histories', value: 'view', },
        { label: 'alerts_histories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
alertId,
alert_id,
modifications,
scope,
type
FROM azure.alerts_management.vw_alerts_histories
WHERE alertId = '{{ alertId }}'
AND scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.alerts_management.alerts_histories
WHERE alertId = '{{ alertId }}'
AND scope = '{{ scope }}';
```
</TabItem></Tabs>

