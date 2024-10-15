---
title: gallery_items
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_items
  - gallery_admin
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

Creates, updates, deletes, gets or lists a <code>gallery_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.gallery_admin.gallery_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_items', value: 'view', },
        { label: 'gallery_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="additional_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="category_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="definition_templates" /> | `text` | field from the `properties` object |
| <CopyableCode code="filters" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_file_uris" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="images" /> | `text` | field from the `properties` object |
| <CopyableCode code="item_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="item_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="item_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="links" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="long_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketing_material" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="products" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Properties of a gallery item. |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="screenshot_uris" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
| <CopyableCode code="ui_definition_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a gallery item. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryItemName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryItemName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_items', value: 'view', },
        { label: 'gallery_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
additional_properties,
artifacts,
category_ids,
changed_time,
created_time,
definition_templates,
filters,
galleryItemName,
icon_file_uris,
identity,
images,
item_display_name,
item_name,
item_type,
links,
location,
long_summary,
marketing_material,
metadata,
products,
properties,
publisher,
publisher_display_name,
resource_group_name,
screenshot_uris,
subscriptionId,
summary,
tags,
type,
ui_definition_uri,
version
FROM azure_stack.gallery_admin.vw_gallery_items
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure_stack.gallery_admin.gallery_items
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gallery_items</code> resource.

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
INSERT INTO azure_stack.gallery_admin.gallery_items (
subscriptionId,
galleryItemUri
)
SELECT 
'{{ subscriptionId }}',
'{{ galleryItemUri }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: galleryItemUri
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>gallery_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.gallery_admin.gallery_items
WHERE galleryItemName = '{{ galleryItemName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
