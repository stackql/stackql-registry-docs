---
title: storelayoutpages
hide_title: false
hide_table_of_contents: false
keywords:
  - storelayoutpages
  - androidenterprise
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
<tr><td><b>Name</b></td><td><code>storelayoutpages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.storelayoutpages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of this page. Assigned by the server. Immutable once assigned. |
| `name` | `array` | Ordered list of localized strings giving the name of this page. The text displayed is the one that best matches the user locale, or the first entry if there is no good match. There needs to be at least one entry. |
| `link` | `array` | Ordered list of pages a user should be able to reach from this page. The list can't include this page. It is recommended that the basic pages are created first, before adding the links between pages. The API doesn't verify that the pages exist or the pages are reachable. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `enterpriseId, pageId` | Retrieves details of a store page. |
| `list` | `SELECT` | `enterpriseId` | Retrieves the details of all pages in the store. |
| `insert` | `INSERT` | `enterpriseId` | Inserts a new store page. |
| `delete` | `DELETE` | `enterpriseId, pageId` | Deletes a store page. |
| `update` | `EXEC` | `enterpriseId, pageId` | Updates the content of a store page. |
