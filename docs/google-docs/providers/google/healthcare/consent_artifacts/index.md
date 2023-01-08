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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consent_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.consent_artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the Consent artifact, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/consentArtifacts/&#123;consent_artifact_id&#125;`. Cannot be changed after creation. |
| `userId` | `string` | Required. User's UUID provided by the client. |
| `userSignature` | `object` | User signature. |
| `witnessSignature` | `object` | User signature. |
| `consentContentScreenshots` | `array` | Optional. Screenshots, PDFs, or other binary information documenting the user's consent. |
| `consentContentVersion` | `string` | Optional. An string indicating the version of the consent information shown to the user. |
| `guardianSignature` | `object` | User signature. |
| `metadata` | `object` | Optional. Metadata associated with the Consent artifact. For example, the consent locale or user agent version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_consentStores_consentArtifacts_get` | `SELECT` | `consentArtifactsId, consentStoresId, datasetsId, locationsId, projectsId` | Gets the specified Consent artifact. |
| `projects_locations_datasets_consentStores_consentArtifacts_list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the Consent artifacts in the specified consent store. |
| `projects_locations_datasets_consentStores_consentArtifacts_create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new Consent artifact in the parent consent store. |
| `projects_locations_datasets_consentStores_consentArtifacts_delete` | `DELETE` | `consentArtifactsId, consentStoresId, datasetsId, locationsId, projectsId` | Deletes the specified Consent artifact. Fails if the artifact is referenced by the latest revision of any Consent. |
