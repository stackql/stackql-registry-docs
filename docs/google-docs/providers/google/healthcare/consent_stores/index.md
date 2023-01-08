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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | Resource name of the consent store, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;`. Cannot be changed after creation. |
| `defaultConsentTtl` | `string` | Optional. Default time to live for Consents created in this store. Must be at least 24 hours. Updating this field will not affect the expiration time of existing consents. |
| `enableConsentCreateOnUpdate` | `boolean` | Optional. If `true`, UpdateConsent creates the Consent if it does not already exist. If unspecified, defaults to `false`. |
| `labels` | `object` | Optional. User-supplied key-value pairs used to organize consent stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p&#123;Ll&#125;\p&#123;Lo&#125;&#123;0,62&#125;. Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p&#123;Ll&#125;\p&#123;Lo&#125;\p&#123;N&#125;_-]&#123;0,63&#125;. No more than 64 labels can be associated with a given store. For more information: https://cloud.google.com/healthcare/docs/how-tos/labeling-resources |
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
| `projects_locations_datasets_consentStores_queryAccessibleData` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId` | Queries all data_ids that are consented for a specified use in the given consent store and writes them to a specified destination. The returned Operation includes a progress counter for the number of User data mappings processed. If the request is successful, a detailed response is returned of type QueryAccessibleDataResponse, contained in the response field when the operation finishes. The metadata field type is OperationMetadata. Errors are logged to Cloud Logging (see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging)). For example, the following sample log entry shows a `failed to evaluate consent policy` error that occurred during a QueryAccessibleData call to consent store `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;`. ```json jsonPayload: &#123; @type: "type.googleapis.com/google.cloud.healthcare.logging.QueryAccessibleDataLogEntry" error: &#123; code: 9 message: "failed to evaluate consent policy" &#125; resourceName: "projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/consents/&#123;consent_id&#125;" &#125; logName: "projects/&#123;project_id&#125;/logs/healthcare.googleapis.com%2Fquery_accessible_data" operation: &#123; id: "projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/operations/&#123;operation_id&#125;" producer: "healthcare.googleapis.com/QueryAccessibleData" &#125; receiveTimestamp: "TIMESTAMP" resource: &#123; labels: &#123; consent_store_id: "&#123;consent_store_id&#125;" dataset_id: "&#123;dataset_id&#125;" location: "&#123;location_id&#125;" project_id: "&#123;project_id&#125;" &#125; type: "healthcare_consent_store" &#125; severity: "ERROR" timestamp: "TIMESTAMP" ``` |
