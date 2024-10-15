---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `text` | Resource name associated with the resource. |
| <CopyableCode code="activity_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_instance_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_set_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_data_store_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_user_triggered" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobId" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="progress_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="progress_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="rehydration_priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_data_store_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vault_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | AzureBackup Job Class |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobId, resourceGroupName, subscriptionId, vaultName" /> | Gets a job with id in a backup vault |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Returns list of jobs belonging to a backup vault |

## `SELECT` examples

Returns list of jobs belonging to a backup vault

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
activity_id,
backup_instance_friendly_name,
backup_instance_id,
data_source_id,
data_source_location,
data_source_name,
data_source_set_name,
data_source_type,
destination_data_store_name,
duration,
end_time,
error_details,
etag,
extended_info,
is_user_triggered,
jobId,
operation,
operation_category,
policy_id,
policy_name,
progress_enabled,
progress_url,
rehydration_priority,
resourceGroupName,
restore_type,
source_data_store_name,
source_resource_group,
source_subscription_id,
start_time,
status,
subscriptionId,
subscription_id,
supported_actions,
system_data,
type,
vaultName,
vault_name
FROM azure.data_protection.vw_jobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_protection.jobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

