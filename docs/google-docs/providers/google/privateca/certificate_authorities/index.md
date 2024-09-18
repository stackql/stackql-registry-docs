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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>certificate_authorities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_authorities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.privateca.certificate_authorities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="pemCsr" /> | `string` | Output only. The PEM-encoded signed certificate signing request (CSR). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch" /> | `SELECT` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Fetch a certificate signing request (CSR) from a CertificateAuthority that is in state AWAITING_USER_ACTIVATION and is of type SUBORDINATE. The CSR must then be signed by the desired parent Certificate Authority, which could be another CertificateAuthority resource, or could be an on-prem certificate authority. See also ActivateCertificateAuthority. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Returns a CertificateAuthority. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Lists CertificateAuthorities. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Create a new CertificateAuthority in a given Project and Location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Delete a CertificateAuthority. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Update a CertificateAuthority. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Activate a CertificateAuthority that is in state AWAITING_USER_ACTIVATION and is of type SUBORDINATE. After the parent Certificate Authority signs a certificate signing request from FetchCertificateAuthorityCsr, this method can complete the activation process. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Disable a CertificateAuthority. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Enable a CertificateAuthority. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="caPoolsId, certificateAuthoritiesId, locationsId, projectsId" /> | Undelete a CertificateAuthority that has been deleted. |

## `SELECT` examples

Lists CertificateAuthorities.

```sql
SELECT
pemCsr
FROM google.privateca.certificate_authorities
WHERE caPoolsId = '{{ caPoolsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificate_authorities</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.privateca.certificate_authorities (
caPoolsId,
locationsId,
projectsId,
type,
config,
lifetime,
keySpec,
subordinateConfig,
gcsBucket,
labels
)
SELECT 
'{{ caPoolsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ type }}',
'{{ config }}',
'{{ lifetime }}',
'{{ keySpec }}',
'{{ subordinateConfig }}',
'{{ gcsBucket }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
type: string
config:
  subjectConfig:
    subject:
      commonName: string
      countryCode: string
      organization: string
      organizationalUnit: string
      locality: string
      province: string
      streetAddress: string
      postalCode: string
    subjectAltName:
      dnsNames:
        - type: string
      uris:
        - type: string
      emailAddresses:
        - type: string
      ipAddresses:
        - type: string
      customSans:
        - objectId:
            objectIdPath:
              - type: string
                format: string
          critical: boolean
          value: string
  x509Config:
    keyUsage:
      baseKeyUsage:
        digitalSignature: boolean
        contentCommitment: boolean
        keyEncipherment: boolean
        dataEncipherment: boolean
        keyAgreement: boolean
        certSign: boolean
        crlSign: boolean
        encipherOnly: boolean
        decipherOnly: boolean
      extendedKeyUsage:
        serverAuth: boolean
        clientAuth: boolean
        codeSigning: boolean
        emailProtection: boolean
        timeStamping: boolean
        ocspSigning: boolean
      unknownExtendedKeyUsages:
        - objectIdPath:
            - type: string
              format: string
    caOptions:
      isCa: boolean
      maxIssuerPathLength: integer
    policyIds:
      - objectIdPath:
          - type: string
            format: string
    aiaOcspServers:
      - type: string
    nameConstraints:
      critical: boolean
      permittedDnsNames:
        - type: string
      excludedDnsNames:
        - type: string
      permittedIpRanges:
        - type: string
      excludedIpRanges:
        - type: string
      permittedEmailAddresses:
        - type: string
      excludedEmailAddresses:
        - type: string
      permittedUris:
        - type: string
      excludedUris:
        - type: string
    additionalExtensions:
      - critical: boolean
        value: string
  publicKey:
    key: string
    format: string
  subjectKeyId:
    keyId: string
lifetime: string
keySpec:
  cloudKmsKeyVersion: string
  algorithm: string
subordinateConfig:
  certificateAuthority: string
  pemIssuerChain:
    pemCertificates:
      - type: string
tier: string
state: string
pemCaCertificates:
  - type: string
caCertificateDescriptions:
  - subjectDescription:
      hexSerialNumber: string
      lifetime: string
      notBeforeTime: string
      notAfterTime: string
    subjectKeyId:
      keyId: string
    crlDistributionPoints:
      - type: string
    aiaIssuingCertificateUrls:
      - type: string
    certFingerprint:
      sha256Hash: string
    tbsCertificateDigest: string
gcsBucket: string
accessUrls:
  caCertificateAccessUrl: string
  crlAccessUrls:
    - type: string
createTime: string
updateTime: string
deleteTime: string
expireTime: string
labels: object
satisfiesPzs: boolean
satisfiesPzi: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificate_authorities</code> resource.

```sql
/*+ update */
UPDATE google.privateca.certificate_authorities
SET 
type = '{{ type }}',
config = '{{ config }}',
lifetime = '{{ lifetime }}',
keySpec = '{{ keySpec }}',
subordinateConfig = '{{ subordinateConfig }}',
gcsBucket = '{{ gcsBucket }}',
labels = '{{ labels }}'
WHERE 
caPoolsId = '{{ caPoolsId }}'
AND certificateAuthoritiesId = '{{ certificateAuthoritiesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>certificate_authorities</code> resource.

```sql
/*+ delete */
DELETE FROM google.privateca.certificate_authorities
WHERE caPoolsId = '{{ caPoolsId }}'
AND certificateAuthoritiesId = '{{ certificateAuthoritiesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
