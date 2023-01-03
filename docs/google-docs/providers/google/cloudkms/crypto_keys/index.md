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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>crypto_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.crypto_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this CryptoKey in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*`. |
| `cryptoKeyBackend` | `string` | Immutable. The resource name of the backend environment where the key material for all CryptoKeyVersions associated with this CryptoKey reside and where all related cryptographic operations are performed. Only applicable if CryptoKeyVersions have a ProtectionLevel of EXTERNAL_VPC, with the resource name in the format `projects/*/locations/*/ekmConnections/*`. Note, this list is non-exhaustive and may apply to additional ProtectionLevels in the future. |
| `importOnly` | `boolean` | Immutable. Whether this key may contain imported versions only. |
| `versionTemplate` | `object` | A CryptoKeyVersionTemplate specifies the properties to use when creating a new CryptoKeyVersion, either manually with CreateCryptoKeyVersion or automatically as a result of auto-rotation. |
| `createTime` | `string` | Output only. The time at which this CryptoKey was created. |
| `rotationPeriod` | `string` | next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted. |
| `nextRotationTime` | `string` | At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted. |
| `destroyScheduledDuration` | `string` | Immutable. The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 24 hours. |
| `purpose` | `string` | Immutable. The immutable purpose of this CryptoKey. |
| `labels` | `object` | Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys). |
| `primary` | `object` | A CryptoKeyVersion represents an individual cryptographic key, and the associated key material. An ENABLED version can be used for cryptographic operations. For security reasons, the raw cryptographic key material represented by a CryptoKeyVersion can never be viewed or exported. It can only be used to encrypt, decrypt, or sign data when an authorized user or application invokes Cloud KMS. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_keyRings_cryptoKeys_get` | `SELECT` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Returns metadata for a given CryptoKey, as well as its primary CryptoKeyVersion. |
| `projects_locations_keyRings_cryptoKeys_list` | `SELECT` | `keyRingsId, locationsId, projectsId` | Lists CryptoKeys. |
| `projects_locations_keyRings_cryptoKeys_create` | `INSERT` | `keyRingsId, locationsId, projectsId` | Create a new CryptoKey within a KeyRing. CryptoKey.purpose and CryptoKey.version_template.algorithm are required. |
| `projects_locations_keyRings_cryptoKeys_decrypt` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Decrypts data that was protected by Encrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT. |
| `projects_locations_keyRings_cryptoKeys_encrypt` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Encrypts data, so that it can only be recovered by a call to Decrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT. |
| `projects_locations_keyRings_cryptoKeys_patch` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Update a CryptoKey. |
| `projects_locations_keyRings_cryptoKeys_updatePrimaryVersion` | `EXEC` | `cryptoKeysId, keyRingsId, locationsId, projectsId` | Update the version of a CryptoKey that will be used in Encrypt. Returns an error if called on a key whose purpose is not ENCRYPT_DECRYPT. |
