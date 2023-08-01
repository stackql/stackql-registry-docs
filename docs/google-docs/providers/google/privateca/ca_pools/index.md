---
title: ca_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_pools
  - privateca
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
<tr><td><b>Name</b></td><td><code>ca_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.ca_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `caPools` | `array` | The list of CaPools. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListCertificateAuthoritiesRequest.next_page_token to retrieve the next page of results. |
| `unreachable` | `array` | A list of locations (e.g. "us-west1") that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `caPoolsId, locationsId, projectsId` | Returns a CaPool. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists CaPools. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a CaPool. |
| `delete` | `DELETE` | `caPoolsId, locationsId, projectsId` | Delete a CaPool. |
| `patch` | `EXEC` | `caPoolsId, locationsId, projectsId` | Update a CaPool. |
