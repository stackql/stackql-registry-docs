---
title: consents
hide_title: false
hide_table_of_contents: false
keywords:
  - consents
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

Creates, updates, deletes, gets or lists a <code>consents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.consents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the Consent, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}`. Cannot be changed after creation. |
| <CopyableCode code="consentArtifact" /> | `string` | Required. The resource name of the Consent artifact that contains proof of the end user's consent, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}`. |
| <CopyableCode code="expireTime" /> | `string` | Timestamp in UTC of when this Consent is considered expired. |
| <CopyableCode code="metadata" /> | `object` | Optional. User-supplied key-value pairs used to organize Consent resources. Metadata keys must: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - begin with a letter - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes Metadata values must be: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes No more than 64 metadata entries can be associated with a given consent. |
| <CopyableCode code="policies" /> | `array` | Optional. Represents a user's consent in terms of the resources that can be accessed and under what conditions. |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. The timestamp that the revision was created. |
| <CopyableCode code="revisionId" /> | `string` | Output only. The revision ID of the Consent. The format is an 8-character hexadecimal string. Refer to a specific revision of a Consent by appending `@{revision_id}` to the Consent's resource name. |
| <CopyableCode code="state" /> | `string` | Required. Indicates the current state of this Consent. |
| <CopyableCode code="ttl" /> | `string` | Input only. The time to live for this Consent from when it is created. |
| <CopyableCode code="userId" /> | `string` | Required. User's UUID provided by the client. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consentStoresId, consentsId, datasetsId, locationsId, projectsId" /> | Gets the specified revision of a Consent, or the latest revision if `revision_id` is not specified in the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Lists the Consent in the given consent store, returning each Consent's latest revision. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Creates a new Consent in the parent consent store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consentStoresId, consentsId, datasetsId, locationsId, projectsId" /> | Deletes the Consent and its revisions. To keep a record of the Consent but mark it inactive, see [RevokeConsent]. To delete a revision of a Consent, see [DeleteConsentRevision]. This operation does not delete the related Consent artifact. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="consentStoresId, consentsId, datasetsId, locationsId, projectsId" /> | Updates the latest revision of the specified Consent by committing a new revision with the changes. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="consentStoresId, consentsId, datasetsId, locationsId, projectsId" /> | Activates the latest revision of the specified Consent by committing a new revision with `state` updated to `ACTIVE`. If the latest revision of the specified Consent is in the `ACTIVE` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state. |
| <CopyableCode code="reject" /> | `EXEC` | <CopyableCode code="consentStoresId, consentsId, datasetsId, locationsId, projectsId" /> | Rejects the latest revision of the specified Consent by committing a new revision with `state` updated to `REJECTED`. If the latest revision of the specified Consent is in the `REJECTED` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `ACTIVE` or `REVOKED` state. |
| <CopyableCode code="revoke" /> | `EXEC` | <CopyableCode code="consentStoresId, consentsId, datasetsId, locationsId, projectsId" /> | Revokes the latest revision of the specified Consent by committing a new revision with `state` updated to `REVOKED`. If the latest revision of the specified Consent is in the `REVOKED` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the given consent is in `DRAFT` or `REJECTED` state. |

## `SELECT` examples

Lists the Consent in the given consent store, returning each Consent's latest revision.

```sql
SELECT
name,
consentArtifact,
expireTime,
metadata,
policies,
revisionCreateTime,
revisionId,
state,
ttl,
userId
FROM google.healthcare.consents
WHERE consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>consents</code> resource.

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
INSERT INTO google.healthcare.consents (
consentStoresId,
datasetsId,
locationsId,
projectsId,
name,
revisionId,
revisionCreateTime,
userId,
policies,
consentArtifact,
state,
expireTime,
ttl,
metadata
)
SELECT 
'{{ consentStoresId }}',
'{{ datasetsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ revisionId }}',
'{{ revisionCreateTime }}',
'{{ userId }}',
'{{ policies }}',
'{{ consentArtifact }}',
'{{ state }}',
'{{ expireTime }}',
'{{ ttl }}',
'{{ metadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: revisionId
      value: '{{ revisionId }}'
    - name: revisionCreateTime
      value: '{{ revisionCreateTime }}'
    - name: userId
      value: '{{ userId }}'
    - name: policies
      value: '{{ policies }}'
    - name: consentArtifact
      value: '{{ consentArtifact }}'
    - name: state
      value: '{{ state }}'
    - name: expireTime
      value: '{{ expireTime }}'
    - name: ttl
      value: '{{ ttl }}'
    - name: metadata
      value: '{{ metadata }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>consents</code> resource.

```sql
/*+ update */
UPDATE google.healthcare.consents
SET 
name = '{{ name }}',
revisionId = '{{ revisionId }}',
revisionCreateTime = '{{ revisionCreateTime }}',
userId = '{{ userId }}',
policies = '{{ policies }}',
consentArtifact = '{{ consentArtifact }}',
state = '{{ state }}',
expireTime = '{{ expireTime }}',
ttl = '{{ ttl }}',
metadata = '{{ metadata }}'
WHERE 
consentStoresId = '{{ consentStoresId }}'
AND consentsId = '{{ consentsId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>consents</code> resource.

```sql
/*+ delete */
DELETE FROM google.healthcare.consents
WHERE consentStoresId = '{{ consentStoresId }}'
AND consentsId = '{{ consentsId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
