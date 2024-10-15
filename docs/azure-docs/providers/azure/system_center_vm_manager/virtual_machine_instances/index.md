---
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.virtual_machine_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Retrieves information about a virtual machine instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Lists all of the virtual machine instances within the specified parent resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri, data__extendedLocation" /> | The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri" /> | The operation to delete a virtual machine instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceUri" /> | The operation to update a virtual machine instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to restart a virtual machine instance. |
| <CopyableCode code="restore_checkpoint" /> | `EXEC` | <CopyableCode code="resourceUri" /> | Restores to a checkpoint in virtual machine instance. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to start a virtual machine instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to power off (stop) a virtual machine instance. |

## `SELECT` examples

Retrieves information about a virtual machine instance.


```sql
SELECT
extendedLocation,
properties
FROM azure.system_center_vm_manager.virtual_machine_instances
WHERE resourceUri = '{{ resourceUri }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_instances</code> resource.

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
INSERT INTO azure.system_center_vm_manager.virtual_machine_instances (
resourceUri,
data__extendedLocation,
properties,
extendedLocation
)
SELECT 
'{{ resourceUri }}',
'{{ data__extendedLocation }}',
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
        - name: availabilitySets
          value:
            - - name: id
                value: string
              - name: name
                value: string
        - name: osProfile
          value:
            - name: adminPassword
              value: string
            - name: computerName
              value: string
            - name: osType
              value: []
            - name: osSku
              value: string
            - name: osVersion
              value: string
            - name: domainName
              value: string
            - name: domainUsername
              value: string
            - name: domainPassword
              value: string
            - name: workgroup
              value: string
            - name: productKey
              value: string
            - name: timezone
              value: integer
            - name: runOnceCommands
              value: string
        - name: hardwareProfile
          value:
            - name: memoryMB
              value: integer
            - name: cpuCount
              value: integer
            - name: limitCpuForMigration
              value: []
            - name: dynamicMemoryEnabled
              value: []
            - name: dynamicMemoryMaxMB
              value: integer
            - name: dynamicMemoryMinMB
              value: integer
            - name: isHighlyAvailable
              value: []
        - name: networkProfile
          value:
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
        - name: storageProfile
          value:
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
        - name: infrastructureProfile
          value:
            - name: inventoryItemId
              value: string
            - name: vmmServerId
              value: string
            - name: cloudId
              value: string
            - name: templateId
              value: string
            - name: vmName
              value: string
            - name: uuid
              value: string
            - name: lastRestoredVMCheckpoint
              value:
                - name: parentCheckpointID
                  value: string
                - name: checkpointID
                  value: string
                - name: name
                  value: string
                - name: description
                  value: string
            - name: checkpoints
              value:
                - - name: parentCheckpointID
                    value: string
                  - name: checkpointID
                    value: string
                  - name: name
                    value: string
                  - name: description
                    value: string
            - name: checkpointType
              value: string
            - name: generation
              value: integer
            - name: biosGuid
              value: string
        - name: powerState
          value: string
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_instances</code> resource.

```sql
/*+ update */
UPDATE azure.system_center_vm_manager.virtual_machine_instances
SET 
properties = '{{ properties }}'
WHERE 
resourceUri = '{{ resourceUri }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.system_center_vm_manager.virtual_machine_instances
WHERE resourceUri = '{{ resourceUri }}';
```
