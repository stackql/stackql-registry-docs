---
title: certificate_revocation_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_revocation_lists
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
<tr><td><b>Name</b></td><td><code>certificate_revocation_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.certificate_revocation_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `certificateRevocationLists` | `array` | The list of CertificateRevocationLists. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListCertificateRevocationListsRequest.next_page_token to retrieve the next page of results. |
| `unreachable` | `array` | A list of locations (e.g. "us-west1") that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `caPoolsId, certificateAuthoritiesId, certificateRevocationListsId, locationsId, projectsId` | Returns a CertificateRevocationList. |
| `list` | `SELECT` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Lists CertificateRevocationLists. |
| `patch` | `EXEC` | `caPoolsId, certificateAuthoritiesId, certificateRevocationListsId, locationsId, projectsId` | Update a CertificateRevocationList. |
