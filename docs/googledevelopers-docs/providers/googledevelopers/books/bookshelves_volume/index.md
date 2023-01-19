---
title: bookshelves_volume
hide_title: false
hide_table_of_contents: false
keywords:
  - bookshelves_volume
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
<tr><td><b>Name</b></td><td><code>bookshelves_volume</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.bookshelves_volume</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `mylibrary_bookshelves_addVolume` | `EXEC` | `shelf, volumeId` | Adds a volume to a bookshelf. |
| `mylibrary_bookshelves_removeVolume` | `EXEC` | `shelf, volumeId` | Removes a volume from a bookshelf. |
