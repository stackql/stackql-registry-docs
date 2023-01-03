---
title: consent_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - consent_stores
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
<tr><td><b>Name</b></td><td><code>consent_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.consent_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the consent store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}`. Cannot be changed after creation. |
| `defaultConsentTtl` | `string` | Optional. Default time to live for Consents created in this store. Must be at least 24 hours. Updating this field will not affect the expiration time of existing consents. |
| `enableConsentCreateOnUpdate` | `boolean` | Optional. If `true`, UpdateConsent creates the Consent if it does not already exist. If unspecified, defaults to `false`. |
| `labels` | `object` | Optional. User-supplied key-value pairs used to organize consent stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62}. Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}. No more than 64 labels can be associated with a given store. For more information: https://cloud.google.com/healthcare/docs/how-tos/labeling-resources |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_consentStores_get` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Gets the specified consent store. |
| `projects_locations_datasets_consentStores_list` | `SELECT` | `datasetsId, locationsId, projectsId` | Lists the consent stores in the specified dataset. |
| `projects_locations_datasets_consentStores_create` | `INSERT` | `datasetsId, locationsId, projectsId` | Creates a new consent store in the parent dataset. Attempting to create a consent store with the same ID as an existing store fails with an ALREADY_EXISTS error. |
| `projects_locations_datasets_consentStores_delete` | `DELETE` | `consentStoresId, datasetsId, locationsId, projectsId` | Deletes the specified consent store and removes all the consent store's data. |
| `projects_locations_datasets_consentStores_checkDataAccess` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId` | Checks if a particular data_id of a User data mapping in the specified consent store is consented for the specified use. |
| `projects_locations_datasets_consentStores_evaluateUserConsents` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId` | Evaluates the user's Consents for all matching User data mappings. Note: User data mappings are indexed asynchronously, which can cause a slight delay between the time mappings are created or updated and when they are included in EvaluateUserConsents results. |
| `projects_locations_datasets_consentStores_patch` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId` | Updates the specified consent store. |
| `projects_locations_datasets_consentStores_queryAccessibleData` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId` | Queries all data_ids that are consented for a specified use in the given consent store and writes them to a specified destination. The returned Operation includes a progress counter for the number of User data mappings processed. If the request is successful, a detailed response is returned of type QueryAccessibleDataResponse, contained in the response field when the operation finishes. The metadata field type is OperationMetadata. Errors are logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). For example, the following sample log entry shows a `failed to evaluate consent policy` error that occurred during a QueryAccessibleData call to consent store `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}`. ```json jsonPayload: { @type: "type.googleapis.com/google.cloud.healthcare.logging.QueryAccessibleDataLogEntry" error: { code: 9 message: "failed to evaluate consent policy" } resourceName: "projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/consents/{consent_id}" } logName: "projects/{project_id}/logs/healthcare.googleapis.com%2Fquery_accessible_data" operation: { id: "projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/operations/{operation_id}" producer: "healthcare.googleapis.com/QueryAccessibleData" } receiveTimestamp: "TIMESTAMP" resource: { labels: { consent_store_id: "{consent_store_id}" dataset_id: "{dataset_id}" location: "{location_id}" project_id: "{project_id}" } type: "healthcare_consent_store" } severity: "ERROR" timestamp: "TIMESTAMP" ``` |
