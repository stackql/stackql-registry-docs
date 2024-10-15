---
title: virtual_machine_scale_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_scale_sets', value: 'view', },
        { label: 'virtual_machine_scale_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="additional_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="automatic_repairs_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="constrained_maximum_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="do_not_run_extensions_on_overprovisioned_vms" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag is property returned in Create/Update/Get response of the VMSS, so that customer can supply it in the header to ensure optimistic updates |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the virtual machine scale set. |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="orchestration_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="overprovision" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**. |
| <CopyableCode code="platform_fault_domain_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority_mix_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="proximity_placement_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="resiliency_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_in_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_events_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="single_placement_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="sku_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="spot_restore_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="unique_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="upgrade_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmScaleSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="zonal_platform_fault_domain_align_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_balance" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | The virtual machine scale set zones. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Etag is property returned in Create/Update/Get response of the VMSS, so that customer can supply it in the header to ensure optimistic updates |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the virtual machine scale set. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="plan" /> | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Scale Set. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | The virtual machine scale set zones. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Display information about a virtual machine scale set. |
| <CopyableCode code="get_instance_view" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Gets the status of a VM scale set instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of all VM scale sets under a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of VM Scale Sets. Do this till nextLink is null to fetch all the VM Scale Sets. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets all the VM scale sets under the specified subscription for the specified location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Create or update a VM scale set. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Deletes a VM scale set. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Update a VM scale set. |
| <CopyableCode code="approve_rolling_upgrade" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Approve upgrade on deferred rolling upgrades for OS disks in the virtual machines in a VM scale set. |
| <CopyableCode code="convert_to_single_placement_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Converts SinglePlacementGroup property to false for a existing virtual machine scale set. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates. |
| <CopyableCode code="delete_instances" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName, data__instanceIds" /> | Deletes virtual machines in a VM scale set. |
| <CopyableCode code="force_recovery_service_fabric_platform_update_domain_walk" /> | `EXEC` | <CopyableCode code="platformUpdateDomain, resourceGroupName, subscriptionId, vmScaleSetName" /> | Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set. |
| <CopyableCode code="perform_maintenance" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Perform maintenance on one or more virtual machines in a VM scale set. Operation on instances which are not eligible for perform maintenance will be failed. Please refer to best practices for more details: https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maintenance-notifications |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges. |
| <CopyableCode code="reapply" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Reapplies the Virtual Machine Scale Set Virtual Machine Profile to the Virtual Machine Instances |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. |
| <CopyableCode code="reimage_all" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Restarts one or more virtual machines in a VM scale set. |
| <CopyableCode code="set_orchestration_service_state" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName, data__action, data__serviceName" /> | Changes ServiceState property for a given service |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Starts one or more virtual machines in a VM scale set. |

## `SELECT` examples

Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group. Use nextLink property in the response to get the next page of VM Scale Sets. Do this till nextLink is null to fetch all the VM Scale Sets.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_scale_sets', value: 'view', },
        { label: 'virtual_machine_scale_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_capabilities,
automatic_repairs_policy,
constrained_maximum_capacity,
do_not_run_extensions_on_overprovisioned_vms,
etag,
extended_location,
host_group,
identity,
location,
orchestration_mode,
overprovision,
plan,
platform_fault_domain_count,
priority_mix_policy,
provisioning_state,
proximity_placement_group,
resiliency_policy,
resourceGroupName,
scale_in_policy,
scheduled_events_policy,
single_placement_group,
sku,
sku_profile,
spot_restore_policy,
subscriptionId,
tags,
time_created,
type,
unique_id,
upgrade_policy,
virtual_machine_profile,
vmScaleSetName,
zonal_platform_fault_domain_align_mode,
zone_balance,
zones
FROM azure.compute.vw_virtual_machine_scale_sets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
extendedLocation,
identity,
location,
plan,
properties,
sku,
tags,
type,
zones
FROM azure.compute.virtual_machine_scale_sets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_scale_sets</code> resource.

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
INSERT INTO azure.compute.virtual_machine_scale_sets (
resourceGroupName,
subscriptionId,
vmScaleSetName,
sku,
plan,
properties,
identity,
zones,
extendedLocation,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vmScaleSetName }}',
'{{ sku }}',
'{{ plan }}',
'{{ properties }}',
'{{ identity }}',
'{{ zones }}',
'{{ extendedLocation }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer
    - name: plan
      value:
        - name: name
          value: string
        - name: publisher
          value: string
        - name: product
          value: string
        - name: promotionCode
          value: string
    - name: properties
      value:
        - name: upgradePolicy
          value:
            - name: mode
              value: string
            - name: rollingUpgradePolicy
              value:
                - name: maxBatchInstancePercent
                  value: integer
                - name: maxUnhealthyInstancePercent
                  value: integer
                - name: maxUnhealthyUpgradedInstancePercent
                  value: integer
                - name: pauseTimeBetweenBatches
                  value: string
                - name: enableCrossZoneUpgrade
                  value: boolean
                - name: prioritizeUnhealthyInstances
                  value: boolean
                - name: rollbackFailedInstancesOnPolicyBreach
                  value: boolean
                - name: maxSurge
                  value: boolean
            - name: automaticOSUpgradePolicy
              value:
                - name: enableAutomaticOSUpgrade
                  value: boolean
                - name: disableAutomaticRollback
                  value: boolean
                - name: useRollingUpgradePolicy
                  value: boolean
                - name: osRollingUpgradeDeferral
                  value: boolean
        - name: scheduledEventsPolicy
          value:
            - name: userInitiatedRedeploy
              value:
                - name: automaticallyApprove
                  value: boolean
            - name: userInitiatedReboot
              value:
                - name: automaticallyApprove
                  value: boolean
            - name: scheduledEventsAdditionalPublishingTargets
              value:
                - name: eventGridAndResourceGraph
                  value:
                    - name: enable
                      value: boolean
        - name: automaticRepairsPolicy
          value:
            - name: enabled
              value: boolean
            - name: gracePeriod
              value: string
            - name: repairAction
              value: string
        - name: virtualMachineProfile
          value:
            - name: osProfile
              value:
                - name: computerNamePrefix
                  value: string
                - name: adminUsername
                  value: string
                - name: adminPassword
                  value: string
                - name: customData
                  value: string
                - name: windowsConfiguration
                  value:
                    - name: provisionVMAgent
                      value: boolean
                    - name: enableAutomaticUpdates
                      value: boolean
                    - name: timeZone
                      value: string
                    - name: additionalUnattendContent
                      value:
                        - - name: passName
                            value: string
                          - name: componentName
                            value: string
                          - name: settingName
                            value: string
                          - name: content
                            value: string
                    - name: patchSettings
                      value:
                        - name: patchMode
                          value: string
                        - name: enableHotpatching
                          value: boolean
                        - name: assessmentMode
                          value: string
                        - name: automaticByPlatformSettings
                          value:
                            - name: rebootSetting
                              value: string
                            - name: bypassPlatformSafetyChecksOnUserSchedule
                              value: boolean
                    - name: winRM
                      value:
                        - name: listeners
                          value:
                            - - name: protocol
                                value: string
                              - name: certificateUrl
                                value: string
                    - name: enableVMAgentPlatformUpdates
                      value: boolean
                - name: linuxConfiguration
                  value:
                    - name: disablePasswordAuthentication
                      value: boolean
                    - name: ssh
                      value:
                        - name: publicKeys
                          value:
                            - - name: path
                                value: string
                              - name: keyData
                                value: string
                    - name: provisionVMAgent
                      value: boolean
                    - name: patchSettings
                      value:
                        - name: patchMode
                          value: string
                        - name: assessmentMode
                          value: string
                        - name: automaticByPlatformSettings
                          value:
                            - name: rebootSetting
                              value: string
                            - name: bypassPlatformSafetyChecksOnUserSchedule
                              value: boolean
                    - name: enableVMAgentPlatformUpdates
                      value: boolean
                - name: secrets
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
                - name: allowExtensionOperations
                  value: boolean
                - name: requireGuestProvisionSignal
                  value: boolean
            - name: storageProfile
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
                    - name: exactVersion
                      value: string
                    - name: sharedGalleryImageId
                      value: string
                    - name: communityGalleryImageId
                      value: string
                    - name: id
                      value: string
                - name: osDisk
                  value:
                    - name: name
                      value: string
                    - name: caching
                      value: []
                    - name: writeAcceleratorEnabled
                      value: boolean
                    - name: createOption
                      value: []
                    - name: diffDiskSettings
                      value:
                        - name: option
                          value: []
                        - name: placement
                          value: []
                    - name: diskSizeGB
                      value: integer
                    - name: osType
                      value: string
                    - name: image
                      value:
                        - name: uri
                          value: string
                    - name: vhdContainers
                      value:
                        - string
                    - name: managedDisk
                      value:
                        - name: storageAccountType
                          value: []
                        - name: diskEncryptionSet
                          value:
                            - name: id
                              value: string
                        - name: securityProfile
                          value:
                            - name: securityEncryptionType
                              value: string
                    - name: deleteOption
                      value: []
                - name: dataDisks
                  value:
                    - - name: name
                        value: string
                      - name: lun
                        value: integer
                      - name: writeAcceleratorEnabled
                        value: boolean
                      - name: diskSizeGB
                        value: integer
                      - name: diskIOPSReadWrite
                        value: integer
                      - name: diskMBpsReadWrite
                        value: integer
                - name: diskControllerType
                  value: string
            - name: networkProfile
              value:
                - name: healthProbe
                  value:
                    - name: id
                      value: string
                - name: networkInterfaceConfigurations
                  value:
                    - - name: name
                        value: string
                      - name: properties
                        value:
                          - name: primary
                            value: boolean
                          - name: enableAcceleratedNetworking
                            value: boolean
                          - name: disableTcpStateTracking
                            value: boolean
                          - name: enableFpga
                            value: boolean
                          - name: dnsSettings
                            value:
                              - name: dnsServers
                                value:
                                  - string
                          - name: ipConfigurations
                            value:
                              - - name: name
                                  value: string
                                - name: properties
                                  value:
                                    - name: primary
                                      value: boolean
                                    - name: publicIPAddressConfiguration
                                      value:
                                        - name: name
                                          value: string
                                        - name: properties
                                          value:
                                            - name: idleTimeoutInMinutes
                                              value: integer
                                            - name: dnsSettings
                                              value:
                                                - name: domainNameLabel
                                                  value: string
                                                - name: domainNameLabelScope
                                                  value: string
                                            - name: ipTags
                                              value:
                                                - - name: ipTagType
                                                    value: string
                                                  - name: tag
                                                    value: string
                                            - name: publicIPAddressVersion
                                              value: string
                                            - name: deleteOption
                                              value: string
                                        - name: sku
                                          value:
                                            - name: name
                                              value: string
                                            - name: tier
                                              value: string
                                    - name: privateIPAddressVersion
                                      value: string
                                    - name: applicationGatewayBackendAddressPools
                                      value:
                                        - - name: id
                                            value: string
                                    - name: applicationSecurityGroups
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
                          - name: enableIPForwarding
                            value: boolean
                          - name: deleteOption
                            value: string
                          - name: auxiliaryMode
                            value: string
                          - name: auxiliarySku
                            value: string
                - name: networkApiVersion
                  value: string
            - name: securityProfile
              value:
                - name: uefiSettings
                  value:
                    - name: secureBootEnabled
                      value: boolean
                    - name: vTpmEnabled
                      value: boolean
                - name: encryptionAtHost
                  value: boolean
                - name: securityType
                  value: string
                - name: encryptionIdentity
                  value:
                    - name: userAssignedIdentityResourceId
                      value: string
                - name: proxyAgentSettings
                  value:
                    - name: enabled
                      value: boolean
                    - name: mode
                      value: string
                    - name: keyIncarnationId
                      value: integer
            - name: diagnosticsProfile
              value:
                - name: bootDiagnostics
                  value:
                    - name: enabled
                      value: boolean
                    - name: storageUri
                      value: string
            - name: extensionProfile
              value:
                - name: extensions
                  value:
                    - - name: name
                        value: string
                      - name: type
                        value: string
                      - name: properties
                        value:
                          - name: forceUpdateTag
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
                          - name: provisioningState
                            value: string
                          - name: provisionAfterExtensions
                            value:
                              - string
                          - name: suppressFailures
                            value: boolean
                          - name: protectedSettingsFromKeyVault
                            value:
                              - name: secretUrl
                                value: string
                      - name: id
                        value: string
                - name: extensionsTimeBudget
                  value: string
            - name: licenseType
              value: string
            - name: priority
              value: []
            - name: evictionPolicy
              value: []
            - name: billingProfile
              value:
                - name: maxPrice
                  value: number
            - name: scheduledEventsProfile
              value:
                - name: terminateNotificationProfile
                  value:
                    - name: notBeforeTimeout
                      value: string
                    - name: enable
                      value: boolean
                - name: osImageNotificationProfile
                  value:
                    - name: notBeforeTimeout
                      value: string
                    - name: enable
                      value: boolean
            - name: userData
              value: string
            - name: capacityReservation
              value: []
            - name: applicationProfile
              value:
                - name: galleryApplications
                  value:
                    - - name: tags
                        value: string
                      - name: order
                        value: integer
                      - name: packageReferenceId
                        value: string
                      - name: configurationReference
                        value: string
                      - name: treatFailureAsDeploymentFailure
                        value: boolean
                      - name: enableAutomaticUpgrade
                        value: boolean
            - name: hardwareProfile
              value:
                - name: vmSizeProperties
                  value:
                    - name: vCPUsAvailable
                      value: integer
                    - name: vCPUsPerCore
                      value: integer
            - name: serviceArtifactReference
              value:
                - name: id
                  value: string
            - name: securityPostureReference
              value:
                - name: id
                  value: string
                - name: excludeExtensions
                  value:
                    - string
                - name: isOverridable
                  value: boolean
            - name: timeCreated
              value: string
        - name: provisioningState
          value: string
        - name: overprovision
          value: boolean
        - name: doNotRunExtensionsOnOverprovisionedVMs
          value: boolean
        - name: uniqueId
          value: string
        - name: singlePlacementGroup
          value: boolean
        - name: zoneBalance
          value: boolean
        - name: platformFaultDomainCount
          value: integer
        - name: additionalCapabilities
          value:
            - name: ultraSSDEnabled
              value: boolean
            - name: hibernationEnabled
              value: boolean
        - name: scaleInPolicy
          value:
            - name: rules
              value:
                - string
            - name: forceDeletion
              value: boolean
        - name: orchestrationMode
          value: []
        - name: spotRestorePolicy
          value:
            - name: enabled
              value: boolean
            - name: restoreTimeout
              value: string
        - name: priorityMixPolicy
          value:
            - name: baseRegularPriorityCount
              value: integer
            - name: regularPriorityPercentageAboveBase
              value: integer
        - name: timeCreated
          value: string
        - name: constrainedMaximumCapacity
          value: boolean
        - name: resiliencyPolicy
          value:
            - name: resilientVMCreationPolicy
              value:
                - name: enabled
                  value: boolean
            - name: resilientVMDeletionPolicy
              value:
                - name: enabled
                  value: boolean
        - name: zonalPlatformFaultDomainAlignMode
          value: []
        - name: skuProfile
          value:
            - name: vmSizes
              value:
                - - name: name
                    value: string
            - name: allocationStrategy
              value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: []
    - name: zones
      value:
        - string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_scale_sets</code> resource.

```sql
/*+ update */
UPDATE azure.compute.virtual_machine_scale_sets
SET 
sku = '{{ sku }}',
plan = '{{ plan }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
zones = '{{ zones }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_scale_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.virtual_machine_scale_sets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```
