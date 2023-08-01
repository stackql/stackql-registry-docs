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
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `consentArtifacts` | `array` | The returned Consent artifacts. The maximum number of artifacts returned is determined by the value of page_size in the ListConsentArtifactsRequest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `consentArtifactsId, consentStoresId, datasetsId, locationsId, projectsId` | Gets the specified Consent artifact. |
| `list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the Consent artifacts in the specified consent store. |
| `create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new Consent artifact in the parent consent store. |
| `delete` | `DELETE` | `consentArtifactsId, consentStoresId, datasetsId, locationsId, projectsId` | Deletes the specified Consent artifact. Fails if the artifact is referenced by the latest revision of any Consent. |
