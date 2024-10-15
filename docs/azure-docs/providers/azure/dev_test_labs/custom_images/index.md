---
title: custom_images
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_images
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

Creates, updates, deletes, gets or lists a <code>custom_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.custom_images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_images', value: 'view', },
        { label: 'custom_images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_image_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_disk_storage_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_plan_authorized" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="managed_image_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_snapshot_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="vhd" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a custom image. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Get custom image. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | List custom images in a given lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing custom image. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Delete custom image. This operation can take a while to complete. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of custom images. All other properties will be ignored. |

## `SELECT` examples

List custom images in a given lab.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_images', value: 'view', },
        { label: 'custom_images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
author,
creation_date,
custom_image_plan,
data_disk_storage_info,
is_plan_authorized,
labName,
location,
managed_image_id,
managed_snapshot_id,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type,
unique_identifier,
vhd,
vm
FROM azure.dev_test_labs.vw_custom_images
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
FROM azure.dev_test_labs.custom_images
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_images</code> resource.

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
INSERT INTO azure.dev_test_labs.custom_images (
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
        - name: vm
          value:
            - name: sourceVmId
              value: string
            - name: windowsOsInfo
              value:
                - name: windowsOsState
                  value: string
            - name: linuxOsInfo
              value:
                - name: linuxOsState
                  value: string
        - name: vhd
          value:
            - name: imageName
              value: string
            - name: sysPrep
              value: boolean
            - name: osType
              value: string
        - name: description
          value: string
        - name: author
          value: string
        - name: creationDate
          value: string
        - name: managedImageId
          value: string
        - name: managedSnapshotId
          value: string
        - name: dataDiskStorageInfo
          value:
            - - name: lun
                value: string
              - name: storageType
                value: string
        - name: customImagePlan
          value:
            - name: id
              value: string
            - name: publisher
              value: string
            - name: offer
              value: string
        - name: isPlanAuthorized
          value: boolean
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>custom_images</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.custom_images
SET 
tags = '{{ tags }}'
WHERE 
labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>custom_images</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.custom_images
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
