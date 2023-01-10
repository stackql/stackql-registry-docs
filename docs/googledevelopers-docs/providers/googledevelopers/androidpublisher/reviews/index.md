---
title: reviews
hide_title: false
hide_table_of_contents: false
keywords:
  - reviews
  - androidpublisher
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
<tr><td><b>Name</b></td><td><code>reviews</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.reviews</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `comments` | `array` | A repeated field containing comments for the review. |
| `reviewId` | `string` | Unique identifier for this review. |
| `authorName` | `string` | The name of the user who wrote the review. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageName, reviewId` | Gets a single review. |
| `list` | `SELECT` | `packageName` | Lists all reviews. |
| `reply` | `EXEC` | `packageName, reviewId` | Replies to a single review, or updates an existing reply. |
