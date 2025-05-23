---
title: crypto_key_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_key_versions
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

Creates, updates, deletes, gets or lists a <code>crypto_key_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_key_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.crypto_key_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this CryptoKeyVersion in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*`. |
| <CopyableCode code="algorithm" /> | `string` | Output only. The CryptoKeyVersionAlgorithm that this CryptoKeyVersion supports. |
| <CopyableCode code="attestation" /> | `object` | Contains an HSM-generated attestation about a key operation. For more information, see [Verifying attestations] (https://cloud.google.com/kms/docs/attest-key). |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this CryptoKeyVersion was created. |
| <CopyableCode code="destroyEventTime" /> | `string` | Output only. The time this CryptoKeyVersion's key material was destroyed. Only present if state is DESTROYED. |
| <CopyableCode code="destroyTime" /> | `string` | Output only. The time this CryptoKeyVersion's key material is scheduled for destruction. Only present if state is DESTROY_SCHEDULED. |
| <CopyableCode code="externalDestructionFailureReason" /> | `string` | Output only. The root cause of the most recent external destruction failure. Only present if state is EXTERNAL_DESTRUCTION_FAILED. |
| <CopyableCode code="externalProtectionLevelOptions" /> | `object` | ExternalProtectionLevelOptions stores a group of additional fields for configuring a CryptoKeyVersion that are specific to the EXTERNAL protection level and EXTERNAL_VPC protection levels. |
| <CopyableCode code="generateTime" /> | `string` | Output only. The time this CryptoKeyVersion's key material was generated. |
| <CopyableCode code="generationFailureReason" /> | `string` | Output only. The root cause of the most recent generation failure. Only present if state is GENERATION_FAILED. |
| <CopyableCode code="importFailureReason" /> | `string` | Output only. The root cause of the most recent import failure. Only present if state is IMPORT_FAILED. |
| <CopyableCode code="importJob" /> | `string` | Output only. The name of the ImportJob used in the most recent import of this CryptoKeyVersion. Only present if the underlying key material was imported. |
| <CopyableCode code="importTime" /> | `string` | Output only. The time at which this CryptoKeyVersion's key material was most recently imported. |
| <CopyableCode code="protectionLevel" /> | `string` | Output only. The ProtectionLevel describing how crypto operations are performed with this CryptoKeyVersion. |
| <CopyableCode code="reimportEligible" /> | `boolean` | Output only. Whether or not this key version is eligible for reimport, by being specified as a target in ImportCryptoKeyVersionRequest.crypto_key_version. |
| <CopyableCode code="state" /> | `string` | The current state of the CryptoKeyVersion. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Returns metadata for a given CryptoKeyVersion. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Lists CryptoKeyVersions. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Create a new CryptoKeyVersion in a CryptoKey. The server will assign the next sequential id. If unset, state will be set to ENABLED. |
| <CopyableCode code="destroy" /> | `DELETE` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Schedule a CryptoKeyVersion for destruction. Upon calling this method, CryptoKeyVersion.state will be set to DESTROY_SCHEDULED, and destroy_time will be set to the time destroy_scheduled_duration in the future. At that time, the state will automatically change to DESTROYED, and the key material will be irrevocably destroyed. Before the destroy_time is reached, RestoreCryptoKeyVersion may be called to reverse the process. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Update a CryptoKeyVersion's metadata. state may be changed between ENABLED and DISABLED using this method. See DestroyCryptoKeyVersion and RestoreCryptoKeyVersion to move between other states. |
| <CopyableCode code="asymmetric_decrypt" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Decrypts data that was encrypted with a public key retrieved from GetPublicKey corresponding to a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_DECRYPT. |
| <CopyableCode code="asymmetric_sign" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Signs data using a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_SIGN, producing a signature that can be verified with the public key retrieved from GetPublicKey. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Import wrapped key material into a CryptoKeyVersion. All requests must specify a CryptoKey. If a CryptoKeyVersion is additionally specified in the request, key material will be reimported into that version. Otherwise, a new version will be created, and will be assigned the next sequential id within the CryptoKey. |
| <CopyableCode code="mac_sign" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Signs data using a CryptoKeyVersion with CryptoKey.purpose MAC, producing a tag that can be verified by another source with the same key. |
| <CopyableCode code="mac_verify" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Verifies MAC tag using a CryptoKeyVersion with CryptoKey.purpose MAC, and returns a response that indicates whether or not the verification was successful. |
| <CopyableCode code="raw_decrypt" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Decrypts data that was originally encrypted using a raw cryptographic mechanism. The CryptoKey.purpose must be RAW_ENCRYPT_DECRYPT. |
| <CopyableCode code="raw_encrypt" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Encrypts data using portable cryptographic primitives. Most users should choose Encrypt and Decrypt rather than their raw counterparts. The CryptoKey.purpose must be RAW_ENCRYPT_DECRYPT. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Restore a CryptoKeyVersion in the DESTROY_SCHEDULED state. Upon restoration of the CryptoKeyVersion, state will be set to DISABLED, and destroy_time will be cleared. |

## `SELECT` examples

Lists CryptoKeyVersions.

```sql
SELECT
name,
algorithm,
attestation,
createTime,
destroyEventTime,
destroyTime,
externalDestructionFailureReason,
externalProtectionLevelOptions,
generateTime,
generationFailureReason,
importFailureReason,
importJob,
importTime,
protectionLevel,
reimportEligible,
state
FROM google.cloudkms.crypto_key_versions
WHERE cryptoKeysId = '{{ cryptoKeysId }}'
AND keyRingsId = '{{ keyRingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>crypto_key_versions</code> resource.

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
INSERT INTO google.cloudkms.crypto_key_versions (
cryptoKeysId,
keyRingsId,
locationsId,
projectsId,
state,
externalProtectionLevelOptions
)
SELECT 
'{{ cryptoKeysId }}',
'{{ keyRingsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ state }}',
'{{ externalProtectionLevelOptions }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: state
      value: string
    - name: protectionLevel
      value: string
    - name: algorithm
      value: string
    - name: attestation
      value:
        - name: format
          value: string
        - name: content
          value: string
        - name: certChains
          value:
            - name: caviumCerts
              value:
                - string
            - name: googleCardCerts
              value:
                - string
            - name: googlePartitionCerts
              value:
                - string
    - name: createTime
      value: string
    - name: generateTime
      value: string
    - name: destroyTime
      value: string
    - name: destroyEventTime
      value: string
    - name: importJob
      value: string
    - name: importTime
      value: string
    - name: importFailureReason
      value: string
    - name: generationFailureReason
      value: string
    - name: externalDestructionFailureReason
      value: string
    - name: externalProtectionLevelOptions
      value:
        - name: externalKeyUri
          value: string
        - name: ekmConnectionKeyPath
          value: string
    - name: reimportEligible
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>crypto_key_versions</code> resource.

```sql
/*+ update */
UPDATE google.cloudkms.crypto_key_versions
SET 
state = '{{ state }}',
externalProtectionLevelOptions = '{{ externalProtectionLevelOptions }}'
WHERE 
cryptoKeyVersionsId = '{{ cryptoKeyVersionsId }}'
AND cryptoKeysId = '{{ cryptoKeysId }}'
AND keyRingsId = '{{ keyRingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>crypto_key_versions</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudkms.crypto_key_versions
WHERE cryptoKeyVersionsId = '{{ cryptoKeyVersionsId }}'
AND cryptoKeysId = '{{ cryptoKeysId }}'
AND keyRingsId = '{{ keyRingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
