---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - sphere
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.images" /></td></tr>
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
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="component_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="image" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="regional_data_boundary" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of image |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, imageName, resourceGroupName, subscriptionId" /> | Get a Image |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | List Image resources by Catalog |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, imageName, resourceGroupName, subscriptionId" /> | Create a Image |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, imageName, resourceGroupName, subscriptionId" /> | Delete a Image |

## `SELECT` examples

List Image resources by Catalog

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
description,
catalogName,
component_id,
image,
imageName,
image_id,
image_name,
image_type,
provisioning_state,
regional_data_boundary,
resourceGroupName,
subscriptionId,
uri
FROM azure.sphere.vw_images
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sphere.images
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.sphere.images (
catalogName,
imageName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ catalogName }}',
'{{ imageName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: image
          value: string
        - name: imageId
          value: string
        - name: imageName
          value: string
        - name: regionalDataBoundary
          value: []
        - name: uri
          value: string
        - name: description
          value: string
        - name: componentId
          value: string
        - name: imageType
          value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>images</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sphere.images
WHERE catalogName = '{{ catalogName }}'
AND imageName = '{{ imageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
