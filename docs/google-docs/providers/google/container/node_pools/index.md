---
title: node_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - node_pools
  - container
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

Creates, updates, deletes, gets or lists a <code>node_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.container.node_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the node pool. |
| <CopyableCode code="autoscaling" /> | `object` | NodePoolAutoscaling contains information required by cluster autoscaler to adjust the size of the node pool to the current cluster usage. |
| <CopyableCode code="bestEffortProvisioning" /> | `object` | Best effort provisioning. |
| <CopyableCode code="conditions" /> | `array` | Which conditions caused the current node pool state. |
| <CopyableCode code="config" /> | `object` | Parameters that describe the nodes in a cluster. GKE Autopilot clusters do not recognize parameters in `NodeConfig`. Use AutoprovisioningNodePoolDefaults instead. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of node pool fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="initialNodeCount" /> | `integer` | The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. |
| <CopyableCode code="instanceGroupUrls" /> | `array` | Output only. The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool. During the node pool blue-green upgrade operation, the URLs contain both blue and green resources. |
| <CopyableCode code="locations" /> | `array` | The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located. If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead. Warning: changing node pool locations will result in nodes being added and/or removed. |
| <CopyableCode code="management" /> | `object` | NodeManagement defines the set of node management services turned on for the node pool. |
| <CopyableCode code="maxPodsConstraint" /> | `object` | Constraints applied to pods. |
| <CopyableCode code="networkConfig" /> | `object` | Parameters for node pool-level network config. |
| <CopyableCode code="placementPolicy" /> | `object` | PlacementPolicy defines the placement policy used by the node pool. |
| <CopyableCode code="podIpv4CidrSize" /> | `integer` | Output only. The pod CIDR block size per node in this node pool. |
| <CopyableCode code="queuedProvisioning" /> | `object` | QueuedProvisioning defines the queued provisioning used by the node pool. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined URL for the resource. |
| <CopyableCode code="status" /> | `string` | Output only. The status of the nodes in this pool instance. |
| <CopyableCode code="statusMessage" /> | `string` | Output only. Deprecated. Use conditions instead. Additional information about the current status of this node pool instance, if available. |
| <CopyableCode code="updateInfo" /> | `object` | UpdateInfo contains resource (instance groups, etc), status and other intermediate information relevant to a node pool upgrade. |
| <CopyableCode code="upgradeSettings" /> | `object` | These upgrade settings control the level of parallelism and the level of disruption caused by an upgrade. maxUnavailable controls the number of nodes that can be simultaneously unavailable. maxSurge controls the number of additional nodes that can be added to the node pool temporarily for the time of the upgrade to increase the number of available nodes. (maxUnavailable + maxSurge) determines the level of parallelism (how many nodes are being upgraded at the same time). Note: upgrades inevitably introduce some disruption since workloads need to be moved from old nodes to new, upgraded ones. Even if maxUnavailable=0, this holds true. (Disruption stays within the limits of PodDisruptionBudget, if it is configured.) Consider a hypothetical node pool with 5 nodes having maxSurge=2, maxUnavailable=1. This means the upgrade process upgrades 3 nodes simultaneously. It creates 2 additional (upgraded) nodes, then it brings down 3 old (not yet upgraded) nodes at the same time. This ensures that there are always at least 4 nodes available. These upgrade settings configure the upgrade strategy for the node pool. Use strategy to switch between the strategies applied to the node pool. If the strategy is ROLLING, use max_surge and max_unavailable to control the level of parallelism and the level of disruption caused by upgrade. 1. maxSurge controls the number of additional nodes that can be added to the node pool temporarily for the time of the upgrade to increase the number of available nodes. 2. maxUnavailable controls the number of nodes that can be simultaneously unavailable. 3. (maxUnavailable + maxSurge) determines the level of parallelism (how many nodes are being upgraded at the same time). If the strategy is BLUE_GREEN, use blue_green_settings to configure the blue-green upgrade related settings. 1. standard_rollout_policy is the default policy. The policy is used to control the way blue pool gets drained. The draining is executed in the batch mode. The batch size could be specified as either percentage of the node pool size or the number of nodes. batch_soak_duration is the soak time after each batch gets drained. 2. node_pool_soak_duration is the soak time after all blue nodes are drained. After this period, the blue pool nodes will be deleted. |
| <CopyableCode code="version" /> | `string` | The version of Kubernetes running on this NodePool's nodes. If unspecified, it defaults as described [here](https://cloud.google.com/kubernetes-engine/versioning#specifying_node_version). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_clusters_node_pools_get" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, nodePoolsId, projectsId" /> | Retrieves the requested node pool. |
| <CopyableCode code="projects_locations_clusters_node_pools_list" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Lists the node pools for a cluster. |
| <CopyableCode code="projects_zones_clusters_node_pools_get" /> | `SELECT` | <CopyableCode code="clusterId, nodePoolId, projectId, zone" /> | Retrieves the requested node pool. |
| <CopyableCode code="projects_zones_clusters_node_pools_list" /> | `SELECT` | <CopyableCode code="clusterId, projectId, zone" /> | Lists the node pools for a cluster. |
| <CopyableCode code="projects_locations_clusters_node_pools_create" /> | `INSERT` | <CopyableCode code="clustersId, locationsId, projectsId" /> | Creates a node pool for a cluster. |
| <CopyableCode code="projects_zones_clusters_node_pools_create" /> | `INSERT` | <CopyableCode code="clusterId, projectId, zone" /> | Creates a node pool for a cluster. |
| <CopyableCode code="projects_locations_clusters_node_pools_delete" /> | `DELETE` | <CopyableCode code="clustersId, locationsId, nodePoolsId, projectsId" /> | Deletes a node pool from a cluster. |
| <CopyableCode code="projects_zones_clusters_node_pools_delete" /> | `DELETE` | <CopyableCode code="clusterId, nodePoolId, projectId, zone" /> | Deletes a node pool from a cluster. |
| <CopyableCode code="projects_zones_clusters_node_pools_update" /> | `UPDATE` | <CopyableCode code="clusterId, nodePoolId, projectId, zone" /> | Updates the version and/or image type for the specified node pool. |
| <CopyableCode code="projects_locations_clusters_node_pools_update" /> | `REPLACE` | <CopyableCode code="clustersId, locationsId, nodePoolsId, projectsId" /> | Updates the version and/or image type for the specified node pool. |
| <CopyableCode code="projects_locations_clusters_node_pools_complete_upgrade" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, nodePoolsId, projectsId" /> | CompleteNodePoolUpgrade will signal an on-going node pool upgrade to complete. |
| <CopyableCode code="projects_locations_clusters_node_pools_rollback" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, nodePoolsId, projectsId" /> | Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |
| <CopyableCode code="projects_locations_clusters_node_pools_set_autoscaling" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, nodePoolsId, projectsId" /> | Sets the autoscaling settings for the specified node pool. |
| <CopyableCode code="projects_locations_clusters_node_pools_set_management" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, nodePoolsId, projectsId" /> | Sets the NodeManagement options for a node pool. |
| <CopyableCode code="projects_locations_clusters_node_pools_set_size" /> | `EXEC` | <CopyableCode code="clustersId, locationsId, nodePoolsId, projectsId" /> | Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |
| <CopyableCode code="projects_zones_clusters_node_pools_autoscaling" /> | `EXEC` | <CopyableCode code="clusterId, nodePoolId, projectId, zone" /> | Sets the autoscaling settings for the specified node pool. |
| <CopyableCode code="projects_zones_clusters_node_pools_rollback" /> | `EXEC` | <CopyableCode code="clusterId, nodePoolId, projectId, zone" /> | Rolls back a previously Aborted or Failed NodePool upgrade. This makes no changes if the last upgrade successfully completed. |
| <CopyableCode code="projects_zones_clusters_node_pools_set_management" /> | `EXEC` | <CopyableCode code="clusterId, nodePoolId, projectId, zone" /> | Sets the NodeManagement options for a node pool. |
| <CopyableCode code="projects_zones_clusters_node_pools_set_size" /> | `EXEC` | <CopyableCode code="clusterId, nodePoolId, projectId, zone" /> | Sets the size for a specific node pool. The new size will be used for all replicas, including future replicas created by modifying NodePool.locations. |

