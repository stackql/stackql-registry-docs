---
title: available_service_tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - available_service_tiers
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>available_service_tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.available_service_tiers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacityReservationLevel" /> | `integer` | The capacity reservation level in GB per day. Returned for the Capacity Reservation Service Tier. |
| <CopyableCode code="defaultRetention" /> | `integer` | The default retention for the Service Tier, in days. |
| <CopyableCode code="enabled" /> | `boolean` | True if the Service Tier is enabled for the workspace. |
| <CopyableCode code="lastSkuUpdate" /> | `string` | Time when the sku was last updated for the workspace. Returned for the Capacity Reservation Service Tier. |
| <CopyableCode code="maximumRetention" /> | `integer` | The maximum retention for the Service Tier, in days. |
| <CopyableCode code="minimumRetention" /> | `integer` | The minimum retention for the Service Tier, in days. |
| <CopyableCode code="serviceTier" /> | `string` | The name of the Service Tier. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
