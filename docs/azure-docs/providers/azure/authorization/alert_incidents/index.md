---
title: alert_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_incidents
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

Creates, updates, deletes, gets or lists a <code>alert_incidents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alert_incidents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_incidents', value: 'view', },
        { label: 'alert_incidents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The alert incident ID. |
| <CopyableCode code="name" /> | `text` | The alert incident name. |
| <CopyableCode code="alertId" /> | `text` | field from the `properties` object |
| <CopyableCode code="alertIncidentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_incident_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The alert incident type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The alert incident ID. |
| <CopyableCode code="name" /> | `string` | The alert incident name. |
| <CopyableCode code="properties" /> | `object` | Alert incident properties |
| <CopyableCode code="type" /> | `string` | The alert incident type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertId, alertIncidentId, scope" /> | Get the specified alert incident. |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | Gets alert incidents for a resource scope. |
| <CopyableCode code="remediate" /> | `EXEC` | <CopyableCode code="alertId, alertIncidentId, scope" /> | Remediate an alert incident. |

## `SELECT` examples

Gets alert incidents for a resource scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_incidents', value: 'view', },
        { label: 'alert_incidents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
alertId,
alertIncidentId,
alert_incident_type,
scope,
type
FROM azure.authorization.vw_alert_incidents
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
FROM azure.authorization.alert_incidents
WHERE alertId = '{{ alertId }}'
AND scope = '{{ scope }}';
```
</TabItem></Tabs>

