---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - aks
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

Creates, updates, deletes, gets or lists a <code>agent_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.agent_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agent_pools', value: 'view', },
        { label: 'agent_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="agentPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zones" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_reservation_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="count" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_orchestrator_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_auto_scaling" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_encryption_at_host" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_fips" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_node_public_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_ultra_ssd" /> | `text` | field from the `properties` object |
| <CopyableCode code="gpu_instance_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubelet_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubelet_disk_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="linux_os_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_pods" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_image_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_public_ip_prefix_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_taints" /> | `text` | field from the `properties` object |
| <CopyableCode code="orchestrator_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_disk_size_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_disk_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="pod_subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="proximity_placement_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_down_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_set_eviction_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_set_priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="spot_max_price" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="upgrade_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="windows_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_runtime" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for the container service agent pool profile. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="abort_latest_operation" /> | `EXEC` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> | Aborts the currently running operation on the agent pool. The Agent Pool will be moved to a Canceling state and eventually to a Canceled state when cancellation finishes. If the operation completes before cancellation can take place, a 409 error code is returned. |
| <CopyableCode code="upgrade_node_image_version" /> | `EXEC` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> | Upgrading the node image version of an agent pool applies the newest OS and runtime updates to the nodes. AKS provides one new image per week with the latest updates. For more details on node image versions, see: https://docs.microsoft.com/azure/aks/node-image-upgrade |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agent_pools', value: 'view', },
        { label: 'agent_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agentPoolName,
availability_zones,
capacity_reservation_group_id,
count,
creation_data,
current_orchestrator_version,
enable_auto_scaling,
enable_encryption_at_host,
enable_fips,
enable_node_public_ip,
enable_ultra_ssd,
gpu_instance_profile,
host_group_id,
kubelet_config,
kubelet_disk_type,
linux_os_config,
max_count,
max_pods,
min_count,
mode,
network_profile,
node_image_version,
node_labels,
node_public_ip_prefix_id,
node_taints,
orchestrator_version,
os_disk_size_gb,
os_disk_type,
os_sku,
os_type,
pod_subnet_id,
power_state,
provisioning_state,
proximity_placement_group_id,
resourceGroupName,
resourceName,
scale_down_mode,
scale_set_eviction_policy,
scale_set_priority,
security_profile,
spot_max_price,
subscriptionId,
tags,
type,
upgrade_settings,
vm_size,
vnet_subnet_id,
windows_profile,
workload_runtime
FROM azure.aks.vw_agent_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.aks.agent_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>agent_pools</code> resource.

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
INSERT INTO azure.aks.agent_pools (
agentPoolName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ agentPoolName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: count
          value: integer
        - name: vmSize
          value: string
        - name: osDiskSizeGB
          value: []
        - name: osDiskType
          value: []
        - name: kubeletDiskType
          value: []
        - name: workloadRuntime
          value: []
        - name: vnetSubnetID
          value: string
        - name: podSubnetID
          value: string
        - name: maxPods
          value: integer
        - name: osType
          value: []
        - name: osSKU
          value: []
        - name: maxCount
          value: integer
        - name: minCount
          value: integer
        - name: enableAutoScaling
          value: boolean
        - name: scaleDownMode
          value: []
        - name: type
          value: []
        - name: mode
          value: []
        - name: orchestratorVersion
          value: string
        - name: currentOrchestratorVersion
          value: string
        - name: nodeImageVersion
          value: string
        - name: upgradeSettings
          value:
            - name: maxSurge
              value: string
            - name: drainTimeoutInMinutes
              value: integer
            - name: nodeSoakDurationInMinutes
              value: integer
        - name: provisioningState
          value: string
        - name: powerState
          value:
            - name: code
              value: string
        - name: availabilityZones
          value:
            - string
        - name: enableNodePublicIP
          value: boolean
        - name: nodePublicIPPrefixID
          value: string
        - name: scaleSetPriority
          value: []
        - name: scaleSetEvictionPolicy
          value: []
        - name: spotMaxPrice
          value: []
        - name: tags
          value: object
        - name: nodeLabels
          value: object
        - name: nodeTaints
          value:
            - string
        - name: proximityPlacementGroupID
          value: []
        - name: kubeletConfig
          value:
            - name: cpuManagerPolicy
              value: string
            - name: cpuCfsQuota
              value: boolean
            - name: cpuCfsQuotaPeriod
              value: string
            - name: imageGcHighThreshold
              value: integer
            - name: imageGcLowThreshold
              value: integer
            - name: topologyManagerPolicy
              value: string
            - name: allowedUnsafeSysctls
              value:
                - string
            - name: failSwapOn
              value: boolean
            - name: containerLogMaxSizeMB
              value: integer
            - name: containerLogMaxFiles
              value: integer
            - name: podMaxPids
              value: integer
        - name: linuxOSConfig
          value:
            - name: sysctls
              value:
                - name: netCoreSomaxconn
                  value: integer
                - name: netCoreNetdevMaxBacklog
                  value: integer
                - name: netCoreRmemDefault
                  value: integer
                - name: netCoreRmemMax
                  value: integer
                - name: netCoreWmemDefault
                  value: integer
                - name: netCoreWmemMax
                  value: integer
                - name: netCoreOptmemMax
                  value: integer
                - name: netIpv4TcpMaxSynBacklog
                  value: integer
                - name: netIpv4TcpMaxTwBuckets
                  value: integer
                - name: netIpv4TcpFinTimeout
                  value: integer
                - name: netIpv4TcpKeepaliveTime
                  value: integer
                - name: netIpv4TcpKeepaliveProbes
                  value: integer
                - name: netIpv4TcpkeepaliveIntvl
                  value: integer
                - name: netIpv4TcpTwReuse
                  value: boolean
                - name: netIpv4IpLocalPortRange
                  value: string
                - name: netIpv4NeighDefaultGcThresh1
                  value: integer
                - name: netIpv4NeighDefaultGcThresh2
                  value: integer
                - name: netIpv4NeighDefaultGcThresh3
                  value: integer
                - name: netNetfilterNfConntrackMax
                  value: integer
                - name: netNetfilterNfConntrackBuckets
                  value: integer
                - name: fsInotifyMaxUserWatches
                  value: integer
                - name: fsFileMax
                  value: integer
                - name: fsAioMaxNr
                  value: integer
                - name: fsNrOpen
                  value: integer
                - name: kernelThreadsMax
                  value: integer
                - name: vmMaxMapCount
                  value: integer
                - name: vmSwappiness
                  value: integer
                - name: vmVfsCachePressure
                  value: integer
            - name: transparentHugePageEnabled
              value: string
            - name: transparentHugePageDefrag
              value: string
            - name: swapFileSizeMB
              value: integer
        - name: enableEncryptionAtHost
          value: boolean
        - name: enableUltraSSD
          value: boolean
        - name: enableFIPS
          value: boolean
        - name: gpuInstanceProfile
          value: []
        - name: creationData
          value:
            - name: sourceResourceId
              value: string
        - name: capacityReservationGroupID
          value: []
        - name: hostGroupID
          value: string
        - name: networkProfile
          value:
            - name: nodePublicIPTags
              value: []
            - name: allowedHostPorts
              value:
                - - name: portStart
                    value: integer
                  - name: portEnd
                    value: integer
                  - name: protocol
                    value: string
            - name: applicationSecurityGroups
              value:
                - string
        - name: windowsProfile
          value:
            - name: disableOutboundNat
              value: boolean
        - name: securityProfile
          value:
            - name: enableVTPM
              value: boolean
            - name: enableSecureBoot
              value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>agent_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aks.agent_pools
WHERE agentPoolName = '{{ agentPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
