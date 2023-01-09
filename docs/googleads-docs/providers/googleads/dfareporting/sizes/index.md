---
title: sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - sizes
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.sizes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this size. This is a read-only, auto-generated field. |
| `iab` | `boolean` | IAB standard size. This is a read-only, auto-generated field. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#size". |
| `width` | `integer` | Width of this size. Acceptable values are 0 to 32767, inclusive. |
| `height` | `integer` | Height of this size. Acceptable values are 0 to 32767, inclusive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, profileId` | Gets one size by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of sizes, possibly filtered. Retrieved sizes are globally unique and may include values not currently in use by your account. Due to this, the list of sizes returned by this method may differ from the list seen in the Trafficking UI. |
| `insert` | `INSERT` | `profileId` | Inserts a new size. |
