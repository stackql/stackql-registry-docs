---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - backupdr
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

Creates, updates, deletes, gets or lists a <code>data_sources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.backupdr.data_sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name. |
| <CopyableCode code="backupConfigInfo" /> | `object` | BackupConfigInfo has information about how the resource is configured for Backup and about the most recent backup to this vault. |
| <CopyableCode code="backupCount" /> | `string` | Number of backups in the data source. |
| <CopyableCode code="configState" /> | `string` | Output only. The backup configuration state. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created. |
| <CopyableCode code="dataSourceBackupApplianceApplication" /> | `object` | BackupApplianceApplication describes a Source Resource when it is an application backed up by a BackupAppliance. |
| <CopyableCode code="dataSourceGcpResource" /> | `object` | DataSourceGcpResource is used for protected resources that are Google Cloud Resources. This name is easeier to understand than GcpResourceDataSource or GcpDataSourceResource |
| <CopyableCode code="etag" /> | `string` | Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user provided metadata. No labels currently defined: |
| <CopyableCode code="state" /> | `string` | Output only. The DataSource resource instance state. |
| <CopyableCode code="totalStoredBytes" /> | `string` | The number of bytes (metadata and data) stored in this datasource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the instance was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Gets details of a DataSource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="backupVaultsId, locationsId, projectsId" /> | Lists DataSources in a given project and location. |
| <CopyableCode code="remove" /> | `DELETE` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Deletes a DataSource. This is a custom method instead of a standard delete method because external clients will not delete DataSources except for BackupDR backup appliances. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Updates the settings of a DataSource. |
| <CopyableCode code="abandon_backup" /> | `EXEC` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Internal only. Abandons a backup. |
| <CopyableCode code="finalize_backup" /> | `EXEC` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Internal only. Finalize a backup that was started by a call to InitiateBackup. |
| <CopyableCode code="initiate_backup" /> | `EXEC` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Internal only. Initiates a backup. |
| <CopyableCode code="set_internal_status" /> | `EXEC` | <CopyableCode code="backupVaultsId, dataSourcesId, locationsId, projectsId" /> | Sets the internal status of a DataSource. |

## `SELECT` examples

Lists DataSources in a given project and location.

```sql
SELECT
name,
backupConfigInfo,
backupCount,
configState,
createTime,
dataSourceBackupApplianceApplication,
dataSourceGcpResource,
etag,
labels,
state,
totalStoredBytes,
updateTime
FROM google.backupdr.data_sources
WHERE backupVaultsId = '{{ backupVaultsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>data_sources</code> resource.

```sql
/*+ update */
UPDATE google.backupdr.data_sources
SET 
labels = '{{ labels }}',
backupCount = '{{ backupCount }}',
etag = '{{ etag }}',
totalStoredBytes = '{{ totalStoredBytes }}',
dataSourceGcpResource = '{{ dataSourceGcpResource }}',
dataSourceBackupApplianceApplication = '{{ dataSourceBackupApplianceApplication }}'
WHERE 
backupVaultsId = '{{ backupVaultsId }}'
AND dataSourcesId = '{{ dataSourcesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>data_sources</code> resource.

```sql
/*+ delete */
DELETE FROM google.backupdr.data_sources
WHERE backupVaultsId = '{{ backupVaultsId }}'
AND dataSourcesId = '{{ dataSourcesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
