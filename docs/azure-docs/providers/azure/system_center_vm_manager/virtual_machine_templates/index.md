---
title: virtual_machine_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_templates
  - system_center_vm_manager
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.virtual_machine_templates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_templates', value: 'view', },
        { label: 'virtual_machine_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="computer_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_memory_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_memory_max_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_memory_min_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="inventory_item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_customizable" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_highly_available" /> | `text` | field from the `properties` object |
| <CopyableCode code="limit_cpu_for_migration" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="memory_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_interfaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualMachineTemplateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmm_server_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | Implements VirtualMachineTemplate GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List of VirtualMachineTemplates in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of VirtualMachineTemplates in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineTemplateName, data__extendedLocation" /> | Onboards the ScVmm VM Template as an Azure VM Template resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | Deregisters the ScVmm VM Template from Azure. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineTemplateName" /> | Updates the VirtualMachineTemplate resource. |

## `SELECT` examples

List of VirtualMachineTemplates in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_templates', value: 'view', },
        { label: 'virtual_machine_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
computer_name,
cpu_count,
disks,
dynamic_memory_enabled,
dynamic_memory_max_mb,
dynamic_memory_min_mb,
extended_location,
generation,
inventory_item_id,
is_customizable,
is_highly_available,
limit_cpu_for_migration,
location,
memory_mb,
network_interfaces,
os_name,
os_type,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
uuid,
virtualMachineTemplateName,
vmm_server_id
FROM azure.system_center_vm_manager.vw_virtual_machine_templates
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
FROM azure.system_center_vm_manager.virtual_machine_templates
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_templates</code> resource.

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
INSERT INTO azure.system_center_vm_manager.virtual_machine_templates (
resourceGroupName,
subscriptionId,
virtualMachineTemplateName,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualMachineTemplateName }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
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
        - name: inventoryItemId
          value: string
        - name: uuid
          value: string
        - name: vmmServerId
          value: string
        - name: osType
          value: []
        - name: osName
          value: string
        - name: computerName
          value: string
        - name: memoryMB
          value: integer
        - name: cpuCount
          value: integer
        - name: limitCpuForMigration
          value: []
        - name: dynamicMemoryEnabled
          value: []
        - name: isCustomizable
          value: []
        - name: dynamicMemoryMaxMB
          value: integer
        - name: dynamicMemoryMinMB
          value: integer
        - name: isHighlyAvailable
          value: []
        - name: generation
          value: integer
        - name: networkInterfaces
          value:
            - - name: name
                value: string
              - name: displayName
                value: string
              - name: ipv4Addresses
                value:
                  - string
              - name: ipv6Addresses
                value:
                  - string
              - name: macAddress
                value: string
              - name: virtualNetworkId
                value: string
              - name: networkName
                value: string
              - name: ipv4AddressType
                value: []
              - name: nicId
                value: string
        - name: disks
          value:
            - - name: name
                value: string
              - name: displayName
                value: string
              - name: diskId
                value: string
              - name: diskSizeGB
                value: integer
              - name: maxDiskSizeGB
                value: integer
              - name: bus
                value: integer
              - name: lun
                value: integer
              - name: busType
                value: string
              - name: vhdType
                value: string
              - name: volumeType
                value: string
              - name: vhdFormatType
                value: string
              - name: templateDiskId
                value: string
              - name: storageQoSPolicy
                value:
                  - name: name
                    value: string
                  - name: id
                    value: string
              - name: createDiffDisk
                value: []
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_templates</code> resource.

```sql
/*+ update */
UPDATE azure.system_center_vm_manager.virtual_machine_templates
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineTemplateName = '{{ virtualMachineTemplateName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_templates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.system_center_vm_manager.virtual_machine_templates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineTemplateName = '{{ virtualMachineTemplateName }}';
```
