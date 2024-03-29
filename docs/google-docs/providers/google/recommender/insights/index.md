---
title: insights
hide_title: false
hide_table_of_contents: false
keywords:
  - insights
  - recommender
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
<tr><td><b>Name</b></td><td><code>insights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommender.insights</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the insight. |
| `description` | `string` | Free-form human readable summary in English. The maximum length is 500 characters. |
| `lastRefreshTime` | `string` | Timestamp of the latest data used to generate the insight. |
| `targetResources` | `array` | Fully qualified resource names that this insight is targeting. |
| `content` | `object` | A struct of custom fields to explain the insight. Example: "grantedPermissionsCount": "1000" |
| `etag` | `string` | Fingerprint of the Insight. Provides optimistic locking when updating states. |
| `stateInfo` | `object` | Information related to insight state. |
| `associatedRecommendations` | `array` | Recommendations derived from this insight. |
| `category` | `string` | Category being targeted by the insight. |
| `insightSubtype` | `string` | Insight subtype. Insight content schema will be stable for a given subtype. |
| `observationPeriod` | `string` | Observation period that led to the insight. The source data used to generate the insight ends at last_refresh_time and begins at (last_refresh_time - observation_period). |
| `severity` | `string` | Insight's severity. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_locations_insight_types_insights_get` | `SELECT` | `billingAccountsId, insightTypesId, insightsId, locationsId` | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| `billing_accounts_locations_insight_types_insights_list` | `SELECT` | `billingAccountsId, insightTypesId, locationsId` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `folders_locations_insight_types_insights_get` | `SELECT` | `foldersId, insightTypesId, insightsId, locationsId` | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| `folders_locations_insight_types_insights_list` | `SELECT` | `foldersId, insightTypesId, locationsId` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `organizations_locations_insight_types_insights_get` | `SELECT` | `insightTypesId, insightsId, locationsId, organizationsId` | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| `organizations_locations_insight_types_insights_list` | `SELECT` | `insightTypesId, locationsId, organizationsId` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `projects_locations_insight_types_insights_get` | `SELECT` | `insightTypesId, insightsId, locationsId, projectsId` | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| `projects_locations_insight_types_insights_list` | `SELECT` | `insightTypesId, locationsId, projectsId` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `_billing_accounts_locations_insight_types_insights_list` | `EXEC` | `billingAccountsId, insightTypesId, locationsId` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `_folders_locations_insight_types_insights_list` | `EXEC` | `foldersId, insightTypesId, locationsId` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `_organizations_locations_insight_types_insights_list` | `EXEC` | `insightTypesId, locationsId, organizationsId` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `_projects_locations_insight_types_insights_list` | `EXEC` | `insightTypesId, locationsId, projectsId` | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| `billing_accounts_locations_insight_types_insights_mark_accepted` | `EXEC` | `billingAccountsId, insightTypesId, insightsId, locationsId` | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| `folders_locations_insight_types_insights_mark_accepted` | `EXEC` | `foldersId, insightTypesId, insightsId, locationsId` | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| `organizations_locations_insight_types_insights_mark_accepted` | `EXEC` | `insightTypesId, insightsId, locationsId, organizationsId` | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| `projects_locations_insight_types_insights_mark_accepted` | `EXEC` | `insightTypesId, insightsId, locationsId, projectsId` | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
