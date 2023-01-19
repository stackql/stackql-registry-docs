---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - manufacturers
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.manufacturers.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name in the format `&#123;target_country&#125;:&#123;content_language&#125;:&#123;product_id&#125;`. `target_country` - The target country of the product as a CLDR territory code (for example, US). `content_language` - The content language of the product as a two-letter ISO 639-1 language code (for example, en). `product_id` - The ID of the product. For more information, see https://support.google.com/manufacturers/answer/6124116#id. |
| `productId` | `string` | The ID of the product. For more information, see https://support.google.com/manufacturers/answer/6124116#id. |
| `targetCountry` | `string` | The target country of the product as a CLDR territory code (for example, US). |
| `attributes` | `object` | Attributes of the product. For more information, see https://support.google.com/manufacturers/answer/6124116. |
| `contentLanguage` | `string` | The content language of the product as a two-letter ISO 639-1 language code (for example, en). |
| `destinationStatuses` | `array` | The status of the destinations. |
| `issues` | `array` | A server-generated list of issues associated with the product. |
| `parent` | `string` | Parent ID in the format `accounts/&#123;account_id&#125;`. `account_id` - The ID of the Manufacturer Center account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_products_get` | `SELECT` | `accountsId, productsId` | Gets the product from a Manufacturer Center account, including product issues. A recently updated product takes around 15 minutes to process. Changes are only visible after it has been processed. While some issues may be available once the product has been processed, other issues may take days to appear. |
| `accounts_products_list` | `SELECT` | `accountsId` | Lists all the products in a Manufacturer Center account. |
| `accounts_products_delete` | `DELETE` | `accountsId, productsId` | Deletes the product from a Manufacturer Center account. |
| `accounts_products_update` | `EXEC` | `accountsId, productsId` | Inserts or updates the attributes of the product in a Manufacturer Center account. Creates a product with the provided attributes. If the product already exists, then all attributes are replaced with the new ones. The checks at upload time are minimal. All required attributes need to be present for a product to be valid. Issues may show up later after the API has accepted a new upload for a product and it is possible to overwrite an existing valid product with an invalid product. To detect this, you should retrieve the product and check it for issues once the new version is available. Uploaded attributes first need to be processed before they can be retrieved. Until then, new products will be unavailable, and retrieval of previously uploaded products will return the original state of the product. |
