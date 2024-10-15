---
title: virtual_hard_disks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hard_disks
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>virtual_hard_disks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_hard_disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.virtual_hard_disks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_hard_disks', value: 'view', },
        { label: 'virtual_hard_disks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="block_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_file_format" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_size_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="logical_sector_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="physical_sector_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="virtualHardDiskName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties under the virtual hard disk resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHardDiskName" /> | Gets a virtual hard disk |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the virtual hard disks in the specified resource group. Use the nextLink property in the response to get the next page of virtual hard disks. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the virtual hard disks in the specified subscription. Use the nextLink property in the response to get the next page of virtual hard disks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHardDiskName" /> | The operation to create or update a virtual hard disk. Please note some properties can be set only during virtual hard disk creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHardDiskName" /> | The operation to delete a virtual hard disk. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHardDiskName" /> | The operation to update a virtual hard disk. |

## `SELECT` examples

Lists all of the virtual hard disks in the specified subscription. Use the nextLink property in the response to get the next page of virtual hard disks.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_hard_disks', value: 'view', },
        { label: 'virtual_hard_disks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
block_size_bytes,
container_id,
disk_file_format,
disk_size_gb,
dynamic,
extended_location,
hyper_v_generation,
location,
logical_sector_bytes,
physical_sector_bytes,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
tags,
virtualHardDiskName
FROM azure_stack.azure_stack_hci.vw_virtual_hard_disks
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
FROM azure_stack.azure_stack_hci.virtual_hard_disks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_hard_disks</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.virtual_hard_disks (
resourceGroupName,
subscriptionId,
virtualHardDiskName,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualHardDiskName }}',
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
        - name: blockSizeBytes
          value: integer
        - name: diskSizeGB
          value: integer
        - name: dynamic
          value: boolean
        - name: logicalSectorBytes
          value: integer
        - name: physicalSectorBytes
          value: integer
        - name: hyperVGeneration
          value: string
        - name: diskFileFormat
          value: string
        - name: provisioningState
          value: string
        - name: containerId
          value: string
        - name: status
          value:
            - name: errorCode
              value: string
            - name: errorMessage
              value: string
            - name: provisioningStatus
              value:
                - name: operationId
                  value: string
                - name: status
                  value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_hard_disks</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.virtual_hard_disks
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHardDiskName = '{{ virtualHardDiskName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_hard_disks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.virtual_hard_disks
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHardDiskName = '{{ virtualHardDiskName }}';
```
