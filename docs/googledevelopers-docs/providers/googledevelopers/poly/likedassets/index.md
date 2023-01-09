---
title: likedassets
hide_title: false
hide_table_of_contents: false
keywords:
  - likedassets
  - poly
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
<tr><td><b>Name</b></td><td><code>likedassets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.poly.likedassets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalSize` | `integer` | The total number of assets in the list, without pagination. |
| `assets` | `array` | A list of assets that match the criteria specified in the request. |
| `nextPageToken` | `string` | The continuation token for retrieving the next page. If empty, indicates that there are no more pages. To get the next page, submit the same request specifying this value as the page_token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users_likedassets_list` | `SELECT` | `usersId` |
