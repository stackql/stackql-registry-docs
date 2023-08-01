---
title: certificate_map_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_map_entries
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
<tr><td><b>Name</b></td><td><code>certificate_map_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.certificate_map_entries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
| `unreachable` | `array` | Locations that could not be reached. |
| `certificateMapEntries` | `array` | A list of certificate map entries for the parent resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateMapEntriesId, certificateMapsId, locationsId, projectsId` | Gets details of a single CertificateMapEntry. |
| `list` | `SELECT` | `certificateMapsId, locationsId, projectsId` | Lists CertificateMapEntries in a given project and location. |
| `create` | `INSERT` | `certificateMapsId, locationsId, projectsId` | Creates a new CertificateMapEntry in a given project and location. |
| `delete` | `DELETE` | `certificateMapEntriesId, certificateMapsId, locationsId, projectsId` | Deletes a single CertificateMapEntry. |
| `patch` | `EXEC` | `certificateMapEntriesId, certificateMapsId, locationsId, projectsId` | Updates a CertificateMapEntry. |
