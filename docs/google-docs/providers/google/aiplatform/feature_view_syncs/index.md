---
title: feature_view_syncs
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_view_syncs
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>feature_view_syncs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_view_syncs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.feature_view_syncs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the FeatureViewSync. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when this FeatureViewSync is created. Creation of a FeatureViewSync means that the job is pending / waiting for sufficient resources but may not have started the actual data transfer yet. |
| <CopyableCode code="finalStatus" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="runTime" /> | `object` | Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive). The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="syncSummary" /> | `object` | Summary from the Sync job. For continuous syncs, the summary is updated periodically. For batch syncs, it gets updated on completion of the sync. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, featureViewSyncsId, featureViewsId, locationsId, projectsId" /> | Gets details of a single FeatureViewSync. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Lists FeatureViewSyncs in a given FeatureView. |

## `SELECT` examples

Lists FeatureViewSyncs in a given FeatureView.

```sql
SELECT
name,
createTime,
finalStatus,
runTime,
satisfiesPzi,
satisfiesPzs,
syncSummary
FROM google.aiplatform.feature_view_syncs
WHERE featureOnlineStoresId = '{{ featureOnlineStoresId }}'
AND featureViewsId = '{{ featureViewsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
