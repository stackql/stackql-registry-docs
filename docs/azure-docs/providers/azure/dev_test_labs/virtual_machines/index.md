---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - dev_test_labs
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.virtual_machines" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="allow_claim" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicable_schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifact_deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_vm" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by_user" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by_user_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_image_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_disk_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="disallow_public_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="gallery_image_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_authentication_with_ssh_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="lab_subnet_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="lab_virtual_network_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_known_power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="network_interface" /> | `text` | field from the `properties` object |
| <CopyableCode code="notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="owner_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="owner_user_principal_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="password" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssh_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine_creation_source" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a virtual machine. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Get virtual machine. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | List virtual machines in a given lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing virtual machine. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Delete virtual machine. This operation can take a while to complete. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of virtual machines. All other properties will be ignored. |
| <CopyableCode code="add_data_disk" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Attach a new or existing data disk to virtual machine. This operation can take a while to complete. |
| <CopyableCode code="apply_artifacts" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Apply artifacts to virtual machine. This operation can take a while to complete. |
| <CopyableCode code="claim" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Take ownership of an existing virtual machine This operation can take a while to complete. |
| <CopyableCode code="detach_data_disk" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Detach the specified disk from the virtual machine. This operation can take a while to complete. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Redeploy a virtual machine This operation can take a while to complete. |
| <CopyableCode code="resize" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Resize Virtual Machine. This operation can take a while to complete. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Restart a virtual machine. This operation can take a while to complete. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Start a virtual machine. This operation can take a while to complete. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Stop a virtual machine This operation can take a while to complete. |
| <CopyableCode code="transfer_disks" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Transfers all data disks attached to the virtual machine to be owned by the current user. This operation can take a while to complete. |
| <CopyableCode code="un_claim" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Release ownership of an existing virtual machine This operation can take a while to complete. |

## `SELECT` examples

List virtual machines in a given lab.

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
allow_claim,
applicable_schedule,
artifact_deployment_status,
artifacts,
compute_id,
compute_vm,
created_by_user,
created_by_user_id,
created_date,
custom_image_id,
data_disk_parameters,
disallow_public_ip_address,
environment_id,
expiration_date,
fqdn,
gallery_image_reference,
is_authentication_with_ssh_key,
labName,
lab_subnet_name,
lab_virtual_network_id,
last_known_power_state,
location,
network_interface,
notes,
os_type,
owner_object_id,
owner_user_principal_name,
password,
plan_id,
provisioning_state,
resourceGroupName,
schedule_parameters,
size,
ssh_key,
storage_type,
subscriptionId,
tags,
type,
unique_identifier,
user_name,
virtual_machine_creation_source
FROM azure.dev_test_labs.vw_virtual_machines
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.dev_test_labs.virtual_machines
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.dev_test_labs.virtual_machines (
labName,
name,
resourceGroupName,
subscriptionId,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ labName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
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
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: notes
          value: string
        - name: ownerObjectId
          value: string
        - name: ownerUserPrincipalName
          value: string
        - name: createdByUserId
          value: string
        - name: createdByUser
          value: string
        - name: createdDate
          value: string
        - name: computeId
          value: string
        - name: customImageId
          value: string
        - name: osType
          value: string
        - name: size
          value: string
        - name: userName
          value: string
        - name: password
          value: string
        - name: sshKey
          value: string
        - name: isAuthenticationWithSshKey
          value: boolean
        - name: fqdn
          value: string
        - name: labSubnetName
          value: string
        - name: labVirtualNetworkId
          value: string
        - name: disallowPublicIpAddress
          value: boolean
        - name: artifacts
          value:
            - - name: artifactId
                value: string
              - name: artifactTitle
                value: string
              - name: parameters
                value:
                  - - name: name
                      value: string
                    - name: value
                      value: string
              - name: status
                value: string
              - name: deploymentStatusMessage
                value: string
              - name: vmExtensionStatusMessage
                value: string
              - name: installTime
                value: string
        - name: artifactDeploymentStatus
          value:
            - name: deploymentStatus
              value: string
            - name: artifactsApplied
              value: integer
            - name: totalArtifacts
              value: integer
        - name: galleryImageReference
          value:
            - name: offer
              value: string
            - name: publisher
              value: string
            - name: sku
              value: string
            - name: osType
              value: string
            - name: version
              value: string
        - name: planId
          value: string
        - name: computeVm
          value:
            - name: statuses
              value:
                - - name: code
                    value: string
                  - name: displayStatus
                    value: string
                  - name: message
                    value: string
            - name: osType
              value: string
            - name: vmSize
              value: string
            - name: networkInterfaceId
              value: string
            - name: osDiskId
              value: string
            - name: dataDiskIds
              value:
                - string
            - name: dataDisks
              value:
                - - name: name
                    value: string
                  - name: diskUri
                    value: string
                  - name: managedDiskId
                    value: string
                  - name: diskSizeGiB
                    value: integer
        - name: networkInterface
          value:
            - name: virtualNetworkId
              value: string
            - name: subnetId
              value: string
            - name: publicIpAddressId
              value: string
            - name: publicIpAddress
              value: string
            - name: privateIpAddress
              value: string
            - name: dnsName
              value: string
            - name: rdpAuthority
              value: string
            - name: sshAuthority
              value: string
            - name: sharedPublicIpAddressConfiguration
              value:
                - name: inboundNatRules
                  value:
                    - - name: transportProtocol
                        value: string
                      - name: frontendPort
                        value: integer
                      - name: backendPort
                        value: integer
        - name: applicableSchedule
          value:
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
            - name: properties
              value:
                - name: labVmsShutdown
                  value:
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
                    - name: properties
                      value:
                        - name: status
                          value: string
                        - name: taskType
                          value: string
                        - name: weeklyRecurrence
                          value:
                            - name: weekdays
                              value:
                                - string
                            - name: time
                              value: string
                        - name: dailyRecurrence
                          value:
                            - name: time
                              value: string
                        - name: hourlyRecurrence
                          value:
                            - name: minute
                              value: integer
                        - name: timeZoneId
                          value: string
                        - name: notificationSettings
                          value:
                            - name: status
                              value: string
                            - name: timeInMinutes
                              value: integer
                            - name: webhookUrl
                              value: string
                            - name: emailRecipient
                              value: string
                            - name: notificationLocale
                              value: string
                        - name: createdDate
                          value: string
                        - name: targetResourceId
                          value: string
                        - name: provisioningState
                          value: string
                        - name: uniqueIdentifier
                          value: string
        - name: expirationDate
          value: string
        - name: allowClaim
          value: boolean
        - name: storageType
          value: string
        - name: virtualMachineCreationSource
          value: string
        - name: environmentId
          value: string
        - name: dataDiskParameters
          value:
            - - name: attachNewDataDiskOptions
                value:
                  - name: diskSizeGiB
                    value: integer
                  - name: diskName
                    value: string
                  - name: diskType
                    value: string
              - name: existingLabDiskId
                value: string
              - name: hostCaching
                value: string
        - name: scheduleParameters
          value:
            - - name: properties
                value:
                  - name: status
                    value: string
                  - name: taskType
                    value: string
                  - name: timeZoneId
                    value: string
                  - name: targetResourceId
                    value: string
              - name: name
                value: string
              - name: location
                value: string
              - name: tags
                value: object
        - name: lastKnownPowerState
          value: string
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machines</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.virtual_machines
SET 
tags = '{{ tags }}'
WHERE 
labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.virtual_machines
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
