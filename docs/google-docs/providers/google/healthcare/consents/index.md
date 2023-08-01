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
| `consents` | `array` | The returned Consents. The maximum number of Consents returned is determined by the value of page_size in the ListConsentsRequest. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Gets the specified revision of a Consent, or the latest revision if `revision_id` is not specified in the resource name. |
| `list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the Consent in the given consent store, returning each Consent's latest revision. |
| `create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new Consent in the parent consent store. |
| `delete` | `DELETE` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Deletes the Consent and its revisions. To keep a record of the Consent but mark it inactive, see [RevokeConsent]. To delete a revision of a Consent, see [DeleteConsentRevision]. This operation does not delete the related Consent artifact. |
| `activate` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Activates the latest revision of the specified Consent by committing a new revision with `state` updated to `ACTIVE`. If the latest revision of the specified Consent is in the `ACTIVE` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state. |
| `patch` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Updates the latest revision of the specified Consent by committing a new revision with the changes. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `REJECTED` or `REVOKED` state. |
| `reject` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Rejects the latest revision of the specified Consent by committing a new revision with `state` updated to `REJECTED`. If the latest revision of the specified Consent is in the `REJECTED` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the specified Consent is in the `ACTIVE` or `REVOKED` state. |
| `revoke` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` | Revokes the latest revision of the specified Consent by committing a new revision with `state` updated to `REVOKED`. If the latest revision of the specified Consent is in the `REVOKED` state, no new revision is committed. A FAILED_PRECONDITION error occurs if the latest revision of the given consent is in `DRAFT` or `REJECTED` state. |
