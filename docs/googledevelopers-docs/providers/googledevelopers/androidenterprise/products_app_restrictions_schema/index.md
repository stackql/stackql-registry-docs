---
title: products_app_restrictions_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - products_app_restrictions_schema
  - androidenterprise
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
<tr><td><b>Name</b></td><td><code>products_app_restrictions_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.products_app_restrictions_schema</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Deprecated. |
| `restrictions` | `array` | The set of restrictions that make up this schema. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `products_getAppRestrictionsSchema` | `SELECT` | `enterpriseId, productId` |
