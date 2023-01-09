---
title: categories
hide_title: false
hide_table_of_contents: false
keywords:
  - categories
  - mybusinessbusinessinformation
  - googlemybusiness    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>categories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessbusinessinformation.categories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `categories` | `array` | The matching categories based on the requested parameters. |
| `nextPageToken` | `string` | If the number of categories exceeded the requested page size, this field will be populated with a token to fetch the next page of categories on a subsequent call to `ListCategories`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` |  | Returns a list of business categories. Search will match the category name but not the category ID. Search only matches the front of a category name (that is, 'food' may return 'Food Court' but not 'Fast Food Restaurant'). |
| `batchGet` | `EXEC` |  | Returns a list of business categories for the provided language and GConcept ids. |
