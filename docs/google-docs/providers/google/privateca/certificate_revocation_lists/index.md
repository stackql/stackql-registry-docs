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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Output only. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`. |
| `sequenceNumber` | `string` | Output only. The CRL sequence number that appears in pem_crl. |
| `createTime` | `string` | Output only. The time at which this CertificateRevocationList was created. |
| `revokedCertificates` | `array` | Output only. The revoked serial numbers that appear in pem_crl. |
| `pemCrl` | `string` | Output only. The PEM-encoded X.509 CRL. |
| `accessUrl` | `string` | Output only. The location where 'pem_crl' can be accessed. |
| `labels` | `object` | Optional. Labels with user-defined metadata. |
| `revisionId` | `string` | Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string. |
| `updateTime` | `string` | Output only. The time at which this CertificateRevocationList was updated. |
| `state` | `string` | Output only. The State for this CertificateRevocationList. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_caPools_certificateAuthorities_certificateRevocationLists_get` | `SELECT` | `caPoolsId, certificateAuthoritiesId, certificateRevocationListsId, locationsId, projectsId` | Returns a CertificateRevocationList. |
| `projects_locations_caPools_certificateAuthorities_certificateRevocationLists_list` | `SELECT` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Lists CertificateRevocationLists. |
| `projects_locations_caPools_certificateAuthorities_certificateRevocationLists_patch` | `EXEC` | `caPoolsId, certificateAuthoritiesId, certificateRevocationListsId, locationsId, projectsId` | Update a CertificateRevocationList. |
