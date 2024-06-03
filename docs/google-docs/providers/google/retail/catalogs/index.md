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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.catalogs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Immutable. The fully qualified resource name of the catalog. |
| <CopyableCode code="displayName" /> | `string` | Required. Immutable. The catalog display name. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. |
| <CopyableCode code="productLevelConfig" /> | `object` | Configures what level the product should be uploaded with regards to how users will be send events and how predictions will be made. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the Catalogs associated with the project. |
| <CopyableCode code="projects_locations_catalogs_patch" /> | `UPDATE` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Updates the Catalogs. |
| <CopyableCode code="_projects_locations_catalogs_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all the Catalogs associated with the project. |
| <CopyableCode code="projects_locations_catalogs_complete_query" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Completes the specified prefix with keyword suggestions. This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature. |
| <CopyableCode code="projects_locations_catalogs_export_analytics_metrics" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Exports analytics metrics. `Operation.response` is of type `ExportAnalyticsMetricsResponse`. `Operation.metadata` is of type `ExportMetadata`. |
| <CopyableCode code="projects_locations_catalogs_set_default_branch" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Set a specified branch id as default branch. API methods such as SearchService.Search, ProductService.GetProduct, ProductService.ListProducts will treat requests using "default_branch" to the actual branch id set as default. For example, if `projects/*/locations/*/catalogs/*/branches/1` is set as default, setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/default_branch` is equivalent to setting SearchRequest.branch to `projects/*/locations/*/catalogs/*/branches/1`. Using multiple branches can be useful when developers would like to have a staging branch to test and verify for future usage. When it becomes ready, developers switch on the staging branch using this API while keeping using `projects/*/locations/*/catalogs/*/branches/default_branch` as SearchRequest.branch to route the traffic to this staging branch. CAUTION: If you have live predict/search traffic, switching the default branch could potentially cause outages if the ID space of the new branch is very different from the old one. More specifically: * PredictionService will only return product IDs from branch &#123;newBranch&#125;. * SearchService will only return product IDs from branch &#123;newBranch&#125; (if branch is not explicitly set). * UserEventService will only join events with products from branch &#123;newBranch&#125;. |
