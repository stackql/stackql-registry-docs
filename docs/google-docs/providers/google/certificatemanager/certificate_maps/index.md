---
title: certificate_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_maps
  - certificatemanager
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
<tr><td><b>Name</b></td><td><code>certificate_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.certificate_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
| `unreachable` | `array` | Locations that could not be reached. |
| `certificateMaps` | `array` | A list of certificate maps for the parent resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateMapsId, locationsId, projectsId` | Gets details of a single CertificateMap. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists CertificateMaps in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new CertificateMap in a given project and location. |
| `delete` | `DELETE` | `certificateMapsId, locationsId, projectsId` | Deletes a single CertificateMap. A Certificate Map can't be deleted if it contains Certificate Map Entries. Remove all the entries from the map before calling this method. |
| `patch` | `EXEC` | `certificateMapsId, locationsId, projectsId` | Updates a CertificateMap. |
