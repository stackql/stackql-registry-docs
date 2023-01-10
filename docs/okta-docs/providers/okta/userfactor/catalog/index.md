---
title: catalog
hide_title: false
hide_table_of_contents: false
keywords:
  - catalog
  - userfactor
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.userfactor.catalog</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `provider` | `string` |
| `_links` | `object` |
| `status` | `string` |
| `created` | `string` |
| `lastUpdated` | `string` |
| `_embedded` | `object` |
| `factorType` | `string` |
| `verify` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `userId` |
