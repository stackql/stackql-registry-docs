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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consents_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.consents_revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the Consent, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/consents/&#123;consent_id&#125;`. Cannot be changed after creation. |
| `ttl` | `string` | Input only. The time to live for this Consent from when it is created. |
| `userId` | `string` | Required. User's UUID provided by the client. |
| `revisionId` | `string` | Output only. The revision ID of the Consent. The format is an 8-character hexadecimal string. Refer to a specific revision of a Consent by appending `@&#123;revision_id&#125;` to the Consent's resource name. |
| `expireTime` | `string` | Timestamp in UTC of when this Consent is considered expired. |
| `metadata` | `object` | Optional. User-supplied key-value pairs used to organize Consent resources. Metadata keys must: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - begin with a letter - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes Metadata values must be: - be between 1 and 63 characters long - have a UTF-8 encoding of maximum 128 bytes - consist of up to 63 characters including lowercase letters, numeric characters, underscores, and dashes No more than 64 metadata entries can be associated with a given consent. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
| `state` | `string` | Required. Indicates the current state of this Consent. |
| `policies` | `array` | Optional. Represents a user's consent in terms of the resources that can be accessed and under what conditions. |
| `consentArtifact` | `string` | Required. The resource name of the Consent artifact that contains proof of the end user's consent, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/consentArtifacts/&#123;consent_artifact_id&#125;`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_revisions` | `SELECT` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` |
| `_list_revisions` | `EXEC` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` |
