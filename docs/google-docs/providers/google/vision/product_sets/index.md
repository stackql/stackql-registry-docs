---
title: product_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - product_sets
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vision.product_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `productSets` | `array` | List of ProductSets. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_product_sets_get` | `SELECT` | `locationsId, productSetsId, projectsId` | Gets information associated with a ProductSet. Possible errors: * Returns NOT_FOUND if the ProductSet does not exist. |
| `projects_locations_product_sets_list` | `SELECT` | `locationsId, projectsId` | Lists ProductSets in an unspecified order. Possible errors: * Returns INVALID_ARGUMENT if page_size is greater than 100, or less than 1. |
| `projects_locations_product_sets_create` | `INSERT` | `locationsId, projectsId` | Creates and returns a new ProductSet resource. Possible errors: * Returns INVALID_ARGUMENT if display_name is missing, or is longer than 4096 characters. |
| `projects_locations_product_sets_delete` | `DELETE` | `locationsId, productSetsId, projectsId` | Permanently deletes a ProductSet. Products and ReferenceImages in the ProductSet are not deleted. The actual image files are not deleted from Google Cloud Storage. |
| `projects_locations_product_sets_import` | `EXEC` | `locationsId, projectsId` | Asynchronous API that imports a list of reference images to specified product sets based on a list of image information. The google.longrunning.Operation API can be used to keep track of the progress and results of the request. `Operation.metadata` contains `BatchOperationMetadata`. (progress) `Operation.response` contains `ImportProductSetsResponse`. (results) The input source of this method is a csv file on Google Cloud Storage. For the format of the csv file please see ImportProductSetsGcsSource.csv_file_uri. |
| `projects_locations_product_sets_patch` | `EXEC` | `locationsId, productSetsId, projectsId` | Makes changes to a ProductSet resource. Only display_name can be updated currently. Possible errors: * Returns NOT_FOUND if the ProductSet does not exist. * Returns INVALID_ARGUMENT if display_name is present in update_mask but missing from the request or longer than 4096 characters. |
