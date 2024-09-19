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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>import_jobs</code> resource.

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

## `SELECT` examples

Lists ImportJobs.

```sql
SELECT
name,
attestation,
createTime,
expireEventTime,
expireTime,
generateTime,
importMethod,
protectionLevel,
publicKey,
state
FROM google.cloudkms.import_jobs
WHERE keyRingsId = '{{ keyRingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>import_jobs</code> resource.

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
INSERT INTO google.cloudkms.import_jobs (
keyRingsId,
locationsId,
projectsId,
importMethod,
protectionLevel
)
SELECT 
'{{ keyRingsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ importMethod }}',
'{{ protectionLevel }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: importMethod
      value: string
    - name: protectionLevel
      value: string
    - name: createTime
      value: string
    - name: generateTime
      value: string
    - name: expireTime
      value: string
    - name: expireEventTime
      value: string
    - name: state
      value: string
    - name: publicKey
      value:
        - name: pem
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

```
</TabItem>
</Tabs>
