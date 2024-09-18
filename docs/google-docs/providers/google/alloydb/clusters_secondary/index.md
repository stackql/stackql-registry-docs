---
title: clusters_secondary
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_secondary
  - alloydb
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

Creates, updates, deletes, gets or lists a <code>clusters_secondary</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_secondary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.clusters_secondary" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="createsecondary" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a cluster of type SECONDARY in the given location using the primary cluster as the source. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters_secondary</code> resource.

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
INSERT INTO google.alloydb.clusters_secondary (
locationsId,
projectsId,
displayName,
labels,
databaseVersion,
networkConfig,
network,
etag,
annotations,
initialUser,
automatedBackupPolicy,
sslConfig,
encryptionConfig,
continuousBackupConfig,
secondaryConfig,
pscConfig,
maintenanceUpdatePolicy,
subscriptionType
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ labels }}',
'{{ databaseVersion }}',
'{{ networkConfig }}',
'{{ network }}',
'{{ etag }}',
'{{ annotations }}',
'{{ initialUser }}',
'{{ automatedBackupPolicy }}',
'{{ sslConfig }}',
'{{ encryptionConfig }}',
'{{ continuousBackupConfig }}',
'{{ secondaryConfig }}',
'{{ pscConfig }}',
'{{ maintenanceUpdatePolicy }}',
'{{ subscriptionType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
backupSource:
  backupUid: string
  backupName: string
migrationSource:
  hostPort: string
  referenceId: string
  sourceType: string
name: string
displayName: string
uid: string
createTime: string
updateTime: string
deleteTime: string
labels: object
state: string
clusterType: string
databaseVersion: string
networkConfig:
  network: string
  allocatedIpRange: string
network: string
etag: string
annotations: object
reconciling: boolean
initialUser:
  user: string
  password: string
automatedBackupPolicy:
  weeklySchedule:
    startTimes:
      - hours: integer
        minutes: integer
        seconds: integer
        nanos: integer
    daysOfWeek:
      - type: string
        enumDescriptions: string
        enum: string
  timeBasedRetention:
    retentionPeriod: string
  quantityBasedRetention:
    count: integer
  enabled: boolean
  backupWindow: string
  encryptionConfig:
    kmsKeyName: string
  location: string
  labels: object
sslConfig:
  sslMode: string
  caSource: string
encryptionInfo:
  encryptionType: string
  kmsKeyVersions:
    - type: string
continuousBackupConfig:
  enabled: boolean
  recoveryWindowDays: integer
continuousBackupInfo:
  enabledTime: string
  schedule:
    - type: string
      enumDescriptions: string
      enum: string
  earliestRestorableTime: string
secondaryConfig:
  primaryClusterName: string
primaryConfig:
  secondaryClusterNames:
    - type: string
satisfiesPzs: boolean
pscConfig:
  pscEnabled: boolean
maintenanceUpdatePolicy:
  maintenanceWindows:
    - day: string
      startTime:
        hours: integer
        minutes: integer
        seconds: integer
        nanos: integer
maintenanceSchedule:
  startTime: string
subscriptionType: string
trialMetadata:
  startTime: string
  endTime: string
  upgradeTime: string
  graceEndTime: string

```
</TabItem>
</Tabs>
