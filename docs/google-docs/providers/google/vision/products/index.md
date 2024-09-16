---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - vision
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

Creates, updates, deletes, gets or lists a <code>products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vision.products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the product. Format is: `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`. This field is ignored when creating a product. |
| <CopyableCode code="description" /> | `string` | User-provided metadata to be stored with this product. Must be at most 4096 characters long. |
| <CopyableCode code="displayName" /> | `string` | The user-provided name for this Product. Must not be empty. Must be at most 4096 characters long. |
| <CopyableCode code="productCategory" /> | `string` | Immutable. The category for the product identified by the reference image. This should be one of "homegoods-v2", "apparel-v2", "toys-v2", "packagedgoods-v1" or "general-v1". The legacy categories "homegoods", "apparel", and "toys" are still supported, but these should not be used for new products. |
| <CopyableCode code="productLabels" /> | `array` | Key-value pairs that can be attached to a product. At query time, constraints can be specified based on the product_labels. Note that integer values can be provided as strings, e.g. "1199". Only strings with integer values can match a range-based restriction which is to be supported soon. Multiple values can be assigned to the same key. One product may have up to 500 product_labels. Notice that the total number of distinct product_labels over all products in one ProductSet cannot exceed 1M, otherwise the product search pipeline will refuse to work for that ProductSet. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_product_sets_products_list" /> | `SELECT` | <CopyableCode code="locationsId, productSetsId, projectsId" /> | Lists the Products in a ProductSet, in an unspecified order. If the ProductSet does not exist, the products field of the response will be empty. Possible errors: * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. |
| <CopyableCode code="projects_locations_products_get" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Gets information associated with a Product. Possible errors: * Returns NOT_FOUND if the Product does not exist. |
| <CopyableCode code="projects_locations_products_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists products in an unspecified order. Possible errors: * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1. |
| <CopyableCode code="projects_locations_products_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates and returns a new product resource. Possible errors: * Returns INVALID_ARGUMENT if display_name is missing or longer than 4096 characters. * Returns INVALID_ARGUMENT if description is longer than 4096 characters. * Returns INVALID_ARGUMENT if product_category is missing or invalid. |
| <CopyableCode code="projects_locations_products_delete" /> | `DELETE` | <CopyableCode code="locationsId, productsId, projectsId" /> | Permanently deletes a product and its reference images. Metadata of the product and all its images will be deleted right away, but search queries against ProductSets containing the product may still work until all related caches are refreshed. |
| <CopyableCode code="projects_locations_products_patch" /> | `UPDATE` | <CopyableCode code="locationsId, productsId, projectsId" /> | Makes changes to a Product resource. Only the `display_name`, `description`, and `labels` fields can be updated right now. If labels are updated, the change will not be reflected in queries until the next index time. Possible errors: * Returns NOT_FOUND if the Product does not exist. * Returns INVALID_ARGUMENT if display_name is present in update_mask but is missing from the request or longer than 4096 characters. * Returns INVALID_ARGUMENT if description is present in update_mask but is longer than 4096 characters. * Returns INVALID_ARGUMENT if product_category is present in update_mask. |
| <CopyableCode code="projects_locations_products_purge" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Asynchronous API to delete all Products in a ProductSet or all Products that are in no ProductSet. If a Product is a member of the specified ProductSet in addition to other ProductSets, the Product will still be deleted. It is recommended to not delete the specified ProductSet until after this operation has completed. It is also recommended to not add any of the Products involved in the batch delete to a new ProductSet while this operation is running because those Products may still end up deleted. It's not possible to undo the PurgeProducts operation. Therefore, it is recommended to keep the csv files used in ImportProductSets (if that was how you originally built the Product Set) before starting PurgeProducts, in case you need to re-import the data after deletion. If the plan is to purge all of the Products from a ProductSet and then re-use the empty ProductSet to re-import new Products into the empty ProductSet, you must wait until the PurgeProducts operation has finished for that ProductSet. The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) |

## `SELECT` examples

Lists products in an unspecified order. Possible errors: * Returns INVALID_ARGUMENT if page_size is greater than 100 or less than 1.

```sql
SELECT
name,
description,
displayName,
productCategory,
productLabels
FROM google.vision.products
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>products</code> resource.

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
INSERT INTO google.vision.products (
locationsId,
projectsId,
name,
displayName,
description,
productCategory,
productLabels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ productCategory }}',
'{{ productLabels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'
    - name: productCategory
      value: '{{ productCategory }}'
    - name: productLabels
      value: '{{ productLabels }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>products</code> resource.

```sql
/*+ update */
UPDATE google.vision.products
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
productCategory = '{{ productCategory }}',
productLabels = '{{ productLabels }}'
WHERE 
locationsId = '{{ locationsId }}'
AND productsId = '{{ productsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>products</code> resource.

```sql
/*+ delete */
DELETE FROM google.vision.products
WHERE locationsId = '{{ locationsId }}'
AND productsId = '{{ productsId }}'
AND projectsId = '{{ projectsId }}';
```
