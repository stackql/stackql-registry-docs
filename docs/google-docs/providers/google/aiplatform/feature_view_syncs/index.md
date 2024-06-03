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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_view_syncs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.feature_view_syncs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the FeatureViewSync. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/featureOnlineStores/&#123;feature_online_store&#125;/featureViews/&#123;feature_view&#125;/featureViewSyncs/&#123;feature_view_sync&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when this FeatureViewSync is created. Creation of a FeatureViewSync means that the job is pending / waiting for sufficient resources but may not have started the actual data transfer yet. |
| <CopyableCode code="finalStatus" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="runTime" /> | `object` | Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive). The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time. |
| <CopyableCode code="syncSummary" /> | `object` | Summary from the Sync job. For continuous syncs, the summary is updated periodically. For batch syncs, it gets updated on completion of the sync. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, featureViewSyncsId, featureViewsId, locationsId, projectsId" /> | Gets details of a single FeatureViewSync. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Lists FeatureViewSyncs in a given FeatureView. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Lists FeatureViewSyncs in a given FeatureView. |