## `SELECT` examples

Lists the node pools for a cluster.

```sql
SELECT
name,
autoscaling,
bestEffortProvisioning,
conditions,
config,
etag,
initialNodeCount,
instanceGroupUrls,
locations,
management,
maxPodsConstraint,
networkConfig,
placementPolicy,
podIpv4CidrSize,
queuedProvisioning,
selfLink,
status,
statusMessage,
updateInfo,
upgradeSettings,
version
FROM google.container.node_pools
WHERE clusterId = '{{ clusterId }}'
AND projectId = '{{ projectId }}'
AND zone = '{{ zone }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>node_pools</code> resource.

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
INSERT INTO google.container.node_pools (
clusterId,
projectId,
zone,
projectId,
zone,
clusterId,
nodePool,
parent
)
SELECT 
'{{ clusterId }}',
'{{ projectId }}',
'{{ zone }}',
'{{ projectId }}',
'{{ zone }}',
'{{ clusterId }}',
'{{ nodePool }}',
'{{ parent }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: projectId
      value: string
    - name: zone
      value: string
    - name: clusterId
      value: string
    - name: nodePool
      value:
        - name: name
          value: string
        - name: config
          value:
            - name: machineType
              value: string
            - name: diskSizeGb
              value: integer
            - name: oauthScopes
              value:
                - string
            - name: serviceAccount
              value: string
            - name: metadata
              value: object
            - name: imageType
              value: string
            - name: labels
              value: object
            - name: localSsdCount
              value: integer
            - name: tags
              value:
                - string
            - name: preemptible
              value: boolean
            - name: accelerators
              value:
                - - name: acceleratorCount
                    value: string
                  - name: acceleratorType
                    value: string
                  - name: gpuPartitionSize
                    value: string
                  - name: gpuSharingConfig
                    value:
                      - name: maxSharedClientsPerGpu
                        value: string
                      - name: gpuSharingStrategy
                        value: string
                  - name: gpuDriverInstallationConfig
                    value:
                      - name: gpuDriverVersion
                        value: string
            - name: diskType
              value: string
            - name: minCpuPlatform
              value: string
            - name: workloadMetadataConfig
              value:
                - name: mode
                  value: string
            - name: taints
              value:
                - - name: key
                    value: string
                  - name: value
                    value: string
                  - name: effect
                    value: string
            - name: sandboxConfig
              value:
                - name: type
                  value: string
            - name: nodeGroup
              value: string
            - name: reservationAffinity
              value:
                - name: consumeReservationType
                  value: string
                - name: key
                  value: string
                - name: values
                  value:
                    - string
            - name: shieldedInstanceConfig
              value:
                - name: enableSecureBoot
                  value: boolean
                - name: enableIntegrityMonitoring
                  value: boolean
            - name: linuxNodeConfig
              value:
                - name: sysctls
                  value: object
                - name: cgroupMode
                  value: string
                - name: hugepages
                  value:
                    - name: hugepageSize2m
                      value: integer
                    - name: hugepageSize1g
                      value: integer
            - name: kubeletConfig
              value:
                - name: cpuManagerPolicy
                  value: string
                - name: cpuCfsQuota
                  value: boolean
                - name: cpuCfsQuotaPeriod
                  value: string
                - name: podPidsLimit
                  value: string
                - name: insecureKubeletReadonlyPortEnabled
                  value: boolean
            - name: bootDiskKmsKey
              value: string
            - name: gcfsConfig
              value:
                - name: enabled
                  value: boolean
            - name: advancedMachineFeatures
              value:
                - name: threadsPerCore
                  value: string
                - name: enableNestedVirtualization
                  value: boolean
            - name: gvnic
              value:
                - name: enabled
                  value: boolean
            - name: spot
              value: boolean
            - name: confidentialNodes
              value:
                - name: enabled
                  value: boolean
            - name: fastSocket
              value:
                - name: enabled
                  value: boolean
            - name: resourceLabels
              value: object
            - name: loggingConfig
              value:
                - name: variantConfig
                  value:
                    - name: variant
                      value: string
            - name: windowsNodeConfig
              value:
                - name: osVersion
                  value: string
            - name: localNvmeSsdBlockConfig
              value:
                - name: localSsdCount
                  value: integer
            - name: ephemeralStorageLocalSsdConfig
              value:
                - name: localSsdCount
                  value: integer
            - name: soleTenantConfig
              value:
                - name: nodeAffinities
                  value:
                    - - name: key
                        value: string
                      - name: operator
                        value: string
                      - name: values
                        value:
                          - string
            - name: containerdConfig
              value:
                - name: privateRegistryAccessConfig
                  value:
                    - name: enabled
                      value: boolean
                    - name: certificateAuthorityDomainConfig
                      value:
                        - - name: fqdns
                            value:
                              - string
                          - name: gcpSecretManagerCertificateConfig
                            value:
                              - name: secretUri
                                value: string
            - name: resourceManagerTags
              value:
                - name: tags
                  value: object
            - name: enableConfidentialStorage
              value: boolean
            - name: secondaryBootDisks
              value:
                - - name: mode
                    value: string
                  - name: diskImage
                    value: string
            - name: storagePools
              value:
                - string
            - name: secondaryBootDiskUpdateStrategy
              value: []
        - name: initialNodeCount
          value: integer
        - name: locations
          value:
            - string
        - name: networkConfig
          value:
            - name: createPodRange
              value: boolean
            - name: podRange
              value: string
            - name: podIpv4CidrBlock
              value: string
            - name: enablePrivateNodes
              value: boolean
            - name: networkPerformanceConfig
              value:
                - name: totalEgressBandwidthTier
                  value: string
            - name: podCidrOverprovisionConfig
              value:
                - name: disable
                  value: boolean
            - name: additionalNodeNetworkConfigs
              value:
                - - name: network
                    value: string
                  - name: subnetwork
                    value: string
            - name: additionalPodNetworkConfigs
              value:
                - - name: subnetwork
                    value: string
                  - name: secondaryPodRange
                    value: string
                  - name: maxPodsPerNode
                    value:
                      - name: maxPodsPerNode
                        value: string
            - name: podIpv4RangeUtilization
              value: number
        - name: selfLink
          value: string
        - name: version
          value: string
        - name: instanceGroupUrls
          value:
            - string
        - name: status
          value: string
        - name: statusMessage
          value: string
        - name: autoscaling
          value:
            - name: enabled
              value: boolean
            - name: minNodeCount
              value: integer
            - name: maxNodeCount
              value: integer
            - name: autoprovisioned
              value: boolean
            - name: locationPolicy
              value: string
            - name: totalMinNodeCount
              value: integer
            - name: totalMaxNodeCount
              value: integer
        - name: management
          value:
            - name: autoUpgrade
              value: boolean
            - name: autoRepair
              value: boolean
            - name: upgradeOptions
              value:
                - name: autoUpgradeStartTime
                  value: string
                - name: description
                  value: string
        - name: conditions
          value:
            - - name: code
                value: string
              - name: message
                value: string
              - name: canonicalCode
                value: string
        - name: podIpv4CidrSize
          value: integer
        - name: upgradeSettings
          value:
            - name: maxSurge
              value: integer
            - name: maxUnavailable
              value: integer
            - name: strategy
              value: string
            - name: blueGreenSettings
              value:
                - name: standardRolloutPolicy
                  value:
                    - name: batchPercentage
                      value: number
                    - name: batchNodeCount
                      value: integer
                    - name: batchSoakDuration
                      value: string
                - name: nodePoolSoakDuration
                  value: string
        - name: placementPolicy
          value:
            - name: type
              value: string
            - name: tpuTopology
              value: string
            - name: policyName
              value: string
        - name: updateInfo
          value:
            - name: blueGreenInfo
              value:
                - name: phase
                  value: string
                - name: blueInstanceGroupUrls
                  value:
                    - string
                - name: greenInstanceGroupUrls
                  value:
                    - string
                - name: bluePoolDeletionStartTime
                  value: string
                - name: greenPoolVersion
                  value: string
        - name: etag
          value: string
        - name: queuedProvisioning
          value:
            - name: enabled
              value: boolean
        - name: bestEffortProvisioning
          value:
            - name: enabled
              value: boolean
            - name: minProvisionNodes
              value: integer
    - name: parent
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>node_pools</code> resource.

```sql
/*+ update */
UPDATE google.container.node_pools
SET 
projectId = '{{ projectId }}',
zone = '{{ zone }}',
clusterId = '{{ clusterId }}',
nodePoolId = '{{ nodePoolId }}',
nodeVersion = '{{ nodeVersion }}',
imageType = '{{ imageType }}',
name = '{{ name }}',
locations = '{{ locations }}',
workloadMetadataConfig = '{{ workloadMetadataConfig }}',
upgradeSettings = '{{ upgradeSettings }}',
tags = '{{ tags }}',
taints = '{{ taints }}',
labels = '{{ labels }}',
linuxNodeConfig = '{{ linuxNodeConfig }}',
kubeletConfig = '{{ kubeletConfig }}',
nodeNetworkConfig = '{{ nodeNetworkConfig }}',
gcfsConfig = '{{ gcfsConfig }}',
confidentialNodes = '{{ confidentialNodes }}',
gvnic = '{{ gvnic }}',
etag = '{{ etag }}',
fastSocket = '{{ fastSocket }}',
loggingConfig = '{{ loggingConfig }}',
resourceLabels = '{{ resourceLabels }}',
windowsNodeConfig = '{{ windowsNodeConfig }}',
accelerators = '{{ accelerators }}',
machineType = '{{ machineType }}',
diskType = '{{ diskType }}',
diskSizeGb = '{{ diskSizeGb }}',
resourceManagerTags = '{{ resourceManagerTags }}',
containerdConfig = '{{ containerdConfig }}',
queuedProvisioning = '{{ queuedProvisioning }}',
storagePools = '{{ storagePools }}'
WHERE 
clusterId = '{{ clusterId }}'
AND nodePoolId = '{{ nodePoolId }}'
AND projectId = '{{ projectId }}'
AND zone = '{{ zone }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>node_pools</code> resource.

