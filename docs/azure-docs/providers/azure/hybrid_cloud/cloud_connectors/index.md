---
title: cloud_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_connectors
  - hybrid_cloud
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
<tr><td><b>Name</b></td><td><code>cloud_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_cloud.cloud_connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Cloud connector resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Gets the specified cloud connector in a specified resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Return list of cloud connectors in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Return list of cloud connectors in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Creates or updates a cloud connector resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Deletes a specified cloud connector resource. |
| <CopyableCode code="discover_resources" /> | `EXEC` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Returns a list of discovered remote cloud resources via this cloud connector resource. |
