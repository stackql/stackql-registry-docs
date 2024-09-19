---
title: instance_partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_partitions
  - spanner
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

Creates, updates, deletes, gets or lists a <code>instance_partitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.instance_partitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. A unique identifier for the instance partition. Values are of the form `projects//instances//instancePartitions/a-z*[a-z0-9]`. The final segment of the name must be between 2 and 64 characters in length. An instance partition's name cannot be changed after the instance partition is created. |
| <CopyableCode code="config" /> | `string` | Required. The name of the instance partition's configuration. Values are of the form `projects//instanceConfigs/`. See also InstanceConfig and ListInstanceConfigs. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the instance partition was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The descriptive name for this instance partition as it appears in UIs. Must be unique per project and between 4 and 30 characters in length. |
| <CopyableCode code="etag" /> | `string` | Used for optimistic concurrency control as a way to help prevent simultaneous updates of a instance partition from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform instance partition updates in order to avoid race conditions: An etag is returned in the response which contains instance partitions, and systems are expected to put that etag in the request to update instance partitions to ensure that their change will be applied to the same version of the instance partition. If no etag is provided in the call to update instance partition, then the existing instance partition is overwritten blindly. |
| <CopyableCode code="nodeCount" /> | `integer` | The number of nodes allocated to this instance partition. Users can set the `node_count` field to specify the target number of nodes allocated to the instance partition. This may be zero in API responses for instance partitions that are not yet in state `READY`. |
| <CopyableCode code="processingUnits" /> | `integer` | The number of processing units allocated to this instance partition. Users can set the `processing_units` field to specify the target number of processing units allocated to the instance partition. This might be zero in API responses for instance partitions that are not yet in the `READY` state. |
| <CopyableCode code="referencingBackups" /> | `array` | Output only. Deprecated: This field is not populated. Output only. The names of the backups that reference this instance partition. Referencing backups should share the parent instance. The existence of any referencing backup prevents the instance partition from being deleted. |
| <CopyableCode code="referencingDatabases" /> | `array` | Output only. The names of the databases that reference this instance partition. Referencing databases should share the parent instance. The existence of any referencing database prevents the instance partition from being deleted. |
| <CopyableCode code="state" /> | `string` | Output only. The current instance partition state. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which the instance partition was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_instance_partitions_get" /> | `SELECT` | <CopyableCode code="instancePartitionsId, instancesId, projectsId" /> | Gets information about a particular instance partition. |
| <CopyableCode code="projects_instances_instance_partitions_list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Lists all instance partitions for the given instance. |
| <CopyableCode code="projects_instances_instance_partitions_create" /> | `INSERT` | <CopyableCode code="instancesId, projectsId" /> | Creates an instance partition and begins preparing it to be used. The returned long-running operation can be used to track the progress of preparing the new instance partition. The instance partition name is assigned by the caller. If the named instance partition already exists, `CreateInstancePartition` returns `ALREADY_EXISTS`. Immediately upon completion of this request: * The instance partition is readable via the API, with all requested attributes but no allocated resources. Its state is `CREATING`. Until completion of the returned operation: * Cancelling the operation renders the instance partition immediately unreadable via the API. * The instance partition can be deleted. * All other attempts to modify the instance partition are rejected. Upon completion of the returned operation: * Billing for all successfully-allocated resources begins (some types may have lower than the requested levels). * Databases can start using this instance partition. * The instance partition's allocated resource levels are readable via the API. * The instance partition's state becomes `READY`. The returned long-running operation will have a name of the format `/operations/` and can be used to track creation of the instance partition. The metadata field type is CreateInstancePartitionMetadata. The response field type is InstancePartition, if successful. |
| <CopyableCode code="projects_instances_instance_partitions_delete" /> | `DELETE` | <CopyableCode code="instancePartitionsId, instancesId, projectsId" /> | Deletes an existing instance partition. Requires that the instance partition is not used by any database or backup and is not the default instance partition of an instance. Authorization requires `spanner.instancePartitions.delete` permission on the resource name. |
| <CopyableCode code="projects_instances_instance_partitions_patch" /> | `UPDATE` | <CopyableCode code="instancePartitionsId, instancesId, projectsId" /> | Updates an instance partition, and begins allocating or releasing resources as requested. The returned long-running operation can be used to track the progress of updating the instance partition. If the named instance partition does not exist, returns `NOT_FOUND`. Immediately upon completion of this request: * For resource types for which a decrease in the instance partition's allocation has been requested, billing is based on the newly-requested level. Until completion of the returned operation: * Cancelling the operation sets its metadata's cancel_time, and begins restoring resources to their pre-request values. The operation is guaranteed to succeed at undoing all resource changes, after which point it terminates with a `CANCELLED` status. * All other attempts to modify the instance partition are rejected. * Reading the instance partition via the API continues to give the pre-request resource levels. Upon completion of the returned operation: * Billing begins for all successfully-allocated resources (some types may have lower than the requested levels). * All newly-reserved resources are available for serving the instance partition's tables. * The instance partition's new resource levels are readable via the API. The returned long-running operation will have a name of the format `/operations/` and can be used to track the instance partition modification. The metadata field type is UpdateInstancePartitionMetadata. The response field type is InstancePartition, if successful. Authorization requires `spanner.instancePartitions.update` permission on the resource name. |

## `SELECT` examples

Lists all instance partitions for the given instance.

```sql
SELECT
name,
config,
createTime,
displayName,
etag,
nodeCount,
processingUnits,
referencingBackups,
referencingDatabases,
state,
updateTime
FROM google.spanner.instance_partitions
WHERE instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_partitions</code> resource.

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
INSERT INTO google.spanner.instance_partitions (
instancesId,
projectsId,
instancePartitionId,
instancePartition
)
SELECT 
'{{ instancesId }}',
'{{ projectsId }}',
'{{ instancePartitionId }}',
'{{ instancePartition }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: instancePartitionId
      value: string
    - name: instancePartition
      value:
        - name: name
          value: string
        - name: config
          value: string
        - name: displayName
          value: string
        - name: nodeCount
          value: integer
        - name: processingUnits
          value: integer
        - name: state
          value: string
        - name: createTime
          value: string
        - name: updateTime
          value: string
        - name: referencingDatabases
          value:
            - string
        - name: referencingBackups
          value:
            - string
        - name: etag
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instance_partitions</code> resource.

```sql
/*+ update */
UPDATE google.spanner.instance_partitions
SET 
instancePartition = '{{ instancePartition }}',
fieldMask = '{{ fieldMask }}'
WHERE 
instancePartitionsId = '{{ instancePartitionsId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>instance_partitions</code> resource.

```sql
/*+ delete */
DELETE FROM google.spanner.instance_partitions
WHERE instancePartitionsId = '{{ instancePartitionsId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
