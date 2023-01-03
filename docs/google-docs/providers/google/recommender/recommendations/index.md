---
title: recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendations
  - recommender
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
<tr><td><b>Name</b></td><td><code>recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommender.recommendations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of recommendation. |
| `description` | `string` | Free-form human readable summary in English. The maximum length is 500 characters. |
| `xorGroupId` | `string` | Corresponds to a mutually exclusive group ID within a recommender. A non-empty ID indicates that the recommendation belongs to a mutually exclusive group. This means that only one recommendation within the group is suggested to be applied. |
| `content` | `object` | Contains what resources are changing and how they are changing. |
| `stateInfo` | `object` | Information for state. Contains state and metadata. |
| `additionalImpact` | `array` | Optional set of additional impact that this recommendation may have when trying to optimize for the primary category. These may be positive or negative. |
| `associatedInsights` | `array` | Insights that led to this recommendation. |
| `etag` | `string` | Fingerprint of the Recommendation. Provides optimistic locking when updating states. |
| `priority` | `string` | Recommendation's priority. |
| `recommenderSubtype` | `string` | Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to `content` or `primary_impact.category` are introduced. See the Recommenders section to see a list of subtypes for a given Recommender. Examples: For recommender = "google.iam.policy.Recommender", recommender_subtype can be one of "REMOVE_ROLE"/"REPLACE_ROLE" |
| `lastRefreshTime` | `string` | Last time this recommendation was refreshed by the system that created it in the first place. |
| `primaryImpact` | `object` | Contains the impact a recommendation can have for a given category. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAccounts_locations_recommenders_recommendations_get` | `SELECT` | `billingAccountsId, locationsId, recommendationsId, recommendersId` | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| `billingAccounts_locations_recommenders_recommendations_list` | `SELECT` | `billingAccountsId, locationsId, recommendersId` | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_get` | `SELECT` | `foldersId, locationsId, recommendationsId, recommendersId` | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_list` | `SELECT` | `foldersId, locationsId, recommendersId` | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_get` | `SELECT` | `locationsId, organizationsId, recommendationsId, recommendersId` | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_list` | `SELECT` | `locationsId, organizationsId, recommendersId` | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_get` | `SELECT` | `locationsId, projectsId, recommendationsId, recommendersId` | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_list` | `SELECT` | `locationsId, projectsId, recommendersId` | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| `billingAccounts_locations_recommenders_recommendations_markClaimed` | `EXEC` | `billingAccountsId, locationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `billingAccounts_locations_recommenders_recommendations_markFailed` | `EXEC` | `billingAccountsId, locationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `billingAccounts_locations_recommenders_recommendations_markSucceeded` | `EXEC` | `billingAccountsId, locationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_markClaimed` | `EXEC` | `foldersId, locationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_markFailed` | `EXEC` | `foldersId, locationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `folders_locations_recommenders_recommendations_markSucceeded` | `EXEC` | `foldersId, locationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_markClaimed` | `EXEC` | `locationsId, organizationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_markFailed` | `EXEC` | `locationsId, organizationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `organizations_locations_recommenders_recommendations_markSucceeded` | `EXEC` | `locationsId, organizationsId, recommendationsId, recommendersId` | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_markClaimed` | `EXEC` | `locationsId, projectsId, recommendationsId, recommendersId` | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_markFailed` | `EXEC` | `locationsId, projectsId, recommendationsId, recommendersId` | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| `projects_locations_recommenders_recommendations_markSucceeded` | `EXEC` | `locationsId, projectsId, recommendationsId, recommendersId` | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
