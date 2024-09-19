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
- name: your_resource_model_name
  props:
    - name: backupSource
      value:
        - name: backupUid
          value: string
        - name: backupName
          value: string
    - name: migrationSource
      value:
        - name: hostPort
          value: string
        - name: referenceId
          value: string
        - name: sourceType
          value: string
    - name: name
      value: string
    - name: displayName
      value: string
    - name: uid
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: deleteTime
      value: string
    - name: labels
      value: object
    - name: state
      value: string
    - name: clusterType
      value: string
    - name: databaseVersion
      value: string
    - name: networkConfig
      value:
        - name: network
          value: string
        - name: allocatedIpRange
          value: string
    - name: network
      value: string
    - name: etag
      value: string
    - name: annotations
      value: object
    - name: reconciling
      value: boolean
    - name: initialUser
      value:
        - name: user
          value: string
        - name: password
          value: string
    - name: automatedBackupPolicy
      value:
        - name: weeklySchedule
          value:
            - name: startTimes
              value:
                - - name: hours
                    value: integer
                  - name: minutes
                    value: integer
                  - name: seconds
                    value: integer
                  - name: nanos
                    value: integer
            - name: daysOfWeek
              value:
                - string
        - name: timeBasedRetention
          value:
            - name: retentionPeriod
              value: string
        - name: quantityBasedRetention
          value:
            - name: count
              value: integer
        - name: enabled
          value: boolean
        - name: backupWindow
          value: string
        - name: encryptionConfig
          value:
            - name: kmsKeyName
              value: string
        - name: location
          value: string
        - name: labels
          value: object
    - name: sslConfig
      value:
        - name: sslMode
          value: string
        - name: caSource
          value: string
    - name: encryptionInfo
      value:
        - name: encryptionType
          value: string
        - name: kmsKeyVersions
          value:
            - string
    - name: continuousBackupConfig
      value:
        - name: enabled
          value: boolean
        - name: recoveryWindowDays
          value: integer
    - name: continuousBackupInfo
      value:
        - name: enabledTime
          value: string
        - name: schedule
          value:
            - string
        - name: earliestRestorableTime
          value: string
    - name: secondaryConfig
      value:
        - name: primaryClusterName
          value: string
    - name: primaryConfig
      value:
        - name: secondaryClusterNames
          value:
            - string
    - name: satisfiesPzs
      value: boolean
    - name: pscConfig
      value:
        - name: pscEnabled
          value: boolean
    - name: maintenanceUpdatePolicy
      value:
        - name: maintenanceWindows
          value:
            - - name: day
                value: string
              - name: startTime
                value:
                  - name: hours
                    value: integer
                  - name: minutes
                    value: integer
                  - name: seconds
                    value: integer
                  - name: nanos
                    value: integer
    - name: maintenanceSchedule
      value:
        - name: startTime
          value: string
    - name: subscriptionType
      value: string
    - name: trialMetadata
      value:
        - name: startTime
          value: string
        - name: endTime
          value: string
        - name: upgradeTime
          value: string
        - name: graceEndTime
          value: string

```
</TabItem>
</Tabs>
