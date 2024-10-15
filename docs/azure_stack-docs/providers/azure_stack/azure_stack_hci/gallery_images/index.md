---
title: gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_images
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

Creates, updates, deletes, gets or lists a <code>gallery_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.gallery_images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_images', value: 'view', },
        { label: 'gallery_images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cloud_init_data_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties under the gallery image resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, resourceGroupName, subscriptionId" /> | Gets a gallery image |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the gallery images in the specified resource group. Use the nextLink property in the response to get the next page of gallery images. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the gallery images in the specified subscription. Use the nextLink property in the response to get the next page of gallery images. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryImageName, resourceGroupName, subscriptionId" /> | The operation to create or update a gallery image. Please note some properties can be set only during gallery image creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryImageName, resourceGroupName, subscriptionId" /> | The operation to delete a gallery image. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="galleryImageName, resourceGroupName, subscriptionId" /> | The operation to update a gallery image. |

## `SELECT` examples

Lists all of the gallery images in the specified subscription. Use the nextLink property in the response to get the next page of gallery images.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_images', value: 'view', },
        { label: 'gallery_images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cloud_init_data_source,
container_id,
extended_location,
galleryImageName,
hyper_v_generation,
identifier,
image_path,
location,
os_type,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
tags,
version
FROM azure_stack.azure_stack_hci.vw_gallery_images
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
FROM azure_stack.azure_stack_hci.gallery_images
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gallery_images</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.gallery_images (
galleryImageName,
resourceGroupName,
subscriptionId,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ galleryImageName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: containerId
          value: string
        - name: imagePath
          value: string
        - name: osType
          value: string
        - name: cloudInitDataSource
          value: string
        - name: hyperVGeneration
          value: string
        - name: identifier
          value:
            - name: publisher
              value: string
            - name: offer
              value: string
            - name: sku
              value: string
        - name: version
          value:
            - name: name
              value: string
            - name: properties
              value:
                - name: storageProfile
                  value:
                    - name: osDiskImage
                      value:
                        - name: sizeInMB
                          value: integer
        - name: provisioningState
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
            - name: downloadStatus
              value:
                - name: downloadSizeInMB
                  value: integer
            - name: progressPercentage
              value: integer
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

Updates a <code>gallery_images</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.gallery_images
SET 
tags = '{{ tags }}'
WHERE 
galleryImageName = '{{ galleryImageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>gallery_images</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.gallery_images
WHERE galleryImageName = '{{ galleryImageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
