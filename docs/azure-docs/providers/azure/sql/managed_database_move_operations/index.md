---
title: managed_database_move_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_move_operations
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_database_move_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_database_move_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_move_operations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_database_move_operations', value: 'view', },
        { label: 'managed_database_move_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="error_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_severity" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_cancellable" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_user_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_managed_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_managed_instance_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_managed_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_managed_instance_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Contains the operation result properties for managed database move operation. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, operationId, resourceGroupName, subscriptionId" /> | Gets a managed database move operation. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists managed database move operations. |

## `SELECT` examples

Lists managed database move operations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_database_move_operations', value: 'view', },
        { label: 'managed_database_move_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
error_code,
error_description,
error_severity,
is_cancellable,
is_user_error,
locationName,
operation,
operationId,
operation_friendly_name,
operation_mode,
resourceGroupName,
source_database_name,
source_managed_instance_id,
source_managed_instance_name,
start_time,
state,
subscriptionId,
target_database_name,
target_managed_instance_id,
target_managed_instance_name
FROM azure.sql.vw_managed_database_move_operations
WHERE locationName = '{{ locationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_database_move_operations
WHERE locationName = '{{ locationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

