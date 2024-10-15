---
title: managed_az_resiliency_status
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_az_resiliency_status
  - service_fabric_managed_clusters
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

Creates, updates, deletes, gets or lists a <code>managed_az_resiliency_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_az_resiliency_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.managed_az_resiliency_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="baseResourceStatus" /> | `array` | List of Managed VM Sizes for Service Fabric Managed Clusters. |
| <CopyableCode code="isClusterZoneResilient" /> | `boolean` | URL to get the next set of Managed VM Sizes if there are any. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Action to get Az Resiliency Status of all the Base resources constituting Service Fabric Managed Clusters. |

## `SELECT` examples

Action to get Az Resiliency Status of all the Base resources constituting Service Fabric Managed Clusters.


```sql
SELECT
baseResourceStatus,
isClusterZoneResilient
FROM azure.service_fabric_managed_clusters.managed_az_resiliency_status
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```