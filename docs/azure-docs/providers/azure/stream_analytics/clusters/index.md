---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - stream_analytics
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The current entity tag for the cluster. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties associated with a Stream Analytics cluster. |
| <CopyableCode code="sku" /> | `object` | The SKU of the cluster. This determines the size/capacity of the cluster. Required on PUT (CreateOrUpdate) requests. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets information about the specified cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the clusters in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the clusters in the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Creates a Stream Analytics Cluster or replaces an already existing cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes the specified cluster. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the clusters in the given resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all of the clusters in the given subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Updates an existing cluster. This can be used to partially update (ie. update one or two properties) a cluster without affecting the rest of the cluster definition. |
