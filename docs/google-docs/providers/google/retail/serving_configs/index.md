---
title: serving_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_configs
  - retail
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
<tr><td><b>Name</b></td><td><code>serving_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.serving_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Pagination token, if not returned indicates the last page. |
| `servingConfigs` | `array` | All the ServingConfigs for a given catalog. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_serving_configs_get` | `SELECT` | `catalogsId, locationsId, projectsId, servingConfigsId` | Gets a ServingConfig. Returns a NotFound error if the ServingConfig does not exist. |
| `projects_locations_catalogs_serving_configs_list` | `SELECT` | `catalogsId, locationsId, projectsId` | Lists all ServingConfigs linked to this catalog. |
| `projects_locations_catalogs_serving_configs_create` | `INSERT` | `catalogsId, locationsId, projectsId` | Creates a ServingConfig. A maximum of 100 ServingConfigs are allowed in a Catalog, otherwise a FAILED_PRECONDITION error is returned. |
| `projects_locations_catalogs_serving_configs_delete` | `DELETE` | `catalogsId, locationsId, projectsId, servingConfigsId` | Deletes a ServingConfig. Returns a NotFound error if the ServingConfig does not exist. |
| `projects_locations_catalogs_serving_configs_patch` | `EXEC` | `catalogsId, locationsId, projectsId, servingConfigsId` | Updates a ServingConfig. |
| `projects_locations_catalogs_serving_configs_predict` | `EXEC` | `catalogsId, locationsId, projectsId, servingConfigsId` | Makes a recommendation prediction. |
| `projects_locations_catalogs_serving_configs_search` | `EXEC` | `catalogsId, locationsId, projectsId, servingConfigsId` | Performs a search. This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature. |
