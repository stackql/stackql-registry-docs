---
title: readingpositions
hide_title: false
hide_table_of_contents: false
keywords:
  - readingpositions
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
<tr><td><b>Name</b></td><td><code>readingpositions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.readingpositions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Resource type for a reading position. |
| `pdfPosition` | `string` | Position in a PDF file. |
| `updated` | `string` | Timestamp when this reading position was last updated (formatted UTC timestamp with millisecond resolution). |
| `volumeId` | `string` | Volume id associated with this reading position. |
| `epubCfiPosition` | `string` | Position in an EPUB as a CFI. |
| `gbImagePosition` | `string` | Position in a volume for image-based content. |
| `gbTextPosition` | `string` | Position in a volume for text-based content. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `mylibrary_readingpositions_get` | `SELECT` | `volumeId` | Retrieves my reading position information for a volume. |
| `mylibrary_readingpositions_setPosition` | `EXEC` | `position, timestamp, volumeId` | Sets my reading position information for a volume. |
