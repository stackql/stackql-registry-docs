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
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: endTime
      value: string
    - name: state
      value: string
    - name: serviceRevision
      value:
        - name: hiveMetastoreConfig
          value:
            - name: version
              value: string
            - name: configOverrides
              value: object
            - name: kerberosConfig
              value:
                - name: keytab
                  value:
                    - name: cloudSecret
                      value: string
                - name: principal
                  value: string
                - name: krb5ConfigGcsUri
                  value: string
            - name: endpointProtocol
              value: string
            - name: auxiliaryVersions
              value: object
        - name: name
          value: string
        - name: createTime
          value: string
        - name: updateTime
          value: string
        - name: labels
          value: object
        - name: network
          value: string
        - name: endpointUri
          value: string
        - name: port
          value: integer
        - name: state
          value: string
        - name: stateMessage
          value: string
        - name: artifactGcsUri
          value: string
        - name: tier
          value: string
        - name: metadataIntegration
          value:
            - name: dataCatalogConfig
              value:
                - name: enabled
                  value: boolean
        - name: maintenanceWindow
          value:
            - name: hourOfDay
              value: integer
            - name: dayOfWeek
              value: string
        - name: uid
          value: string
        - name: metadataManagementActivity
          value:
            - name: metadataExports
              value:
                - - name: destinationGcsUri
                    value: string
                  - name: startTime
                    value: string
                  - name: endTime
                    value: string
                  - name: state
                    value: string
                  - name: databaseDumpType
                    value: string
            - name: restores
              value:
                - - name: startTime
                    value: string
                  - name: endTime
                    value: string
                  - name: state
                    value: string
                  - name: backup
                    value: string
                  - name: type
                    value: string
                  - name: details
                    value: string
                  - name: backupLocation
                    value: string
        - name: releaseChannel
          value: string
        - name: encryptionConfig
          value:
            - name: kmsKey
              value: string
        - name: networkConfig
          value:
            - name: consumers
              value:
                - - name: subnetwork
                    value: string
                  - name: endpointUri
                    value: string
                  - name: endpointLocation
                    value: string
        - name: databaseType
          value: string
        - name: telemetryConfig
          value:
            - name: logFormat
              value: string
        - name: scalingConfig
          value:
            - name: instanceSize
              value: string
            - name: scalingFactor
              value: number
            - name: autoscalingConfig
              value:
                - name: autoscalingFactor
                  value: number
                - name: autoscalingEnabled
                  value: boolean
                - name: limitConfig
                  value:
                    - name: maxScalingFactor
                      value: number
                    - name: minScalingFactor
                      value: number
        - name: scheduledBackup
          value:
            - name: enabled
              value: boolean
            - name: cronSchedule
              value: string
            - name: timeZone
              value: string
            - name: nextScheduledTime
              value: string
            - name: backupLocation
              value: string
            - name: latestBackup
              value:
                - name: backupId
                  value: string
                - name: startTime
                  value: string
                - name: state
                  value: string
                - name: duration
                  value: string
        - name: deletionProtection
          value: boolean
    - name: description
      value: string
    - name: restoringServices
      value:
        - string

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
