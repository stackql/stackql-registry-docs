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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>region_instance_group_managers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_instance_group_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_instance_group_managers" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceGroupManager, project, region" /> | Returns all of the details about the specified managed instance group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves the list of managed instance groups that are contained within the specified region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a managed instance group using the information that you specify in the request. After the group is created, instances in the group are created using the specified instance template. This operation is marked as DONE when the group is created even if the instances in the group have not yet been created. You must separately verify the status of the individual instances with the listmanagedinstances method. A regional managed instance group can contain up to 2000 instances. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceGroupManager, project, region" /> | Deletes the specified managed instance group and all of the instances in that group. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instanceGroupManager, project, region" /> | Updates a managed instance group using the information that you specify in the request. This operation is marked as DONE when the group is patched even if the instances in the group are still in the process of being patched. You must separately verify the status of the individual instances with the listmanagedinstances method. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. If you update your group to specify a new template or instance configuration, it's possible that your intended specification for each VM in the group is different from the current state of that VM. To learn how to apply an updated configuration to the VMs in a MIG, see Updating instances in a MIG. |
| <CopyableCode code="patch_per_instance_configs" /> | `UPDATE` | <CopyableCode code="instanceGroupManager, project, region" /> | Inserts or patches per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |
| <CopyableCode code="abandon_instances" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, region" /> | Flags the specified instances to be immediately removed from the managed instance group. Abandoning an instance does not delete the instance, but it does remove the instance from any target pools that are applied by the managed instance group. This method reduces the targetSize of the managed instance group by the number of instances that you abandon. This operation is marked as DONE when the action is scheduled even if the instances have not yet been removed from the group. You must separately verify the status of the abandoning action with the listmanagedinstances method. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| <CopyableCode code="apply_updates_to_instances" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, region" /> | Apply updates to selected instances the managed instance group. |
| <CopyableCode code="recreate_instances" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, region" /> | Flags the specified VM instances in the managed instance group to be immediately recreated. Each instance is recreated using the group's current configuration. This operation is marked as DONE when the flag is set even if the instances have not yet been recreated. You must separately verify the status of each instance by checking its currentAction field; for more information, see Checking the status of managed instances. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. You can specify a maximum of 1000 instances with this method per request. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, region, size" /> | Changes the intended size of the managed instance group. If you increase the size, the group creates new instances using the current instance template. If you decrease the size, the group deletes one or more instances. The resize operation is marked DONE if the resize request is successful. The underlying actions take additional time. You must separately verify the status of the creating or deleting actions with the listmanagedinstances method. If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted. |
| <CopyableCode code="set_instance_template" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, region" /> | Sets the instance template to use when creating new instances or recreating instances in this group. Existing instances are not affected. |
| <CopyableCode code="set_target_pools" /> | `EXEC` | <CopyableCode code="instanceGroupManager, project, region" /> | Modifies the target pools to which all new instances in this group are assigned. Existing instances in the group are not affected. |

## `SELECT` examples

Retrieves the list of managed instance groups that are contained within the specified region.

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
FROM google.compute.region_instance_group_managers
WHERE project = '{{ project }}'
AND region = '{{ region }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_instance_group_managers</code> resource.

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
INSERT INTO google.compute.region_instance_group_managers (
project,
region,
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
'{{ region }}',
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
'{{ autoHealingPolicies }}',
'{{ updatePolicy }}',
'{{ namedPorts }}',
'{{ statefulPolicy }}',
'{{ instanceLifecyclePolicy }}',
{{ satisfiesPzi }},
{{ satisfiesPzs }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: creationTimestamp
      value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: zone
      value: string
    - name: region
      value: string
    - name: distributionPolicy
      value:
        - name: zones
          value:
            - - name: zone
                value: string
        - name: targetShape
          value: string
    - name: instanceTemplate
      value: string
    - name: versions
      value:
        - - name: name
            value: string
          - name: instanceTemplate
            value: string
          - name: targetSize
            value:
              - name: fixed
                value: integer
              - name: percent
                value: integer
              - name: calculated
                value: integer
    - name: allInstancesConfig
      value:
        - name: properties
          value:
            - name: metadata
              value: object
            - name: labels
              value: object
    - name: instanceGroup
      value: string
    - name: targetPools
      value:
        - string
    - name: baseInstanceName
      value: string
    - name: fingerprint
      value: string
    - name: currentActions
      value:
        - name: none
          value: integer
        - name: creating
          value: integer
        - name: creatingWithoutRetries
          value: integer
        - name: verifying
          value: integer
        - name: recreating
          value: integer
        - name: deleting
          value: integer
        - name: abandoning
          value: integer
        - name: restarting
          value: integer
        - name: refreshing
          value: integer
        - name: suspending
          value: integer
        - name: resuming
          value: integer
        - name: stopping
          value: integer
        - name: starting
          value: integer
    - name: status
      value:
        - name: isStable
          value: boolean
        - name: allInstancesConfig
          value:
            - name: effective
              value: boolean
            - name: currentRevision
              value: string
        - name: versionTarget
          value:
            - name: isReached
              value: boolean
        - name: stateful
          value:
            - name: hasStatefulConfig
              value: boolean
            - name: perInstanceConfigs
              value:
                - name: allEffective
                  value: boolean
        - name: autoscaler
          value: string
    - name: targetSize
      value: integer
    - name: listManagedInstancesResults
      value: string
    - name: selfLink
      value: string
    - name: autoHealingPolicies
      value:
        - - name: healthCheck
            value: string
          - name: initialDelaySec
            value: integer
    - name: updatePolicy
      value:
        - name: type
          value: string
        - name: instanceRedistributionType
          value: string
        - name: minimalAction
          value: string
        - name: mostDisruptiveAllowedAction
          value: string
        - name: replacementMethod
          value: string
    - name: namedPorts
      value:
        - - name: name
            value: string
          - name: port
            value: integer
    - name: statefulPolicy
      value:
        - name: preservedState
          value:
            - name: disks
              value: object
            - name: internalIPs
              value: object
            - name: externalIPs
              value: object
    - name: instanceLifecyclePolicy
      value:
        - name: forceUpdateOnRepair
          value: string
        - name: defaultActionOnFailure
          value: string
    - name: satisfiesPzi
      value: boolean
    - name: satisfiesPzs
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>region_instance_group_managers</code> resource.

```sql
/*+ update */
UPDATE google.compute.region_instance_group_managers
SET 
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
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified <code>region_instance_group_managers</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.region_instance_group_managers
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
