---
title: pages
hide_title: false
hide_table_of_contents: false
keywords:
  - pages
  - factchecktools
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
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.factchecktools.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of this `ClaimReview` markup page resource, in the form of `pages/&#123;page_id&#125;`. Except for update requests, this field is output-only and should not be set by the user. |
| `pageUrl` | `string` | The URL of the page associated with this `ClaimReview` markup. While every individual `ClaimReview` has its own URL field, semantically this is a page-level field, and each `ClaimReview` on this page will use this value unless individually overridden. Corresponds to `ClaimReview.url` |
| `publishDate` | `string` | The date when the fact check was published. Similar to the URL, semantically this is a page-level field, and each `ClaimReview` on this page will contain the same value. Corresponds to `ClaimReview.datePublished` |
| `versionId` | `string` | The version ID for this markup. Except for update requests, this field is output-only and should not be set by the user. |
| `claimReviewAuthor` | `object` | Information about the claim review author. |
| `claimReviewMarkups` | `array` | A list of individual claim reviews for this page. Each item in the list corresponds to one `ClaimReview` element. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `pagesId` | Get all `ClaimReview` markup on a page. |
| `list` | `SELECT` |  | List the `ClaimReview` markup pages for a specific URL or for an organization. |
| `create` | `INSERT` |  | Create `ClaimReview` markup on a page. |
| `delete` | `DELETE` | `pagesId` | Delete all `ClaimReview` markup on a page. |
| `update` | `EXEC` | `pagesId` | Update for all `ClaimReview` markup on a page Note that this is a full update. To retain the existing `ClaimReview` markup on a page, first perform a Get operation, then modify the returned markup, and finally call Update with the entire `ClaimReview` markup as the body. |
