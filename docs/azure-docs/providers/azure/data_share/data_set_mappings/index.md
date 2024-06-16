---
title: data_set_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - data_set_mappings
  - data_share
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
<tr><td><b>Name</b></td><td><code>data_set_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.data_set_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="kind" /> | `string` | Kind of data set mapping. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, dataSetMappingName, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Get a DataSetMapping in a shareSubscription |
| <CopyableCode code="list_by_share_subscription" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId" /> | List DataSetMappings in a share subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, dataSetMappingName, resourceGroupName, shareSubscriptionName, subscriptionId, data__kind" /> | Create a DataSetMapping  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, dataSetMappingName, resourceGroupName, shareSubscriptionName, subscriptionId" /> | Delete a DataSetMapping in a shareSubscription |
