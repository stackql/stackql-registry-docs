---
title: connector_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_mappings
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>connector_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.connector_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The connector mapping definition. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectorName, hubName, mappingName, resourceGroupName, subscriptionId" /> | Gets a connector mapping in the connector. |
| <CopyableCode code="list_by_connector" /> | `SELECT` | <CopyableCode code="connectorName, hubName, resourceGroupName, subscriptionId" /> | Gets all the connector mappings in the specified connector. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectorName, hubName, mappingName, resourceGroupName, subscriptionId" /> | Creates a connector mapping or updates an existing connector mapping in the connector. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectorName, hubName, mappingName, resourceGroupName, subscriptionId" /> | Deletes a connector mapping in the connector. |
| <CopyableCode code="_list_by_connector" /> | `EXEC` | <CopyableCode code="connectorName, hubName, resourceGroupName, subscriptionId" /> | Gets all the connector mappings in the specified connector. |
