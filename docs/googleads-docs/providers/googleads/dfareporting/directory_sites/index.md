---
title: directory_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_sites
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
<tr><td><b>Name</b></td><td><code>directory_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.directory_sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this directory site. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this directory site. |
| `idDimensionValue` | `object` | Represents a DimensionValue resource. |
| `inpageTagFormats` | `array` | Tag types for regular placements. Acceptable values are: - "STANDARD" - "IFRAME_JAVASCRIPT_INPAGE" - "INTERNAL_REDIRECT_INPAGE" - "JAVASCRIPT_INPAGE"  |
| `interstitialTagFormats` | `array` | Tag types for interstitial placements. Acceptable values are: - "IFRAME_JAVASCRIPT_INTERSTITIAL" - "INTERNAL_REDIRECT_INTERSTITIAL" - "JAVASCRIPT_INTERSTITIAL"  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#directorySite". |
| `settings` | `object` | Directory Site Settings |
| `url` | `string` | URL of this directory site. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `directorySites_get` | `SELECT` | `id, profileId` | Gets one directory site by ID. |
| `directorySites_list` | `SELECT` | `profileId` | Retrieves a list of directory sites, possibly filtered. This method supports paging. |
| `directorySites_insert` | `EXEC` | `profileId` | Inserts a new directory site. |
