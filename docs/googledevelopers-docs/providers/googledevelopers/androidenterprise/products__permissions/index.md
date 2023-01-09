---
title: products__permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - products__permissions
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
<tr><td><b>Name</b></td><td><code>products__permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.products__permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `permission` | `array` | The permissions required by the app. |
| `productId` | `string` | The ID of the app that the permissions relate to, e.g. "app:com.google.android.gm". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `products_getPermissions` | `SELECT` | `enterpriseId, productId` |
