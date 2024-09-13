
---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

Creates, updates, deletes or gets an <code>cluster</code> resource or lists <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the cluster resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see https://google.aip.dev/122. The prefix of the cluster resource name is the name of the parent resource: * projects/{project}/locations/{region} |
| <CopyableCode code="annotations" /> | `object` | Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 |
| <CopyableCode code="automatedBackupPolicy" /> | `object` | Message describing the user-specified automated backup policy. All fields in the automated backup policy are optional. Defaults for each field are provided if they are not set. |
| <CopyableCode code="backupSource" /> | `object` | Message describing a BackupSource. |
| <CopyableCode code="clusterType" /> | `string` | Output only. The type of the cluster. This is an output-only field and it's populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster` |
| <CopyableCode code="continuousBackupConfig" /> | `object` | ContinuousBackupConfig describes the continuous backups recovery configurations of a cluster. |
| <CopyableCode code="continuousBackupInfo" /> | `object` | ContinuousBackupInfo describes the continuous backup properties of a cluster. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time stamp |
| <CopyableCode code="databaseVersion" /> | `string` | Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Delete time stamp |
| <CopyableCode code="displayName" /> | `string` | User-settable and human-readable display name for the Cluster. |
| <CopyableCode code="encryptionConfig" /> | `object` | EncryptionConfig describes the encryption config of a cluster or a backup that is encrypted with a CMEK (customer-managed encryption key). |
| <CopyableCode code="encryptionInfo" /> | `object` | EncryptionInfo describes the encryption information of a cluster or a backup. |
| <CopyableCode code="etag" /> | `string` | For Resource freshness validation (https://google.aip.dev/154) |
| <CopyableCode code="initialUser" /> | `object` | The username/password for a database user. Used for specifying initial users at cluster creation time. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs |
| <CopyableCode code="maintenanceSchedule" /> | `object` | MaintenanceSchedule stores the maintenance schedule generated from the MaintenanceUpdatePolicy, once a maintenance rollout is triggered, if MaintenanceWindow is set, and if there is no conflicting DenyPeriod. The schedule is cleared once the update takes place. This field cannot be manually changed; modify the MaintenanceUpdatePolicy instead. |
| <CopyableCode code="maintenanceUpdatePolicy" /> | `object` | MaintenanceUpdatePolicy defines the policy for system updates. |
| <CopyableCode code="migrationSource" /> | `object` | Subset of the source instance configuration that is available when reading the cluster resource. |
| <CopyableCode code="network" /> | `string` | Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead. |
| <CopyableCode code="networkConfig" /> | `object` | Metadata related to network configuration. |
| <CopyableCode code="primaryConfig" /> | `object` | Configuration for the primary cluster. It has the list of clusters that are replicating from this cluster. This should be set if and only if the cluster is of type PRIMARY. |
| <CopyableCode code="pscConfig" /> | `object` | PscConfig contains PSC related configuration at a cluster level. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Cluster does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="secondaryConfig" /> | `object` | Configuration information for the secondary cluster. This should be set if and only if the cluster is of type SECONDARY. |
| <CopyableCode code="sslConfig" /> | `object` | SSL configuration. |
| <CopyableCode code="state" /> | `string` | Output only. The current serving state of the cluster. |
| <CopyableCode code="subscriptionType" /> | `string` | Optional. Subscription type of the cluster. |
| <CopyableCode code="trialMetadata" /> | `object` | Contains information and all metadata related to TRIAL clusters. |
| <CopyableCode code="uid" /> | `string` | Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time stamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Gets details of a single Cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Clusters in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Cluster in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Deletes a single Cluster. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Updates the parameters of a single Cluster. |
| <CopyableCode code="promote" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Promotes a SECONDARY cluster. This turns down replication from the PRIMARY cluster and promotes a secondary cluster into its own standalone cluster. Imperative only. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Cluster in a given project and location, with a volume restored from the provided source, either a backup ID or a point-in-time and a source cluster. |
| <CopyableCode code="switchover" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Switches the role of PRIMARY and SECONDARY cluster without any data loss. This promotes the SECONDARY cluster to PRIMARY and sets up original PRIMARY cluster to replicate from this newly promoted cluster. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Upgrades a single Cluster. Imperative only. |

## `SELECT` examples

Lists Clusters in a given project and location.

```sql
SELECT
name,
annotations,
automatedBackupPolicy,
backupSource,
clusterType,
continuousBackupConfig,
continuousBackupInfo,
createTime,
databaseVersion,
deleteTime,
displayName,
encryptionConfig,
encryptionInfo,
etag,
initialUser,
labels,
maintenanceSchedule,
maintenanceUpdatePolicy,
migrationSource,
network,
networkConfig,
primaryConfig,
pscConfig,
reconciling,
satisfiesPzs,
secondaryConfig,
sslConfig,
state,
subscriptionType,
trialMetadata,
uid,
updateTime
FROM google.alloydb.clusters
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

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
INSERT INTO google.alloydb.clusters (
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
resources:
  - name: instance
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

## `UPDATE` example

Updates a cluster only if the necessary resources are available.

```sql
UPDATE google.alloydb.clusters
SET 
backupSource = '{{ backupSource }}',
migrationSource = '{{ migrationSource }}',
name = '{{ name }}',
displayName = '{{ displayName }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
deleteTime = '{{ deleteTime }}',
labels = '{{ labels }}',
state = '{{ state }}',
clusterType = '{{ clusterType }}',
databaseVersion = '{{ databaseVersion }}',
networkConfig = '{{ networkConfig }}',
network = '{{ network }}',
etag = '{{ etag }}',
annotations = '{{ annotations }}',
reconciling = true|false,
initialUser = '{{ initialUser }}',
automatedBackupPolicy = '{{ automatedBackupPolicy }}',
sslConfig = '{{ sslConfig }}',
encryptionConfig = '{{ encryptionConfig }}',
encryptionInfo = '{{ encryptionInfo }}',
continuousBackupConfig = '{{ continuousBackupConfig }}',
continuousBackupInfo = '{{ continuousBackupInfo }}',
secondaryConfig = '{{ secondaryConfig }}',
primaryConfig = '{{ primaryConfig }}',
satisfiesPzs = true|false,
pscConfig = '{{ pscConfig }}',
maintenanceUpdatePolicy = '{{ maintenanceUpdatePolicy }}',
maintenanceSchedule = '{{ maintenanceSchedule }}',
subscriptionType = '{{ subscriptionType }}',
trialMetadata = '{{ trialMetadata }}'
WHERE 
clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified cluster resource.

```sql
DELETE FROM google.alloydb.clusters
WHERE clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
