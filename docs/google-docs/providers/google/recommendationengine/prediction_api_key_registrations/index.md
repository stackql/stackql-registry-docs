---
title: prediction_api_key_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - prediction_api_key_registrations
  - recommendationengine
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
<tr><td><b>Name</b></td><td><code>prediction_api_key_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommendationengine.prediction_api_key_registrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If empty, the list is complete. If nonempty, pass the token to the next request's `ListPredictionApiKeysRegistrationsRequest.pageToken`. |
| `predictionApiKeyRegistrations` | `array` | The list of registered API keys. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_eventStores_predictionApiKeyRegistrations_list` | `SELECT` | `catalogsId, eventStoresId, locationsId, projectsId` | List the registered apiKeys for use with predict method. |
| `projects_locations_catalogs_eventStores_predictionApiKeyRegistrations_create` | `INSERT` | `catalogsId, eventStoresId, locationsId, projectsId` | Register an API key for use with predict method. |
| `projects_locations_catalogs_eventStores_predictionApiKeyRegistrations_delete` | `DELETE` | `catalogsId, eventStoresId, locationsId, predictionApiKeyRegistrationsId, projectsId` | Unregister an apiKey from using for predict method. |
