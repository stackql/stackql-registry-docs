---
title: searchapplications
hide_title: false
hide_table_of_contents: false
keywords:
  - searchapplications
  - cloudsearch
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
<tr><td><b>Name</b></td><td><code>searchapplications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsearch.searchapplications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the Search Application. Format: searchapplications/&#123;application_id&#125;. |
| `defaultSortOptions` | `object` |  |
| `operationIds` | `array` | Output only. IDs of the Long Running Operations (LROs) currently running for this schema. Output only field. |
| `enableAuditLog` | `boolean` | Indicates whether audit logging is on/off for requests made for the search application in query APIs. |
| `queryInterpretationConfig` | `object` | Default options to interpret user query. |
| `sourceConfig` | `array` | Configuration for a sources specified in data_source_restrictions. |
| `displayName` | `string` | Display name of the Search Application. The maximum length is 300 characters. |
| `dataSourceRestrictions` | `array` | Retrictions applied to the configurations. The maximum number of elements is 10. |
| `returnResultThumbnailUrls` | `boolean` | With each result we should return the URI for its thumbnail (when applicable) |
| `defaultFacetOptions` | `array` | The default fields for returning facet results. The sources specified here also have been included in data_source_restrictions above. |
| `scoringConfig` | `object` | Scoring configurations for a source while processing a Search or Suggest request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `settings_searchapplications_get` | `SELECT` | `searchapplicationsId` | Gets the specified search application. **Note:** This API requires an admin account to execute. |
| `settings_searchapplications_list` | `SELECT` |  | Lists all search applications. **Note:** This API requires an admin account to execute. |
| `settings_searchapplications_create` | `INSERT` |  | Creates a search application. **Note:** This API requires an admin account to execute. |
| `settings_searchapplications_delete` | `DELETE` | `searchapplicationsId` | Deletes a search application. **Note:** This API requires an admin account to execute. |
| `settings_searchapplications_patch` | `EXEC` | `searchapplicationsId` | Updates a search application. **Note:** This API requires an admin account to execute. |
| `settings_searchapplications_reset` | `EXEC` | `searchapplicationsId` | Resets a search application to default settings. This will return an empty response. **Note:** This API requires an admin account to execute. |
| `settings_searchapplications_update` | `EXEC` | `searchapplicationsId` | Updates a search application. **Note:** This API requires an admin account to execute. |
| `stats_query_searchapplications_get` | `EXEC` | `searchapplicationsId` | Get the query statistics for search application. **Note:** This API requires a standard end user account to execute. |
| `stats_session_searchapplications_get` | `EXEC` | `searchapplicationsId` | Get the # of search sessions, % of successful sessions with a click query statistics for search application. **Note:** This API requires a standard end user account to execute. |
| `stats_user_searchapplications_get` | `EXEC` | `searchapplicationsId` | Get the users statistics for search application. **Note:** This API requires a standard end user account to execute. |
