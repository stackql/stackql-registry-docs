---
title: managed_database_restore_details
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_restore_details
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

Creates, updates, deletes, gets or lists a <code>managed_database_restore_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_database_restore_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_restore_details" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_database_restore_details', value: 'view', },
        { label: 'managed_database_restore_details', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="block_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_backup_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_restore_plan_size_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_restored_size_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_restoring_file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="diff_backup_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="full_backup_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_restored_file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_restored_file_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_uploaded_file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_uploaded_file_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_backup_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_files_detected" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_files_queued" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_files_restored" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_files_restoring" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_files_skipped" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_files_unrestorable" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_completed" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restoreDetailsName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="unrestorable_files" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The managed database's restore details properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, restoreDetailsName, subscriptionId" /> | Gets managed database restore details. |

## `SELECT` examples

Gets managed database restore details.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_database_restore_details', value: 'view', },
        { label: 'managed_database_restore_details', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
block_reason,
current_backup_type,
current_restore_plan_size_mb,
current_restored_size_mb,
current_restoring_file_name,
databaseName,
diff_backup_sets,
full_backup_sets,
last_restored_file_name,
last_restored_file_time,
last_uploaded_file_name,
last_uploaded_file_time,
log_backup_sets,
managedInstanceName,
number_of_files_detected,
number_of_files_queued,
number_of_files_restored,
number_of_files_restoring,
number_of_files_skipped,
number_of_files_unrestorable,
percent_completed,
resourceGroupName,
restoreDetailsName,
status,
subscriptionId,
type,
unrestorable_files
FROM azure.sql.vw_managed_database_restore_details
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND restoreDetailsName = '{{ restoreDetailsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_database_restore_details
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND restoreDetailsName = '{{ restoreDetailsName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

