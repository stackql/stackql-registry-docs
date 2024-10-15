---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
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

Creates, updates, deletes, gets or lists a <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_images', value: 'view', },
        { label: 'images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_virtual_machine" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an Image. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageName, resourceGroupName, subscriptionId" /> | Gets an image. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of Images in the subscription. Use nextLink property in the response to get the next page of Images. Do this till nextLink is null to fetch all the Images. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the list of images under a resource group. Use nextLink property in the response to get the next page of Images. Do this till nextLink is null to fetch all the Images. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="imageName, resourceGroupName, subscriptionId" /> | Create or update an image. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageName, resourceGroupName, subscriptionId" /> | Deletes an Image. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="imageName, resourceGroupName, subscriptionId" /> | Update an image. |

## `SELECT` examples

Gets the list of Images in the subscription. Use nextLink property in the response to get the next page of Images. Do this till nextLink is null to fetch all the Images.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_images', value: 'view', },
        { label: 'images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
extended_location,
hyper_v_generation,
imageName,
location,
provisioning_state,
resourceGroupName,
source_virtual_machine,
storage_profile,
subscriptionId,
tags,
type
FROM azure.compute.vw_images
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
extendedLocation,
location,
properties,
tags,
type
FROM azure.compute.images
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>images</code> resource.

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
INSERT INTO azure.compute.images (
imageName,
resourceGroupName,
subscriptionId,
properties,
extendedLocation,
location,
tags
)
SELECT 
'{{ imageName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
    - name: properties
      value:
        - name: sourceVirtualMachine
          value:
            - name: id
              value: string
        - name: storageProfile
          value:
            - name: osDisk
              value:
                - name: osType
                  value: string
                - name: osState
                  value: string
                - name: blobUri
                  value: string
                - name: caching
                  value: string
                - name: diskSizeGB
                  value: integer
                - name: storageAccountType
                  value: []
                - name: diskEncryptionSet
                  value:
                    - name: id
                      value: string
            - name: dataDisks
              value:
                - - name: lun
                    value: integer
                  - name: blobUri
                    value: string
                  - name: caching
                    value: string
                  - name: diskSizeGB
                    value: integer
            - name: zoneResilient
              value: boolean
        - name: provisioningState
          value: string
        - name: hyperVGeneration
          value: []
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
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

Updates a <code>images</code> resource.

```sql
/*+ update */
UPDATE azure.compute.images
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
imageName = '{{ imageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>images</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.images
WHERE imageName = '{{ imageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
