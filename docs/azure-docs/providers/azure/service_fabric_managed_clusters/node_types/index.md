---
title: node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - node_types
  - service_fabric_managed_clusters
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

Creates, updates, deletes, gets or lists a <code>node_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.node_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_node_types', value: 'view', },
        { label: 'node_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource identifier. |
| <CopyableCode code="name" /> | `text` | Azure resource name. |
| <CopyableCode code="additional_data_disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="additional_network_interface_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_ports" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacities" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="computer_name_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_disk_letter" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_disk_size_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_disk_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="dscp_configuration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_accelerated_networking" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_encryption_at_host" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_node_public_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_node_public_ipv6" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_over_provisioning" /> | `text` | field from the `properties` object |
| <CopyableCode code="ephemeral_ports" /> | `text` | field from the `properties` object |
| <CopyableCode code="eviction_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_primary" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_spot_vm" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_stateless" /> | `text` | field from the `properties` object |
| <CopyableCode code="multiple_placement_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="nat_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="nat_gateway_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_security_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="nodeTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secure_boot_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_artifact_reference_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes a node type sku. |
| <CopyableCode code="spot_restore_timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Azure resource tags. |
| <CopyableCode code="type" /> | `text` | Azure resource type. |
| <CopyableCode code="use_default_public_load_balancer" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_ephemeral_os_disk" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_temp_data_disk" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_applications" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_extensions" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image_offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image_publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_instance_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_managed_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_secrets" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_setup_actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_shared_gallery_image_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="properties" /> | `object` | Describes a node type in the cluster, each node type represents sub set of nodes in the cluster. |
| <CopyableCode code="sku" /> | `object` | Describes a node type sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Get a Service Fabric node type of a given managed cluster. |
| <CopyableCode code="list_by_managed_clusters" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets all Node types of the specified managed cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Create or update a Service Fabric node type of a given managed cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric node type of a given managed cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Update the configuration of a node type of a given managed cluster, only updating tags. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Reimages one or more nodes on the node type. It will disable the fabric nodes, trigger a reimage on the VMs and activate the nodes back again. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Restarts one or more nodes on the node type. It will disable the fabric nodes, trigger a restart on the VMs and activate the nodes back again. |

## `SELECT` examples

Gets all Node types of the specified managed cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_node_types', value: 'view', },
        { label: 'node_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_data_disks,
additional_network_interface_configurations,
application_ports,
capacities,
clusterName,
computer_name_prefix,
data_disk_letter,
data_disk_size_gb,
data_disk_type,
dscp_configuration_id,
enable_accelerated_networking,
enable_encryption_at_host,
enable_node_public_ip,
enable_node_public_ipv6,
enable_over_provisioning,
ephemeral_ports,
eviction_policy,
frontend_configurations,
host_group_id,
is_primary,
is_spot_vm,
is_stateless,
multiple_placement_groups,
nat_configurations,
nat_gateway_id,
network_security_rules,
nodeTypeName,
placement_properties,
provisioning_state,
resourceGroupName,
secure_boot_enabled,
security_type,
service_artifact_reference_id,
sku,
spot_restore_timeout,
subnet_id,
subscriptionId,
system_data,
tags,
type,
use_default_public_load_balancer,
use_ephemeral_os_disk,
use_temp_data_disk,
vm_applications,
vm_extensions,
vm_image_offer,
vm_image_plan,
vm_image_publisher,
vm_image_resource_id,
vm_image_sku,
vm_image_version,
vm_instance_count,
vm_managed_identity,
vm_secrets,
vm_setup_actions,
vm_shared_gallery_image_id,
vm_size,
zones
FROM azure.service_fabric_managed_clusters.vw_node_types
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
sku,
systemData,
tags,
type
FROM azure.service_fabric_managed_clusters.node_types
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>node_types</code> resource.

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
INSERT INTO azure.service_fabric_managed_clusters.node_types (
clusterName,
nodeTypeName,
resourceGroupName,
subscriptionId,
tags,
systemData,
properties,
sku
)
SELECT 
'{{ clusterName }}',
'{{ nodeTypeName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ systemData }}',
'{{ properties }}',
'{{ sku }}'
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
    - name: tags
      value: object
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: isPrimary
          value: boolean
        - name: vmInstanceCount
          value: integer
        - name: dataDiskSizeGB
          value: integer
        - name: dataDiskType
          value: []
        - name: dataDiskLetter
          value: string
        - name: placementProperties
          value: object
        - name: capacities
          value: object
        - name: applicationPorts
          value:
            - name: startPort
              value: integer
            - name: endPort
              value: integer
        - name: vmSize
          value: string
        - name: vmImagePublisher
          value: string
        - name: vmImageOffer
          value: string
        - name: vmImageSku
          value: string
        - name: vmImageVersion
          value: string
        - name: vmSecrets
          value:
            - - name: sourceVault
                value:
                  - name: id
                    value: string
              - name: vaultCertificates
                value:
                  - - name: certificateUrl
                      value: string
                    - name: certificateStore
                      value: string
        - name: vmExtensions
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: publisher
                    value: string
                  - name: type
                    value: string
                  - name: typeHandlerVersion
                    value: string
                  - name: autoUpgradeMinorVersion
                    value: boolean
                  - name: settings
                    value: object
                  - name: protectedSettings
                    value: object
                  - name: forceUpdateTag
                    value: string
                  - name: provisionAfterExtensions
                    value:
                      - string
                  - name: provisioningState
                    value: string
                  - name: enableAutomaticUpgrade
                    value: boolean
                  - name: setupOrder
                    value:
                      - []
        - name: vmManagedIdentity
          value:
            - name: userAssignedIdentities
              value:
                - string
        - name: isStateless
          value: boolean
        - name: multiplePlacementGroups
          value: boolean
        - name: frontendConfigurations
          value:
            - - name: ipAddressType
                value: []
              - name: loadBalancerBackendAddressPoolId
                value: string
              - name: loadBalancerInboundNatPoolId
                value: string
              - name: applicationGatewayBackendAddressPoolId
                value: string
        - name: networkSecurityRules
          value:
            - - name: name
                value: string
              - name: description
                value: string
              - name: protocol
                value: string
              - name: sourceAddressPrefixes
                value:
                  - string
              - name: destinationAddressPrefixes
                value:
                  - string
              - name: sourcePortRanges
                value:
                  - string
              - name: destinationPortRanges
                value:
                  - string
              - name: sourceAddressPrefix
                value: string
              - name: destinationAddressPrefix
                value: string
              - name: sourcePortRange
                value: string
              - name: destinationPortRange
                value: string
              - name: access
                value: string
              - name: priority
                value: integer
              - name: direction
                value: string
        - name: additionalDataDisks
          value:
            - - name: lun
                value: integer
              - name: diskSizeGB
                value: integer
              - name: diskLetter
                value: string
        - name: enableEncryptionAtHost
          value: boolean
        - name: provisioningState
          value: []
        - name: enableAcceleratedNetworking
          value: boolean
        - name: useDefaultPublicLoadBalancer
          value: boolean
        - name: useTempDataDisk
          value: boolean
        - name: enableOverProvisioning
          value: boolean
        - name: zones
          value:
            - string
        - name: isSpotVM
          value: boolean
        - name: hostGroupId
          value: string
        - name: useEphemeralOSDisk
          value: boolean
        - name: spotRestoreTimeout
          value: string
        - name: evictionPolicy
          value: []
        - name: vmImageResourceId
          value: string
        - name: subnetId
          value: string
        - name: vmSetupActions
          value:
            - []
        - name: securityType
          value: string
        - name: secureBootEnabled
          value: boolean
        - name: enableNodePublicIP
          value: boolean
        - name: enableNodePublicIPv6
          value: boolean
        - name: vmSharedGalleryImageId
          value: string
        - name: natGatewayId
          value: string
        - name: natConfigurations
          value:
            - - name: backendPort
                value: integer
              - name: frontendPortRangeStart
                value: integer
              - name: frontendPortRangeEnd
                value: integer
        - name: vmImagePlan
          value:
            - name: name
              value: string
            - name: product
              value: string
            - name: promotionCode
              value: string
            - name: publisher
              value: string
        - name: serviceArtifactReferenceId
          value: string
        - name: dscpConfigurationId
          value: string
        - name: additionalNetworkInterfaceConfigurations
          value:
            - - name: name
                value: string
              - name: enableAcceleratedNetworking
                value: boolean
              - name: ipConfigurations
                value:
                  - - name: name
                      value: string
                    - name: applicationGatewayBackendAddressPools
                      value:
                        - - name: id
                            value: string
                    - name: loadBalancerBackendAddressPools
                      value:
                        - - name: id
                            value: string
                    - name: loadBalancerInboundNatPools
                      value:
                        - - name: id
                            value: string
                    - name: privateIPAddressVersion
                      value: string
                    - name: publicIPAddressConfiguration
                      value:
                        - name: name
                          value: string
                        - name: ipTags
                          value:
                            - - name: ipTagType
                                value: string
                              - name: tag
                                value: string
                        - name: publicIPAddressVersion
                          value: string
        - name: computerNamePrefix
          value: string
        - name: vmApplications
          value:
            - - name: configurationReference
                value: string
              - name: enableAutomaticUpgrade
                value: boolean
              - name: order
                value: integer
              - name: packageReferenceId
                value: string
              - name: vmGalleryTags
                value: string
              - name: treatFailureAsDeploymentFailure
                value: boolean
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>node_types</code> resource.

```sql
/*+ update */
UPDATE azure.service_fabric_managed_clusters.node_types
SET 
tags = '{{ tags }}',
sku = '{{ sku }}'
WHERE 
clusterName = '{{ clusterName }}'
AND nodeTypeName = '{{ nodeTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>node_types</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_managed_clusters.node_types
WHERE clusterName = '{{ clusterName }}'
AND nodeTypeName = '{{ nodeTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
