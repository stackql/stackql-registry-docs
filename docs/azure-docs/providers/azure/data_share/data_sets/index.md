---
title: data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sets
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
<tr><td><b>Name</b></td><td><code>data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.data_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="kind" /> | `string` | Kind of data set. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, dataSetName, resourceGroupName, shareName, subscriptionId" /> | Get a DataSet in a share |
| <CopyableCode code="list_by_share" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, shareName, subscriptionId" /> | List DataSets in a share |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, dataSetName, resourceGroupName, shareName, subscriptionId, data__kind" /> | Create a DataSet  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, dataSetName, resourceGroupName, shareName, subscriptionId" /> | Delete a DataSet in a share |
