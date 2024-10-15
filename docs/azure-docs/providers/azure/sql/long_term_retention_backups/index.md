---
title: long_term_retention_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_backups
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

Creates, updates, deletes, gets or lists a <code>long_term_retention_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>long_term_retention_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_backups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_long_term_retention_backups', value: 'view', },
        { label: 'long_term_retention_backups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_storage_access_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_storage_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_deletion_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_backup_immutable" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="longTermRetentionDatabaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="longTermRetentionServerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="requested_backup_storage_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_create_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_name" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Gets a long term retention backup. |
| <CopyableCode code="get_by_resource_group" /> | `SELECT` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Gets a long term retention backup. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Lists all long term retention backups for a database. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Lists the long term retention backups for a given location. |
| <CopyableCode code="list_by_resource_group_database" /> | `SELECT` | <CopyableCode code="locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Lists all long term retention backups for a database based on a particular resource group. |
| <CopyableCode code="list_by_resource_group_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists the long term retention backups for a given location based on resource group. |
| <CopyableCode code="list_by_resource_group_server" /> | `SELECT` | <CopyableCode code="locationName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Lists the long term retention backups for a given server based on resource groups. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="locationName, longTermRetentionServerName, subscriptionId" /> | Lists the long term retention backups for a given server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Deletes a long term retention backup. |
| <CopyableCode code="delete_by_resource_group" /> | `DELETE` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Deletes a long term retention backup. |
| <CopyableCode code="change_access_tier" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId, data__backupStorageAccessTier, data__operationMode" /> | Change a long term retention backup access tier. |
| <CopyableCode code="change_access_tier_by_resource_group" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId, data__backupStorageAccessTier, data__operationMode" /> | Change a long term retention backup access tier. |
| <CopyableCode code="copy" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Copy an existing long term retention backup. |
| <CopyableCode code="copy_by_resource_group" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Copy an existing long term retention backup to a different server. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, subscriptionId" /> | Updates an existing long term retention backup. |
| <CopyableCode code="update_by_resource_group" /> | `EXEC` | <CopyableCode code="backupName, locationName, longTermRetentionDatabaseName, longTermRetentionServerName, resourceGroupName, subscriptionId" /> | Updates an existing long term retention backup. |

## `SELECT` examples

Lists the long term retention backups for a given location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_long_term_retention_backups', value: 'view', },
        { label: 'long_term_retention_backups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
backupName,
backup_expiration_time,
backup_storage_access_tier,
backup_storage_redundancy,
backup_time,
database_deletion_time,
database_name,
is_backup_immutable,
locationName,
longTermRetentionDatabaseName,
longTermRetentionServerName,
requested_backup_storage_redundancy,
resourceGroupName,
server_create_time,
server_name,
subscriptionId
FROM azure.sql.vw_long_term_retention_backups
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.long_term_retention_backups
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>long_term_retention_backups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.long_term_retention_backups
WHERE backupName = '{{ backupName }}'
AND locationName = '{{ locationName }}'
AND longTermRetentionDatabaseName = '{{ longTermRetentionDatabaseName }}'
AND longTermRetentionServerName = '{{ longTermRetentionServerName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
