---
title: provisioned_cluster_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioned_cluster_instances
  - hybrid_aks
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

Creates, updates, deletes, gets or lists a <code>provisioned_cluster_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioned_cluster_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.provisioned_cluster_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provisioned_cluster_instances', value: 'view', },
        { label: 'provisioned_cluster_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agent_pool_profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_scaler_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_provider_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_vm_access_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectedClusterResourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="control_plane" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="linux_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location pointing to the underlying infrastructure |
| <CopyableCode code="properties" /> | `object` | Properties of the provisioned cluster. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Gets the provisioned cluster instance |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Lists the ProvisionedClusterInstance resource associated with the ConnectedCluster |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectedClusterResourceUri" /> | Creates or updates the provisioned cluster instance |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedClusterResourceUri" /> | Deletes the provisioned cluster instance |

## `SELECT` examples

Gets the provisioned cluster instance

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provisioned_cluster_instances', value: 'view', },
        { label: 'provisioned_cluster_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
agent_pool_profiles,
auto_scaler_profile,
cloud_provider_profile,
cluster_vm_access_profile,
connectedClusterResourceUri,
control_plane,
extended_location,
kubernetes_version,
license_profile,
linux_profile,
network_profile,
provisioning_state,
status,
storage_profile
FROM azure.hybrid_aks.vw_provisioned_cluster_instances
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
properties
FROM azure.hybrid_aks.provisioned_cluster_instances
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provisioned_cluster_instances</code> resource.

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
INSERT INTO azure.hybrid_aks.provisioned_cluster_instances (
connectedClusterResourceUri,
properties,
extendedLocation
)
SELECT 
'{{ connectedClusterResourceUri }}',
'{{ properties }}',
'{{ extendedLocation }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: linuxProfile
          value:
            - name: ssh
              value:
                - name: publicKeys
                  value:
                    - - name: keyData
                        value: string
        - name: controlPlane
          value:
            - name: count
              value: integer
            - name: vmSize
              value: string
            - name: controlPlaneEndpoint
              value:
                - name: hostIP
                  value: string
        - name: kubernetesVersion
          value: string
        - name: networkProfile
          value:
            - name: loadBalancerProfile
              value:
                - name: count
                  value: integer
            - name: networkPolicy
              value: string
            - name: podCidr
              value: string
        - name: storageProfile
          value:
            - name: smbCsiDriver
              value:
                - name: enabled
                  value: boolean
            - name: nfsCsiDriver
              value:
                - name: enabled
                  value: boolean
        - name: clusterVMAccessProfile
          value:
            - name: authorizedIPRanges
              value: string
        - name: agentPoolProfiles
          value:
            - - name: osType
                value: []
              - name: osSKU
                value: []
              - name: nodeLabels
                value: object
              - name: nodeTaints
                value:
                  - string
              - name: maxCount
                value: integer
              - name: minCount
                value: integer
              - name: enableAutoScaling
                value: boolean
              - name: maxPods
                value: integer
              - name: count
                value: integer
              - name: vmSize
                value: string
              - name: kubernetesVersion
                value: string
              - name: name
                value: string
        - name: cloudProviderProfile
          value:
            - name: infraNetworkProfile
              value:
                - name: vnetSubnetIds
                  value:
                    - string
        - name: provisioningState
          value: []
        - name: status
          value:
            - name: controlPlaneStatus
              value:
                - - name: name
                    value: string
                  - name: phase
                    value: string
                  - name: ready
                    value: boolean
                  - name: errorMessage
                    value: string
            - name: errorMessage
              value: string
        - name: licenseProfile
          value:
            - name: azureHybridBenefit
              value: string
        - name: autoScalerProfile
          value:
            - name: balance-similar-node-groups
              value: string
            - name: expander
              value: string
            - name: max-empty-bulk-delete
              value: string
            - name: max-graceful-termination-sec
              value: string
            - name: max-node-provision-time
              value: string
            - name: max-total-unready-percentage
              value: string
            - name: new-pod-scale-up-delay
              value: string
            - name: ok-total-unready-count
              value: string
            - name: scan-interval
              value: string
            - name: scale-down-delay-after-add
              value: string
            - name: scale-down-delay-after-delete
              value: string
            - name: scale-down-delay-after-failure
              value: string
            - name: scale-down-unneeded-time
              value: string
            - name: scale-down-unready-time
              value: string
            - name: scale-down-utilization-threshold
              value: string
            - name: skip-nodes-with-local-storage
              value: string
            - name: skip-nodes-with-system-pods
              value: string
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>provisioned_cluster_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_aks.provisioned_cluster_instances
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
