---
title: alert_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_configurations
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

Creates, updates, deletes, gets or lists a <code>alert_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alert_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_configurations', value: 'view', },
        { label: 'alert_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The alert configuration ID. |
| <CopyableCode code="name" /> | `text` | The alert configuration name. |
| <CopyableCode code="alertId" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_configuration_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="alert_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The alert configuration type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The alert configuration ID. |
| <CopyableCode code="name" /> | `string` | The alert configuration name. |
| <CopyableCode code="properties" /> | `object` | Alert configuration properties. |
| <CopyableCode code="type" /> | `string` | The alert configuration type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | Get the specified alert configuration. |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets alert configurations for a resource scope. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="alertId, scope" /> | Update an alert configuration. |

## `SELECT` examples

Gets alert configurations for a resource scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_configurations', value: 'view', },
        { label: 'alert_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
alertId,
alert_configuration_type,
alert_definition,
alert_definition_id,
is_enabled,
scope,
type
FROM azure.authorization.vw_alert_configurations
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
FROM azure.authorization.alert_configurations
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>alert_configurations</code> resource.

```sql
/*+ update */
UPDATE azure.authorization.alert_configurations
SET 
properties = '{{ properties }}'
WHERE 
alertId = '{{ alertId }}'
AND scope = '{{ scope }}';
```
