---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
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

Creates, updates, deletes, gets or lists a <code>virtual_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.virtual_machines" /></td></tr>
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
| <CopyableCode code="admin_username" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="bare_metal_machine_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="boot_method" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_services_network_attachment" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_cores" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="isolate_emulator_thread" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="memory_size_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_attachments" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_hints" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssh_public_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtio_interface" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualMachineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_device_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_image_repository_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="volumes" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Get properties of the provided virtual machine. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of virtual machines in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of virtual machines in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName, data__extendedLocation, data__properties" /> | Create a new virtual machine or update the properties of the existing virtual machine. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Delete the provided virtual machine. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Patch the properties of the provided virtual machine, or update the tags associated with the virtual machine. Properties and tag updates can be done independently. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Power off the provided virtual machine. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Reimage the provided virtual machine. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Restart the provided virtual machine. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Start the provided virtual machine. |

## `SELECT` examples

Get a list of virtual machines in the provided subscription.

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
admin_username,
availability_zone,
bare_metal_machine_id,
boot_method,
cloud_services_network_attachment,
cluster_id,
cpu_cores,
detailed_status,
detailed_status_message,
extended_location,
isolate_emulator_thread,
location,
memory_size_gb,
network_attachments,
network_data,
placement_hints,
power_state,
provisioning_state,
resourceGroupName,
ssh_public_keys,
storage_profile,
subscriptionId,
tags,
user_data,
virtio_interface,
virtualMachineName,
vm_device_model,
vm_image,
vm_image_repository_credentials,
volumes
FROM azure.nexus.vw_virtual_machines
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
FROM azure.nexus.virtual_machines
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
INSERT INTO azure.nexus.virtual_machines (
resourceGroupName,
subscriptionId,
virtualMachineName,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualMachineName }}',
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
        - name: adminUsername
          value: string
        - name: availabilityZone
          value: string
        - name: bareMetalMachineId
          value: string
        - name: bootMethod
          value: string
        - name: cloudServicesNetworkAttachment
          value:
            - name: attachedNetworkId
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
        - name: clusterId
          value: string
        - name: cpuCores
          value: integer
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: isolateEmulatorThread
          value: string
        - name: memorySizeGB
          value: integer
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
        - name: networkData
          value: string
        - name: placementHints
          value:
            - - name: hintType
                value: string
              - name: resourceId
                value: string
              - name: schedulingExecution
                value: string
              - name: scope
                value: string
        - name: powerState
          value: string
        - name: provisioningState
          value: string
        - name: sshPublicKeys
          value:
            - - name: keyData
                value: string
        - name: storageProfile
          value:
            - name: osDisk
              value:
                - name: createOption
                  value: string
                - name: deleteOption
                  value: string
                - name: diskSizeGB
                  value: integer
            - name: volumeAttachments
              value:
                - string
        - name: userData
          value: string
        - name: virtioInterface
          value: string
        - name: vmDeviceModel
          value: string
        - name: vmImage
          value: string
        - name: vmImageRepositoryCredentials
          value:
            - name: password
              value: string
            - name: registryUrl
              value: string
            - name: username
              value: string
        - name: volumes
          value:
            - string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machines</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.virtual_machines
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.virtual_machines
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```
