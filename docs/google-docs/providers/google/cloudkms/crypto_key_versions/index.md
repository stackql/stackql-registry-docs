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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_key_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.crypto_key_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this CryptoKeyVersion in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*`. |
| `importTime` | `string` | Output only. The time at which this CryptoKeyVersion's key material was most recently imported. |
| `createTime` | `string` | Output only. The time at which this CryptoKeyVersion was created. |
| `destroyEventTime` | `string` | Output only. The time this CryptoKeyVersion's key material was destroyed. Only present if state is DESTROYED. |
| `attestation` | `object` | Contains an HSM-generated attestation about a key operation. For more information, see [Verifying attestations] (https://cloud.google.com/kms/docs/attest-key). |
| `externalProtectionLevelOptions` | `object` | ExternalProtectionLevelOptions stores a group of additional fields for configuring a CryptoKeyVersion that are specific to the EXTERNAL protection level and EXTERNAL_VPC protection levels. |
| `state` | `string` | The current state of the CryptoKeyVersion. |
| `destroyTime` | `string` | Output only. The time this CryptoKeyVersion's key material is scheduled for destruction. Only present if state is DESTROY_SCHEDULED. |
| `protectionLevel` | `string` | Output only. The ProtectionLevel describing how crypto operations are performed with this CryptoKeyVersion. |
| `importJob` | `string` | Output only. The name of the ImportJob used in the most recent import of this CryptoKeyVersion. Only present if the underlying key material was imported. |
| `reimportEligible` | `boolean` | Output only. Whether or not this key version is eligible for reimport, by being specified as a target in ImportCryptoKeyVersionRequest.crypto_key_version. |
| `generateTime` | `string` | Output only. The time this CryptoKeyVersion's key material was generated. |
| `importFailureReason` | `string` | Output only. The root cause of the most recent import failure. Only present if state is IMPORT_FAILED. |
| `algorithm` | `string` | Output only. The CryptoKeyVersionAlgorithm that this CryptoKeyVersion supports. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_get` | `SELECT` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Returns metadata for a given CryptoKeyVersion. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_list` | `SELECT` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Lists CryptoKeyVersions. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_create` | `INSERT` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Create a new CryptoKeyVersion in a CryptoKey. The server will assign the next sequential id. If unset, state will be set to ENABLED. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_destroy` | `DELETE` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Schedule a CryptoKeyVersion for destruction. Upon calling this method, CryptoKeyVersion.state will be set to DESTROY_SCHEDULED, and destroy_time will be set to the time destroy_scheduled_duration in the future. At that time, the state will automatically change to DESTROYED, and the key material will be irrevocably destroyed. Before the destroy_time is reached, RestoreCryptoKeyVersion may be called to reverse the process. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_asymmetricDecrypt` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Decrypts data that was encrypted with a public key retrieved from GetPublicKey corresponding to a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_DECRYPT. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_asymmetricSign` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Signs data using a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_SIGN, producing a signature that can be verified with the public key retrieved from GetPublicKey. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_import` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Import wrapped key material into a CryptoKeyVersion. All requests must specify a CryptoKey. If a CryptoKeyVersion is additionally specified in the request, key material will be reimported into that version. Otherwise, a new version will be created, and will be assigned the next sequential id within the CryptoKey. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_macSign` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Signs data using a CryptoKeyVersion with CryptoKey.purpose MAC, producing a tag that can be verified by another source with the same key. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_macVerify` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Verifies MAC tag using a CryptoKeyVersion with CryptoKey.purpose MAC, and returns a response that indicates whether or not the verification was successful. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_patch` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Update a CryptoKeyVersion's metadata. state may be changed between ENABLED and DISABLED using this method. See DestroyCryptoKeyVersion and RestoreCryptoKeyVersion to move between other states. |
| `projects_locations_keyRings_cryptoKeys_cryptoKeyVersions_restore` | `EXEC` | `cryptoKeyVersionsId, cryptoKeysId, keyRingsId, locationsId, projectsId` | Restore a CryptoKeyVersion in the DESTROY_SCHEDULED state. Upon restoration of the CryptoKeyVersion, state will be set to DISABLED, and destroy_time will be cleared. |
