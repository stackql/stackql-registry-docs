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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.privateca.certificate_authorities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this CertificateAuthority in the format `projects/*/locations/*/caPools/*/certificateAuthorities/*`. |
| <CopyableCode code="accessUrls" /> | `object` | URLs where a CertificateAuthority will publish content. |
| <CopyableCode code="caCertificateDescriptions" /> | `array` | Output only. A structured description of this CertificateAuthority's CA certificate and its issuers. Ordered as self-to-root. |
| <CopyableCode code="config" /> | `object` | A CertificateConfig describes an X.509 certificate or CSR that is to be created, as an alternative to using ASN.1. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this CertificateAuthority was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The time at which this CertificateAuthority was soft deleted, if it is in the DELETED state. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time at which this CertificateAuthority will be permanently purged, if it is in the DELETED state. |
| <CopyableCode code="gcsBucket" /> | `string` | Immutable. The name of a Cloud Storage bucket where this CertificateAuthority will publish content, such as the CA certificate and CRLs. This must be a bucket name, without any prefixes (such as `gs://`) or suffixes (such as `.googleapis.com`). For example, to use a bucket named `my-bucket`, you would simply specify `my-bucket`. If not specified, a managed bucket will be created. |
| <CopyableCode code="keySpec" /> | `object` | A Cloud KMS key configuration that a CertificateAuthority will use. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels with user-defined metadata. |
| <CopyableCode code="lifetime" /> | `string` | Required. Immutable. The desired lifetime of the CA certificate. Used to create the "not_before_time" and "not_after_time" fields inside an X.509 certificate. |
| <CopyableCode code="pemCaCertificates" /> | `array` | Output only. This CertificateAuthority's certificate chain, including the current CertificateAuthority's certificate. Ordered such that the root issuer is the final element (consistent with RFC 5246). For a self-signed CA, this will only list the current CertificateAuthority's certificate. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The State for this CertificateAuthority. |
| <CopyableCode code="subordinateConfig" /> | `object` | Describes a subordinate CA's issuers. This is either a resource name to a known issuing CertificateAuthority, or a PEM issuer certificate chain. |
| <CopyableCode code="tier" /> | `string` | Output only. The CaPool.Tier of the CaPool that includes this CertificateAuthority. |
| <CopyableCode code="type" /> | `string` | Required. Immutable. The Type of this CertificateAuthority. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which this CertificateAuthority was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Returns a CertificateAuthority. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Lists CertificateAuthorities. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Create a new CertificateAuthority in a given Project and Location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Delete a CertificateAuthority. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Update a CertificateAuthority. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Lists CertificateAuthorities. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Activate a CertificateAuthority that is in state AWAITING_USER_ACTIVATION and is of type SUBORDINATE. After the parent Certificate Authority signs a certificate signing request from FetchCertificateAuthorityCsr, this method can complete the activation process. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Disable a CertificateAuthority. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Enable a CertificateAuthority. |
| <CopyableCode code="fetch" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Fetch a certificate signing request (CSR) from a CertificateAuthority that is in state AWAITING_USER_ACTIVATION and is of type SUBORDINATE. The CSR must then be signed by the desired parent Certificate Authority, which could be another CertificateAuthority resource, or could be an on-prem certificate authority. See also ActivateCertificateAuthority. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Undelete a CertificateAuthority that has been deleted. |
