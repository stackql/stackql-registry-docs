---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - authorization
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

Creates, updates, deletes, gets or lists a <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alerts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts', value: 'view', },
        { label: 'alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The alert ID. |
| <CopyableCode code="name" /> | `text` | The alert name. |
| <CopyableCode code="alertId" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_incidents" /> | `text` | field from the `properties` object |
| <CopyableCode code="incident_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_active" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_scanned_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The alert type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The alert ID. |
| <CopyableCode code="name" /> | `string` | The alert name. |
| <CopyableCode code="properties" /> | `object` | Alert properties. |
| <CopyableCode code="type" /> | `string` | The alert type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | Get the specified alert. |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets alerts for a resource scope. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="alertId, scope" /> | Update an alert. |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="alertId, scope" /> | Refresh an alert. |
| <CopyableCode code="refresh_all" /> | `EXEC` | <CopyableCode code="scope" /> | Refresh all alerts for a resource scope. |

## `SELECT` examples

Gets alerts for a resource scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alerts', value: 'view', },
        { label: 'alerts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
alertId,
alert_configuration,
alert_definition,
alert_incidents,
incident_count,
is_active,
last_modified_date_time,
last_scanned_date_time,
scope,
type
FROM azure.authorization.vw_alerts
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
FROM azure.authorization.alerts
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>alerts</code> resource.

```sql
/*+ update */
UPDATE azure.authorization.alerts
SET 
properties = '{{ properties }}'
WHERE 
alertId = '{{ alertId }}'
AND scope = '{{ scope }}';
```
