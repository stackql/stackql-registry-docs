---
title: crypto_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_keys
  - cloudkms
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

Creates, updates, deletes or gets an <code>crypto_key</code> resource or lists <code>crypto_keys</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.crypto_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this CryptoKey in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this CryptoKey was created. |
| <CopyableCode code="cryptoKeyBackend" /> | `string` | Immutable. The resource name of the backend environment where the key material for all CryptoKeyVersions associated with this CryptoKey reside and where all related cryptographic operations are performed. Only applicable if CryptoKeyVersions have a ProtectionLevel of EXTERNAL_VPC, with the resource name in the format `projects/*/locations/*/ekmConnections/*`. Note, this list is non-exhaustive and may apply to additional ProtectionLevels in the future. |
| <CopyableCode code="destroyScheduledDuration" /> | `string` | Immutable. The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 30 days. |
| <CopyableCode code="importOnly" /> | `boolean` | Immutable. Whether this key may contain imported versions only. |
| <CopyableCode code="keyAccessJustificationsPolicy" /> | `object` | A KeyAccessJustificationsPolicy specifies zero or more allowed AccessReason values for encrypt, decrypt, and sign operations on a CryptoKey. |
| <CopyableCode code="labels" /> | `object` | Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys). |
| <CopyableCode code="nextRotationTime" /> | `string` | At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted. |
| <CopyableCode code="primary" /> | `object` | A CryptoKeyVersion represents an individual cryptographic key, and the associated key material. An ENABLED version can be used for cryptographic operations. For security reasons, the raw cryptographic key material represented by a CryptoKeyVersion can never be viewed or exported. It can only be used to encrypt, decrypt, or sign data when an authorized user or application invokes Cloud KMS. |
| <CopyableCode code="purpose" /> | `string` | Immutable. The immutable purpose of this CryptoKey. |
| <CopyableCode code="rotationPeriod" /> | `string` | next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted. |
| <CopyableCode code="versionTemplate" /> | `object` | A CryptoKeyVersionTemplate specifies the properties to use when creating a new CryptoKeyVersion, either manually with CreateCryptoKeyVersion or automatically as a result of auto-rotation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Returns metadata for a given CryptoKey, as well as its primary CryptoKeyVersion. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="keyRingsId, locationsId, projectsId" /> | Lists CryptoKeys. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="keyRingsId, locationsId, projectsId" /> | Create a new CryptoKey within a KeyRing. CryptoKey.purpose and CryptoKey.version_template.algorithm are required. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Update a CryptoKey. |
| <CopyableCode code="decrypt" /> | `EXEC` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Decrypts data that was protected by Encrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT. |
| <CopyableCode code="encrypt" /> | `EXEC` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Encrypts data, so that it can only be recovered by a call to Decrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT. |

## `SELECT` examples

Lists CryptoKeys.

```sql
SELECT
name,
createTime,
cryptoKeyBackend,
destroyScheduledDuration,
importOnly,
keyAccessJustificationsPolicy,
labels,
nextRotationTime,
primary,
purpose,
rotationPeriod,
versionTemplate
FROM google.cloudkms.crypto_keys
WHERE keyRingsId = '{{ keyRingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>crypto_keys</code> resource.

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
INSERT INTO google.cloudkms.crypto_keys (
keyRingsId,
locationsId,
projectsId,
name,
primary,
purpose,
createTime,
nextRotationTime,
rotationPeriod,
versionTemplate,
labels,
importOnly,
destroyScheduledDuration,
cryptoKeyBackend,
keyAccessJustificationsPolicy
)
SELECT 
'{{ keyRingsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ primary }}',
'{{ purpose }}',
'{{ createTime }}',
'{{ nextRotationTime }}',
'{{ rotationPeriod }}',
'{{ versionTemplate }}',
'{{ labels }}',
true|false,
'{{ destroyScheduledDuration }}',
'{{ cryptoKeyBackend }}',
'{{ keyAccessJustificationsPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: primary
        value: '{{ primary }}'
      - name: purpose
        value: '{{ purpose }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: nextRotationTime
        value: '{{ nextRotationTime }}'
      - name: rotationPeriod
        value: '{{ rotationPeriod }}'
      - name: versionTemplate
        value: '{{ versionTemplate }}'
      - name: labels
        value: '{{ labels }}'
      - name: importOnly
        value: '{{ importOnly }}'
      - name: destroyScheduledDuration
        value: '{{ destroyScheduledDuration }}'
      - name: cryptoKeyBackend
        value: '{{ cryptoKeyBackend }}'
      - name: keyAccessJustificationsPolicy
        value: '{{ keyAccessJustificationsPolicy }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a crypto_key only if the necessary resources are available.

```sql
UPDATE google.cloudkms.crypto_keys
SET 
name = '{{ name }}',
primary = '{{ primary }}',
purpose = '{{ purpose }}',
createTime = '{{ createTime }}',
nextRotationTime = '{{ nextRotationTime }}',
rotationPeriod = '{{ rotationPeriod }}',
versionTemplate = '{{ versionTemplate }}',
labels = '{{ labels }}',
importOnly = true|false,
destroyScheduledDuration = '{{ destroyScheduledDuration }}',
cryptoKeyBackend = '{{ cryptoKeyBackend }}',
keyAccessJustificationsPolicy = '{{ keyAccessJustificationsPolicy }}'
WHERE 
cryptoKeysId = '{{ cryptoKeysId }}'
AND keyRingsId = '{{ keyRingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
