---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this Certificate in the format `projects/*/locations/*/caPools/*/certificates/*`. |
| `pemCsr` | `string` | Immutable. A pem-encoded X.509 certificate signing request (CSR). |
| `certificateDescription` | `object` | A CertificateDescription describes an X.509 certificate or CSR that has been issued, as an alternative to using ASN.1 / X.509. |
| `revocationDetails` | `object` | Describes fields that are relavent to the revocation of a Certificate. |
| `subjectMode` | `string` | Immutable. Specifies how the Certificate's identity fields are to be decided. If this is omitted, the `DEFAULT` subject mode will be used. |
| `createTime` | `string` | Output only. The time at which this Certificate was created. |
| `labels` | `object` | Optional. Labels with user-defined metadata. |
| `pemCertificateChain` | `array` | Output only. The chain that may be used to verify the X.509 certificate. Expected to be in issuer-to-root order according to RFC 5246. |
| `issuerCertificateAuthority` | `string` | Output only. The resource name of the issuing CertificateAuthority in the format `projects/*/locations/*/caPools/*/certificateAuthorities/*`. |
| `config` | `object` | A CertificateConfig describes an X.509 certificate or CSR that is to be created, as an alternative to using ASN.1. |
| `lifetime` | `string` | Required. Immutable. The desired lifetime of a certificate. Used to create the "not_before_time" and "not_after_time" fields inside an X.509 certificate. Note that the lifetime may be truncated if it would extend past the life of any certificate authority in the issuing chain. |
| `pemCertificate` | `string` | Output only. The pem-encoded, signed X.509 certificate. |
| `updateTime` | `string` | Output only. The time at which this Certificate was updated. |
| `certificateTemplate` | `string` | Immutable. The resource name for a CertificateTemplate used to issue this certificate, in the format `projects/*/locations/*/certificateTemplates/*`. If this is specified, the caller must have the necessary permission to use this template. If this is omitted, no template will be used. This template must be in the same location as the Certificate. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_caPools_certificates_get` | `SELECT` | `caPoolsId, certificatesId, locationsId, projectsId` | Returns a Certificate. |
| `projects_locations_caPools_certificates_list` | `SELECT` | `caPoolsId, locationsId, projectsId` | Lists Certificates. |
| `projects_locations_caPools_certificates_create` | `INSERT` | `caPoolsId, locationsId, projectsId` | Create a new Certificate in a given Project, Location from a particular CaPool. |
| `projects_locations_caPools_certificates_patch` | `EXEC` | `caPoolsId, certificatesId, locationsId, projectsId` | Update a Certificate. Currently, the only field you can update is the labels field. |
| `projects_locations_caPools_certificates_revoke` | `EXEC` | `caPoolsId, certificatesId, locationsId, projectsId` | Revoke a Certificate. |
