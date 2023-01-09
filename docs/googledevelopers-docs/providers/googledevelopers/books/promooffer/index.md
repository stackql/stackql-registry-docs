---
title: promooffer
hide_title: false
hide_table_of_contents: false
keywords:
  - promooffer
  - books
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
<tr><td><b>Name</b></td><td><code>promooffer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.promooffer</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `items` | `array` |
| `artUrl` | `string` |
| `gservicesKey` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Returns a list of promo offers available to the user |
| `accept` | `EXEC` |  | Accepts the promo offer. |
| `dismiss` | `EXEC` |  | Marks the promo offer as dismissed. |
