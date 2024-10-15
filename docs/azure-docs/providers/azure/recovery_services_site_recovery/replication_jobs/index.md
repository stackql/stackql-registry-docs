---
title: replication_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_jobs
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_jobs', value: 'view', },
        { label: 'replication_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="activity_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scenario_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_instance_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_object_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="tasks" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Job custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, resourceName, subscriptionId" /> | Get the details of an Azure Site Recovery job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the list of Azure Site Recovery Jobs for the vault. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, resourceName, subscriptionId" /> | The operation to cancel an Azure Site Recovery job. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation to export the details of the Azure Site Recovery jobs of the vault. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, resourceName, subscriptionId" /> | The operation to restart an Azure Site Recovery job. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, resourceName, subscriptionId" /> | The operation to resume an Azure Site Recovery job. |

## `SELECT` examples

Gets the list of Azure Site Recovery Jobs for the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_jobs', value: 'view', },
        { label: 'replication_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
activity_id,
allowed_actions,
custom_details,
end_time,
errors,
friendly_name,
jobName,
location,
resourceGroupName,
resourceName,
scenario_name,
start_time,
state,
state_description,
subscriptionId,
target_instance_type,
target_object_id,
target_object_name,
tasks,
type
FROM azure.recovery_services_site_recovery.vw_replication_jobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
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
FROM azure.recovery_services_site_recovery.replication_jobs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

