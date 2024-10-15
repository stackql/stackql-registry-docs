---
title: db_system_shapes
hide_title: false
hide_table_of_contents: false
keywords:
  - db_system_shapes
  - oracle
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

Creates, updates, deletes, gets or lists a <code>db_system_shapes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_system_shapes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.db_system_shapes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_db_system_shapes', value: 'view', },
        { label: 'db_system_shapes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="available_core_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_core_count_per_node" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_data_storage_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_data_storage_per_server_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_db_node_per_node_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_db_node_storage_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_memory_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_memory_per_node_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="core_count_increment" /> | `text` | field from the `properties` object |
| <CopyableCode code="dbsystemshapename" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_storage_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="maximum_node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_core_count_per_node" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_data_storage_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_db_node_storage_per_node_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_memory_per_node_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_storage_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimum_core_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimum_node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="runtime_minimum_core_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="shape_family" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | DbSystemShape resource model |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dbsystemshapename, location, subscriptionId" /> | Get a DbSystemShape |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List DbSystemShape resources by Location |

## `SELECT` examples

List DbSystemShape resources by Location

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_db_system_shapes', value: 'view', },
        { label: 'db_system_shapes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
available_core_count,
available_core_count_per_node,
available_data_storage_in_tbs,
available_data_storage_per_server_in_tbs,
available_db_node_per_node_in_gbs,
available_db_node_storage_in_gbs,
available_memory_in_gbs,
available_memory_per_node_in_gbs,
core_count_increment,
dbsystemshapename,
location,
max_storage_count,
maximum_node_count,
min_core_count_per_node,
min_data_storage_in_tbs,
min_db_node_storage_per_node_in_gbs,
min_memory_per_node_in_gbs,
min_storage_count,
minimum_core_count,
minimum_node_count,
runtime_minimum_core_count,
shape_family,
subscriptionId
FROM azure_isv.oracle.vw_db_system_shapes
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.db_system_shapes
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

