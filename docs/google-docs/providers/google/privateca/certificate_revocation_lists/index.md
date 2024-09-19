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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>certificate_revocation_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_revocation_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.privateca.certificate_revocation_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this CertificateRevocationList in the format `projects/*/locations/*/caPools/*certificateAuthorities/*/ certificateRevocationLists/*`. |
| <CopyableCode code="accessUrl" /> | `string` | Output only. The location where 'pem_crl' can be accessed. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this CertificateRevocationList was created. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels with user-defined metadata. |
| <CopyableCode code="pemCrl" /> | `string` | Output only. The PEM-encoded X.509 CRL. |
| <CopyableCode code="revisionId" /> | `string` | Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string. |
| <CopyableCode code="revokedCertificates" /> | `array` | Output only. The revoked serial numbers that appear in pem_crl. |
| <CopyableCode code="sequenceNumber" /> | `string` | Output only. The CRL sequence number that appears in pem_crl. |
| <CopyableCode code="state" /> | `string` | Output only. The State for this CertificateRevocationList. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which this CertificateRevocationList was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, certificateRevocationListsId, locationsId, projectsId" /> | Returns a CertificateRevocationList. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Lists CertificateRevocationLists. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, certificateRevocationListsId, locationsId, projectsId" /> | Update a CertificateRevocationList. |

## `SELECT` examples

Lists CertificateRevocationLists.

```sql
SELECT
name,
accessUrl,
createTime,
labels,
pemCrl,
revisionId,
revokedCertificates,
sequenceNumber,
state,
updateTime
FROM google.privateca.certificate_revocation_lists
WHERE caPoolsId = '{{ caPoolsId }}'
AND certificateAuthoritiesId = '{{ certificateAuthoritiesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `UPDATE` example

Updates a <code>certificate_revocation_lists</code> resource.

```sql
/*+ update */
UPDATE google.privateca.certificate_revocation_lists
SET 
labels = '{{ labels }}'
WHERE 
caPoolsId = '{{ caPoolsId }}'
AND certificateAuthoritiesId = '{{ certificateAuthoritiesId }}'
AND certificateRevocationListsId = '{{ certificateRevocationListsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
