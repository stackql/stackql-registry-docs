---
title: catalog_items
hide_title: false
hide_table_of_contents: false
keywords:
  - catalog_items
  - recommendationengine
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

Creates, updates, deletes, gets or lists a <code>catalog_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalog_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recommendationengine.catalog_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Required. Catalog item identifier. UTF-8 encoded string with a length limit of 128 bytes. This id must be unique among all catalog items within the same catalog. It should also be used when logging user events in order for the user events to be joined with the Catalog. |
| <CopyableCode code="description" /> | `string` | Optional. Catalog item description. UTF-8 encoded string with a length limit of 5 KiB. |
| <CopyableCode code="categoryHierarchies" /> | `array` | Required. Catalog item categories. This field is repeated for supporting one catalog item belonging to several parallel category hierarchies. For example, if a shoes product belongs to both ["Shoes & Accessories" -> "Shoes"] and ["Sports & Fitness" -> "Athletic Clothing" -> "Shoes"], it could be represented as: "categoryHierarchies": [ { "categories": ["Shoes & Accessories", "Shoes"]}, { "categories": ["Sports & Fitness", "Athletic Clothing", "Shoes"] } ] |
| <CopyableCode code="itemAttributes" /> | `object` | FeatureMap represents extra features that customers want to include in the recommendation model for catalogs/user events as categorical/numerical features. |
| <CopyableCode code="itemGroupId" /> | `string` | Optional. Variant group identifier for prediction results. UTF-8 encoded string with a length limit of 128 bytes. This field must be enabled before it can be used. [Learn more](/recommendations-ai/docs/catalog#item-group-id). |
| <CopyableCode code="languageCode" /> | `string` | Optional. Deprecated. The model automatically detects the text language. Your catalog can include text in different languages, but duplicating catalog items to provide text in multiple languages can result in degraded model performance. |
| <CopyableCode code="productMetadata" /> | `object` | ProductCatalogItem captures item metadata specific to retail products. |
| <CopyableCode code="tags" /> | `array` | Optional. Filtering tags associated with the catalog item. Each tag should be a UTF-8 encoded string with a length limit of 1 KiB. This tag can be used for filtering recommendation results by passing the tag as part of the predict request filter. |
| <CopyableCode code="title" /> | `string` | Required. Catalog item title. UTF-8 encoded string with a length limit of 1 KiB. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_catalog_items_get" /> | `SELECT` | <CopyableCode code="catalogItemsId, catalogsId, locationsId, projectsId" /> | Gets a specific catalog item. |
| <CopyableCode code="projects_locations_catalogs_catalog_items_list" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Gets a list of catalog items. |
| <CopyableCode code="projects_locations_catalogs_catalog_items_create" /> | `INSERT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Creates a catalog item. |
| <CopyableCode code="projects_locations_catalogs_catalog_items_delete" /> | `DELETE` | <CopyableCode code="catalogItemsId, catalogsId, locationsId, projectsId" /> | Deletes a catalog item. |
| <CopyableCode code="projects_locations_catalogs_catalog_items_patch" /> | `UPDATE` | <CopyableCode code="catalogItemsId, catalogsId, locationsId, projectsId" /> | Updates a catalog item. Partial updating is supported. Non-existing items will be created. |
| <CopyableCode code="projects_locations_catalogs_catalog_items_import" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Bulk import of multiple catalog items. Request processing may be synchronous. No partial updating supported. Non-existing items will be created. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully updated. |

## `SELECT` examples

Gets a list of catalog items.

```sql
SELECT
id,
description,
categoryHierarchies,
itemAttributes,
itemGroupId,
languageCode,
productMetadata,
tags,
title
FROM google.recommendationengine.catalog_items
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>catalog_items</code> resource.

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
INSERT INTO google.recommendationengine.catalog_items (
catalogsId,
locationsId,
projectsId,
categoryHierarchies,
title,
description,
itemAttributes,
languageCode,
tags,
itemGroupId,
productMetadata
)
SELECT 
'{{ catalogsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ categoryHierarchies }}',
'{{ title }}',
'{{ description }}',
'{{ itemAttributes }}',
'{{ languageCode }}',
'{{ tags }}',
'{{ itemGroupId }}',
'{{ productMetadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: categoryHierarchies
      value:
        - - name: categories
            value:
              - string
    - name: title
      value: string
    - name: description
      value: string
    - name: itemAttributes
      value:
        - name: categoricalFeatures
          value: object
        - name: numericalFeatures
          value: object
    - name: languageCode
      value: string
    - name: tags
      value:
        - string
    - name: itemGroupId
      value: string
    - name: productMetadata
      value:
        - name: exactPrice
          value:
            - name: displayPrice
              value: number
            - name: originalPrice
              value: number
        - name: priceRange
          value:
            - name: min
              value: number
            - name: max
              value: number
        - name: costs
          value: object
        - name: currencyCode
          value: string
        - name: stockState
          value: string
        - name: availableQuantity
          value: string
        - name: canonicalProductUri
          value: string
        - name: images
          value:
            - - name: uri
                value: string
              - name: height
                value: integer
              - name: width
                value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>catalog_items</code> resource.

```sql
/*+ update */
UPDATE google.recommendationengine.catalog_items
SET 
categoryHierarchies = '{{ categoryHierarchies }}',
title = '{{ title }}',
description = '{{ description }}',
itemAttributes = '{{ itemAttributes }}',
languageCode = '{{ languageCode }}',
tags = '{{ tags }}',
itemGroupId = '{{ itemGroupId }}',
productMetadata = '{{ productMetadata }}'
WHERE 
catalogItemsId = '{{ catalogItemsId }}'
AND catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>catalog_items</code> resource.

```sql
/*+ delete */
DELETE FROM google.recommendationengine.catalog_items
WHERE catalogItemsId = '{{ catalogItemsId }}'
AND catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
