---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
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

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. A unique identifier for the instance, which cannot be changed after the instance is created. Values are of the form `projects//instances/a-z*[a-z0-9]`. The final segment of the name must be between 2 and 64 characters in length. |
| <CopyableCode code="autoscalingConfig" /> | `object` | Autoscaling configuration for an instance. |
| <CopyableCode code="config" /> | `string` | Required. The name of the instance's configuration. Values are of the form `projects//instanceConfigs/`. See also InstanceConfig and ListInstanceConfigs. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the instance was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The descriptive name for this instance as it appears in UIs. Must be unique per project and between 4 and 30 characters in length. |
| <CopyableCode code="edition" /> | `string` | Optional. The `Edition` of the current instance. |
| <CopyableCode code="endpointUris" /> | `array` | Deprecated. This field is not populated. |
| <CopyableCode code="freeInstanceMetadata" /> | `object` | Free instance specific metadata that is kept even after an instance has been upgraded for tracking purposes. |
| <CopyableCode code="instanceType" /> | `string` | The `InstanceType` of the current instance. |
| <CopyableCode code="labels" /> | `object` | Cloud Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. Cloud Labels can be used to filter collections of resources. They can be used to control how resource metrics are aggregated. And they can be used as arguments to policy management rules (e.g. route, firewall, load balancing, etc.). * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `a-z{0,62}`. * Label values must be between 0 and 63 characters long and must conform to the regular expression `[a-z0-9_-]{0,63}`. * No more than 64 labels can be associated with a given resource. See https://goo.gl/xmQnxf for more information on and examples of labels. If you plan to use labels in your own code, please note that additional characters may be allowed in the future. And so you are advised to use an internal label representation, such as JSON, which doesn't rely upon specific characters being disallowed. For example, representing labels as the string: name + "_" + value would prove problematic if we were to allow "_" in a future release. |
| <CopyableCode code="nodeCount" /> | `integer` | The number of nodes allocated to this instance. At most, one of either `node_count` or `processing_units` should be present in the message. Users can set the `node_count` field to specify the target number of nodes allocated to the instance. If autoscaling is enabled, `node_count` is treated as an `OUTPUT_ONLY` field and reflects the current number of nodes allocated to the instance. This might be zero in API responses for instances that are not yet in the `READY` state. For more information, see [Compute capacity, nodes, and processing units](https://cloud.google.com/spanner/docs/compute-capacity). |
| <CopyableCode code="processingUnits" /> | `integer` | The number of processing units allocated to this instance. At most, one of either `processing_units` or `node_count` should be present in the message. Users can set the `processing_units` field to specify the target number of processing units allocated to the instance. If autoscaling is enabled, `processing_units` is treated as an `OUTPUT_ONLY` field and reflects the current number of processing units allocated to the instance. This might be zero in API responses for instances that are not yet in the `READY` state. For more information, see [Compute capacity, nodes and processing units](https://cloud.google.com/spanner/docs/compute-capacity). |
| <CopyableCode code="state" /> | `string` | Output only. The current instance state. For CreateInstance, the state must be either omitted or set to `CREATING`. For UpdateInstance, the state must be either omitted or set to `READY`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which the instance was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_get" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Gets information about a particular instance. |
| <CopyableCode code="projects_instances_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all instances in the given project. |
| <CopyableCode code="projects_instances_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an instance and begins preparing it to begin serving. The returned long-running operation can be used to track the progress of preparing the new instance. The instance name is assigned by the caller. If the named instance already exists, `CreateInstance` returns `ALREADY_EXISTS`. Immediately upon completion of this request: * The instance is readable via the API, with all requested attributes but no allocated resources. Its state is `CREATING`. Until completion of the returned operation: * Cancelling the operation renders the instance immediately unreadable via the API. * The instance can be deleted. * All other attempts to modify the instance are rejected. Upon completion of the returned operation: * Billing for all successfully-allocated resources begins (some types may have lower than the requested levels). * Databases can be created in the instance. * The instance's allocated resource levels are readable via the API. * The instance's state becomes `READY`. The returned long-running operation will have a name of the format `/operations/` and can be used to track creation of the instance. The metadata field type is CreateInstanceMetadata. The response field type is Instance, if successful. |
| <CopyableCode code="projects_instances_delete" /> | `DELETE` | <CopyableCode code="instancesId, projectsId" /> | Deletes an instance. Immediately upon completion of the request: * Billing ceases for all of the instance's reserved resources. Soon afterward: * The instance and *all of its databases* immediately and irrevocably disappear from the API. All data in the databases is permanently deleted. |
| <CopyableCode code="projects_instances_patch" /> | `UPDATE` | <CopyableCode code="instancesId, projectsId" /> | Updates an instance, and begins allocating or releasing resources as requested. The returned long-running operation can be used to track the progress of updating the instance. If the named instance does not exist, returns `NOT_FOUND`. Immediately upon completion of this request: * For resource types for which a decrease in the instance's allocation has been requested, billing is based on the newly-requested level. Until completion of the returned operation: * Cancelling the operation sets its metadata's cancel_time, and begins restoring resources to their pre-request values. The operation is guaranteed to succeed at undoing all resource changes, after which point it terminates with a `CANCELLED` status. * All other attempts to modify the instance are rejected. * Reading the instance via the API continues to give the pre-request resource levels. Upon completion of the returned operation: * Billing begins for all successfully-allocated resources (some types may have lower than the requested levels). * All newly-reserved resources are available for serving the instance's tables. * The instance's new resource levels are readable via the API. The returned long-running operation will have a name of the format `/operations/` and can be used to track the instance modification. The metadata field type is UpdateInstanceMetadata. The response field type is Instance, if successful. Authorization requires `spanner.instances.update` permission on the resource name. |
| <CopyableCode code="projects_instances_move" /> | `EXEC` | <CopyableCode code="instancesId, projectsId" /> | Moves an instance to the target instance configuration. You can use the returned long-running operation to track the progress of moving the instance. `MoveInstance` returns `FAILED_PRECONDITION` if the instance meets any of the following criteria: * Is undergoing a move to a different instance configuration * Has backups * Has an ongoing update * Contains any CMEK-enabled databases * Is a free trial instance While the operation is pending: * All other attempts to modify the instance, including changes to its compute capacity, are rejected. * The following database and backup admin operations are rejected: * `DatabaseAdmin.CreateDatabase` * `DatabaseAdmin.UpdateDatabaseDdl` (disabled if default_leader is specified in the request.) * `DatabaseAdmin.RestoreDatabase` * `DatabaseAdmin.CreateBackup` * `DatabaseAdmin.CopyBackup` * Both the source and target instance configurations are subject to hourly compute and storage charges. * The instance might experience higher read-write latencies and a higher transaction abort rate. However, moving an instance doesn't cause any downtime. The returned long-running operation has a name of the format `/operations/` and can be used to track the move instance operation. The metadata field type is MoveInstanceMetadata. The response field type is Instance, if successful. Cancelling the operation sets its metadata's cancel_time. Cancellation is not immediate because it involves moving any data previously moved to the target instance configuration back to the original instance configuration. You can use this operation to track the progress of the cancellation. Upon successful completion of the cancellation, the operation terminates with `CANCELLED` status. If not cancelled, upon completion of the returned operation: * The instance successfully moves to the target instance configuration. * You are billed for compute and storage in target instance configuration. Authorization requires the `spanner.instances.update` permission on the resource instance. For more details, see [Move an instance](https://cloud.google.com/spanner/docs/move-instance). |

## `SELECT` examples

Lists all instances in the given project.

```sql
SELECT
name,
autoscalingConfig,
config,
createTime,
displayName,
edition,
endpointUris,
freeInstanceMetadata,
instanceType,
labels,
nodeCount,
processingUnits,
state,
updateTime
FROM google.spanner.instances
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

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
INSERT INTO google.spanner.instances (
projectsId,
instanceId,
instance
)
SELECT 
'{{ projectsId }}',
'{{ instanceId }}',
'{{ instance }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: instanceId
      value: string
    - name: instance
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
        - name: autoscalingConfig
          value:
            - name: autoscalingLimits
              value:
                - name: minNodes
                  value: integer
                - name: minProcessingUnits
                  value: integer
                - name: maxNodes
                  value: integer
                - name: maxProcessingUnits
                  value: integer
            - name: autoscalingTargets
              value:
                - name: highPriorityCpuUtilizationPercent
                  value: integer
                - name: storageUtilizationPercent
                  value: integer
        - name: state
          value: string
        - name: labels
          value: object
        - name: instanceType
          value: string
        - name: endpointUris
          value:
            - string
        - name: createTime
          value: string
        - name: updateTime
          value: string
        - name: freeInstanceMetadata
          value:
            - name: expireTime
              value: string
            - name: upgradeTime
              value: string
            - name: expireBehavior
              value: string
        - name: edition
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instances</code> resource.

```sql
/*+ update */
UPDATE google.spanner.instances
SET 
instance = '{{ instance }}',
fieldMask = '{{ fieldMask }}'
WHERE 
instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.spanner.instances
WHERE instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```
