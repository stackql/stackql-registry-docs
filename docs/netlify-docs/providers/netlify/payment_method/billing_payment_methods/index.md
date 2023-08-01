---
title: billing_payment_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_payment_methods
  - payment_method
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_payment_methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.payment_method.billing_payment_methods</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `method_name` | `string` |
| `state` | `string` |
| `type` | `string` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `data` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listPaymentMethodsForUser` | `SELECT` |  |
