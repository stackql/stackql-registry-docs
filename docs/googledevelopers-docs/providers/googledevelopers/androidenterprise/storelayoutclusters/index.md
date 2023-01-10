---
title: storelayoutclusters
hide_title: false
hide_table_of_contents: false
keywords:
  - storelayoutclusters
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
<tr><td><b>Name</b></td><td><code>storelayoutclusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.storelayoutclusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of this cluster. Assigned by the server. Immutable once assigned. |
| `name` | `array` | Ordered list of localized strings giving the name of this page. The text displayed is the one that best matches the user locale, or the first entry if there is no good match. There needs to be at least one entry. |
| `orderInPage` | `string` | String (US-ASCII only) used to determine order of this cluster within the parent page's elements. Page elements are sorted in lexicographic order of this field. Duplicated values are allowed, but ordering between elements with duplicate order is undefined. The value of this field is never visible to a user, it is used solely for the purpose of defining an ordering. Maximum length is 256 characters. |
| `productId` | `array` | List of products in the order they are displayed in the cluster. There should not be duplicates within a cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterId, enterpriseId, pageId` | Retrieves details of a cluster. |
| `list` | `SELECT` | `enterpriseId, pageId` | Retrieves the details of all clusters on the specified page. |
| `insert` | `INSERT` | `enterpriseId, pageId` | Inserts a new cluster in a page. |
| `delete` | `DELETE` | `clusterId, enterpriseId, pageId` | Deletes a cluster. |
| `update` | `EXEC` | `clusterId, enterpriseId, pageId` | Updates a cluster. |
