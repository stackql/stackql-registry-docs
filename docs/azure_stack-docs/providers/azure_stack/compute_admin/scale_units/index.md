---
title: scale_units
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_units
  - compute_admin
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

Creates, updates, deletes, gets or lists a <code>scale_units</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scale_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.scale_units" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scale_units', value: 'view', },
        { label: 'scale_units', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="scaleUnitName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_unit_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for a scale unit |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, scaleUnitName, subscriptionId" /> | Get the scale unit view. |

## `SELECT` examples

Get the scale unit view.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scale_units', value: 'view', },
        { label: 'scale_units', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
last_updated_time,
location,
nodes,
scaleUnitName,
scale_unit_name,
subscriptionId,
type
FROM azure_stack.compute_admin.vw_scale_units
WHERE location = '{{ location }}'
AND scaleUnitName = '{{ scaleUnitName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_stack.compute_admin.scale_units
WHERE location = '{{ location }}'
AND scaleUnitName = '{{ scaleUnitName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

