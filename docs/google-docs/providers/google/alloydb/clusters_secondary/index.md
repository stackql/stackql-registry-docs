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
    - name: displayName
      value: '{{ displayName }}'
    - name: labels
      value: '{{ labels }}'
    - name: databaseVersion
      value: '{{ databaseVersion }}'
    - name: networkConfig
      value:
        - name: network
          value: '{{ network }}'
        - name: allocatedIpRange
          value: '{{ allocatedIpRange }}'
    - name: network
      value: '{{ network }}'
    - name: etag
      value: '{{ etag }}'
    - name: annotations
      value: '{{ annotations }}'
    - name: initialUser
      value:
        - name: user
          value: '{{ user }}'
        - name: password
          value: '{{ password }}'
    - name: automatedBackupPolicy
      value:
        - name: weeklySchedule
          value:
            - name: startTimes
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: daysOfWeek
              value:
                - name: type
                  value: '{{ type }}'
                - name: enumDescriptions
                  value: '{{ enumDescriptions }}'
                - name: enum
                  value: '{{ enum }}'
        - name: timeBasedRetention
          value:
            - name: retentionPeriod
              value: '{{ retentionPeriod }}'
        - name: quantityBasedRetention
          value:
            - name: count
              value: '{{ count }}'
        - name: enabled
          value: '{{ enabled }}'
        - name: backupWindow
          value: '{{ backupWindow }}'
        - name: encryptionConfig
          value:
            - name: kmsKeyName
              value: '{{ kmsKeyName }}'
        - name: location
          value: '{{ location }}'
        - name: labels
          value: '{{ labels }}'
    - name: sslConfig
      value:
        - name: sslMode
          value: '{{ sslMode }}'
        - name: caSource
          value: '{{ caSource }}'
    - name: continuousBackupConfig
      value:
        - name: enabled
          value: '{{ enabled }}'
        - name: recoveryWindowDays
          value: '{{ recoveryWindowDays }}'
    - name: secondaryConfig
      value:
        - name: primaryClusterName
          value: '{{ primaryClusterName }}'
    - name: pscConfig
      value:
        - name: pscEnabled
          value: '{{ pscEnabled }}'
    - name: maintenanceUpdatePolicy
      value:
        - name: maintenanceWindows
          value:
            - name: $ref
              value: '{{ $ref }}'
    - name: subscriptionType
      value: '{{ subscriptionType }}'

```
</TabItem>
</Tabs>
