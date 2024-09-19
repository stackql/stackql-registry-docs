---
title: ca_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_pools
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

Creates, updates, deletes, gets or lists a <code>ca_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.privateca.ca_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this CaPool in the format `projects/*/locations/*/caPools/*`. |
| <CopyableCode code="issuancePolicy" /> | `object` | Defines controls over all certificate issuance within a CaPool. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels with user-defined metadata. |
| <CopyableCode code="publishingOptions" /> | `object` | Options relating to the publication of each CertificateAuthority's CA certificate and CRLs and their inclusion as extensions in issued Certificates. The options set here apply to certificates issued by any CertificateAuthority in the CaPool. |
| <CopyableCode code="tier" /> | `string` | Required. Immutable. The Tier of this CaPool. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Returns a CaPool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CaPools. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a CaPool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Delete a CaPool. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Update a CaPool. |

## `SELECT` examples

Lists CaPools.

```sql
SELECT
name,
issuancePolicy,
labels,
publishingOptions,
tier
FROM google.privateca.ca_pools
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ca_pools</code> resource.

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
INSERT INTO google.privateca.ca_pools (
locationsId,
projectsId,
tier,
issuancePolicy,
publishingOptions,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ tier }}',
'{{ issuancePolicy }}',
'{{ publishingOptions }}',
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
    - name: tier
      value: string
    - name: issuancePolicy
      value:
        - name: allowedKeyTypes
          value:
            - - name: rsa
                value:
                  - name: minModulusSize
                    value: string
                  - name: maxModulusSize
                    value: string
              - name: ellipticCurve
                value:
                  - name: signatureAlgorithm
                    value: string
        - name: maximumLifetime
          value: string
        - name: allowedIssuanceModes
          value:
            - name: allowCsrBasedIssuance
              value: boolean
            - name: allowConfigBasedIssuance
              value: boolean
        - name: baselineValues
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
                - - name: objectId
                    value:
                      - name: objectIdPath
                        value:
                          - integer
                  - name: critical
                    value: boolean
                  - name: value
                    value: string
        - name: identityConstraints
          value:
            - name: celExpression
              value:
                - name: expression
                  value: string
                - name: title
                  value: string
                - name: description
                  value: string
                - name: location
                  value: string
            - name: allowSubjectPassthrough
              value: boolean
            - name: allowSubjectAltNamesPassthrough
              value: boolean
        - name: passthroughExtensions
          value:
            - name: knownExtensions
              value:
                - string
            - name: additionalExtensions
              value:
                - - name: objectIdPath
                    value:
                      - integer
    - name: publishingOptions
      value:
        - name: publishCaCert
          value: boolean
        - name: publishCrl
          value: boolean
        - name: encodingFormat
          value: string
    - name: labels
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>ca_pools</code> resource.

```sql
/*+ update */
UPDATE google.privateca.ca_pools
SET 
tier = '{{ tier }}',
issuancePolicy = '{{ issuancePolicy }}',
publishingOptions = '{{ publishingOptions }}',
labels = '{{ labels }}'
WHERE 
caPoolsId = '{{ caPoolsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>ca_pools</code> resource.

```sql
/*+ delete */
DELETE FROM google.privateca.ca_pools
WHERE caPoolsId = '{{ caPoolsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
