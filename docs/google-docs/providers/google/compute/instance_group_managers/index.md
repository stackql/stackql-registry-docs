
---
title: instance_group_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_managers
  - compute
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

Creates, updates, deletes or gets an <code>instance_group_manager</code> resource or lists <code>instance_group_managers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_group_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instance_group_managers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] A unique identifier for this resource type. The server generates this identifier. |
| <CopyableCode code="name" /> | `string` | The name of the managed instance group. The name must be 1-63 characters long, and comply with RFC1035. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. |
| <CopyableCode code="allInstancesConfig" /> | `object` |  |
| <CopyableCode code="autoHealingPolicies" /> | `array` | The autohealing policy for this managed instance group. You can specify only one value. |
| <CopyableCode code="baseInstanceName" /> | `string` | The base instance name is a prefix that you want to attach to the names of all VMs in a MIG. The maximum character length is 58 and the name must comply with RFC1035 format. When a VM is created in the group, the MIG appends a hyphen and a random four-character string to the base instance name. If you want the MIG to assign sequential numbers instead of a random string, then end the base instance name with a hyphen followed by one or more hash symbols. The hash symbols indicate the number of digits. For example, a base instance name of "vm-###" results in "vm-001" as a VM name. @pattern [a-z](([-a-z0-9]{0,57})|([-a-z0-9]{0,51}-#{1,10}(\\[[0-9]{1,10}\\])?)) |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] The creation timestamp for this managed instance group in RFC3339 text format. |
| <CopyableCode code="currentActions" /> | `object` |  |
| <CopyableCode code="distributionPolicy" /> | `object` |  |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. This field may be used in optimistic locking. It will be ignored when inserting an InstanceGroupManager. An up-to-date fingerprint must be provided in order to update the InstanceGroupManager, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve an InstanceGroupManager. |
| <CopyableCode code="instanceGroup" /> | `string` | [Output Only] The URL of the Instance Group resource. |
| <CopyableCode code="instanceLifecyclePolicy" /> | `object` |  |
| <CopyableCode code="instanceTemplate" /> | `string` | The URL of the instance template that is specified for this managed instance group. The group uses this template to create all new instances in the managed instance group. The templates for existing instances in the group do not change unless you run recreateInstances, run applyUpdatesToInstances, or set the group's updatePolicy.type to PROACTIVE. |
| <CopyableCode code="kind" /> | `string` | [Output Only] The resource type, which is always compute#instanceGroupManager for managed instance groups. |
| <CopyableCode code="listManagedInstancesResults" /> | `string` | Pagination behavior of the listManagedInstances API method for this managed instance group. |
| <CopyableCode code="namedPorts" /> | `array` | Named ports configured for the Instance Groups complementary to this Instance Group Manager. |
| <CopyableCode code="region" /> | `string` | [Output Only] The URL of the region where the managed instance group resides (for regional resources). |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | [Output Only] Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | [Output Only] Reserved for future use. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] The URL for this managed instance group. The server defines this URL. |
| <CopyableCode code="statefulPolicy" /> | `object` |  |
| <CopyableCode code="status" /> | `object` |  |
| <CopyableCode code="targetPools" /> | `array` | The URLs for all TargetPool resources to which instances in the instanceGroup field are added. The target pools automatically apply to all of the instances in the managed instance group. |
| <CopyableCode code="targetSize" /> | `integer` | The target number of running instances for this managed instance group. You can reduce this number by using the instanceGroupManager deleteInstances or abandonInstances methods. Resizing the group also changes this number. |
| <CopyableCode code="updatePolicy" /> | `object` |  |
| <CopyableCode code="versions" /> | `array` | Specifies the instance templates used by this managed instance group to create instances. Each version is defined by an instanceTemplate and a name. Every version can appear at most once per instance group. This field overrides the top-level instanceTemplate field. Read more about the relationships between these fields. Exactly one version must leave the targetSize field unset. That version will be applied to all remaining instances. For more information, read about canary updates. |
| <CopyableCode code="zone" /> | `string` | [Output Only] The URL of a zone where the managed instance group is located (for zonal resources). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of managed instance groups and groups them by zone. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceGroupManager, project, zone" /> | Returns all of the details about the specified managed instance group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | Retrieves a list of managed instance groups that are contained within the specified project and zone. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, zone" /> | Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with the listmanagedinstances method. A managed instance group can have up to 1000 VM instances per group. Please contact Cloud Support if you need an increase in this limit. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceGroupManager, project, zone" /> | Deletes the specified managed instance group and all of the instances in that group. Note that the instance group must not belong to a backend service. Read Deleting an instance group for more information. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instanceGroupManager, project, zone" /> | Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listManagedInstances method. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, see Updating instances in a MIG. |
| <CopyableCode code="patch_per_instance_configs" /> | `UPDATE` | <CopyableCode code="instanceGroupManager, project, zone" /> | Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |
| <CopyableCode code="abandon_instances" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, zone" /> | Flags the specified instances to be removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces the targetSize of the managed instance group by the number of instances that you abandon. This operation is marked as DONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with the listmanagedinstances method. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| <CopyableCode code="apply_updates_to_instances" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, zone" /> | Applies changes to selected instances on the managed instance group. This method can be used to apply new overrides and/or new versions. |
| <CopyableCode code="recreate_instances" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, zone" /> | Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking its currentAction field; for more information, see Checking the status of managed instances. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, size, zone" /> | Resizes the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes instances. The resize operation is marked DONE when the resize actions are scheduled even if the group has not yet added or deleted any instances. You must separately verify the status of the creating or deleting actions with the listmanagedinstances method. When resizing down, the instance group arbitrarily chooses the order in which VMs are deleted. The group takes into account some VM attributes when making the selection including: + The status of the VM instance. + The health of the VM instance. + The instance template version the VM is based on. + For regional managed instance groups, the location of the VM instance. This list is subject to change. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. |
| <CopyableCode code="set_instance_template" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, zone" /> | Specifies the instance template to use when creating new instances in this group. The templates for existing instances in the group do not change unless you run recreateInstances, run applyUpdatesToInstances, or set the group's updatePolicy.type to PROACTIVE. |
| <CopyableCode code="set_target_pools" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, zone" /> | Modifies the target pools to which all instances in this managed instance group are assigned. The target pools automatically apply to all of the instances in the managed instance group. This operation is marked DONE when you make the request even if the instances have not yet been added to their target pools. The change might take some time to apply to all of the instances in the group depending on the size of the group. |

## `SELECT` examples

Retrieves the list of managed instance groups and groups them by zone. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
allInstancesConfig,
autoHealingPolicies,
baseInstanceName,
creationTimestamp,
currentActions,
distributionPolicy,
fingerprint,
instanceGroup,
instanceLifecyclePolicy,
instanceTemplate,
kind,
listManagedInstancesResults,
namedPorts,
region,
satisfiesPzi,
satisfiesPzs,
selfLink,
statefulPolicy,
status,
targetPools,
targetSize,
updatePolicy,
versions,
zone
FROM google.compute.instance_group_managers
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_group_managers</code> resource.

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
INSERT INTO google.compute.instance_group_managers (
project,
zone,
kind,
id,
creationTimestamp,
name,
description,
zone,
region,
distributionPolicy,
instanceTemplate,
versions,
allInstancesConfig,
instanceGroup,
targetPools,
baseInstanceName,
fingerprint,
currentActions,
status,
targetSize,
listManagedInstancesResults,
selfLink,
autoHealingPolicies,
updatePolicy,
namedPorts,
statefulPolicy,
instanceLifecyclePolicy,
satisfiesPzi,
satisfiesPzs
)
SELECT 
'{{ project }}',
'{{ zone }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ name }}',
'{{ description }}',
'{{ zone }}',
'{{ region }}',
'{{ distributionPolicy }}',
'{{ instanceTemplate }}',
'{{ versions }}',
'{{ allInstancesConfig }}',
'{{ instanceGroup }}',
'{{ targetPools }}',
'{{ baseInstanceName }}',
'{{ fingerprint }}',
'{{ currentActions }}',
'{{ status }}',
'{{ targetSize }}',
'{{ listManagedInstancesResults }}',
'{{ selfLink }}',
'{{ autoHealingPolicies }}',
'{{ updatePolicy }}',
'{{ namedPorts }}',
'{{ statefulPolicy }}',
'{{ instanceLifecyclePolicy }}',
true|false,
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: zone
        value: '{{ zone }}'
      - name: region
        value: '{{ region }}'
      - name: distributionPolicy
        value: '{{ distributionPolicy }}'
      - name: instanceTemplate
        value: '{{ instanceTemplate }}'
      - name: versions
        value: '{{ versions }}'
      - name: allInstancesConfig
        value: '{{ allInstancesConfig }}'
      - name: instanceGroup
        value: '{{ instanceGroup }}'
      - name: targetPools
        value: '{{ targetPools }}'
      - name: baseInstanceName
        value: '{{ baseInstanceName }}'
      - name: fingerprint
        value: '{{ fingerprint }}'
      - name: currentActions
        value: '{{ currentActions }}'
      - name: status
        value: '{{ status }}'
      - name: targetSize
        value: '{{ targetSize }}'
      - name: listManagedInstancesResults
        value: '{{ listManagedInstancesResults }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: autoHealingPolicies
        value: '{{ autoHealingPolicies }}'
      - name: updatePolicy
        value: '{{ updatePolicy }}'
      - name: namedPorts
        value: '{{ namedPorts }}'
      - name: statefulPolicy
        value: '{{ statefulPolicy }}'
      - name: instanceLifecyclePolicy
        value: '{{ instanceLifecyclePolicy }}'
      - name: satisfiesPzi
        value: '{{ satisfiesPzi }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a instance_group_manager only if the necessary resources are available.

```sql
UPDATE google.compute.instance_group_managers
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
name = '{{ name }}',
description = '{{ description }}',
zone = '{{ zone }}',
region = '{{ region }}',
distributionPolicy = '{{ distributionPolicy }}',
instanceTemplate = '{{ instanceTemplate }}',
versions = '{{ versions }}',
allInstancesConfig = '{{ allInstancesConfig }}',
instanceGroup = '{{ instanceGroup }}',
targetPools = '{{ targetPools }}',
baseInstanceName = '{{ baseInstanceName }}',
fingerprint = '{{ fingerprint }}',
currentActions = '{{ currentActions }}',
status = '{{ status }}',
targetSize = '{{ targetSize }}',
listManagedInstancesResults = '{{ listManagedInstancesResults }}',
selfLink = '{{ selfLink }}',
autoHealingPolicies = '{{ autoHealingPolicies }}',
updatePolicy = '{{ updatePolicy }}',
namedPorts = '{{ namedPorts }}',
statefulPolicy = '{{ statefulPolicy }}',
instanceLifecyclePolicy = '{{ instanceLifecyclePolicy }}',
satisfiesPzi = true|false,
satisfiesPzs = true|false
WHERE 
instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```

## `DELETE` example

Deletes the specified instance_group_manager resource.

```sql
DELETE FROM google.compute.instance_group_managers
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
