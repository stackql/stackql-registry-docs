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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.consents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the Consent, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/consents/&#123;consent_id&#125;`. Cannot be changed after creation. |
| `userId` | `string` | Required. User's UUID provided by the client. |
| `state` | `string` | Required. Indicates the current state of this Consent. |
| `policies` | `array` | Optional. Represents a user's consent in terms of the resources that can be accessed and under what conditions. |
| `revisionId` | `string` | Output only. The revision ID of the Consent. The format is an 8-character hexadecimal string. Refer to a specific revision of a Consent by appending `@&#123;revision_id&#125;` to the Consent's resource name. |
| `consentArtifact` | `string` | Required. The resource name of the Consent artifact that contains proof of the end user's consent, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/consentArtifacts/&#123;consent_artifact_id&#125;`. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
| `ttl` | `string` | Input only. The time to live for this Consent from when it is created. |
| `metadata` | `object` | Optional. User-supplied key-value pairs used to organize Consent resources. Metadata keys must: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - begin with a letter - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes Metadata values must be: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes No more than 64 metadata entries can be associated with a given consent. |
| `expireTime` | `string` | Timestamp in UTC of when this Consent is considered expired. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Gets the specified revision of a Consent, or the latest revision if `revision_id` is not specified in the resource name. |
| `list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the Consent in the given consent store, returning each Consent's latest revision. |
| `create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new Consent in the parent consent store. |
| `delete` | `DELETE` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Deletes the Consent and its revisions. To keep a record of the Consent but mark it inactive, see [RevokeConsent]. To delete a revision of a Consent, see [DeleteConsentRevision]. This operation does not delete the related Consent artifact. |
| `_list` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the Consent in the given consent store, returning each Consent's latest revision. |
| `activate` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Activates the latest revision of the specified Consent by committing a new revision with `state` updated to `ACTIVE`. If the latest revision of the specified Consent is in the `ACTIVE` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state. |
| `patch` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Updates the latest revision of the specified Consent by committing a new revision with the changes. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state. |
| `reject` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Rejects the latest revision of the specified Consent by committing a new revision with `state` updated to `REJECTED`. If the latest revision of the specified Consent is in the `REJECTED` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `ACTIVE` or `REVOKED` state. |
| `revoke` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Revokes the latest revision of the specified Consent by committing a new revision with `state` updated to `REVOKED`. If the latest revision of the specified Consent is in the `REVOKED` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the given consent is in `DRAFT` or `REJECTED` state. |
