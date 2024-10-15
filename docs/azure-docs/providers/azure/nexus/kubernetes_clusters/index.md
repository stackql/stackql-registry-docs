---
title: kubernetes_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes_clusters
  - nexus
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

Creates, updates, deletes, gets or lists a <code>kubernetes_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kubernetes_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.kubernetes_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kubernetes_clusters', value: 'view', },
        { label: 'kubernetes_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aad_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="attached_network_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_upgrades" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="connected_cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="control_plane_kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="control_plane_node_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="feature_statuses" /> | `text` | field from the `properties` object |
| <CopyableCode code="initial_agent_pool_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetesClusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId" /> | Get properties of the provided the Kubernetes cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of Kubernetes clusters in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of Kubernetes clusters in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new Kubernetes cluster or update the properties of the existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId" /> | Delete the provided Kubernetes cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId" /> | Patch the properties of the provided Kubernetes cluster, or update the tags associated with the Kubernetes cluster. Properties and tag updates can be done independently. |
| <CopyableCode code="restart_node" /> | `EXEC` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId, data__nodeName" /> | Restart a targeted node of a Kubernetes cluster. |

## `SELECT` examples

Get a list of Kubernetes clusters in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kubernetes_clusters', value: 'view', },
        { label: 'kubernetes_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aad_configuration,
administrator_configuration,
attached_network_ids,
available_upgrades,
cluster_id,
connected_cluster_id,
control_plane_kubernetes_version,
control_plane_node_configuration,
detailed_status,
detailed_status_message,
extended_location,
feature_statuses,
initial_agent_pool_configurations,
kubernetesClusterName,
kubernetes_version,
location,
managed_resource_group_configuration,
network_configuration,
nodes,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.nexus.vw_kubernetes_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.nexus.kubernetes_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kubernetes_clusters</code> resource.

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
INSERT INTO azure.nexus.kubernetes_clusters (
kubernetesClusterName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ kubernetesClusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ data__properties }}',
'{{ extendedLocation }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: aadConfiguration
          value:
            - name: adminGroupObjectIds
              value:
                - string
        - name: administratorConfiguration
          value:
            - name: adminUsername
              value: string
            - name: sshPublicKeys
              value:
                - - name: keyData
                    value: string
        - name: attachedNetworkIds
          value:
            - string
        - name: availableUpgrades
          value:
            - - name: availabilityLifecycle
                value: string
              - name: version
                value: string
        - name: clusterId
          value: string
        - name: connectedClusterId
          value: string
        - name: controlPlaneKubernetesVersion
          value: string
        - name: controlPlaneNodeConfiguration
          value:
            - name: availabilityZones
              value:
                - string
            - name: count
              value: integer
            - name: vmSkuName
              value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: featureStatuses
          value:
            - - name: detailedStatus
                value: string
              - name: detailedStatusMessage
                value: string
              - name: name
                value: string
              - name: version
                value: string
        - name: initialAgentPoolConfigurations
          value:
            - - name: agentOptions
                value:
                  - name: hugepagesCount
                    value: integer
                  - name: hugepagesSize
                    value: string
              - name: attachedNetworkConfiguration
                value:
                  - name: l2Networks
                    value:
                      - - name: networkId
                          value: string
                        - name: pluginType
                          value: string
                  - name: l3Networks
                    value:
                      - - name: ipamEnabled
                          value: string
                        - name: networkId
                          value: string
                        - name: pluginType
                          value: string
                  - name: trunkedNetworks
                    value:
                      - - name: networkId
                          value: string
                        - name: pluginType
                          value: string
              - name: availabilityZones
                value:
                  - string
              - name: count
                value: integer
              - name: labels
                value:
                  - - name: key
                      value: string
                    - name: value
                      value: string
              - name: mode
                value: string
              - name: name
                value: string
              - name: taints
                value:
                  - - name: key
                      value: string
                    - name: value
                      value: string
              - name: upgradeSettings
                value:
                  - name: drainTimeout
                    value: integer
                  - name: maxSurge
                    value: string
                  - name: maxUnavailable
                    value: string
              - name: vmSkuName
                value: string
        - name: kubernetesVersion
          value: string
        - name: managedResourceGroupConfiguration
          value:
            - name: location
              value: string
            - name: name
              value: string
        - name: networkConfiguration
          value:
            - name: bgpServiceLoadBalancerConfiguration
              value:
                - name: bgpAdvertisements
                  value:
                    - - name: advertiseToFabric
                        value: string
                      - name: communities
                        value:
                          - string
                      - name: ipAddressPools
                        value:
                          - string
                      - name: peers
                        value:
                          - string
                - name: bgpPeers
                  value:
                    - - name: bfdEnabled
                        value: string
                      - name: bgpMultiHop
                        value: string
                      - name: holdTime
                        value: string
                      - name: keepAliveTime
                        value: string
                      - name: myAsn
                        value: integer
                      - name: name
                        value: string
                      - name: password
                        value: string
                      - name: peerAddress
                        value: string
                      - name: peerAsn
                        value: integer
                      - name: peerPort
                        value: integer
                - name: fabricPeeringEnabled
                  value: string
                - name: ipAddressPools
                  value:
                    - - name: addresses
                        value:
                          - string
                      - name: autoAssign
                        value: string
                      - name: name
                        value: string
                      - name: onlyUseHostIps
                        value: string
            - name: cloudServicesNetworkId
              value: string
            - name: cniNetworkId
              value: string
            - name: dnsServiceIp
              value: string
            - name: l2ServiceLoadBalancerConfiguration
              value:
                - name: ipAddressPools
                  value:
                    - - name: addresses
                        value:
                          - string
                      - name: autoAssign
                        value: string
                      - name: name
                        value: string
                      - name: onlyUseHostIps
                        value: string
            - name: podCidrs
              value:
                - string
            - name: serviceCidrs
              value:
                - string
        - name: nodes
          value:
            - - name: agentPoolId
                value: string
              - name: availabilityZone
                value: string
              - name: bareMetalMachineId
                value: string
              - name: cpuCores
                value: integer
              - name: detailedStatus
                value: string
              - name: detailedStatusMessage
                value: string
              - name: diskSizeGB
                value: integer
              - name: image
                value: string
              - name: kubernetesVersion
                value: string
              - name: labels
                value:
                  - - name: key
                      value: string
                    - name: value
                      value: string
              - name: memorySizeGB
                value: integer
              - name: mode
                value: string
              - name: name
                value: string
              - name: networkAttachments
                value:
                  - - name: attachedNetworkId
                      value: string
                    - name: defaultGateway
                      value: string
                    - name: ipAllocationMethod
                      value: string
                    - name: ipv4Address
                      value: string
                    - name: ipv6Address
                      value: string
                    - name: macAddress
                      value: string
                    - name: networkAttachmentName
                      value: string
              - name: powerState
                value: string
              - name: role
                value: string
              - name: taints
                value:
                  - - name: key
                      value: string
                    - name: value
                      value: string
              - name: vmSkuName
                value: string
        - name: provisioningState
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>kubernetes_clusters</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.kubernetes_clusters
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>kubernetes_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.kubernetes_clusters
WHERE kubernetesClusterName = '{{ kubernetesClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
