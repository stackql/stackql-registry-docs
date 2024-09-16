---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.metastore.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The relative resource name of the metastore service, in the following format:projects/{project_number}/locations/{location_id}/services/{service_id}. |
| <CopyableCode code="artifactGcsUri" /> | `string` | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the metastore service was created. |
| <CopyableCode code="databaseType" /> | `string` | Immutable. The database type that the Metastore service stores its data. |
| <CopyableCode code="deletionProtection" /> | `boolean` | Optional. Indicates if the dataproc metastore should be protected against accidental deletions. |
| <CopyableCode code="encryptionConfig" /> | `object` | Encryption settings for the service. |
| <CopyableCode code="endpointUri" /> | `string` | Output only. The URI of the endpoint used to access the metastore service. |
| <CopyableCode code="hiveMetastoreConfig" /> | `object` | Specifies configuration information specific to running Hive metastore software as the metastore service. |
| <CopyableCode code="labels" /> | `object` | User-defined labels for the metastore service. |
| <CopyableCode code="maintenanceWindow" /> | `object` | Maintenance window. This specifies when Dataproc Metastore may perform system maintenance operation to the service. |
| <CopyableCode code="metadataIntegration" /> | `object` | Specifies how metastore metadata should be integrated with external services. |
| <CopyableCode code="metadataManagementActivity" /> | `object` | The metadata management activities of the metastore service. |
| <CopyableCode code="network" /> | `string` | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/{project_number}/global/networks/{network_id}. |
| <CopyableCode code="networkConfig" /> | `object` | Network configuration for the Dataproc Metastore service. |
| <CopyableCode code="port" /> | `integer` | The TCP port at which the metastore service is reached. Default: 9083. |
| <CopyableCode code="releaseChannel" /> | `string` | Immutable. The release channel of the service. If unspecified, defaults to STABLE. |
| <CopyableCode code="scalingConfig" /> | `object` | Represents the scaling configuration of a metastore service. |
| <CopyableCode code="scheduledBackup" /> | `object` | This specifies the configuration of scheduled backup. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the metastore service. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. Additional information about the current state of the metastore service, if available. |
| <CopyableCode code="telemetryConfig" /> | `object` | Telemetry Configuration for the Dataproc Metastore service. |
| <CopyableCode code="tier" /> | `string` | The tier of the service. |
| <CopyableCode code="uid" /> | `string` | Output only. The globally unique resource identifier of the metastore service. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the metastore service was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Gets the details of a single service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists services in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a metastore service in a project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Deletes a single service. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Updates the parameters of a single service. |
| <CopyableCode code="alter_location" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location. |
| <CopyableCode code="alter_table_properties" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Alter metadata table properties. |
| <CopyableCode code="cancel_migration" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Cancels the ongoing Managed Migration process. |
| <CopyableCode code="complete_migration" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Completes the managed migration process. The Dataproc Metastore service will switch to using its own backend database after successful migration. |
| <CopyableCode code="export_metadata" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Exports metadata from a service. |
| <CopyableCode code="move_table_to_database" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Move a table to another database. |
| <CopyableCode code="query_metadata" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Query Dataproc Metastore metadata. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Restores a service from a backup. |
| <CopyableCode code="start_migration" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Starts the Managed Migration process. |

## `SELECT` examples

Lists services in a project and location.

```sql
SELECT
name,
artifactGcsUri,
createTime,
databaseType,
deletionProtection,
encryptionConfig,
endpointUri,
hiveMetastoreConfig,
labels,
maintenanceWindow,
metadataIntegration,
metadataManagementActivity,
network,
networkConfig,
port,
releaseChannel,
scalingConfig,
scheduledBackup,
state,
stateMessage,
telemetryConfig,
tier,
uid,
updateTime
FROM google.metastore.services
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO google.metastore.services (
locationsId,
projectsId,
hiveMetastoreConfig,
name,
createTime,
updateTime,
labels,
network,
endpointUri,
port,
state,
stateMessage,
artifactGcsUri,
tier,
metadataIntegration,
maintenanceWindow,
uid,
metadataManagementActivity,
releaseChannel,
encryptionConfig,
networkConfig,
databaseType,
telemetryConfig,
scalingConfig,
scheduledBackup,
deletionProtection
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ hiveMetastoreConfig }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ network }}',
'{{ endpointUri }}',
'{{ port }}',
'{{ state }}',
'{{ stateMessage }}',
'{{ artifactGcsUri }}',
'{{ tier }}',
'{{ metadataIntegration }}',
'{{ maintenanceWindow }}',
'{{ uid }}',
'{{ metadataManagementActivity }}',
'{{ releaseChannel }}',
'{{ encryptionConfig }}',
'{{ networkConfig }}',
'{{ databaseType }}',
'{{ telemetryConfig }}',
'{{ scalingConfig }}',
'{{ scheduledBackup }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: hiveMetastoreConfig
      value: '{{ hiveMetastoreConfig }}'
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: network
      value: '{{ network }}'
    - name: endpointUri
      value: '{{ endpointUri }}'
    - name: port
      value: '{{ port }}'
    - name: state
      value: '{{ state }}'
    - name: stateMessage
      value: '{{ stateMessage }}'
    - name: artifactGcsUri
      value: '{{ artifactGcsUri }}'
    - name: tier
      value: '{{ tier }}'
    - name: metadataIntegration
      value: '{{ metadataIntegration }}'
    - name: maintenanceWindow
      value: '{{ maintenanceWindow }}'
    - name: uid
      value: '{{ uid }}'
    - name: metadataManagementActivity
      value: '{{ metadataManagementActivity }}'
    - name: releaseChannel
      value: '{{ releaseChannel }}'
    - name: encryptionConfig
      value: '{{ encryptionConfig }}'
    - name: networkConfig
      value: '{{ networkConfig }}'
    - name: databaseType
      value: '{{ databaseType }}'
    - name: telemetryConfig
      value: '{{ telemetryConfig }}'
    - name: scalingConfig
      value: '{{ scalingConfig }}'
    - name: scheduledBackup
      value: '{{ scheduledBackup }}'
    - name: deletionProtection
      value: '{{ deletionProtection }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE google.metastore.services
SET 
hiveMetastoreConfig = '{{ hiveMetastoreConfig }}',
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
network = '{{ network }}',
endpointUri = '{{ endpointUri }}',
port = '{{ port }}',
state = '{{ state }}',
stateMessage = '{{ stateMessage }}',
artifactGcsUri = '{{ artifactGcsUri }}',
tier = '{{ tier }}',
metadataIntegration = '{{ metadataIntegration }}',
maintenanceWindow = '{{ maintenanceWindow }}',
uid = '{{ uid }}',
metadataManagementActivity = '{{ metadataManagementActivity }}',
releaseChannel = '{{ releaseChannel }}',
encryptionConfig = '{{ encryptionConfig }}',
networkConfig = '{{ networkConfig }}',
databaseType = '{{ databaseType }}',
telemetryConfig = '{{ telemetryConfig }}',
scalingConfig = '{{ scalingConfig }}',
scheduledBackup = '{{ scheduledBackup }}',
deletionProtection = true|false
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM google.metastore.services
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
