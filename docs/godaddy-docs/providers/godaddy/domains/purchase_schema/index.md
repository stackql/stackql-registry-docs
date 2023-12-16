---
title: purchase_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - purchase_schema
  - domains
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>purchase_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.domains.purchase_schema</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `models` | `object` |
| `properties` | `object` |
| `required` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `schema` | `SELECT` | `tld` |
