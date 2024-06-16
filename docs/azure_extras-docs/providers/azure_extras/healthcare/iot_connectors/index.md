---
title: iot_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_connectors
  - healthcare
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
<tr><td><b>Name</b></td><td><code>iot_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.iot_connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Setting indicating whether the service has a managed identity associated with it. |
| <CopyableCode code="properties" /> | `object` | IoT Connector properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified IoT Connector. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all IoT Connectors for the given workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates an IoT Connector resource with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes an IoT Connector. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="iotConnectorName, resourceGroupName, subscriptionId, workspaceName" /> | Patch an IoT Connector. |
