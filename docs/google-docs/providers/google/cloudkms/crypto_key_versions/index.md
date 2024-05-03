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
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Lists CryptoKeyVersions. |
| <CopyableCode code="asymmetric_decrypt" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Decrypts data that was encrypted with a public key retrieved from GetPublicKey corresponding to a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_DECRYPT. |
| <CopyableCode code="asymmetric_sign" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Signs data using a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_SIGN, producing a signature that can be verified with the public key retrieved from GetPublicKey. |
| <CopyableCode code="destroy" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Schedule a CryptoKeyVersion for destruction. Upon calling this method, CryptoKeyVersion.state will be set to DESTROY_SCHEDULED, and destroy_time will be set to the time destroy_scheduled_duration in the future. At that time, the state will automatically change to DESTROYED, and the key material will be irrevocably destroyed. Before the destroy_time is reached, RestoreCryptoKeyVersion may be called to reverse the process. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Import wrapped key material into a CryptoKeyVersion. All requests must specify a CryptoKey. If a CryptoKeyVersion is additionally specified in the request, key material will be reimported into that version. Otherwise, a new version will be created, and will be assigned the next sequential id within the CryptoKey. |
| <CopyableCode code="mac_sign" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Signs data using a CryptoKeyVersion with CryptoKey.purpose MAC, producing a tag that can be verified by another source with the same key. |
| <CopyableCode code="mac_verify" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Verifies MAC tag using a CryptoKeyVersion with CryptoKey.purpose MAC, and returns a response that indicates whether or not the verification was successful. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Update a CryptoKeyVersion's metadata. state may be changed between ENABLED and DISABLED using this method. See DestroyCryptoKeyVersion and RestoreCryptoKeyVersion to move between other states. |
| <CopyableCode code="raw_decrypt" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Decrypts data that was originally encrypted using a raw cryptographic mechanism. The CryptoKey.purpose must be RAW_ENCRYPT_DECRYPT. |
| <CopyableCode code="raw_encrypt" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Encrypts data using portable cryptographic primitives. Most users should choose Encrypt and Decrypt rather than their raw counterparts. The CryptoKey.purpose must be RAW_ENCRYPT_DECRYPT. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId" /> | Restore a CryptoKeyVersion in the DESTROY_SCHEDULED state. Upon restoration of the CryptoKeyVersion, state will be set to DISABLED, and destroy_time will be cleared. |
