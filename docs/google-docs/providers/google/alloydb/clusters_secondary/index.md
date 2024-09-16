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
backupSource,
migrationSource,
name,
displayName,
uid,
createTime,
updateTime,
deleteTime,
labels,
state,
clusterType,
databaseVersion,
networkConfig,
network,
etag,
annotations,
reconciling,
initialUser,
automatedBackupPolicy,
sslConfig,
encryptionConfig,
encryptionInfo,
continuousBackupConfig,
continuousBackupInfo,
secondaryConfig,
primaryConfig,
satisfiesPzs,
pscConfig,
maintenanceUpdatePolicy,
maintenanceSchedule,
subscriptionType,
trialMetadata
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ backupSource }}',
'{{ migrationSource }}',
'{{ name }}',
'{{ displayName }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ labels }}',
'{{ state }}',
'{{ clusterType }}',
'{{ databaseVersion }}',
'{{ networkConfig }}',
'{{ network }}',
'{{ etag }}',
'{{ annotations }}',
true|false,
'{{ initialUser }}',
'{{ automatedBackupPolicy }}',
'{{ sslConfig }}',
'{{ encryptionConfig }}',
'{{ encryptionInfo }}',
'{{ continuousBackupConfig }}',
'{{ continuousBackupInfo }}',
'{{ secondaryConfig }}',
'{{ primaryConfig }}',
true|false,
'{{ pscConfig }}',
'{{ maintenanceUpdatePolicy }}',
'{{ maintenanceSchedule }}',
'{{ subscriptionType }}',
'{{ trialMetadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: backupSource
      value: '{{ backupSource }}'
    - name: migrationSource
      value: '{{ migrationSource }}'
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: uid
      value: '{{ uid }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: deleteTime
      value: '{{ deleteTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: state
      value: '{{ state }}'
    - name: clusterType
      value: '{{ clusterType }}'
    - name: databaseVersion
      value: '{{ databaseVersion }}'
    - name: networkConfig
      value: '{{ networkConfig }}'
    - name: network
      value: '{{ network }}'
    - name: etag
      value: '{{ etag }}'
    - name: annotations
      value: '{{ annotations }}'
    - name: reconciling
      value: '{{ reconciling }}'
    - name: initialUser
      value: '{{ initialUser }}'
    - name: automatedBackupPolicy
      value: '{{ automatedBackupPolicy }}'
    - name: sslConfig
      value: '{{ sslConfig }}'
    - name: encryptionConfig
      value: '{{ encryptionConfig }}'
    - name: encryptionInfo
      value: '{{ encryptionInfo }}'
    - name: continuousBackupConfig
      value: '{{ continuousBackupConfig }}'
    - name: continuousBackupInfo
      value: '{{ continuousBackupInfo }}'
    - name: secondaryConfig
      value: '{{ secondaryConfig }}'
    - name: primaryConfig
      value: '{{ primaryConfig }}'
    - name: satisfiesPzs
      value: '{{ satisfiesPzs }}'
    - name: pscConfig
      value: '{{ pscConfig }}'
    - name: maintenanceUpdatePolicy
      value: '{{ maintenanceUpdatePolicy }}'
    - name: maintenanceSchedule
      value: '{{ maintenanceSchedule }}'
    - name: subscriptionType
      value: '{{ subscriptionType }}'
    - name: trialMetadata
      value: '{{ trialMetadata }}'

```
</TabItem>
</Tabs>
