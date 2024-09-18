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
name: string
tier: string
issuancePolicy:
  allowedKeyTypes:
    - rsa:
        minModulusSize: string
        maxModulusSize: string
      ellipticCurve:
        signatureAlgorithm: string
  maximumLifetime: string
  allowedIssuanceModes:
    allowCsrBasedIssuance: boolean
    allowConfigBasedIssuance: boolean
  baselineValues:
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
      - objectId:
          objectIdPath:
            - type: string
              format: string
        critical: boolean
        value: string
  identityConstraints:
    celExpression:
      expression: string
      title: string
      description: string
      location: string
    allowSubjectPassthrough: boolean
    allowSubjectAltNamesPassthrough: boolean
  passthroughExtensions:
    knownExtensions:
      - type: string
        enumDescriptions: string
        enum: string
    additionalExtensions:
      - objectIdPath:
          - type: string
            format: string
publishingOptions:
  publishCaCert: boolean
  publishCrl: boolean
  encodingFormat: string
labels: object

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
