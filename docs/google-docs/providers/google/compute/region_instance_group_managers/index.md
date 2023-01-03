---
title: region_instance_group_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_group_managers
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_instance_group_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_instance_group_managers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] A unique identifier for this resource type. The server generates this identifier. |
| `name` | `string` | The name of the managed instance group. The name must be 1-63 characters long, and comply with RFC1035. |
| `description` | `string` | An optional description of this resource. |
| `distributionPolicy` | `object` |  |
| `fingerprint` | `string` | Fingerprint of this resource. This field may be used in optimistic locking. It will be ignored when inserting an InstanceGroupManager. An up-to-date fingerprint must be provided in order to update the InstanceGroupManager, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve an InstanceGroupManager. |
| `namedPorts` | `array` | Named ports configured for the Instance Groups complementary to this Instance Group Manager. |
| `region` | `string` | [Output Only] The URL of the region where the managed instance group resides (for regional resources). |
| `statefulPolicy` | `object` |  |
| `updatePolicy` | `object` |  |
| `kind` | `string` | [Output Only] The resource type, which is always compute#instanceGroupManager for managed instance groups. |
| `autoHealingPolicies` | `array` | The autohealing policy for this managed instance group. You can specify only one value. |
| `versions` | `array` | Specifies the instance templates used by this managed instance group to create instances. Each version is defined by an instanceTemplate and a name. Every version can appear at most once per instance group. This field overrides the top-level instanceTemplate field. Read more about the relationships between these fields. Exactly one version must leave the targetSize field unset. That version will be applied to all remaining instances. For more information, read about canary updates. |
| `currentActions` | `object` |  |
| `selfLink` | `string` | [Output Only] The URL for this managed instance group. The server defines this URL. |
| `instanceTemplate` | `string` | The URL of the instance template that is specified for this managed instance group. The group uses this template to create all new instances in the managed instance group. The templates for existing instances in the group do not change unless you run recreateInstances, run applyUpdatesToInstances, or set the group's updatePolicy.type to PROACTIVE. |
| `creationTimestamp` | `string` | [Output Only] The creation timestamp for this managed instance group in RFC3339 text format. |
| `status` | `object` |  |
| `zone` | `string` | [Output Only] The URL of a zone where the managed instance group is located (for zonal resources). |
| `targetSize` | `integer` | The target number of running instances for this managed instance group. You can reduce this number by using the instanceGroupManager deleteInstances or abandonInstances methods. Resizing the group also changes this number. |
| `targetPools` | `array` | The URLs for all TargetPool resources to which instances in the instanceGroup field are added. The target pools automatically apply to all of the instances in the managed instance group. |
| `baseInstanceName` | `string` | The base instance name to use for instances in this group. The value must be 1-58 characters long. Instances are named by appending a hyphen and a random four-character string to the base instance name. The base instance name must comply with RFC1035. |
| `instanceGroup` | `string` | [Output Only] The URL of the Instance Group resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionInstanceGroupManagers_get` | `SELECT` | `instanceGroupManager, project, region` | Returns all of the details about the specified managed instance group. |
| `regionInstanceGroupManagers_list` | `SELECT` | `project, region` | Retrieves the list of managed instance groups that are contained within the specified region. |
| `regionInstanceGroupManagers_insert` | `INSERT` | `project, region` | Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with the listmanagedinstances method. A regional managed instance group can contain up to 2000 instances. |
| `regionInstanceGroupManagers_delete` | `DELETE` | `instanceGroupManager, project, region` | Deletes the specified managed instance group and all of the instances in that group. |
| `regionInstanceGroupManagers_abandonInstances` | `EXEC` | `instanceGroupManager, project, region` | Flags the specified instances to be immediately removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces the targetSize of the managed instance group by the number of instances that you abandon. This operation is marked as DONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with the listmanagedinstances method. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| `regionInstanceGroupManagers_applyUpdatesToInstances` | `EXEC` | `instanceGroupManager, project, region` | Apply updates to selected instances the managed instance group. |
| `regionInstanceGroupManagers_patch` | `EXEC` | `instanceGroupManager, project, region` | Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listmanagedinstances method. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, see Updating instances in a MIG. |
| `regionInstanceGroupManagers_patchPerInstanceConfigs` | `EXEC` | `instanceGroupManager, project, region` | Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |
| `regionInstanceGroupManagers_recreateInstances` | `EXEC` | `instanceGroupManager, project, region` | Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking its currentAction field; for more information, see Checking the status of managed instances. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| `regionInstanceGroupManagers_resize` | `EXEC` | `instanceGroupManager, project, region, size` | Changes the intended size of the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes one or more instances. The resize operation is marked DONE if the resize request is successful. The underlying actions take additional time. You must separately verify the status of the creating or deleting actions with the listmanagedinstances method. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. |
| `regionInstanceGroupManagers_setInstanceTemplate` | `EXEC` | `instanceGroupManager, project, region` | Sets the instance template to use when creating new instances or recreating instances in this group. Existing instances are not affected. |
| `regionInstanceGroupManagers_setTargetPools` | `EXEC` | `instanceGroupManager, project, region` | Modifies the target pools to which all new instances in this group are assigned. Existing instances in the group are not affected. |
| `regionInstanceGroupManagers_updatePerInstanceConfigs` | `EXEC` | `instanceGroupManager, project, region` | Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |
