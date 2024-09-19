---
title: consent_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - consent_artifacts
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>consent_artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consent_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.consent_artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the Consent artifact, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}`. Cannot be changed after creation. |
| <CopyableCode code="consentContentScreenshots" /> | `array` | Optional. Screenshots, PDFs, or other binary information documenting the user's consent. |
| <CopyableCode code="consentContentVersion" /> | `string` | Optional. An string indicating the version of the consent information shown to the user. |
| <CopyableCode code="guardianSignature" /> | `object` | User signature. |
| <CopyableCode code="metadata" /> | `object` | Optional. Metadata associated with the Consent artifact. For example, the consent locale or user agent version. |
| <CopyableCode code="userId" /> | `string` | Required. User's UUID provided by the client. |
| <CopyableCode code="userSignature" /> | `object` | User signature. |
| <CopyableCode code="witnessSignature" /> | `object` | User signature. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consentArtifactsId, consentStoresId, datasetsId, locationsId, projectsId" /> | Gets the specified Consent artifact. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Lists the Consent artifacts in the specified consent store. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Creates a new Consent artifact in the parent consent store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consentArtifactsId, consentStoresId, datasetsId, locationsId, projectsId" /> | Deletes the specified Consent artifact. Fails if the artifact is referenced by the latest revision of any Consent. |

## `SELECT` examples

Lists the Consent artifacts in the specified consent store.

```sql
SELECT
name,
consentContentScreenshots,
consentContentVersion,
guardianSignature,
metadata,
userId,
userSignature,
witnessSignature
FROM google.healthcare.consent_artifacts
WHERE consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>consent_artifacts</code> resource.

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
INSERT INTO google.healthcare.consent_artifacts (
consentStoresId,
datasetsId,
locationsId,
projectsId,
name,
userId,
userSignature,
guardianSignature,
witnessSignature,
consentContentScreenshots,
consentContentVersion,
metadata
)
SELECT 
'{{ consentStoresId }}',
'{{ datasetsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ userId }}',
'{{ userSignature }}',
'{{ guardianSignature }}',
'{{ witnessSignature }}',
'{{ consentContentScreenshots }}',
'{{ consentContentVersion }}',
'{{ metadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: userId
      value: string
    - name: userSignature
      value:
        - name: userId
          value: string
        - name: image
          value:
            - name: rawBytes
              value: string
            - name: gcsUri
              value: string
        - name: metadata
          value: object
        - name: signatureTime
          value: string
    - name: consentContentScreenshots
      value:
        - - name: rawBytes
            value: string
          - name: gcsUri
            value: string
    - name: consentContentVersion
      value: string
    - name: metadata
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>consent_artifacts</code> resource.

```sql
/*+ delete */
DELETE FROM google.healthcare.consent_artifacts
WHERE consentArtifactsId = '{{ consentArtifactsId }}'
AND consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
