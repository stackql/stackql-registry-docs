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
    - name: tier
      value: '{{ tier }}'
    - name: issuancePolicy
      value:
        - name: allowedKeyTypes
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: maximumLifetime
          value: '{{ maximumLifetime }}'
        - name: allowedIssuanceModes
          value:
            - name: allowCsrBasedIssuance
              value: '{{ allowCsrBasedIssuance }}'
            - name: allowConfigBasedIssuance
              value: '{{ allowConfigBasedIssuance }}'
        - name: baselineValues
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
        - name: identityConstraints
          value:
            - name: celExpression
              value:
                - name: expression
                  value: '{{ expression }}'
                - name: title
                  value: '{{ title }}'
                - name: description
                  value: '{{ description }}'
                - name: location
                  value: '{{ location }}'
            - name: allowSubjectPassthrough
              value: '{{ allowSubjectPassthrough }}'
            - name: allowSubjectAltNamesPassthrough
              value: '{{ allowSubjectAltNamesPassthrough }}'
        - name: passthroughExtensions
          value:
            - name: knownExtensions
              value:
                - name: type
                  value: '{{ type }}'
                - name: enumDescriptions
                  value: '{{ enumDescriptions }}'
                - name: enum
                  value: '{{ enum }}'
            - name: additionalExtensions
              value:
                - name: $ref
                  value: '{{ $ref }}'
    - name: publishingOptions
      value:
        - name: publishCaCert
          value: '{{ publishCaCert }}'
        - name: publishCrl
          value: '{{ publishCrl }}'
        - name: encodingFormat
          value: '{{ encodingFormat }}'
    - name: labels
      value: '{{ labels }}'

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
