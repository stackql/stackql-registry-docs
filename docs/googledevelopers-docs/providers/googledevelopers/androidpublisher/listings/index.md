---
title: listings
hide_title: false
hide_table_of_contents: false
keywords:
  - listings
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
<tr><td><b>Name</b></td><td><code>listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.listings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `fullDescription` | `string` | Full description of the app. |
| `language` | `string` | Language localization code (a BCP-47 language tag; for example, "de-AT" for Austrian German). |
| `shortDescription` | `string` | Short description of the app. |
| `title` | `string` | Localized title of the app. |
| `video` | `string` | URL of a promotional YouTube video for the app. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `edits_listings_get` | `SELECT` | `editId, language, packageName` | Gets a localized store listing. |
| `edits_listings_list` | `SELECT` | `editId, packageName` | Lists all localized store listings. |
| `edits_listings_delete` | `DELETE` | `editId, language, packageName` | Deletes a localized store listing. |
| `edits_listings_patch` | `EXEC` | `editId, language, packageName` | Patches a localized store listing. |
| `edits_listings_update` | `EXEC` | `editId, language, packageName` | Creates or updates a localized store listing. |
