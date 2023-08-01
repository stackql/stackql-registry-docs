---
title: certificate_authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_authorities
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
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.certificate_authorities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | A list of locations (e.g. "us-west1") that could not be reached. |
| `certificateAuthorities` | `array` | The list of CertificateAuthorities. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListCertificateAuthoritiesRequest.next_page_token to retrieve the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Returns a CertificateAuthority. |
| `list` | `SELECT` | `caPoolsId, locationsId, projectsId` | Lists CertificateAuthorities. |
| `create` | `INSERT` | `caPoolsId, locationsId, projectsId` | Create a new CertificateAuthority in a given Project and Location. |
| `delete` | `DELETE` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Delete a CertificateAuthority. |
| `activate` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Activate a CertificateAuthority that is in state AWAITING_USER_ACTIVATION and is of type SUBORDINATE. After the parent Certificate Authority signs a certificate signing request from FetchCertificateAuthorityCsr, this method can complete the activation process. |
| `disable` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Disable a CertificateAuthority. |
| `enable` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Enable a CertificateAuthority. |
| `fetch` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Fetch a certificate signing request (CSR) from a CertificateAuthority that is in state AWAITING_USER_ACTIVATION and is of type SUBORDINATE. The CSR must then be signed by the desired parent Certificate Authority, which could be another CertificateAuthority resource, or could be an on-prem certificate authority. See also ActivateCertificateAuthority. |
| `patch` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Update a CertificateAuthority. |
| `undelete` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Undelete a CertificateAuthority that has been deleted. |
