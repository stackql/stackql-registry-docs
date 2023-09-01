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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.instance_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A unique identifier for the instance configuration. Values are of the form `projects//instanceConfigs/a-z*`. |
| `state` | `string` | Output only. The current instance config state. Applicable only for USER_MANAGED configs. |
| `configType` | `string` | Output only. Whether this instance config is a Google or User Managed Configuration. |
| `reconciling` | `boolean` | Output only. If true, the instance config is being created or updated. If false, there are no ongoing operations for the instance config. |
| `labels` | `object` | Cloud Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. Cloud Labels can be used to filter collections of resources. They can be used to control how resource metrics are aggregated. And they can be used as arguments to policy management rules (e.g. route, firewall, load balancing, etc.). * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `a-z&#123;0,62&#125;`. * Label values must be between 0 and 63 characters long and must conform to the regular expression `[a-z0-9_-]&#123;0,63&#125;`. * No more than 64 labels can be associated with a given resource. See https://goo.gl/xmQnxf for more information on and examples of labels. If you plan to use labels in your own code, please note that additional characters may be allowed in the future. Therefore, you are advised to use an internal label representation, such as JSON, which doesn't rely upon specific characters being disallowed. For example, representing labels as the string: name + "_" + value would prove problematic if we were to allow "_" in a future release. |
| `leaderOptions` | `array` | Allowed values of the "default_leader" schema option for databases in instances that use this instance configuration. |
| `optionalReplicas` | `array` | Output only. The available optional replicas to choose from for user managed configurations. Populated for Google managed configurations. |
| `replicas` | `array` | The geographic placement of nodes in this instance configuration and their replication properties. |
| `baseConfig` | `string` | Base configuration name, e.g. projects//instanceConfigs/nam3, based on which this configuration is created. Only set for user managed configurations. `base_config` must refer to a configuration of type GOOGLE_MANAGED in the same project as this configuration. |
| `etag` | `string` | etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a instance config from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform instance config updates in order to avoid race conditions: An etag is returned in the response which contains instance configs, and systems are expected to put that etag in the request to update instance config to ensure that their change will be applied to the same version of the instance config. If no etag is provided in the call to update instance config, then the existing instance config is overwritten blindly. |
| `freeInstanceAvailability` | `string` | Output only. Describes whether free instances are available to be created in this instance config. |
| `displayName` | `string` | The name of this instance configuration as it appears in UIs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instance_configs_get` | `SELECT` | `instanceConfigsId, projectsId` | Gets information about a particular instance configuration. |
| `projects_instance_configs_list` | `SELECT` | `projectsId` | Lists the supported instance configurations for a given project. |
| `projects_instance_configs_create` | `INSERT` | `projectsId` | Creates an instance config and begins preparing it to be used. The returned long-running operation can be used to track the progress of preparing the new instance config. The instance config name is assigned by the caller. If the named instance config already exists, `CreateInstanceConfig` returns `ALREADY_EXISTS`. Immediately after the request returns: * The instance config is readable via the API, with all requested attributes. The instance config's reconciling field is set to true. Its state is `CREATING`. While the operation is pending: * Cancelling the operation renders the instance config immediately unreadable via the API. * Except for deleting the creating resource, all other attempts to modify the instance config are rejected. Upon completion of the returned operation: * Instances can be created using the instance configuration. * The instance config's reconciling field becomes false. Its state becomes `READY`. The returned long-running operation will have a name of the format `/operations/` and can be used to track creation of the instance config. The metadata field type is CreateInstanceConfigMetadata. The response field type is InstanceConfig, if successful. Authorization requires `spanner.instanceConfigs.create` permission on the resource parent. |
| `projects_instance_configs_delete` | `DELETE` | `instanceConfigsId, projectsId` | Deletes the instance config. Deletion is only allowed when no instances are using the configuration. If any instances are using the config, returns `FAILED_PRECONDITION`. Only user managed configurations can be deleted. Authorization requires `spanner.instanceConfigs.delete` permission on the resource name. |
| `_projects_instance_configs_list` | `EXEC` | `projectsId` | Lists the supported instance configurations for a given project. |
| `projects_instance_configs_patch` | `EXEC` | `instanceConfigsId, projectsId` | Updates an instance config. The returned long-running operation can be used to track the progress of updating the instance. If the named instance config does not exist, returns `NOT_FOUND`. Only user managed configurations can be updated. Immediately after the request returns: * The instance config's reconciling field is set to true. While the operation is pending: * Cancelling the operation sets its metadata's cancel_time. The operation is guaranteed to succeed at undoing all changes, after which point it terminates with a `CANCELLED` status. * All other attempts to modify the instance config are rejected. * Reading the instance config via the API continues to give the pre-request values. Upon completion of the returned operation: * Creating instances using the instance configuration uses the new values. * The instance config's new values are readable via the API. * The instance config's reconciling field becomes false. The returned long-running operation will have a name of the format `/operations/` and can be used to track the instance config modification. The metadata field type is UpdateInstanceConfigMetadata. The response field type is InstanceConfig, if successful. Authorization requires `spanner.instanceConfigs.update` permission on the resource name. |
