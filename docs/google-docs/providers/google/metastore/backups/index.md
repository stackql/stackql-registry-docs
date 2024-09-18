---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - metastore
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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.metastore.backups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The relative resource name of the backup, in the following form:projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id} |
| <CopyableCode code="description" /> | `string` | The description of the backup. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the backup was started. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time when the backup finished creating. |
| <CopyableCode code="restoringServices" /> | `array` | Output only. Services that are restoring from the backup. |
| <CopyableCode code="serviceRevision" /> | `object` | A managed metastore service that serves metadata queries. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the backup. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupsId, locationsId, projectsId, servicesId" /> | Gets details of a single backup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists backups in a service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Creates a new backup in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupsId, locationsId, projectsId, servicesId" /> | Deletes a single backup. |

## `SELECT` examples

Lists backups in a service.

```sql
SELECT
name,
description,
createTime,
endTime,
restoringServices,
serviceRevision,
state
FROM google.metastore.backups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backups</code> resource.

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
INSERT INTO google.metastore.backups (
locationsId,
projectsId,
servicesId,
name,
description
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ servicesId }}',
'{{ name }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
endTime: string
state: string
serviceRevision:
  hiveMetastoreConfig:
    version: string
    configOverrides: object
    kerberosConfig:
      keytab:
        cloudSecret: string
      principal: string
      krb5ConfigGcsUri: string
    endpointProtocol: string
    auxiliaryVersions: object
  name: string
  createTime: string
  updateTime: string
  labels: object
  network: string
  endpointUri: string
  port: integer
  state: string
  stateMessage: string
  artifactGcsUri: string
  tier: string
  metadataIntegration:
    dataCatalogConfig:
      enabled: boolean
  maintenanceWindow:
    hourOfDay: integer
    dayOfWeek: string
  uid: string
  metadataManagementActivity:
    metadataExports:
      - destinationGcsUri: string
        startTime: string
        endTime: string
        state: string
        databaseDumpType: string
    restores:
      - startTime: string
        endTime: string
        state: string
        backup: string
        type: string
        details: string
        backupLocation: string
  releaseChannel: string
  encryptionConfig:
    kmsKey: string
  networkConfig:
    consumers:
      - subnetwork: string
        endpointUri: string
        endpointLocation: string
  databaseType: string
  telemetryConfig:
    logFormat: string
  scalingConfig:
    instanceSize: string
    scalingFactor: number
    autoscalingConfig:
      autoscalingFactor: number
      autoscalingEnabled: boolean
      limitConfig:
        maxScalingFactor: number
        minScalingFactor: number
  scheduledBackup:
    enabled: boolean
    cronSchedule: string
    timeZone: string
    nextScheduledTime: string
    backupLocation: string
    latestBackup:
      backupId: string
      startTime: string
      state: string
      duration: string
  deletionProtection: boolean
description: string
restoringServices:
  - type: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backups</code> resource.

```sql
/*+ delete */
DELETE FROM google.metastore.backups
WHERE backupsId = '{{ backupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
