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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>insights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recommender.insights" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the insight. |
| <CopyableCode code="description" /> | `string` | Free-form human readable summary in English. The maximum length is 500 characters. |
| <CopyableCode code="associatedRecommendations" /> | `array` | Recommendations derived from this insight. |
| <CopyableCode code="category" /> | `string` | Category being targeted by the insight. |
| <CopyableCode code="content" /> | `object` | A struct of custom fields to explain the insight. Example: "grantedPermissionsCount": "1000" |
| <CopyableCode code="etag" /> | `string` | Fingerprint of the Insight. Provides optimistic locking when updating states. |
| <CopyableCode code="insightSubtype" /> | `string` | Insight subtype. Insight content schema will be stable for a given subtype. |
| <CopyableCode code="lastRefreshTime" /> | `string` | Timestamp of the latest data used to generate the insight. |
| <CopyableCode code="observationPeriod" /> | `string` | Observation period that led to the insight. The source data used to generate the insight ends at last_refresh_time and begins at (last_refresh_time - observation_period). |
| <CopyableCode code="severity" /> | `string` | Insight's severity. |
| <CopyableCode code="stateInfo" /> | `object` | Information related to insight state. |
| <CopyableCode code="targetResources" /> | `array` | Fully qualified resource names that this insight is targeting. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_insight_types_insights_get" /> | `SELECT` | <CopyableCode code="billingAccountsId, insightTypesId, insightsId, locationsId" /> | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| <CopyableCode code="billing_accounts_locations_insight_types_insights_list" /> | `SELECT` | <CopyableCode code="billingAccountsId, insightTypesId, locationsId" /> | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| <CopyableCode code="folders_locations_insight_types_insights_get" /> | `SELECT` | <CopyableCode code="foldersId, insightTypesId, insightsId, locationsId" /> | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| <CopyableCode code="folders_locations_insight_types_insights_list" /> | `SELECT` | <CopyableCode code="foldersId, insightTypesId, locationsId" /> | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| <CopyableCode code="organizations_locations_insight_types_insights_get" /> | `SELECT` | <CopyableCode code="insightTypesId, insightsId, locationsId, organizationsId" /> | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| <CopyableCode code="organizations_locations_insight_types_insights_list" /> | `SELECT` | <CopyableCode code="insightTypesId, locationsId, organizationsId" /> | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| <CopyableCode code="projects_locations_insight_types_insights_get" /> | `SELECT` | <CopyableCode code="insightTypesId, insightsId, locationsId, projectsId" /> | Gets the requested insight. Requires the recommender.*.get IAM permission for the specified insight type. |
| <CopyableCode code="projects_locations_insight_types_insights_list" /> | `SELECT` | <CopyableCode code="insightTypesId, locationsId, projectsId" /> | Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type. |
| <CopyableCode code="billing_accounts_locations_insight_types_insights_mark_accepted" /> | `EXEC` | <CopyableCode code="billingAccountsId, insightTypesId, insightsId, locationsId" /> | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| <CopyableCode code="folders_locations_insight_types_insights_mark_accepted" /> | `EXEC` | <CopyableCode code="foldersId, insightTypesId, insightsId, locationsId" /> | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| <CopyableCode code="organizations_locations_insight_types_insights_mark_accepted" /> | `EXEC` | <CopyableCode code="insightTypesId, insightsId, locationsId, organizationsId" /> | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |
| <CopyableCode code="projects_locations_insight_types_insights_mark_accepted" /> | `EXEC` | <CopyableCode code="insightTypesId, insightsId, locationsId, projectsId" /> | Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated. MarkInsightAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight. |

## `SELECT` examples

Lists insights for the specified Cloud Resource. Requires the recommender.*.list IAM permission for the specified insight type.

```sql
SELECT
name,
description,
associatedRecommendations,
category,
content,
etag,
insightSubtype,
lastRefreshTime,
observationPeriod,
severity,
stateInfo,
targetResources
FROM google.recommender.insights
WHERE foldersId = '{{ foldersId }}'
AND insightTypesId = '{{ insightTypesId }}'
AND locationsId = '{{ locationsId }}'; 
```
