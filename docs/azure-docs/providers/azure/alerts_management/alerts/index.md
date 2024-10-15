---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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

Creates, updates, deletes, gets or lists a <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alerts" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="alertId" /> | `text` | field from the `properties` object |
| <CopyableCode code="context" /> | `text` | field from the `properties` object |
| <CopyableCode code="egress_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="essentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Alert property bag |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all" /> | `SELECT` | <CopyableCode code="scope" /> | List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime.  |
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | Get information related to a specific alert |
| <CopyableCode code="change_state" /> | `EXEC` | <CopyableCode code="alertId, newState, scope" /> | Change the state of an alert. |
| <CopyableCode code="meta_data" /> | `EXEC` | <CopyableCode code="identifier" /> | List alerts meta data information based on value of identifier parameter. |

## `SELECT` examples

List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime. 

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
context,
egress_config,
essentials,
scope,
type
FROM azure.alerts_management.vw_alerts
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
FROM azure.alerts_management.alerts
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

