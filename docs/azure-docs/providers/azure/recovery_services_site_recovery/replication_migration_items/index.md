---
title: replication_migration_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_migration_items
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

Creates, updates, deletes, gets or lists a <code>replication_migration_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_migration_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_migration_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_migration_items', value: 'view', },
        { label: 'replication_migration_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="allowed_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="critical_job_history" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="health" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_migration_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_migration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_test_migration_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_test_migration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="machine_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="migrationItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectionContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_services_provider_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_migrate_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_migrate_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Migration item properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR migration items in the protection container. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to create an ASR migration item (enable migration). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete an ASR migration item. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update the recovery settings of an ASR migration item. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate migration of the item. |
| <CopyableCode code="pause_replication" /> | `EXEC` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate pause replication of the item. |
| <CopyableCode code="resume_replication" /> | `EXEC` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate resume replication of the item. |
| <CopyableCode code="resync" /> | `EXEC` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to resynchronize replication of an ASR migration item. |
| <CopyableCode code="test_migrate" /> | `EXEC` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate test migration of the item. |
| <CopyableCode code="test_migrate_cleanup" /> | `EXEC` | <CopyableCode code="fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate test migrate cleanup. |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_migration_items', value: 'view', },
        { label: 'replication_migration_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allowed_operations,
critical_job_history,
current_job,
event_correlation_id,
fabricName,
health,
health_errors,
last_migration_status,
last_migration_time,
last_test_migration_status,
last_test_migration_time,
location,
machine_name,
migrationItemName,
migration_state,
migration_state_description,
policy_friendly_name,
policy_id,
protectionContainerName,
provider_specific_details,
recovery_services_provider_id,
replication_status,
resourceGroupName,
resourceName,
subscriptionId,
test_migrate_state,
test_migrate_state_description,
type
FROM azure.recovery_services_site_recovery.vw_replication_migration_items
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
FROM azure.recovery_services_site_recovery.replication_migration_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_migration_items</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.recovery_services_site_recovery.replication_migration_items (
fabricName,
migrationItemName,
protectionContainerName,
resourceGroupName,
resourceName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ fabricName }}',
'{{ migrationItemName }}',
'{{ protectionContainerName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: policyId
          value: string
        - name: providerSpecificDetails
          value:
            - name: instanceType
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replication_migration_items</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services_site_recovery.replication_migration_items
SET 
properties = '{{ properties }}'
WHERE 
fabricName = '{{ fabricName }}'
AND migrationItemName = '{{ migrationItemName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>replication_migration_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_migration_items
WHERE fabricName = '{{ fabricName }}'
AND migrationItemName = '{{ migrationItemName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
