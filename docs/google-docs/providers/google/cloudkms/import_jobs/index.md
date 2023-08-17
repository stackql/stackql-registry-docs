---
title: import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.import_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this ImportJob in the format `projects/*/locations/*/keyRings/*/importJobs/*`. |
| `importMethod` | `string` | Required. Immutable. The wrapping method to be used for incoming key material. |
| `expireTime` | `string` | Output only. The time at which this ImportJob is scheduled for expiration and can no longer be used to import key material. |
| `generateTime` | `string` | Output only. The time this ImportJob's key material was generated. |
| `publicKey` | `object` | The public key component of the wrapping key. For details of the type of key this public key corresponds to, see the ImportMethod. |
| `attestation` | `object` | Contains an HSM-generated attestation about a key operation. For more information, see [Verifying attestations] (https://cloud.google.com/kms/docs/attest-key). |
| `createTime` | `string` | Output only. The time at which this ImportJob was created. |
| `protectionLevel` | `string` | Required. Immutable. The protection level of the ImportJob. This must match the protection_level of the version_template on the CryptoKey you attempt to import into. |
| `state` | `string` | Output only. The current state of the ImportJob, indicating if it can be used. |
| `expireEventTime` | `string` | Output only. The time this ImportJob expired. Only present if state is EXPIRED. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `importJobsId, keyRingsId, locationsId, projectsId` | Returns metadata for a given ImportJob. |
| `list` | `SELECT` | `keyRingsId, locationsId, projectsId` | Lists ImportJobs. |
| `create` | `INSERT` | `keyRingsId, locationsId, projectsId` | Create a new ImportJob within a KeyRing. ImportJob.import_method is required. |
| `_list` | `EXEC` | `keyRingsId, locationsId, projectsId` | Lists ImportJobs. |
