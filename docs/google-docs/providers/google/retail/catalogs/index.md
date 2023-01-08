---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
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
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.catalogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `catalogs` | `array` | All the customer's Catalogs. |
| `nextPageToken` | `string` | A token that can be sent as ListCatalogsRequest.page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_list` | `SELECT` | `locationsId, projectsId` | Lists all the Catalogs associated with the project. |
| `projects_locations_catalogs_completeQuery` | `EXEC` | `catalogsId, locationsId, projectsId` | Completes the specified prefix with keyword suggestions. This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature. |
| `projects_locations_catalogs_patch` | `EXEC` | `catalogsId, locationsId, projectsId` | Updates the Catalogs. |
| `projects_locations_catalogs_setDefaultBranch` | `EXEC` | `catalogsId, locationsId, projectsId` | Set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default. For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`. Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as SearchRequest.branch to route the traffic to this staging branch. CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one. More specifically: * PredictionService will only return product IDs from branch &#123;newBranch&#125;. * SearchService will only return product IDs from branch &#123;newBranch&#125; (if branch is not explicitly set). * UserEventService will only join events with products from branch &#123;newBranch&#125;. |
| `projects_locations_catalogs_updateAttributesConfig` | `EXEC` | `catalogsId, locationsId, projectsId` | Updates the AttributesConfig. The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options. |
| `projects_locations_catalogs_updateCompletionConfig` | `EXEC` | `catalogsId, locationsId, projectsId` | Updates the CompletionConfigs. |
