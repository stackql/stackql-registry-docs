---
title: recommended
hide_title: false
hide_table_of_contents: false
keywords:
  - recommended
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
<tr><td><b>Name</b></td><td><code>recommended</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.books.recommended</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for a volume. (In LITE projection.) |
| `searchInfo` | `object` | Search result information related to this volume. |
| `saleInfo` | `object` | Any information about a volume related to the eBookstore and/or purchaseability. This information can depend on the country where the request originates from (i.e. books may not be for sale in certain countries). |
| `accessInfo` | `object` | Any information about a volume related to reading or obtaining that volume text. This information can depend on country (books may be public domain in one country but not in another, e.g.). |
| `selfLink` | `string` | URL to this resource. (In LITE projection.) |
| `recommendedInfo` | `object` | Recommendation related information for this volume. |
| `layerInfo` | `object` | What layers exist in this volume and high level information about them. |
| `volumeInfo` | `object` | General volume information. |
| `userInfo` | `object` | User specific information related to this volume. (e.g. page this user last read or whether they purchased this book) |
| `etag` | `string` | Opaque identifier for a specific version of a volume resource. (In LITE projection) |
| `kind` | `string` | Resource type for a volume. (In LITE projection.) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `volumes_recommended_list` | `SELECT` |  | Return a list of recommended books for the current user. |
| `volumes_recommended_rate` | `EXEC` | `rating, volumeId` | Rate a recommended book for the current user. |
