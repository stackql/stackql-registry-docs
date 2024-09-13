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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>recommendation</code> resource or lists <code>recommendations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recommender.recommendations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of recommendation. |
| <CopyableCode code="description" /> | `string` | Free-form human readable summary in English. The maximum length is 500 characters. |
| <CopyableCode code="additionalImpact" /> | `array` | Optional set of additional impact that this recommendation may have when trying to optimize for the primary category. These may be positive or negative. |
| <CopyableCode code="associatedInsights" /> | `array` | Insights that led to this recommendation. |
| <CopyableCode code="content" /> | `object` | Contains what resources are changing and how they are changing. |
| <CopyableCode code="etag" /> | `string` | Fingerprint of the Recommendation. Provides optimistic locking when updating states. |
| <CopyableCode code="lastRefreshTime" /> | `string` | Last time this recommendation was refreshed by the system that created it in the first place. |
| <CopyableCode code="primaryImpact" /> | `object` | Contains the impact a recommendation can have for a given category. |
| <CopyableCode code="priority" /> | `string` | Recommendation's priority. |
| <CopyableCode code="recommenderSubtype" /> | `string` | Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to `content` or `primary_impact.category` are introduced. See the Recommenders section to see a list of subtypes for a given Recommender. Examples: For recommender = "google.iam.policy.Recommender", recommender_subtype can be one of "REMOVE_ROLE"/"REPLACE_ROLE" |
| <CopyableCode code="stateInfo" /> | `object` | Information for state. Contains state and metadata. |
| <CopyableCode code="targetResources" /> | `array` | Fully qualified resource names that this recommendation is targeting. |
| <CopyableCode code="xorGroupId" /> | `string` | Corresponds to a mutually exclusive group ID within a recommender. A non-empty ID indicates that the recommendation belongs to a mutually exclusive group. This means that only one recommendation within the group is suggested to be applied. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_recommenders_recommendations_get" /> | `SELECT` | <CopyableCode code="billingAccountsId, locationsId, recommendationsId, recommendersId" /> | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| <CopyableCode code="billing_accounts_locations_recommenders_recommendations_list" /> | `SELECT` | <CopyableCode code="billingAccountsId, locationsId, recommendersId" /> | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| <CopyableCode code="folders_locations_recommenders_recommendations_get" /> | `SELECT` | <CopyableCode code="foldersId, locationsId, recommendationsId, recommendersId" /> | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| <CopyableCode code="folders_locations_recommenders_recommendations_list" /> | `SELECT` | <CopyableCode code="foldersId, locationsId, recommendersId" /> | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| <CopyableCode code="organizations_locations_recommenders_recommendations_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, recommendationsId, recommendersId" /> | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| <CopyableCode code="organizations_locations_recommenders_recommendations_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, recommendersId" /> | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| <CopyableCode code="projects_locations_recommenders_recommendations_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, recommendationsId, recommendersId" /> | Gets the requested recommendation. Requires the recommender.*.get IAM permission for the specified recommender. |
| <CopyableCode code="projects_locations_recommenders_recommendations_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, recommendersId" /> | Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender. |
| <CopyableCode code="billing_accounts_locations_recommenders_recommendations_mark_claimed" /> | `EXEC` | <CopyableCode code="billingAccountsId, locationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="billing_accounts_locations_recommenders_recommendations_mark_dismissed" /> | `EXEC` | <CopyableCode code="billingAccountsId, locationsId, recommendationsId, recommendersId" /> | Mark the Recommendation State as Dismissed. Users can use this method to indicate to the Recommender API that an ACTIVE recommendation has to be marked back as DISMISSED. MarkRecommendationDismissed can be applied to recommendations in ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="billing_accounts_locations_recommenders_recommendations_mark_failed" /> | `EXEC` | <CopyableCode code="billingAccountsId, locationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="billing_accounts_locations_recommenders_recommendations_mark_succeeded" /> | `EXEC` | <CopyableCode code="billingAccountsId, locationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="folders_locations_recommenders_recommendations_mark_claimed" /> | `EXEC` | <CopyableCode code="foldersId, locationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="folders_locations_recommenders_recommendations_mark_dismissed" /> | `EXEC` | <CopyableCode code="foldersId, locationsId, recommendationsId, recommendersId" /> | Mark the Recommendation State as Dismissed. Users can use this method to indicate to the Recommender API that an ACTIVE recommendation has to be marked back as DISMISSED. MarkRecommendationDismissed can be applied to recommendations in ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="folders_locations_recommenders_recommendations_mark_failed" /> | `EXEC` | <CopyableCode code="foldersId, locationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="folders_locations_recommenders_recommendations_mark_succeeded" /> | `EXEC` | <CopyableCode code="foldersId, locationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="organizations_locations_recommenders_recommendations_mark_claimed" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="organizations_locations_recommenders_recommendations_mark_dismissed" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, recommendationsId, recommendersId" /> | Mark the Recommendation State as Dismissed. Users can use this method to indicate to the Recommender API that an ACTIVE recommendation has to be marked back as DISMISSED. MarkRecommendationDismissed can be applied to recommendations in ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="organizations_locations_recommenders_recommendations_mark_failed" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="organizations_locations_recommenders_recommendations_mark_succeeded" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="projects_locations_recommenders_recommendations_mark_claimed" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Claimed. Users can use this method to indicate to the Recommender API that they are starting to apply the recommendation themselves. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationClaimed can be applied to recommendations in CLAIMED, SUCCEEDED, FAILED, or ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="projects_locations_recommenders_recommendations_mark_dismissed" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, recommendationsId, recommendersId" /> | Mark the Recommendation State as Dismissed. Users can use this method to indicate to the Recommender API that an ACTIVE recommendation has to be marked back as DISMISSED. MarkRecommendationDismissed can be applied to recommendations in ACTIVE state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="projects_locations_recommenders_recommendations_mark_failed" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Failed. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation failed. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationFailed can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |
| <CopyableCode code="projects_locations_recommenders_recommendations_mark_succeeded" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, recommendationsId, recommendersId" /> | Marks the Recommendation State as Succeeded. Users can use this method to indicate to the Recommender API that they have applied the recommendation themselves, and the operation was successful. This stops the recommendation content from being updated. Associated insights are frozen and placed in the ACCEPTED state. MarkRecommendationSucceeded can be applied to recommendations in ACTIVE, CLAIMED, SUCCEEDED, or FAILED state. Requires the recommender.*.update IAM permission for the specified recommender. |

## `SELECT` examples

Lists recommendations for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified recommender.

```sql
SELECT
name,
description,
additionalImpact,
associatedInsights,
content,
etag,
lastRefreshTime,
primaryImpact,
priority,
recommenderSubtype,
stateInfo,
targetResources,
xorGroupId
FROM google.recommender.recommendations
WHERE foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'
AND recommendersId = '{{ recommendersId }}'; 
```