```sql
/*+ update */
REPLACE google.container.node_pools
SET 
projectId = '{{ projectId }}',
zone = '{{ zone }}',
clusterId = '{{ clusterId }}',
nodePoolId = '{{ nodePoolId }}',
nodeVersion = '{{ nodeVersion }}',
imageType = '{{ imageType }}',
name = '{{ name }}',
locations = '{{ locations }}',
workloadMetadataConfig = '{{ workloadMetadataConfig }}',
upgradeSettings = '{{ upgradeSettings }}',
tags = '{{ tags }}',
taints = '{{ taints }}',
labels = '{{ labels }}',
linuxNodeConfig = '{{ linuxNodeConfig }}',
kubeletConfig = '{{ kubeletConfig }}',
nodeNetworkConfig = '{{ nodeNetworkConfig }}',
gcfsConfig = '{{ gcfsConfig }}',
confidentialNodes = '{{ confidentialNodes }}',
gvnic = '{{ gvnic }}',
etag = '{{ etag }}',
fastSocket = '{{ fastSocket }}',
loggingConfig = '{{ loggingConfig }}',
resourceLabels = '{{ resourceLabels }}',
windowsNodeConfig = '{{ windowsNodeConfig }}',
accelerators = '{{ accelerators }}',
machineType = '{{ machineType }}',
diskType = '{{ diskType }}',
diskSizeGb = '{{ diskSizeGb }}',
resourceManagerTags = '{{ resourceManagerTags }}',
containerdConfig = '{{ containerdConfig }}',
queuedProvisioning = '{{ queuedProvisioning }}',
storagePools = '{{ storagePools }}'
WHERE 
clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND nodePoolsId = '{{ nodePoolsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>node_pools</code> resource.

```sql
/*+ delete */
DELETE FROM google.container.node_pools
WHERE clusterId = '{{ clusterId }}'
AND nodePoolId = '{{ nodePoolId }}'
AND projectId = '{{ projectId }}'
AND zone = '{{ zone }}';
```
