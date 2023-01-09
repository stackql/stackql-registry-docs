---
title: bookshelves
hide_title: false
hide_table_of_contents: false
keywords:
  - bookshelves
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
<tr><td><b>Name</b></td><td><code>bookshelves</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.bookshelves</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Id of this bookshelf, only unique by user. |
| `description` | `string` | Description of this bookshelf. |
| `access` | `string` | Whether this bookshelf is PUBLIC or PRIVATE. |
| `kind` | `string` | Resource type for bookshelf metadata. |
| `title` | `string` | Title of this bookshelf. |
| `selfLink` | `string` | URL to this resource. |
| `volumesLastUpdated` | `string` | Last time a volume was added or removed from this bookshelf (formatted UTC timestamp with millisecond resolution). |
| `created` | `string` | Created time for this bookshelf (formatted UTC timestamp with millisecond resolution). |
| `updated` | `string` | Last modified time of this bookshelf (formatted UTC timestamp with millisecond resolution). |
| `volumeCount` | `integer` | Number of volumes in this bookshelf. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `shelf, userId` | Retrieves metadata for a specific bookshelf for the specified user. |
| `list` | `SELECT` | `userId` | Retrieves a list of public bookshelves for the specified user. |
| `mylibrary_bookshelves_get` | `SELECT` | `shelf` | Retrieves metadata for a specific bookshelf belonging to the authenticated user. |
| `mylibrary_bookshelves_list` | `SELECT` |  | Retrieves a list of bookshelves belonging to the authenticated user. |
| `mylibrary_bookshelves_clearVolumes` | `EXEC` | `shelf` | Clears all volumes from a bookshelf. |
| `mylibrary_bookshelves_moveVolume` | `EXEC` | `shelf, volumeId, volumePosition` | Moves a volume within a bookshelf. |
