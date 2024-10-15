---
title: long_term_retention_managed_instance_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_managed_instance_backups
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

Creates, updates, deletes, gets or lists a <code>long_term_retention_managed_instance_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>long_term_retention_managed_instance_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_managed_instance_backups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_long_term_retention_managed_instance_backups', value: 'view', },
        { label: 'long_term_retention_managed_instance_backups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_storage_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_deletion_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_instance_create_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_instance_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a long term retention backup |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupName, databaseName, locationName, managedInstanceName, subscriptionId" /> | Gets a long term retention backup for a managed database. |
| <CopyableCode code="get_by_resource_group" /> | `SELECT` | <CopyableCode code="backupName, databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a long term retention backup for a managed database. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, locationName, managedInstanceName, subscriptionId" /> | Lists all long term retention backups for a managed database. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Lists the long term retention backups for managed databases in a given location. |
| <CopyableCode code="list_by_resource_group_database" /> | `SELECT` | <CopyableCode code="databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Lists all long term retention backups for a managed database. |
| <CopyableCode code="list_by_resource_group_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists the long term retention backups for managed databases in a given location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupName, databaseName, locationName, managedInstanceName, subscriptionId" /> | Deletes a long term retention backup. |
| <CopyableCode code="delete_by_resource_group" /> | `DELETE` | <CopyableCode code="backupName, databaseName, locationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a long term retention backup. |

## `SELECT` examples

Lists the long term retention backups for managed databases in a given location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_long_term_retention_managed_instance_backups', value: 'view', },
        { label: 'long_term_retention_managed_instance_backups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
backupName,
backup_expiration_time,
backup_storage_redundancy,
backup_time,
databaseName,
database_deletion_time,
database_name,
locationName,
managedInstanceName,
managed_instance_create_time,
managed_instance_name,
resourceGroupName,
subscriptionId
FROM azure.sql.vw_long_term_retention_managed_instance_backups
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.long_term_retention_managed_instance_backups
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>long_term_retention_managed_instance_backups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.long_term_retention_managed_instance_backups
WHERE backupName = '{{ backupName }}'
AND databaseName = '{{ databaseName }}'
AND locationName = '{{ locationName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
