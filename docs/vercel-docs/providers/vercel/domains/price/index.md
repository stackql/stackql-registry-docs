---
title: price
hide_title: false
hide_table_of_contents: false
keywords:
  - price
  - domains
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>price</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.domains.price</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `period` | `number` | The number of years the domain could be held before paying again. |
| `price` | `number` | The domain price in USD. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `check_domain_price` | `SELECT` | `name, teamId` |
