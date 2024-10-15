---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
  - azure_fleet
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

Creates, updates, deletes, gets or lists a <code>fleets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_fleet.fleets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fleets', value: 'view', },
        { label: 'fleets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="compute_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="fleetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="plan" /> | `text` | Plan for the resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="regular_priority_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spot_priority_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="unique_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_sizes_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | Zones in which the Compute Fleet is available |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Details of the Compute Fleet. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | Zones in which the Compute Fleet is available |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Get a Fleet |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Fleet resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Fleet resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Create a Fleet |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Delete a Fleet |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | Update a Fleet |

## `SELECT` examples

List Fleet resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fleets', value: 'view', },
        { label: 'fleets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
compute_profile,
fleetName,
identity,
location,
plan,
provisioning_state,
regular_priority_profile,
resourceGroupName,
spot_priority_profile,
subscriptionId,
tags,
time_created,
unique_id,
vm_sizes_profile,
zones
FROM azure.azure_fleet.vw_fleets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
plan,
properties,
tags,
zones
FROM azure.azure_fleet.fleets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fleets</code> resource.

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
INSERT INTO azure.azure_fleet.fleets (
fleetName,
resourceGroupName,
subscriptionId,
properties,
zones,
identity,
plan,
tags,
location
)
SELECT 
'{{ fleetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ zones }}',
'{{ identity }}',
'{{ plan }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: spotPriorityProfile
          value:
            - name: capacity
              value: integer
            - name: minCapacity
              value: integer
            - name: maxPricePerVM
              value: number
            - name: evictionPolicy
              value: []
            - name: allocationStrategy
              value: []
            - name: maintain
              value: boolean
        - name: regularPriorityProfile
          value:
            - name: capacity
              value: integer
            - name: minCapacity
              value: integer
            - name: allocationStrategy
              value: []
        - name: vmSizesProfile
          value:
            - - name: name
                value: string
              - name: rank
                value: integer
        - name: computeProfile
          value:
            - name: baseVirtualMachineProfile
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
                                value: []
                              - name: content
                                value: string
                        - name: patchSettings
                          value:
                            - name: patchMode
                              value: []
                            - name: enableHotpatching
                              value: boolean
                            - name: assessmentMode
                              value: []
                            - name: automaticByPlatformSettings
                              value:
                                - name: rebootSetting
                                  value: []
                                - name: bypassPlatformSafetyChecksOnUserSchedule
                                  value: boolean
                        - name: winRM
                          value:
                            - name: listeners
                              value:
                                - - name: protocol
                                    value: []
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
                              value: []
                            - name: assessmentMode
                              value: []
                            - name: automaticByPlatformSettings
                              value:
                                - name: rebootSetting
                                  value: []
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
                        - name: id
                          value: string
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
                          value: []
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
                                  value: []
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
                      value: []
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
                                                  value: []
                                                - name: ipTags
                                                  value:
                                                    - []
                                                - name: publicIPAddressVersion
                                                  value: []
                                                - name: deleteOption
                                                  value: []
                                            - name: sku
                                              value:
                                                - name: name
                                                  value: []
                                                - name: tier
                                                  value: []
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
                              - name: auxiliaryMode
                                value: []
                              - name: auxiliarySku
                                value: []
                    - name: networkApiVersion
                      value: []
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
                      value: []
                    - name: encryptionIdentity
                      value:
                        - name: userAssignedIdentityResourceId
                          value: string
                    - name: proxyAgentSettings
                      value:
                        - name: enabled
                          value: boolean
                        - name: mode
                          value: []
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
                        - - name: id
                            value: string
                          - name: name
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
                    - name: extensionsTimeBudget
                      value: string
                - name: licenseType
                  value: string
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
            - name: computeApiVersion
              value: string
            - name: platformFaultDomainCount
              value: integer
        - name: timeCreated
          value: string
        - name: uniqueId
          value: string
    - name: zones
      value:
        - string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
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
        - name: version
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>fleets</code> resource.

```sql
/*+ update */
UPDATE azure.azure_fleet.fleets
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
plan = '{{ plan }}',
properties = '{{ properties }}'
WHERE 
fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>fleets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_fleet.fleets
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
