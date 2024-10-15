---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - batch
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

Creates, updates, deletes, gets or lists a <code>pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pools', value: 'view', },
        { label: 'pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="allocation_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="allocation_state_transition_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_licenses" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_packages" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_scale_run" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificates" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_dedicated_nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_low_priority_nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_node_communication_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="identity" /> | `text` | The identity of the Batch pool, if configured. If the pool identity is updated during update an existing pool, only the new vms which are created after the pool shrinks to 0 will have the updated identities |
| <CopyableCode code="inter_node_communication" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="mount_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state_transition_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resize_operation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_task" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="target_node_communication_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="task_scheduling_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="task_slots_per_node" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="upgrade_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_size" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="identity" /> | `object` | The identity of the Batch pool, if configured. If the pool identity is updated during update an existing pool, only the new vms which are created after the pool shrinks to 0 will have the updated identities |
| <CopyableCode code="properties" /> | `object` | Pool properties. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Gets information about the specified pool. |
| <CopyableCode code="list_by_batch_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all of the pools in the specified account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Creates a new pool inside the specified account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Deletes the specified pool. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing pool. |
| <CopyableCode code="disable_auto_scale" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Disables automatic scaling for a pool. |
| <CopyableCode code="stop_resize" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. After stopping, the pool stabilizes at the number of nodes it was at when the stop operation was done. During the stop operation, the pool allocation state changes first to stopping and then to steady. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created. |

## `SELECT` examples

Lists all of the pools in the specified account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pools', value: 'view', },
        { label: 'pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
allocation_state,
allocation_state_transition_time,
application_licenses,
application_packages,
auto_scale_run,
certificates,
creation_time,
current_dedicated_nodes,
current_low_priority_nodes,
current_node_communication_mode,
deployment_configuration,
display_name,
etag,
identity,
inter_node_communication,
last_modified,
metadata,
mount_configuration,
network_configuration,
poolName,
provisioning_state,
provisioning_state_transition_time,
resize_operation_status,
resourceGroupName,
resource_tags,
scale_settings,
start_task,
subscriptionId,
tags,
target_node_communication_mode,
task_scheduling_policy,
task_slots_per_node,
type,
upgrade_policy,
user_accounts,
vm_size
FROM azure.batch.vw_pools
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
properties,
tags,
type
FROM azure.batch.pools
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pools</code> resource.

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
INSERT INTO azure.batch.pools (
accountName,
poolName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags
)
SELECT 
'{{ accountName }}',
'{{ poolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: displayName
          value: string
        - name: lastModified
          value: string
        - name: creationTime
          value: string
        - name: provisioningState
          value: string
        - name: provisioningStateTransitionTime
          value: string
        - name: allocationState
          value: string
        - name: allocationStateTransitionTime
          value: string
        - name: vmSize
          value: string
        - name: deploymentConfiguration
          value:
            - name: virtualMachineConfiguration
              value:
                - name: imageReference
                  value:
                    - name: publisher
                      value: string
                    - name: offer
                      value: string
                    - name: sku
                      value: string
                    - name: version
                      value: string
                    - name: id
                      value: string
                    - name: sharedGalleryImageId
                      value: string
                    - name: communityGalleryImageId
                      value: string
                - name: nodeAgentSkuId
                  value: string
                - name: windowsConfiguration
                  value:
                    - name: enableAutomaticUpdates
                      value: boolean
                - name: dataDisks
                  value:
                    - - name: lun
                        value: integer
                      - name: caching
                        value: []
                      - name: diskSizeGB
                        value: integer
                      - name: storageAccountType
                        value: []
                - name: licenseType
                  value: string
                - name: containerConfiguration
                  value:
                    - name: type
                      value: string
                    - name: containerImageNames
                      value:
                        - string
                    - name: containerRegistries
                      value:
                        - - name: username
                            value: string
                          - name: password
                            value: string
                          - name: registryServer
                            value: string
                          - name: identityReference
                            value:
                              - name: resourceId
                                value: string
                - name: diskEncryptionConfiguration
                  value:
                    - name: targets
                      value:
                        - string
                - name: nodePlacementConfiguration
                  value:
                    - name: policy
                      value: []
                - name: extensions
                  value:
                    - - name: name
                        value: string
                      - name: publisher
                        value: string
                      - name: type
                        value: string
                      - name: typeHandlerVersion
                        value: string
                      - name: autoUpgradeMinorVersion
                        value: boolean
                      - name: enableAutomaticUpgrade
                        value: boolean
                      - name: settings
                        value: object
                      - name: protectedSettings
                        value: object
                      - name: provisionAfterExtensions
                        value:
                          - string
                - name: osDisk
                  value:
                    - name: ephemeralOSDiskSettings
                      value:
                        - name: placement
                          value: []
                    - name: managedDisk
                      value:
                        - name: securityProfile
                          value:
                            - name: securityEncryptionType
                              value: string
                    - name: diskSizeGB
                      value: integer
                    - name: writeAcceleratorEnabled
                      value: boolean
                - name: securityProfile
                  value:
                    - name: securityType
                      value: string
                    - name: encryptionAtHost
                      value: boolean
                    - name: uefiSettings
                      value:
                        - name: secureBootEnabled
                          value: boolean
                        - name: vTpmEnabled
                          value: boolean
                - name: serviceArtifactReference
                  value:
                    - name: id
                      value: string
        - name: currentDedicatedNodes
          value: integer
        - name: currentLowPriorityNodes
          value: integer
        - name: scaleSettings
          value:
            - name: fixedScale
              value:
                - name: resizeTimeout
                  value: string
                - name: targetDedicatedNodes
                  value: integer
                - name: targetLowPriorityNodes
                  value: integer
                - name: nodeDeallocationOption
                  value: []
            - name: autoScale
              value:
                - name: formula
                  value: string
                - name: evaluationInterval
                  value: string
        - name: autoScaleRun
          value:
            - name: evaluationTime
              value: string
            - name: results
              value: string
            - name: error
              value:
                - name: code
                  value: string
                - name: message
                  value: string
                - name: details
                  value:
                    - - name: code
                        value: string
                      - name: message
                        value: string
                      - name: details
                        value:
                          - - name: code
                              value: string
                            - name: message
                              value: string
                            - name: details
                              value:
                                - - name: code
                                    value: string
                                  - name: message
                                    value: string
                                  - name: details
                                    value:
                                      - - name: code
                                          value: string
                                        - name: message
                                          value: string
                                        - name: details
                                          value:
                                            - - name: code
                                                value: string
                                              - name: message
                                                value: string
                                              - name: details
                                                value:
                                                  - - name: code
                                                      value: string
                                                    - name: message
                                                      value: string
                                                    - name: details
                                                      value:
                                                        - - name: code
                                                            value: string
                                                          - name: message
                                                            value: string
                                                          - name: details
                                                            value:
                                                              - []
        - name: interNodeCommunication
          value: string
        - name: networkConfiguration
          value:
            - name: subnetId
              value: string
            - name: dynamicVnetAssignmentScope
              value: string
            - name: endpointConfiguration
              value:
                - name: inboundNatPools
                  value:
                    - - name: name
                        value: string
                      - name: protocol
                        value: string
                      - name: backendPort
                        value: integer
                      - name: frontendPortRangeStart
                        value: integer
                      - name: frontendPortRangeEnd
                        value: integer
                      - name: networkSecurityGroupRules
                        value:
                          - - name: priority
                              value: integer
                            - name: access
                              value: string
                            - name: sourceAddressPrefix
                              value: string
                            - name: sourcePortRanges
                              value:
                                - string
            - name: publicIPAddressConfiguration
              value:
                - name: provision
                  value: []
                - name: ipAddressIds
                  value:
                    - string
            - name: enableAcceleratedNetworking
              value: boolean
        - name: taskSlotsPerNode
          value: integer
        - name: taskSchedulingPolicy
          value:
            - name: nodeFillType
              value: string
        - name: userAccounts
          value:
            - - name: name
                value: string
              - name: password
                value: string
              - name: elevationLevel
                value: []
              - name: linuxUserConfiguration
                value:
                  - name: uid
                    value: integer
                  - name: gid
                    value: integer
                  - name: sshPrivateKey
                    value: string
              - name: windowsUserConfiguration
                value:
                  - name: loginMode
                    value: string
        - name: metadata
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: startTask
          value:
            - name: commandLine
              value: string
            - name: resourceFiles
              value:
                - - name: autoStorageContainerName
                    value: string
                  - name: storageContainerUrl
                    value: string
                  - name: httpUrl
                    value: string
                  - name: blobPrefix
                    value: string
                  - name: filePath
                    value: string
                  - name: fileMode
                    value: string
            - name: environmentSettings
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
            - name: userIdentity
              value:
                - name: userName
                  value: string
                - name: autoUser
                  value:
                    - name: scope
                      value: string
            - name: maxTaskRetryCount
              value: integer
            - name: waitForSuccess
              value: boolean
            - name: containerSettings
              value:
                - name: containerRunOptions
                  value: string
                - name: imageName
                  value: string
                - name: registry
                  value:
                    - name: username
                      value: string
                    - name: password
                      value: string
                    - name: registryServer
                      value: string
                - name: workingDirectory
                  value: string
                - name: containerHostBatchBindMounts
                  value:
                    - - name: source
                        value: []
                      - name: isReadOnly
                        value: boolean
        - name: certificates
          value:
            - - name: id
                value: string
              - name: storeLocation
                value: string
              - name: storeName
                value: string
              - name: visibility
                value:
                  - string
        - name: applicationPackages
          value:
            - - name: id
                value: string
              - name: version
                value: string
        - name: applicationLicenses
          value:
            - string
        - name: resizeOperationStatus
          value:
            - name: targetDedicatedNodes
              value: integer
            - name: targetLowPriorityNodes
              value: integer
            - name: resizeTimeout
              value: string
            - name: startTime
              value: string
            - name: errors
              value:
                - - name: code
                    value: string
                  - name: message
                    value: string
                  - name: details
                    value:
                      - - name: code
                          value: string
                        - name: message
                          value: string
                        - name: details
                          value:
                            - - name: code
                                value: string
                              - name: message
                                value: string
                              - name: details
                                value:
                                  - - name: code
                                      value: string
                                    - name: message
                                      value: string
                                    - name: details
                                      value:
                                        - - name: code
                                            value: string
                                          - name: message
                                            value: string
                                          - name: details
                                            value:
                                              - - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                                - name: details
                                                  value:
                                                    - - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                      - name: details
                                                        value:
                                                          - - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                            - name: details
                                                              value:
                                                                - []
        - name: mountConfiguration
          value:
            - - name: azureBlobFileSystemConfiguration
                value:
                  - name: accountName
                    value: string
                  - name: containerName
                    value: string
                  - name: accountKey
                    value: string
                  - name: sasKey
                    value: string
                  - name: blobfuseOptions
                    value: string
                  - name: relativeMountPath
                    value: string
              - name: nfsMountConfiguration
                value:
                  - name: source
                    value: string
                  - name: relativeMountPath
                    value: string
                  - name: mountOptions
                    value: string
              - name: cifsMountConfiguration
                value:
                  - name: userName
                    value: string
                  - name: source
                    value: string
                  - name: relativeMountPath
                    value: string
                  - name: mountOptions
                    value: string
                  - name: password
                    value: string
              - name: azureFileShareConfiguration
                value:
                  - name: accountName
                    value: string
                  - name: azureFileUrl
                    value: string
                  - name: accountKey
                    value: string
                  - name: relativeMountPath
                    value: string
                  - name: mountOptions
                    value: string
        - name: targetNodeCommunicationMode
          value: []
        - name: upgradePolicy
          value:
            - name: mode
              value: string
            - name: automaticOSUpgradePolicy
              value:
                - name: disableAutomaticRollback
                  value: boolean
                - name: enableAutomaticOSUpgrade
                  value: boolean
                - name: useRollingUpgradePolicy
                  value: boolean
                - name: osRollingUpgradeDeferral
                  value: boolean
            - name: rollingUpgradePolicy
              value:
                - name: enableCrossZoneUpgrade
                  value: boolean
                - name: maxBatchInstancePercent
                  value: integer
                - name: maxUnhealthyInstancePercent
                  value: integer
                - name: maxUnhealthyUpgradedInstancePercent
                  value: integer
                - name: pauseTimeBetweenBatches
                  value: string
                - name: prioritizeUnhealthyInstances
                  value: boolean
                - name: rollbackFailedInstancesOnPolicyBreach
                  value: boolean
        - name: resourceTags
          value: object
    - name: identity
      value:
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pools</code> resource.

```sql
/*+ update */
UPDATE azure.batch.pools
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.batch.pools
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
