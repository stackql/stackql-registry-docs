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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Resource name of the Consent, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}`. Cannot be changed after creation. |
| `expireTime` | `string` | Timestamp in UTC of when this Consent is considered expired. |
| `userId` | `string` | Required. User's UUID provided by the client. |
| `policies` | `array` | Optional. Represents a user's consent in terms of the resources that can be accessed and under what conditions. |
| `consentArtifact` | `string` | Required. The resource name of the Consent artifact that contains proof of the end user's consent, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consentArtifacts/{consent_artifact_id}`. |
| `metadata` | `object` | Optional. User-supplied key-value pairs used to organize Consent resources. Metadata keys must: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - begin with a letter - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes Metadata values must be: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes No more than 64 metadata entries can be associated with a given consent. |
| `revisionId` | `string` | Output only. The revision ID of the Consent. The format is an 8-character hexadecimal string. Refer to a specific revision of a Consent by appending `@{revision_id}` to the Consent's resource name. |
| `ttl` | `string` | Input only. The time to live for this Consent from when it is created. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
| `state` | `string` | Required. Indicates the current state of this Consent. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_consentStores_consents_get` | `SELECT` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Gets the specified revision of a Consent, or the latest revision if `revision_id` is not specified in the resource name. |
| `projects_locations_datasets_consentStores_consents_list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the Consent in the given consent store, returning each Consent's latest revision. |
| `projects_locations_datasets_consentStores_consents_create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new Consent in the parent consent store. |
| `projects_locations_datasets_consentStores_consents_delete` | `DELETE` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Deletes the Consent and its revisions. To keep a record of the Consent but mark it inactive, see [RevokeConsent]. To delete a revision of a Consent, see [DeleteConsentRevision]. This operation does not delete the related Consent artifact. |
| `projects_locations_datasets_consentStores_consents_activate` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Activates the latest revision of the specified Consent by committing a new revision with `state` updated to `ACTIVE`. If the latest revision of the specified Consent is in the `ACTIVE` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state. |
| `projects_locations_datasets_consentStores_consents_patch` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Updates the latest revision of the specified Consent by committing a new revision with the changes. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state. |
| `projects_locations_datasets_consentStores_consents_reject` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Rejects the latest revision of the specified Consent by committing a new revision with `state` updated to `REJECTED`. If the latest revision of the specified Consent is in the `REJECTED` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `ACTIVE` or `REVOKED` state. |
| `projects_locations_datasets_consentStores_consents_revoke` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Revokes the latest revision of the specified Consent by committing a new revision with `state` updated to `REVOKED`. If the latest revision of the specified Consent is in the `REVOKED` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the given consent is in `DRAFT` or `REJECTED` state. |
