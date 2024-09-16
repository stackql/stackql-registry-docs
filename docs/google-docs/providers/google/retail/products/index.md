---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - retail
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Immutable. Product identifier, which is the final component of name. For example, this field is "id_1", if name is `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/id_1`. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [id](https://support.google.com/merchants/answer/6324405). Schema.org property [Product.sku](https://schema.org/sku). |
| <CopyableCode code="name" /> | `string` | Immutable. Full resource name of the product, such as `projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/product_id`. |
| <CopyableCode code="description" /> | `string` | Product description. This field must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [description](https://support.google.com/merchants/answer/6324468). Schema.org property [Product.description](https://schema.org/description). |
| <CopyableCode code="attributes" /> | `object` | Highly encouraged. Extra product attributes to be included. For example, for products, this could include the store name, vendor, style, color, etc. These are very strong signals for recommendation model, thus we highly recommend providing the attributes here. Features that can take on one of a limited number of possible values. Two types of features can be set are: Textual features. some examples would be the brand/maker of a product, or country of a customer. Numerical features. Some examples would be the height/weight of a product, or age of a customer. For example: `{ "vendor": {"text": ["vendor123", "vendor456"]}, "lengths_cm": {"numbers":[2.3, 15.4]}, "heights_cm": {"numbers":[8.1, 6.4]} }`. This field needs to pass all below criteria, otherwise an INVALID_ARGUMENT error is returned: * Max entries count: 200. * The key must be a UTF-8 encoded string with a length limit of 128 characters. * For indexable attribute, the key must match the pattern: `a-zA-Z0-9*`. For example, `key0LikeThis` or `KEY_1_LIKE_THIS`. * For text attributes, at most 400 values are allowed. Empty values are not allowed. Each value must be a non-empty UTF-8 encoded string with a length limit of 256 characters. * For number attributes, at most 400 values are allowed. |
| <CopyableCode code="audience" /> | `object` | An intended audience of the Product for whom it's sold. |
| <CopyableCode code="availability" /> | `string` | The online availability of the Product. Default to Availability.IN_STOCK. For primary products with variants set the availability of the primary as Availability.OUT_OF_STOCK and set the true availability at the variant level. This way the primary product will be considered "in stock" as long as it has at least one variant in stock. For primary products with no variants set the true availability at the primary level. Corresponding properties: Google Merchant Center property [availability](https://support.google.com/merchants/answer/6324448). Schema.org property [Offer.availability](https://schema.org/availability). |
| <CopyableCode code="availableQuantity" /> | `integer` | The available quantity of the item. |
| <CopyableCode code="availableTime" /> | `string` | The timestamp when this Product becomes available for SearchService.Search. Note that this is only applicable to Type.PRIMARY and Type.COLLECTION, and ignored for Type.VARIANT. |
| <CopyableCode code="brands" /> | `array` | The brands of the product. A maximum of 30 brands are allowed unless overridden through the Google Cloud console. Each brand must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [brand](https://support.google.com/merchants/answer/6324351). Schema.org property [Product.brand](https://schema.org/brand). |
| <CopyableCode code="categories" /> | `array` | Product categories. This field is repeated for supporting one product belonging to several parallel categories. Strongly recommended using the full path for better search / recommendation quality. To represent full path of category, use '>' sign to separate different hierarchies. If '>' is part of the category name, replace it with other character(s). For example, if a shoes product belongs to both ["Shoes & Accessories" -> "Shoes"] and ["Sports & Fitness" -> "Athletic Clothing" -> "Shoes"], it could be represented as: "categories": [ "Shoes & Accessories > Shoes", "Sports & Fitness > Athletic Clothing > Shoes" ] Must be set for Type.PRIMARY Product otherwise an INVALID_ARGUMENT error is returned. At most 250 values are allowed per Product unless overridden through the Google Cloud console. Empty values are not allowed. Each value must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property google_product_category. Schema.org property [Product.category] (https://schema.org/category). [mc_google_product_category]: https://support.google.com/merchants/answer/6324436 |
| <CopyableCode code="collectionMemberIds" /> | `array` | The id of the collection members when type is Type.COLLECTION. Non-existent product ids are allowed. The type of the members must be either Type.PRIMARY or Type.VARIANT otherwise an INVALID_ARGUMENT error is thrown. Should not set it for other types. A maximum of 1000 values are allowed. Otherwise, an INVALID_ARGUMENT error is return. |
| <CopyableCode code="colorInfo" /> | `object` | The color information of a Product. |
| <CopyableCode code="conditions" /> | `array` | The condition of the product. Strongly encouraged to use the standard values: "new", "refurbished", "used". A maximum of 1 value is allowed per Product. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [condition](https://support.google.com/merchants/answer/6324469). Schema.org property [Offer.itemCondition](https://schema.org/itemCondition). |
| <CopyableCode code="expireTime" /> | `string` | Note that this field is applied in the following ways: * If the Product is already expired when it is uploaded, this product is not indexed for search. * If the Product is not expired when it is uploaded, only the Type.PRIMARY's and Type.COLLECTION's expireTime is respected, and Type.VARIANT's expireTime is not used. In general, we suggest the users to delete the stale products explicitly, instead of using this field to determine staleness. expire_time must be later than available_time and publish_time, otherwise an INVALID_ARGUMENT error is thrown. Corresponding properties: Google Merchant Center property [expiration_date](https://support.google.com/merchants/answer/6324499). |
| <CopyableCode code="fulfillmentInfo" /> | `array` | Fulfillment information, such as the store IDs for in-store pickup or region IDs for different shipping methods. All the elements must have distinct FulfillmentInfo.type. Otherwise, an INVALID_ARGUMENT error is returned. |
| <CopyableCode code="gtin" /> | `string` | The Global Trade Item Number (GTIN) of the product. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. This field must be a Unigram. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [gtin](https://support.google.com/merchants/answer/6324461). Schema.org property [Product.isbn](https://schema.org/isbn), [Product.gtin8](https://schema.org/gtin8), [Product.gtin12](https://schema.org/gtin12), [Product.gtin13](https://schema.org/gtin13), or [Product.gtin14](https://schema.org/gtin14). If the value is not a valid GTIN, an INVALID_ARGUMENT error is returned. |
| <CopyableCode code="images" /> | `array` | Product images for the product. We highly recommend putting the main image first. A maximum of 300 images are allowed. Corresponding properties: Google Merchant Center property [image_link](https://support.google.com/merchants/answer/6324350). Schema.org property [Product.image](https://schema.org/image). |
| <CopyableCode code="languageCode" /> | `string` | Language of the title/description and other string attributes. Use language tags defined by [BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). For product prediction, this field is ignored and the model automatically detects the text language. The Product can include text in different languages, but duplicating Products to provide text in multiple languages can result in degraded model performance. For product search this field is in use. It defaults to "en-US" if unset. |
| <CopyableCode code="localInventories" /> | `array` | Output only. A list of local inventories specific to different places. This field can be managed by ProductService.AddLocalInventories and ProductService.RemoveLocalInventories APIs if fine-grained, high-volume updates are necessary. |
| <CopyableCode code="materials" /> | `array` | The material of the product. For example, "leather", "wooden". A maximum of 20 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 200 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [material](https://support.google.com/merchants/answer/6324410). Schema.org property [Product.material](https://schema.org/material). |
| <CopyableCode code="patterns" /> | `array` | The pattern or graphic print of the product. For example, "striped", "polka dot", "paisley". A maximum of 20 values are allowed per Product. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [pattern](https://support.google.com/merchants/answer/6324483). Schema.org property [Product.pattern](https://schema.org/pattern). |
| <CopyableCode code="priceInfo" /> | `object` | The price information of a Product. |
| <CopyableCode code="primaryProductId" /> | `string` | Variant group identifier. Must be an id, with the same parent branch with this product. Otherwise, an error is thrown. For Type.PRIMARY Products, this field can only be empty or set to the same value as id. For VARIANT Products, this field cannot be empty. A maximum of 2,000 products are allowed to share the same Type.PRIMARY Product. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [item_group_id](https://support.google.com/merchants/answer/6324507). Schema.org property [Product.inProductGroupWithID](https://schema.org/inProductGroupWithID). |
| <CopyableCode code="promotions" /> | `array` | The promotions applied to the product. A maximum of 10 values are allowed per Product. Only Promotion.promotion_id will be used, other fields will be ignored if set. |
| <CopyableCode code="publishTime" /> | `string` | The timestamp when the product is published by the retailer for the first time, which indicates the freshness of the products. Note that this field is different from available_time, given it purely describes product freshness regardless of when it is available on search and recommendation. |
| <CopyableCode code="rating" /> | `object` | The rating of a Product. |
| <CopyableCode code="retrievableFields" /> | `string` | Indicates which fields in the Products are returned in SearchResponse. Supported fields for all types: * audience * availability * brands * color_info * conditions * gtin * materials * name * patterns * price_info * rating * sizes * title * uri Supported fields only for Type.PRIMARY and Type.COLLECTION: * categories * description * images Supported fields only for Type.VARIANT: * Only the first image in images To mark attributes as retrievable, include paths of the form "attributes.key" where "key" is the key of a custom attribute, as specified in attributes. For Type.PRIMARY and Type.COLLECTION, the following fields are always returned in SearchResponse by default: * name For Type.VARIANT, the following fields are always returned in by default: * name * color_info The maximum number of paths is 30. Otherwise, an INVALID_ARGUMENT error is returned. Note: Returning more fields in SearchResponse can increase response payload size and serving latency. This field is deprecated. Use the retrievable site-wide control instead. |
| <CopyableCode code="sizes" /> | `array` | The size of the product. To represent different size systems or size types, consider using this format: [[[size_system:]size_type:]size_value]. For example, in "US:MENS:M", "US" represents size system; "MENS" represents size type; "M" represents size value. In "GIRLS:27", size system is empty; "GIRLS" represents size type; "27" represents size value. In "32 inches", both size system and size type are empty, while size value is "32 inches". A maximum of 20 values are allowed per Product. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [size](https://support.google.com/merchants/answer/6324492), [size_type](https://support.google.com/merchants/answer/6324497), and [size_system](https://support.google.com/merchants/answer/6324502). Schema.org property [Product.size](https://schema.org/size). |
| <CopyableCode code="tags" /> | `array` | Custom tags associated with the product. At most 250 values are allowed per Product. This value must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned. This tag can be used for filtering recommendation results by passing the tag as part of the PredictRequest.filter. Corresponding properties: Google Merchant Center property [custom_label_0–4](https://support.google.com/merchants/answer/6324473). |
| <CopyableCode code="title" /> | `string` | Required. Product title. This field must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [title](https://support.google.com/merchants/answer/6324415). Schema.org property [Product.name](https://schema.org/name). |
| <CopyableCode code="ttl" /> | `string` | Input only. The TTL (time to live) of the product. Note that this is only applicable to Type.PRIMARY and Type.COLLECTION, and ignored for Type.VARIANT. In general, we suggest the users to delete the stale products explicitly, instead of using this field to determine staleness. If it is set, it must be a non-negative value, and expire_time is set as current timestamp plus ttl. The derived expire_time is returned in the output and ttl is left blank when retrieving the Product. If it is set, the product is not available for SearchService.Search after current timestamp plus ttl. However, the product can still be retrieved by ProductService.GetProduct and ProductService.ListProducts. |
| <CopyableCode code="type" /> | `string` | Immutable. The type of the product. Default to Catalog.product_level_config.ingestion_product_type if unset. |
| <CopyableCode code="uri" /> | `string` | Canonical URL directly linking to the product detail page. It is strongly recommended to provide a valid uri for the product, otherwise the service performance could be significantly degraded. This field must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT error is returned. Corresponding properties: Google Merchant Center property [link](https://support.google.com/merchants/answer/6324416). Schema.org property [Offer.url](https://schema.org/url). |
| <CopyableCode code="variants" /> | `array` | Output only. Product variants grouped together on primary product which share similar product attributes. It's automatically grouped by primary_product_id for all the product variants. Only populated for Type.PRIMARY Products. Note: This field is OUTPUT_ONLY for ProductService.GetProduct. Do not set this field in API requests. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_branches_products_get" /> | `SELECT` | <CopyableCode code="branchesId, catalogsId, locationsId, productsId, projectsId" /> | Gets a Product. |
| <CopyableCode code="projects_locations_catalogs_branches_products_list" /> | `SELECT` | <CopyableCode code="branchesId, catalogsId, locationsId, projectsId" /> | Gets a list of Products. |
| <CopyableCode code="projects_locations_catalogs_branches_products_create" /> | `INSERT` | <CopyableCode code="branchesId, catalogsId, locationsId, projectsId" /> | Creates a Product. |
| <CopyableCode code="projects_locations_catalogs_branches_products_delete" /> | `DELETE` | <CopyableCode code="branchesId, catalogsId, locationsId, productsId, projectsId" /> | Deletes a Product. |
| <CopyableCode code="projects_locations_catalogs_branches_products_patch" /> | `UPDATE` | <CopyableCode code="branchesId, catalogsId, locationsId, productsId, projectsId" /> | Updates a Product. |
| <CopyableCode code="projects_locations_catalogs_branches_products_import" /> | `EXEC` | <CopyableCode code="branchesId, catalogsId, locationsId, projectsId" /> | Bulk import of multiple Products. Request processing may be synchronous. Non-existing items are created. Note that it is possible for a subset of the Products to be successfully updated. |
| <CopyableCode code="projects_locations_catalogs_branches_products_purge" /> | `EXEC` | <CopyableCode code="branchesId, catalogsId, locationsId, projectsId" /> | Permanently deletes all selected Products under a branch. This process is asynchronous. If the request is valid, the removal will be enqueued and processed offline. Depending on the number of Products, this operation could take hours to complete. Before the operation completes, some Products may still be returned by ProductService.GetProduct or ProductService.ListProducts. Depending on the number of Products, this operation could take hours to complete. To get a sample of Products that would be deleted, set PurgeProductsRequest.force to false. |
| <CopyableCode code="projects_locations_catalogs_branches_products_set_inventory" /> | `EXEC` | <CopyableCode code="branchesId, catalogsId, locationsId, productsId, projectsId" /> | Updates inventory information for a Product while respecting the last update timestamps of each inventory field. This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update is enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts. When inventory is updated with ProductService.CreateProduct and ProductService.UpdateProduct, the specified inventory field value(s) overwrite any existing value(s) while ignoring the last update time for this field. Furthermore, the last update times for the specified inventory fields are overwritten by the times of the ProductService.CreateProduct or ProductService.UpdateProduct request. If no inventory fields are set in CreateProductRequest.product, then any pre-existing inventory information for this product is used. If no inventory fields are set in SetInventoryRequest.set_mask, then any existing inventory information is preserved. Pre-existing inventory information can only be updated with ProductService.SetInventory, ProductService.AddFulfillmentPlaces, and ProductService.RemoveFulfillmentPlaces. The returned Operations is obsolete after one day, and the GetOperation API returns `NOT_FOUND` afterwards. If conflicting updates are issued, the Operations associated with the stale updates are not marked as done until they are obsolete. |

## `SELECT` examples

Gets a list of Products.

```sql
SELECT
id,
name,
description,
attributes,
audience,
availability,
availableQuantity,
availableTime,
brands,
categories,
collectionMemberIds,
colorInfo,
conditions,
expireTime,
fulfillmentInfo,
gtin,
images,
languageCode,
localInventories,
materials,
patterns,
priceInfo,
primaryProductId,
promotions,
publishTime,
rating,
retrievableFields,
sizes,
tags,
title,
ttl,
type,
uri,
variants
FROM google.retail.products
WHERE branchesId = '{{ branchesId }}'
AND catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
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
INSERT INTO google.retail.products (
branchesId,
catalogsId,
locationsId,
projectsId,
expireTime,
ttl,
name,
id,
type,
primaryProductId,
collectionMemberIds,
gtin,
categories,
title,
brands,
description,
languageCode,
attributes,
tags,
priceInfo,
rating,
availableTime,
availability,
availableQuantity,
fulfillmentInfo,
uri,
images,
audience,
colorInfo,
sizes,
materials,
patterns,
conditions,
promotions,
publishTime,
retrievableFields,
variants,
localInventories
)
SELECT 
'{{ branchesId }}',
'{{ catalogsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ expireTime }}',
'{{ ttl }}',
'{{ name }}',
'{{ id }}',
'{{ type }}',
'{{ primaryProductId }}',
'{{ collectionMemberIds }}',
'{{ gtin }}',
'{{ categories }}',
'{{ title }}',
'{{ brands }}',
'{{ description }}',
'{{ languageCode }}',
'{{ attributes }}',
'{{ tags }}',
'{{ priceInfo }}',
'{{ rating }}',
'{{ availableTime }}',
'{{ availability }}',
'{{ availableQuantity }}',
'{{ fulfillmentInfo }}',
'{{ uri }}',
'{{ images }}',
'{{ audience }}',
'{{ colorInfo }}',
'{{ sizes }}',
'{{ materials }}',
'{{ patterns }}',
'{{ conditions }}',
'{{ promotions }}',
'{{ publishTime }}',
'{{ retrievableFields }}',
'{{ variants }}',
'{{ localInventories }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: expireTime
      value: '{{ expireTime }}'
    - name: ttl
      value: '{{ ttl }}'
    - name: name
      value: '{{ name }}'
    - name: id
      value: '{{ id }}'
    - name: type
      value: '{{ type }}'
    - name: primaryProductId
      value: '{{ primaryProductId }}'
    - name: collectionMemberIds
      value: '{{ collectionMemberIds }}'
    - name: gtin
      value: '{{ gtin }}'
    - name: categories
      value: '{{ categories }}'
    - name: title
      value: '{{ title }}'
    - name: brands
      value: '{{ brands }}'
    - name: description
      value: '{{ description }}'
    - name: languageCode
      value: '{{ languageCode }}'
    - name: attributes
      value: '{{ attributes }}'
    - name: tags
      value: '{{ tags }}'
    - name: priceInfo
      value: '{{ priceInfo }}'
    - name: rating
      value: '{{ rating }}'
    - name: availableTime
      value: '{{ availableTime }}'
    - name: availability
      value: '{{ availability }}'
    - name: availableQuantity
      value: '{{ availableQuantity }}'
    - name: fulfillmentInfo
      value: '{{ fulfillmentInfo }}'
    - name: uri
      value: '{{ uri }}'
    - name: images
      value: '{{ images }}'
    - name: audience
      value: '{{ audience }}'
    - name: colorInfo
      value: '{{ colorInfo }}'
    - name: sizes
      value: '{{ sizes }}'
    - name: materials
      value: '{{ materials }}'
    - name: patterns
      value: '{{ patterns }}'
    - name: conditions
      value: '{{ conditions }}'
    - name: promotions
      value: '{{ promotions }}'
    - name: publishTime
      value: '{{ publishTime }}'
    - name: retrievableFields
      value: '{{ retrievableFields }}'
    - name: variants
      value: '{{ variants }}'
    - name: localInventories
      value: '{{ localInventories }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>products</code> resource.

```sql
/*+ update */
UPDATE google.retail.products
SET 
expireTime = '{{ expireTime }}',
ttl = '{{ ttl }}',
name = '{{ name }}',
id = '{{ id }}',
type = '{{ type }}',
primaryProductId = '{{ primaryProductId }}',
collectionMemberIds = '{{ collectionMemberIds }}',
gtin = '{{ gtin }}',
categories = '{{ categories }}',
title = '{{ title }}',
brands = '{{ brands }}',
description = '{{ description }}',
languageCode = '{{ languageCode }}',
attributes = '{{ attributes }}',
tags = '{{ tags }}',
priceInfo = '{{ priceInfo }}',
rating = '{{ rating }}',
availableTime = '{{ availableTime }}',
availability = '{{ availability }}',
availableQuantity = '{{ availableQuantity }}',
fulfillmentInfo = '{{ fulfillmentInfo }}',
uri = '{{ uri }}',
images = '{{ images }}',
audience = '{{ audience }}',
colorInfo = '{{ colorInfo }}',
sizes = '{{ sizes }}',
materials = '{{ materials }}',
patterns = '{{ patterns }}',
conditions = '{{ conditions }}',
promotions = '{{ promotions }}',
publishTime = '{{ publishTime }}',
retrievableFields = '{{ retrievableFields }}',
variants = '{{ variants }}',
localInventories = '{{ localInventories }}'
WHERE 
branchesId = '{{ branchesId }}'
AND catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND productsId = '{{ productsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>products</code> resource.

```sql
/*+ delete */
DELETE FROM google.retail.products
WHERE branchesId = '{{ branchesId }}'
AND catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND productsId = '{{ productsId }}'
AND projectsId = '{{ projectsId }}';
```
