---
title: instance_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_configs
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

Creates, updates, deletes, gets or lists a <code>instance_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.instance_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A unique identifier for the instance configuration. Values are of the form `projects//instanceConfigs/a-z*`. User instance configuration must start with `custom-`. |
| <CopyableCode code="baseConfig" /> | `string` | Base configuration name, e.g. projects//instanceConfigs/nam3, based on which this configuration is created. Only set for user-managed configurations. `base_config` must refer to a configuration of type `GOOGLE_MANAGED` in the same project as this configuration. |
| <CopyableCode code="configType" /> | `string` | Output only. Whether this instance configuration is a Google-managed or user-managed configuration. |
| <CopyableCode code="displayName" /> | `string` | The name of this instance configuration as it appears in UIs. |
| <CopyableCode code="etag" /> | `string` | etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a instance configuration from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform instance configuration updates in order to avoid race conditions: An etag is returned in the response which contains instance configurations, and systems are expected to put that etag in the request to update instance configuration to ensure that their change is applied to the same version of the instance configuration. If no etag is provided in the call to update the instance configuration, then the existing instance configuration is overwritten blindly. |
| <CopyableCode code="freeInstanceAvailability" /> | `string` | Output only. Describes whether free instances are available to be created in this instance configuration. |
| <CopyableCode code="labels" /> | `object` | Cloud Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. Cloud Labels can be used to filter collections of resources. They can be used to control how resource metrics are aggregated. And they can be used as arguments to policy management rules (e.g. route, firewall, load balancing, etc.). * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `a-z{0,62}`. * Label values must be between 0 and 63 characters long and must conform to the regular expression `[a-z0-9_-]{0,63}`. * No more than 64 labels can be associated with a given resource. See https://goo.gl/xmQnxf for more information on and examples of labels. If you plan to use labels in your own code, please note that additional characters may be allowed in the future. Therefore, you are advised to use an internal label representation, such as JSON, which doesn't rely upon specific characters being disallowed. For example, representing labels as the string: name + "_" + value would prove problematic if we were to allow "_" in a future release. |
| <CopyableCode code="leaderOptions" /> | `array` | Allowed values of the "default_leader" schema option for databases in instances that use this instance configuration. |
| <CopyableCode code="optionalReplicas" /> | `array` | Output only. The available optional replicas to choose from for user-managed configurations. Populated for Google-managed configurations. |
| <CopyableCode code="quorumType" /> | `string` | Output only. The `QuorumType` of the instance configuration. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. If true, the instance configuration is being created or updated. If false, there are no ongoing operations for the instance configuration. |
| <CopyableCode code="replicas" /> | `array` | The geographic placement of nodes in this instance configuration and their replication properties. To create user-managed configurations, input `replicas` must include all replicas in `replicas` of the `base_config` and include one or more replicas in the `optional_replicas` of the `base_config`. |
| <CopyableCode code="state" /> | `string` | Output only. The current instance configuration state. Applicable only for `USER_MANAGED` configurations. |
| <CopyableCode code="storageLimitPerProcessingUnit" /> | `string` | Output only. The storage limit in bytes per processing unit. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instance_configs_get" /> | `SELECT` | <CopyableCode code="instanceConfigsId, projectsId" /> | Gets information about a particular instance configuration. |
| <CopyableCode code="projects_instance_configs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the supported instance configurations for a given project. Returns both Google-managed configurations and user-managed configurations. |
| <CopyableCode code="projects_instance_configs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an instance configuration and begins preparing it to be used. The returned long-running operation can be used to track the progress of preparing the new instance configuration. The instance configuration name is assigned by the caller. If the named instance configuration already exists, `CreateInstanceConfig` returns `ALREADY_EXISTS`. Immediately after the request returns: * The instance configuration is readable via the API, with all requested attributes. The instance configuration's reconciling field is set to true. Its state is `CREATING`. While the operation is pending: * Cancelling the operation renders the instance configuration immediately unreadable via the API. * Except for deleting the creating resource, all other attempts to modify the instance configuration are rejected. Upon completion of the returned operation: * Instances can be created using the instance configuration. * The instance configuration's reconciling field becomes false. Its state becomes `READY`. The returned long-running operation will have a name of the format `/operations/` and can be used to track creation of the instance configuration. The metadata field type is CreateInstanceConfigMetadata. The response field type is InstanceConfig, if successful. Authorization requires `spanner.instanceConfigs.create` permission on the resource parent. |
| <CopyableCode code="projects_instance_configs_delete" /> | `DELETE` | <CopyableCode code="instanceConfigsId, projectsId" /> | Deletes the instance configuration. Deletion is only allowed when no instances are using the configuration. If any instances are using the configuration, returns `FAILED_PRECONDITION`. Only user-managed configurations can be deleted. Authorization requires `spanner.instanceConfigs.delete` permission on the resource name. |
| <CopyableCode code="projects_instance_configs_patch" /> | `UPDATE` | <CopyableCode code="instanceConfigsId, projectsId" /> | Updates an instance configuration. The returned long-running operation can be used to track the progress of updating the instance. If the named instance configuration does not exist, returns `NOT_FOUND`. Only user-managed configurations can be updated. Immediately after the request returns: * The instance configuration's reconciling field is set to true. While the operation is pending: * Cancelling the operation sets its metadata's cancel_time. The operation is guaranteed to succeed at undoing all changes, after which point it terminates with a `CANCELLED` status. * All other attempts to modify the instance configuration are rejected. * Reading the instance configuration via the API continues to give the pre-request values. Upon completion of the returned operation: * Creating instances using the instance configuration uses the new values. * The new values of the instance configuration are readable via the API. * The instance configuration's reconciling field becomes false. The returned long-running operation will have a name of the format `/operations/` and can be used to track the instance configuration modification. The metadata field type is UpdateInstanceConfigMetadata. The response field type is InstanceConfig, if successful. Authorization requires `spanner.instanceConfigs.update` permission on the resource name. |

## `SELECT` examples

Lists the supported instance configurations for a given project. Returns both Google-managed configurations and user-managed configurations.

```sql
SELECT
name,
baseConfig,
configType,
displayName,
etag,
freeInstanceAvailability,
labels,
leaderOptions,
optionalReplicas,
quorumType,
reconciling,
replicas,
state,
storageLimitPerProcessingUnit
FROM google.spanner.instance_configs
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_configs</code> resource.

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
INSERT INTO google.spanner.instance_configs (
projectsId,
instanceConfigId,
instanceConfig,
validateOnly
)
SELECT 
'{{ projectsId }}',
'{{ instanceConfigId }}',
'{{ instanceConfig }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: instanceConfigId
      value: '{{ instanceConfigId }}'
    - name: instanceConfig
      value: '{{ instanceConfig }}'
    - name: validateOnly
      value: '{{ validateOnly }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instance_configs</code> resource.

```sql
/*+ update */
UPDATE google.spanner.instance_configs
SET 
instanceConfig = '{{ instanceConfig }}',
updateMask = '{{ updateMask }}',
validateOnly = true|false
WHERE 
instanceConfigsId = '{{ instanceConfigsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>instance_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.spanner.instance_configs
WHERE instanceConfigsId = '{{ instanceConfigsId }}'
AND projectsId = '{{ projectsId }}';
```
