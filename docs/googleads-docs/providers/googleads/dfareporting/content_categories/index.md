---
title: content_categories
hide_title: false
hide_table_of_contents: false
keywords:
  - content_categories
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
<tr><td><b>Name</b></td><td><code>content_categories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.content_categories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this content category. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this content category. This is a required field and must be less than 256 characters long and unique among content categories of the same account. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#contentCategory". |
| `accountId` | `string` | Account ID of this content category. This is a read-only field that can be left blank. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `contentCategories_get` | `SELECT` | `id, profileId` | Gets one content category by ID. |
| `contentCategories_list` | `SELECT` | `profileId` | Retrieves a list of content categories, possibly filtered. This method supports paging. |
| `contentCategories_delete` | `DELETE` | `id, profileId` | Deletes an existing content category. |
| `contentCategories_insert` | `EXEC` | `profileId` | Inserts a new content category. |
| `contentCategories_patch` | `EXEC` | `id, profileId` | Updates an existing content category. This method supports patch semantics. |
| `contentCategories_update` | `EXEC` | `profileId` | Updates an existing content category. |
