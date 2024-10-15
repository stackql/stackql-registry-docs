---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
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

Creates, updates, deletes, gets or lists a <code>virtual_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machines', value: 'view', },
        { label: 'virtual_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="additional_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_reservation" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag is property returned in Create/Update/Get response of the VM, so that customer can supply it in the header to ensure optimistic updates. |
| <CopyableCode code="eviction_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="extensions_time_budget" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="host" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the virtual machine. |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**. |
| <CopyableCode code="platform_fault_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="proximity_placement_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resources" /> | `text` | The virtual machine child extension resources. |
| <CopyableCode code="scheduled_events_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_events_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="user_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine_scale_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | The virtual machine zones. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Etag is property returned in Create/Update/Get response of the VM, so that customer can supply it in the header to ensure optimistic updates. |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the virtual machine. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="managedBy" /> | `string` | ManagedBy is set to Virtual Machine Scale Set(VMSS) flex ARM resourceID, if the VM is part of the VMSS. This property is used by platform for internal resource group delete optimization. |
| <CopyableCode code="plan" /> | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine. |
| <CopyableCode code="resources" /> | `array` | The virtual machine child extension resources. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | The virtual machine zones. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Retrieves information about the model view or the instance view of a virtual machine. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the virtual machines in the specified resource group. Use the nextLink property in the response to get the next page of virtual machines. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the virtual machines in the specified subscription. Use the nextLink property in the response to get the next page of virtual machines. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets all the virtual machines under the specified subscription for the specified location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to create or update a virtual machine. Please note some properties can be set only during virtual machine creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to delete a virtual machine. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to update a virtual machine. |
| <CopyableCode code="assess_patches" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Assess patches on the VM. |
| <CopyableCode code="attach_detach_data_disks" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Attach and detach data disks to/from the virtual machine. |
| <CopyableCode code="capture" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName, data__destinationContainerName, data__overwriteVhds, data__vhdPrefix" /> | Captures the VM by copying virtual hard disks of the VM and outputs a template that can be used to create similar VMs. |
| <CopyableCode code="convert_to_managed_disks" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Converts virtual machine disks from blob-based to managed disks. Virtual machine must be stop-deallocated before invoking this operation. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Shuts down the virtual machine and releases the compute resources. You are not billed for the compute resources that this virtual machine uses. |
| <CopyableCode code="generalize" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Sets the OS state of the virtual machine to generalized. It is recommended to sysprep the virtual machine before performing this operation. For Windows, please refer to [Create a managed image of a generalized VM in Azure](https://docs.microsoft.com/azure/virtual-machines/windows/capture-image-resource). For Linux, please refer to [How to create an image of a virtual machine or VHD](https://docs.microsoft.com/azure/virtual-machines/linux/capture-image). |
| <CopyableCode code="install_patches" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName, data__rebootSetting" /> | Installs patches on the VM. |
| <CopyableCode code="instance_view" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Retrieves information about the run-time state of a virtual machine. |
| <CopyableCode code="perform_maintenance" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to perform maintenance on a virtual machine. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to power off (stop) a virtual machine. The virtual machine can be restarted with the same provisioned resources. You are still charged for this virtual machine. |
| <CopyableCode code="reapply" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to reapply a virtual machine's state. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Shuts down the virtual machine, moves it to a new node, and powers it back on. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Reimages (upgrade the operating system) a virtual machine which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. NOTE: The retaining of old OS disk depends on the value of deleteOption of OS disk. If deleteOption is detach, the old OS disk will be preserved after reimage. If deleteOption is delete, the old OS disk will be deleted after reimage. The deleteOption of the OS disk should be updated accordingly before performing the reimage. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to restart a virtual machine. |
| <CopyableCode code="retrieve_boot_diagnostics_data" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to retrieve SAS URIs for a virtual machine's boot diagnostic logs. |
| <CopyableCode code="run_command" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName, data__commandId" /> | Run command on the VM. |
| <CopyableCode code="simulate_eviction" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to simulate the eviction of spot virtual machine. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to start a virtual machine. |

## `SELECT` examples

Lists all of the virtual machines in the specified subscription. Use the nextLink property in the response to get the next page of virtual machines.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machines', value: 'view', },
        { label: 'virtual_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_capabilities,
application_profile,
availability_set,
billing_profile,
capacity_reservation,
diagnostics_profile,
etag,
eviction_policy,
extended_location,
extensions_time_budget,
hardware_profile,
host,
host_group,
identity,
instance_view,
license_type,
location,
managed_by,
network_profile,
os_profile,
plan,
platform_fault_domain,
priority,
provisioning_state,
proximity_placement_group,
resourceGroupName,
resources,
scheduled_events_policy,
scheduled_events_profile,
security_profile,
storage_profile,
subscriptionId,
tags,
time_created,
type,
user_data,
virtual_machine_scale_set,
vmName,
vm_id,
zones
FROM azure.compute.vw_virtual_machines
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
managedBy,
plan,
properties,
resources,
tags,
type,
zones
FROM azure.compute.virtual_machines
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machines</code> resource.

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
INSERT INTO azure.compute.virtual_machines (
resourceGroupName,
subscriptionId,
vmName,
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
'{{ vmName }}',
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
        - name: hardwareProfile
          value:
            - name: vmSize
              value: string
            - name: vmSizeProperties
              value:
                - name: vCPUsAvailable
                  value: integer
                - name: vCPUsPerCore
                  value: integer
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
                - name: osType
                  value: string
                - name: encryptionSettings
                  value:
                    - name: diskEncryptionKey
                      value:
                        - name: secretUrl
                          value: string
                        - name: sourceVault
                          value:
                            - name: id
                              value: string
                    - name: keyEncryptionKey
                      value:
                        - name: keyUrl
                          value: string
                    - name: enabled
                      value: boolean
                - name: name
                  value: string
                - name: vhd
                  value:
                    - name: uri
                      value: string
                - name: caching
                  value: []
                - name: writeAcceleratorEnabled
                  value: boolean
                - name: diffDiskSettings
                  value:
                    - name: option
                      value: []
                    - name: placement
                      value: []
                - name: createOption
                  value: []
                - name: diskSizeGB
                  value: integer
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
                    - name: id
                      value: string
                - name: deleteOption
                  value: []
            - name: dataDisks
              value:
                - - name: lun
                    value: integer
                  - name: name
                    value: string
                  - name: writeAcceleratorEnabled
                    value: boolean
                  - name: diskSizeGB
                    value: integer
                  - name: sourceResource
                    value:
                      - name: id
                        value: string
                  - name: toBeDetached
                    value: boolean
                  - name: diskIOPSReadWrite
                    value: integer
                  - name: diskMBpsReadWrite
                    value: integer
                  - name: detachOption
                    value: []
            - name: diskControllerType
              value: []
        - name: additionalCapabilities
          value:
            - name: ultraSSDEnabled
              value: boolean
            - name: hibernationEnabled
              value: boolean
        - name: osProfile
          value:
            - name: computerName
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
                - - name: vaultCertificates
                    value:
                      - - name: certificateUrl
                          value: string
                        - name: certificateStore
                          value: string
            - name: allowExtensionOperations
              value: boolean
            - name: requireGuestProvisionSignal
              value: boolean
        - name: networkProfile
          value:
            - name: networkInterfaces
              value:
                - - name: properties
                    value:
                      - name: primary
                        value: boolean
                      - name: deleteOption
                        value: string
                  - name: id
                    value: string
            - name: networkApiVersion
              value: string
            - name: networkInterfaceConfigurations
              value:
                - - name: name
                    value: string
                  - name: properties
                    value:
                      - name: primary
                        value: boolean
                      - name: deleteOption
                        value: string
                      - name: enableAcceleratedNetworking
                        value: boolean
                      - name: disableTcpStateTracking
                        value: boolean
                      - name: enableFpga
                        value: boolean
                      - name: enableIPForwarding
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
                                        - name: deleteOption
                                          value: string
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
                                        - name: publicIPAllocationMethod
                                          value: string
                                    - name: sku
                                      value:
                                        - name: name
                                          value: string
                                        - name: tier
                                          value: string
                                - name: privateIPAddressVersion
                                  value: string
                                - name: applicationSecurityGroups
                                  value:
                                    - - name: id
                                        value: string
                                - name: applicationGatewayBackendAddressPools
                                  value:
                                    - - name: id
                                        value: string
                                - name: loadBalancerBackendAddressPools
                                  value:
                                    - - name: id
                                        value: string
                      - name: auxiliaryMode
                        value: string
                      - name: auxiliarySku
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
        - name: priority
          value: []
        - name: evictionPolicy
          value: []
        - name: billingProfile
          value:
            - name: maxPrice
              value: number
        - name: provisioningState
          value: string
        - name: instanceView
          value:
            - name: platformUpdateDomain
              value: integer
            - name: platformFaultDomain
              value: integer
            - name: computerName
              value: string
            - name: osName
              value: string
            - name: osVersion
              value: string
            - name: hyperVGeneration
              value: string
            - name: rdpThumbPrint
              value: string
            - name: vmAgent
              value:
                - name: vmAgentVersion
                  value: string
                - name: extensionHandlers
                  value:
                    - - name: type
                        value: string
                      - name: typeHandlerVersion
                        value: string
                      - name: status
                        value:
                          - name: code
                            value: string
                          - name: level
                            value: string
                          - name: displayStatus
                            value: string
                          - name: message
                            value: string
                          - name: time
                            value: string
                - name: statuses
                  value:
                    - - name: code
                        value: string
                      - name: level
                        value: string
                      - name: displayStatus
                        value: string
                      - name: message
                        value: string
                      - name: time
                        value: string
            - name: maintenanceRedeployStatus
              value:
                - name: isCustomerInitiatedMaintenanceAllowed
                  value: boolean
                - name: preMaintenanceWindowStartTime
                  value: string
                - name: preMaintenanceWindowEndTime
                  value: string
                - name: maintenanceWindowStartTime
                  value: string
                - name: maintenanceWindowEndTime
                  value: string
                - name: lastOperationResultCode
                  value: string
                - name: lastOperationMessage
                  value: string
            - name: disks
              value:
                - - name: name
                    value: string
                  - name: encryptionSettings
                    value:
                      - - name: enabled
                          value: boolean
                  - name: statuses
                    value:
                      - - name: code
                          value: string
                        - name: level
                          value: string
                        - name: displayStatus
                          value: string
                        - name: message
                          value: string
                        - name: time
                          value: string
            - name: extensions
              value:
                - - name: name
                    value: string
                  - name: type
                    value: string
                  - name: typeHandlerVersion
                    value: string
                  - name: substatuses
                    value:
                      - - name: code
                          value: string
                        - name: level
                          value: string
                        - name: displayStatus
                          value: string
                        - name: message
                          value: string
                        - name: time
                          value: string
                  - name: statuses
                    value:
                      - - name: code
                          value: string
                        - name: level
                          value: string
                        - name: displayStatus
                          value: string
                        - name: message
                          value: string
                        - name: time
                          value: string
            - name: vmHealth
              value: []
            - name: bootDiagnostics
              value:
                - name: consoleScreenshotBlobUri
                  value: string
                - name: serialConsoleLogBlobUri
                  value: string
            - name: assignedHost
              value: string
            - name: statuses
              value:
                - - name: code
                    value: string
                  - name: level
                    value: string
                  - name: displayStatus
                    value: string
                  - name: message
                    value: string
                  - name: time
                    value: string
            - name: patchStatus
              value:
                - name: availablePatchSummary
                  value:
                    - name: status
                      value: string
                    - name: assessmentActivityId
                      value: string
                    - name: rebootPending
                      value: boolean
                    - name: criticalAndSecurityPatchCount
                      value: integer
                    - name: otherPatchCount
                      value: integer
                    - name: startTime
                      value: string
                    - name: lastModifiedTime
                      value: string
                    - name: error
                      value:
                        - name: details
                          value:
                            - - name: code
                                value: string
                              - name: target
                                value: string
                              - name: message
                                value: string
                        - name: innererror
                          value:
                            - name: exceptiontype
                              value: string
                            - name: errordetail
                              value: string
                        - name: code
                          value: string
                        - name: target
                          value: string
                        - name: message
                          value: string
                - name: lastPatchInstallationSummary
                  value:
                    - name: status
                      value: string
                    - name: installationActivityId
                      value: string
                    - name: maintenanceWindowExceeded
                      value: boolean
                    - name: notSelectedPatchCount
                      value: integer
                    - name: excludedPatchCount
                      value: integer
                    - name: pendingPatchCount
                      value: integer
                    - name: installedPatchCount
                      value: integer
                    - name: failedPatchCount
                      value: integer
                    - name: startTime
                      value: string
                    - name: lastModifiedTime
                      value: string
                - name: configurationStatuses
                  value:
                    - - name: code
                        value: string
                      - name: level
                        value: string
                      - name: displayStatus
                        value: string
                      - name: message
                        value: string
                      - name: time
                        value: string
            - name: isVMInStandbyPool
              value: boolean
        - name: licenseType
          value: string
        - name: vmId
          value: string
        - name: extensionsTimeBudget
          value: string
        - name: platformFaultDomain
          value: integer
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
        - name: timeCreated
          value: string
    - name: resources
      value:
        - - name: properties
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
              - name: instanceView
                value:
                  - name: name
                    value: string
                  - name: type
                    value: string
                  - name: typeHandlerVersion
                    value: string
                  - name: substatuses
                    value:
                      - - name: code
                          value: string
                        - name: level
                          value: string
                        - name: displayStatus
                          value: string
                        - name: message
                          value: string
                        - name: time
                          value: string
                  - name: statuses
                    value:
                      - - name: code
                          value: string
                        - name: level
                          value: string
                        - name: displayStatus
                          value: string
                        - name: message
                          value: string
                        - name: time
                          value: string
              - name: suppressFailures
                value: boolean
              - name: provisionAfterExtensions
                value:
                  - string
          - name: location
            value: string
          - name: id
            value: string
          - name: name
            value: string
          - name: type
            value: string
          - name: tags
            value: object
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
    - name: managedBy
      value: string
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

Updates a <code>virtual_machines</code> resource.

```sql
/*+ update */
UPDATE azure.compute.virtual_machines
SET 
plan = '{{ plan }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
zones = '{{ zones }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmName = '{{ vmName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.virtual_machines
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmName = '{{ vmName }}';
```
