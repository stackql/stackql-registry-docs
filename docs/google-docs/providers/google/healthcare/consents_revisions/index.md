---
title: consents_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - consents_revisions
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

Creates, updates, deletes or gets an <code>consents_revision</code> resource or lists <code>consents_revisions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consents_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.consents_revisions" /></td></tr>
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
| <CopyableCode code="list_revisions" /> | `SELECT` | <CopyableCode code="consentStoresId, consentsId, datasetsId, locationsId, projectsId" /> | Lists the revisions of the specified Consent in reverse chronological order. |

## `SELECT` examples

Lists the revisions of the specified Consent in reverse chronological order.

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
FROM google.healthcare.consents_revisions
WHERE consentStoresId = '{{ consentStoresId }}'
AND consentsId = '{{ consentsId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
