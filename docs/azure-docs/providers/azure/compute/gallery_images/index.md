---
title: gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_images
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

Creates, updates, deletes, gets or lists a <code>gallery_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.gallery_images" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="architecture" /> | `text` | field from the `properties` object |
| <CopyableCode code="disallowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_of_life_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="eula" /> | `text` | field from the `properties` object |
| <CopyableCode code="features" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="os_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="privacy_statement_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommended" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_note_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | Retrieves information about a gallery image definition. |
| <CopyableCode code="list_by_gallery" /> | `SELECT` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | List gallery image definitions in a gallery. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | Create or update a gallery image definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | Delete a gallery image. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | Update a gallery image definition. |

## `SELECT` examples

List gallery image definitions in a gallery.

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
id,
name,
description,
architecture,
disallowed,
end_of_life_date,
eula,
features,
galleryImageName,
galleryName,
hyper_v_generation,
identifier,
location,
os_state,
os_type,
privacy_statement_uri,
provisioning_state,
purchase_plan,
recommended,
release_note_uri,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.compute.vw_gallery_images
WHERE galleryName = '{{ galleryName }}'
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
FROM azure.compute.gallery_images
WHERE galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.compute.gallery_images (
galleryImageName,
galleryName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ galleryImageName }}',
'{{ galleryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: description
          value: string
        - name: eula
          value: string
        - name: privacyStatementUri
          value: string
        - name: releaseNoteUri
          value: string
        - name: osType
          value: string
        - name: osState
          value: string
        - name: hyperVGeneration
          value: string
        - name: endOfLifeDate
          value: string
        - name: identifier
          value:
            - name: publisher
              value: string
            - name: offer
              value: string
            - name: sku
              value: string
        - name: recommended
          value:
            - name: vCPUs
              value:
                - name: min
                  value: integer
                - name: max
                  value: integer
        - name: disallowed
          value:
            - name: diskTypes
              value:
                - string
        - name: purchasePlan
          value:
            - name: name
              value: string
            - name: publisher
              value: string
            - name: product
              value: string
        - name: provisioningState
          value: []
        - name: features
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: architecture
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

Updates a <code>gallery_images</code> resource.

```sql
/*+ update */
UPDATE azure.compute.gallery_images
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
galleryImageName = '{{ galleryImageName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>gallery_images</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.gallery_images
WHERE galleryImageName = '{{ galleryImageName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
