---
title: data_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_controllers
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>data_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.data_controllers" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="_list_in_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="_list_in_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> |  |
| <CopyableCode code="list_in_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_in_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> |  |
| <CopyableCode code="patch_data_controller" /> | `EXEC` | <CopyableCode code="api-version, dataControllerName, resourceGroupName, subscriptionId" /> | Updates a dataController resource |
| <CopyableCode code="put_data_controller" /> | `EXEC` | <CopyableCode code="api-version, dataControllerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or replaces a dataController resource |
