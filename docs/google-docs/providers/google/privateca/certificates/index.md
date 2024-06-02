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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="privateca.certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this Certificate in the format `projects/*/locations/*/caPools/*/certificates/*`. |
| <CopyableCode code="certificateDescription" /> | `object` | A CertificateDescription describes an X.509 certificate or CSR that has been issued, as an alternative to using ASN.1 / X.509. |
| <CopyableCode code="certificateTemplate" /> | `string` | Immutable. The resource name for a CertificateTemplate used to issue this certificate, in the format `projects/*/locations/*/certificateTemplates/*`. If this is specified, the caller must have the necessary permission to use this template. If this is omitted, no template will be used. This template must be in the same location as the Certificate. |
| <CopyableCode code="config" /> | `object` | A CertificateConfig describes an X.509 certificate or CSR that is to be created, as an alternative to using ASN.1. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this Certificate was created. |
| <CopyableCode code="issuerCertificateAuthority" /> | `string` | Output only. The resource name of the issuing CertificateAuthority in the format `projects/*/locations/*/caPools/*/certificateAuthorities/*`. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels with user-defined metadata. |
| <CopyableCode code="lifetime" /> | `string` | Required. Immutable. The desired lifetime of a certificate. Used to create the "not_before_time" and "not_after_time" fields inside an X.509 certificate. Note that the lifetime may be truncated if it would extend past the life of any certificate authority in the issuing chain. |
| <CopyableCode code="pemCertificate" /> | `string` | Output only. The pem-encoded, signed X.509 certificate. |
| <CopyableCode code="pemCertificateChain" /> | `array` | Output only. The chain that may be used to verify the X.509 certificate. Expected to be in issuer-to-root order according to RFC 5246. |
| <CopyableCode code="pemCsr" /> | `string` | Immutable. A pem-encoded X.509 certificate signing request (CSR). |
| <CopyableCode code="revocationDetails" /> | `object` | Describes fields that are relavent to the revocation of a Certificate. |
| <CopyableCode code="subjectMode" /> | `string` | Immutable. Specifies how the Certificate's identity fields are to be decided. If this is omitted, the `DEFAULT` subject mode will be used. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which this Certificate was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="caPoolsId, certificatesId, locationsId, projectsId" /> | Returns a Certificate. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Lists Certificates. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Create a new Certificate in a given Project, Location from a particular CaPool. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Lists Certificates. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="caPoolsId, certificatesId, locationsId, projectsId" /> | Update a Certificate. Currently, the only field you can update is the labels field. |
| <CopyableCode code="revoke" /> | `EXEC` | <CopyableCode code="caPoolsId, certificatesId, locationsId, projectsId" /> | Revoke a Certificate. |
