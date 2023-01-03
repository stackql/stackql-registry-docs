---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - cloudbilling
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbilling.skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the SKU. Example: "services/DA34-426B-A397/skus/AA95-CD31-42FE" |
| `description` | `string` | A human readable description of the SKU, has a maximum length of 256 characters. |
| `pricingInfo` | `array` | A timeline of pricing info for this SKU in chronological order. |
| `serviceProviderName` | `string` | Identifies the service provider. This is 'Google' for first party services in Google Cloud Platform. |
| `serviceRegions` | `array` | List of service regions this SKU is offered at. Example: "asia-east1" Service regions can be found at https://cloud.google.com/about/locations/ |
| `skuId` | `string` | The identifier for the SKU. Example: "AA95-CD31-42FE" |
| `category` | `object` | Represents the category hierarchy of a SKU. |
| `geoTaxonomy` | `object` | Encapsulates the geographic taxonomy data for a sku. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `services_skus_list` | `SELECT` | `servicesId` |
