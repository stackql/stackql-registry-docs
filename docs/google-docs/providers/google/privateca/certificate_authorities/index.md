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
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: type
      value: string
    - name: config
      value:
        - name: subjectConfig
          value:
            - name: subject
              value:
                - name: commonName
                  value: string
                - name: countryCode
                  value: string
                - name: organization
                  value: string
                - name: organizationalUnit
                  value: string
                - name: locality
                  value: string
                - name: province
                  value: string
                - name: streetAddress
                  value: string
                - name: postalCode
                  value: string
            - name: subjectAltName
              value:
                - name: dnsNames
                  value:
                    - string
                - name: uris
                  value:
                    - string
                - name: emailAddresses
                  value:
                    - string
                - name: ipAddresses
                  value:
                    - string
                - name: customSans
                  value:
                    - - name: objectId
                        value:
                          - name: objectIdPath
                            value:
                              - integer
                      - name: critical
                        value: boolean
                      - name: value
                        value: string
        - name: x509Config
          value:
            - name: keyUsage
              value:
                - name: baseKeyUsage
                  value:
                    - name: digitalSignature
                      value: boolean
                    - name: contentCommitment
                      value: boolean
                    - name: keyEncipherment
                      value: boolean
                    - name: dataEncipherment
                      value: boolean
                    - name: keyAgreement
                      value: boolean
                    - name: certSign
                      value: boolean
                    - name: crlSign
                      value: boolean
                    - name: encipherOnly
                      value: boolean
                    - name: decipherOnly
                      value: boolean
                - name: extendedKeyUsage
                  value:
                    - name: serverAuth
                      value: boolean
                    - name: clientAuth
                      value: boolean
                    - name: codeSigning
                      value: boolean
                    - name: emailProtection
                      value: boolean
                    - name: timeStamping
                      value: boolean
                    - name: ocspSigning
                      value: boolean
                - name: unknownExtendedKeyUsages
                  value:
                    - - name: objectIdPath
                        value:
                          - integer
            - name: caOptions
              value:
                - name: isCa
                  value: boolean
                - name: maxIssuerPathLength
                  value: integer
            - name: policyIds
              value:
                - - name: objectIdPath
                    value:
                      - integer
            - name: aiaOcspServers
              value:
                - string
            - name: nameConstraints
              value:
                - name: critical
                  value: boolean
                - name: permittedDnsNames
                  value:
                    - string
                - name: excludedDnsNames
                  value:
                    - string
                - name: permittedIpRanges
                  value:
                    - string
                - name: excludedIpRanges
                  value:
                    - string
                - name: permittedEmailAddresses
                  value:
                    - string
                - name: excludedEmailAddresses
                  value:
                    - string
                - name: permittedUris
                  value:
                    - string
                - name: excludedUris
                  value:
                    - string
            - name: additionalExtensions
              value:
                - - name: critical
                    value: boolean
                  - name: value
                    value: string
        - name: publicKey
          value:
            - name: key
              value: string
            - name: format
              value: string
        - name: subjectKeyId
          value:
            - name: keyId
              value: string
    - name: lifetime
      value: string
    - name: keySpec
      value:
        - name: cloudKmsKeyVersion
          value: string
        - name: algorithm
          value: string
    - name: subordinateConfig
      value:
        - name: certificateAuthority
          value: string
        - name: pemIssuerChain
          value:
            - name: pemCertificates
              value:
                - string
    - name: tier
      value: string
    - name: state
      value: string
    - name: pemCaCertificates
      value:
        - string
    - name: caCertificateDescriptions
      value:
        - - name: subjectDescription
            value:
              - name: hexSerialNumber
                value: string
              - name: lifetime
                value: string
              - name: notBeforeTime
                value: string
              - name: notAfterTime
                value: string
          - name: subjectKeyId
            value:
              - name: keyId
                value: string
          - name: crlDistributionPoints
            value:
              - string
          - name: aiaIssuingCertificateUrls
            value:
              - string
          - name: certFingerprint
            value:
              - name: sha256Hash
                value: string
          - name: tbsCertificateDigest
            value: string
    - name: gcsBucket
      value: string
    - name: accessUrls
      value:
        - name: caCertificateAccessUrl
          value: string
        - name: crlAccessUrls
          value:
            - string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: deleteTime
      value: string
    - name: expireTime
      value: string
    - name: labels
      value: object
    - name: satisfiesPzs
      value: boolean
    - name: satisfiesPzi
      value: boolean

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
