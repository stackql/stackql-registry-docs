---
title: feature_views
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_views
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>feature_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.feature_views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the FeatureView. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/featureOnlineStores/&#123;feature_online_store&#125;/featureViews/&#123;feature_view&#125;` |
| <CopyableCode code="bigQuerySource" /> | `object` |  |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this FeatureView was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="featureRegistrySource" /> | `object` | A Feature Registry source for features that need to be synced to Online Store. |
| <CopyableCode code="indexConfig" /> | `object` | Configuration for vector indexing. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your FeatureViews. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="syncConfig" /> | `object` | Configuration for Sync. Only one option is set. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this FeatureView was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Gets details of a single FeatureView. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Lists FeatureViews in a given FeatureOnlineStore. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Creates a new FeatureView in a given FeatureOnlineStore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Deletes a single FeatureView. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Updates the parameters of a single FeatureView. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Lists FeatureViews in a given FeatureOnlineStore. |
| <CopyableCode code="search_nearest_entities" /> | `EXEC` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Search the nearest entities under a FeatureView. Search only works for indexable feature view; if a feature view isn't indexable, returns Invalid argument response. |
| <CopyableCode code="sync" /> | `EXEC` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Triggers on-demand sync for the FeatureView. |
