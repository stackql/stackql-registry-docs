---
title: data_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connectors
  - ag_food_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>data_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.data_connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | The ETag value to implement optimistic concurrency. |
| <CopyableCode code="properties" /> | `object` | DataConnector Properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Get specific Data Connector resource by DataConnectorName. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Lists the Data Connector Credentials for MADMA instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId, data__properties" /> | Create or update Data Connector For MADMA resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Delete a Data Connectors with given dataConnector name. |
