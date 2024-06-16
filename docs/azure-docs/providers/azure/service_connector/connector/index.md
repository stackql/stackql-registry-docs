---
title: connector
hide_title: false
hide_table_of_contents: false
keywords:
  - connector
  - service_connector
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
<tr><td><b>Name</b></td><td><code>connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_connector.connector" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the Linker. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Returns Connector resource for a given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns list of connector which connects to the resource, which supports to config the target service during the resource provision. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId, data__properties" /> | Create or update Connector resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Delete a Connector. |
| <CopyableCode code="generate_configurations" /> | `EXEC` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Generate configurations for a Connector. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Operation to update an existing Connector. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="connectorName, location, resourceGroupName, subscriptionId" /> | Validate a Connector. |
