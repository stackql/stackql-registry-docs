---
title: data_types
hide_title: false
hide_table_of_contents: false
keywords:
  - data_types
  - network_analytics
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
<tr><td><b>Name</b></td><td><code>data_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_analytics.data_types" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Retrieve data type resource. |
| <CopyableCode code="list_by_data_product" /> | `SELECT` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | List data type by parent resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Create data type resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Delete data type resource. |
| <CopyableCode code="generate_storage_container_sas_token" /> | `EXEC` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId, data__expiryTimeStamp, data__ipAddress, data__startTimeStamp" /> | Generate sas token for storage container. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Update data type resource. |
