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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.import_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this ImportJob in the format `projects/*/locations/*/keyRings/*/importJobs/*`. |
| <CopyableCode code="attestation" /> | `object` | Contains an HSM-generated attestation about a key operation. For more information, see [Verifying attestations] (https://cloud.google.com/kms/docs/attest-key). |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this ImportJob was created. |
| <CopyableCode code="expireEventTime" /> | `string` | Output only. The time this ImportJob expired. Only present if state is EXPIRED. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time at which this ImportJob is scheduled for expiration and can no longer be used to import key material. |
| <CopyableCode code="generateTime" /> | `string` | Output only. The time this ImportJob's key material was generated. |
| <CopyableCode code="importMethod" /> | `string` | Required. Immutable. The wrapping method to be used for incoming key material. |
| <CopyableCode code="protectionLevel" /> | `string` | Required. Immutable. The protection level of the ImportJob. This must match the protection_level of the version_template on the CryptoKey you attempt to import into. |
| <CopyableCode code="publicKey" /> | `object` | The public key component of the wrapping key. For details of the type of key this public key corresponds to, see the ImportMethod. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the ImportJob, indicating if it can be used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="importJobsId, keyRingsId, locationsId, projectsId" /> | Returns metadata for a given ImportJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="keyRingsId, locationsId, projectsId" /> | Lists ImportJobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="keyRingsId, locationsId, projectsId" /> | Create a new ImportJob within a KeyRing. ImportJob.import_method is required. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="keyRingsId, locationsId, projectsId" /> | Lists ImportJobs. |
