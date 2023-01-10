---
title: datasources
hide_title: false
hide_table_of_contents: false
keywords:
  - datasources
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
<tr><td><b>Name</b></td><td><code>datasources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsearch.datasources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the datasource resource. Format: datasources/&#123;source_id&#125;. The name is ignored when creating a datasource. |
| `shortName` | `string` | A short name or alias for the source. This value will be used to match the 'source' operator. For example, if the short name is *&lt;value&gt;* then queries like *source:&lt;value&gt;* will only return results for this source. The value must be unique across all datasources. The value must only contain alphanumeric characters (a-zA-Z0-9). The value cannot start with 'google' and cannot be one of the following: mail, gmail, docs, drive, groups, sites, calendar, hangouts, gplus, keep, people, teams. Its maximum length is 32 characters. |
| `disableModifications` | `boolean` | If true, sets the datasource to read-only mode. In read-only mode, the Indexing API rejects any requests to index or delete items in this source. Enabling read-only mode does not stop the processing of previously accepted data. |
| `itemsVisibility` | `array` | This field restricts visibility to items at the datasource level. Items within the datasource are restricted to the union of users and groups included in this field. Note that, this does not ensure access to a specific item, as users need to have ACL permissions on the contained items. This ensures a high level access on the entire datasource, and that the individual items are not shared outside this visibility. |
| `disableServing` | `boolean` | Disable serving any search or assist results. |
| `operationIds` | `array` | IDs of the Long Running Operations (LROs) currently running for this schema. |
| `displayName` | `string` | Required. Display name of the datasource The maximum length is 300 characters. |
| `indexingServiceAccounts` | `array` | List of service accounts that have indexing access. |
| `returnThumbnailUrls` | `boolean` | Can a user request to get thumbnail URI for Items indexed in this data source. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `settings_datasources_get` | `SELECT` | `datasourcesId` | Gets a datasource. **Note:** This API requires an admin account to execute. |
| `settings_datasources_list` | `SELECT` |  | Lists datasources. **Note:** This API requires an admin account to execute. |
| `settings_datasources_create` | `INSERT` |  | Creates a datasource. **Note:** This API requires an admin account to execute. |
| `settings_datasources_delete` | `DELETE` | `datasourcesId` | Deletes a datasource. **Note:** This API requires an admin account to execute. |
| `indexing_datasources_updateSchema` | `EXEC` | `datasourcesId` | Updates the schema of a data source. This method does not perform incremental updates to the schema. Instead, this method updates the schema by overwriting the entire schema. **Note:** This API requires an admin or service account to execute. |
| `settings_datasources_patch` | `EXEC` | `datasourcesId` | Updates a datasource. **Note:** This API requires an admin account to execute. |
| `settings_datasources_update` | `EXEC` | `datasourcesId` | Updates a datasource. **Note:** This API requires an admin account to execute. |
| `stats_index_datasources_get` | `EXEC` | `datasourcesId` | Gets indexed item statistics for a single data source. **Note:** This API requires a standard end user account to execute. |
