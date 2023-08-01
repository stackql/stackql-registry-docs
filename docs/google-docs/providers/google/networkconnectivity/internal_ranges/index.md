---
title: internal_ranges
hide_title: false
hide_table_of_contents: false
keywords:
  - internal_ranges
  - networkconnectivity
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>internal_ranges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.internal_ranges</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `internalRanges` | `array` | Internal ranges to be returned. |
| `nextPageToken` | `string` | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `internalRangesId, locationsId, projectsId` | Gets details of a single internal range. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists internal ranges in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new internal range in a given project and location. |
| `delete` | `DELETE` | `internalRangesId, locationsId, projectsId` | Deletes a single internal range. |
| `patch` | `EXEC` | `internalRangesId, locationsId, projectsId` | Updates the parameters of a single internal range. |
