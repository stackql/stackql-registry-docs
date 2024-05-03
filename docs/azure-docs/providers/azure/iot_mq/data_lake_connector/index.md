---
title: data_lake_connector
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_connector
  - iot_mq
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
<tr><td><b>Name</b></td><td><code>data_lake_connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.data_lake_connector" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MQ DataLakeConnector  Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId" /> | Get a DataLakeConnectorResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List DataLakeConnectorResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a DataLakeConnectorResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId" /> | Delete a DataLakeConnectorResource |
| <CopyableCode code="_list_by_mq_resource" /> | `EXEC` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List DataLakeConnectorResource resources by MqResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId" /> | Update a DataLakeConnectorResource |
