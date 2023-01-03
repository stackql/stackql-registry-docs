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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Output only. The resource name for this CertificateAuthority in the format `projects/*/locations/*/caPools/*/certificateAuthorities/*`. |
| `subordinateConfig` | `object` | Describes a subordinate CA's issuers. This is either a resource name to a known issuing CertificateAuthority, or a PEM issuer certificate chain. |
| `type` | `string` | Required. Immutable. The Type of this CertificateAuthority. |
| `caCertificateDescriptions` | `array` | Output only. A structured description of this CertificateAuthority's CA certificate and its issuers. Ordered as self-to-root. |
| `state` | `string` | Output only. The State for this CertificateAuthority. |
| `tier` | `string` | Output only. The CaPool.Tier of the CaPool that includes this CertificateAuthority. |
| `lifetime` | `string` | Required. Immutable. The desired lifetime of the CA certificate. Used to create the "not_before_time" and "not_after_time" fields inside an X.509 certificate. |
| `pemCaCertificates` | `array` | Output only. This CertificateAuthority's certificate chain, including the current CertificateAuthority's certificate. Ordered such that the root issuer is the final element (consistent with RFC 5246). For a self-signed CA, this will only list the current CertificateAuthority's certificate. |
| `updateTime` | `string` | Output only. The time at which this CertificateAuthority was last updated. |
| `keySpec` | `object` | A Cloud KMS key configuration that a CertificateAuthority will use. |
| `accessUrls` | `object` | URLs where a CertificateAuthority will publish content. |
| `createTime` | `string` | Output only. The time at which this CertificateAuthority was created. |
| `labels` | `object` | Optional. Labels with user-defined metadata. |
| `config` | `object` | A CertificateConfig describes an X.509 certificate or CSR that is to be created, as an alternative to using ASN.1. |
| `expireTime` | `string` | Output only. The time at which this CertificateAuthority will be permanently purged, if it is in the DELETED state. |
| `deleteTime` | `string` | Output only. The time at which this CertificateAuthority was soft deleted, if it is in the DELETED state. |
| `gcsBucket` | `string` | Immutable. The name of a Cloud Storage bucket where this CertificateAuthority will publish content, such as the CA certificate and CRLs. This must be a bucket name, without any prefixes (such as `gs://`) or suffixes (such as `.googleapis.com`). For example, to use a bucket named `my-bucket`, you would simply specify `my-bucket`. If not specified, a managed bucket will be created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_caPools_certificateAuthorities_get` | `SELECT` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Returns a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_list` | `SELECT` | `caPoolsId, locationsId, projectsId` | Lists CertificateAuthorities. |
| `projects_locations_caPools_certificateAuthorities_create` | `INSERT` | `caPoolsId, locationsId, projectsId` | Create a new CertificateAuthority in a given Project and Location. |
| `projects_locations_caPools_certificateAuthorities_delete` | `DELETE` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Delete a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_activate` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Activate a CertificateAuthority that is in state AWAITING_USER_ACTIVATION and is of type SUBORDINATE. After the parent Certificate Authority signs a certificate signing request from FetchCertificateAuthorityCsr, this method can complete the activation process. |
| `projects_locations_caPools_certificateAuthorities_disable` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Disable a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_enable` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Enable a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_patch` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Update a CertificateAuthority. |
| `projects_locations_caPools_certificateAuthorities_undelete` | `EXEC` | `caPoolsId, certificateAuthoritiesId, locationsId, projectsId` | Undelete a CertificateAuthority that has been deleted. |
