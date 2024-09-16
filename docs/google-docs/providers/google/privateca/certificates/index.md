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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.privateca.certificates" /></td></tr>
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
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="caPoolsId, certificatesId, locationsId, projectsId" /> | Update a Certificate. Currently, the only field you can update is the labels field. |
| <CopyableCode code="revoke" /> | `EXEC` | <CopyableCode code="caPoolsId, certificatesId, locationsId, projectsId" /> | Revoke a Certificate. |

## `SELECT` examples

Lists Certificates.

```sql
SELECT
name,
certificateDescription,
certificateTemplate,
config,
createTime,
issuerCertificateAuthority,
labels,
lifetime,
pemCertificate,
pemCertificateChain,
pemCsr,
revocationDetails,
subjectMode,
updateTime
FROM google.privateca.certificates
WHERE caPoolsId = '{{ caPoolsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificates</code> resource.

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
INSERT INTO google.privateca.certificates (
caPoolsId,
locationsId,
projectsId,
pemCsr,
config,
lifetime,
certificateTemplate,
subjectMode,
labels
)
SELECT 
'{{ caPoolsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ pemCsr }}',
'{{ config }}',
'{{ lifetime }}',
'{{ certificateTemplate }}',
'{{ subjectMode }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: pemCsr
      value: '{{ pemCsr }}'
    - name: config
      value:
        - name: subjectConfig
          value:
            - name: subject
              value:
                - name: commonName
                  value: '{{ commonName }}'
                - name: countryCode
                  value: '{{ countryCode }}'
                - name: organization
                  value: '{{ organization }}'
                - name: organizationalUnit
                  value: '{{ organizationalUnit }}'
                - name: locality
                  value: '{{ locality }}'
                - name: province
                  value: '{{ province }}'
                - name: streetAddress
                  value: '{{ streetAddress }}'
                - name: postalCode
                  value: '{{ postalCode }}'
            - name: subjectAltName
              value:
                - name: dnsNames
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: uris
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: emailAddresses
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: ipAddresses
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: customSans
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
        - name: x509Config
          value:
            - name: keyUsage
              value:
                - name: baseKeyUsage
                  value:
                    - name: digitalSignature
                      value: '{{ digitalSignature }}'
                    - name: contentCommitment
                      value: '{{ contentCommitment }}'
                    - name: keyEncipherment
                      value: '{{ keyEncipherment }}'
                    - name: dataEncipherment
                      value: '{{ dataEncipherment }}'
                    - name: keyAgreement
                      value: '{{ keyAgreement }}'
                    - name: certSign
                      value: '{{ certSign }}'
                    - name: crlSign
                      value: '{{ crlSign }}'
                    - name: encipherOnly
                      value: '{{ encipherOnly }}'
                    - name: decipherOnly
                      value: '{{ decipherOnly }}'
                - name: extendedKeyUsage
                  value:
                    - name: serverAuth
                      value: '{{ serverAuth }}'
                    - name: clientAuth
                      value: '{{ clientAuth }}'
                    - name: codeSigning
                      value: '{{ codeSigning }}'
                    - name: emailProtection
                      value: '{{ emailProtection }}'
                    - name: timeStamping
                      value: '{{ timeStamping }}'
                    - name: ocspSigning
                      value: '{{ ocspSigning }}'
                - name: unknownExtendedKeyUsages
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
            - name: caOptions
              value:
                - name: isCa
                  value: '{{ isCa }}'
                - name: maxIssuerPathLength
                  value: '{{ maxIssuerPathLength }}'
            - name: policyIds
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: aiaOcspServers
              value:
                - name: type
                  value: '{{ type }}'
            - name: nameConstraints
              value:
                - name: critical
                  value: '{{ critical }}'
                - name: permittedDnsNames
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: excludedDnsNames
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: permittedIpRanges
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: excludedIpRanges
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: permittedEmailAddresses
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: excludedEmailAddresses
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: permittedUris
                  value:
                    - name: type
                      value: '{{ type }}'
                - name: excludedUris
                  value:
                    - name: type
                      value: '{{ type }}'
            - name: additionalExtensions
              value:
                - name: $ref
                  value: '{{ $ref }}'
        - name: publicKey
          value:
            - name: key
              value: '{{ key }}'
            - name: format
              value: '{{ format }}'
        - name: subjectKeyId
          value:
            - name: keyId
              value: '{{ keyId }}'
    - name: lifetime
      value: '{{ lifetime }}'
    - name: certificateTemplate
      value: '{{ certificateTemplate }}'
    - name: subjectMode
      value: '{{ subjectMode }}'
    - name: labels
      value: '{{ labels }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>certificates</code> resource.

```sql
/*+ update */
UPDATE google.privateca.certificates
SET 
pemCsr = '{{ pemCsr }}',
config = '{{ config }}',
lifetime = '{{ lifetime }}',
certificateTemplate = '{{ certificateTemplate }}',
subjectMode = '{{ subjectMode }}',
labels = '{{ labels }}'
WHERE 
caPoolsId = '{{ caPoolsId }}'
AND certificatesId = '{{ certificatesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
