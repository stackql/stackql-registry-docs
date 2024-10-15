---
title: geographic_hierarchies_defaults
hide_title: false
hide_table_of_contents: false
keywords:
  - geographic_hierarchies_defaults
  - traffic_manager
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

Creates, updates, deletes, gets or lists a <code>geographic_hierarchies_defaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geographic_hierarchies_defaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.geographic_hierarchies_defaults" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_geographic_hierarchies_defaults', value: 'view', },
        { label: 'geographic_hierarchies_defaults', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="geographic_hierarchy" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class representing the properties of the Geographic hierarchy used with the Geographic traffic routing method. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Gets the default Geographic Hierarchy used by the Geographic traffic routing method. |

## `SELECT` examples

Gets the default Geographic Hierarchy used by the Geographic traffic routing method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_geographic_hierarchies_defaults', value: 'view', },
        { label: 'geographic_hierarchies_defaults', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
geographic_hierarchy
FROM azure.traffic_manager.vw_geographic_hierarchies_defaults
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.traffic_manager.geographic_hierarchies_defaults
;
```
</TabItem></Tabs>

