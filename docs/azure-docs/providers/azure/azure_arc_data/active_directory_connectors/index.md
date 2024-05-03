---
title: active_directory_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - active_directory_connectors
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
<tr><td><b>Name</b></td><td><code>active_directory_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.active_directory_connectors" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activeDirectoryConnectorName, api-version, dataControllerName, resourceGroupName, subscriptionId" /> | Retrieves an Active Directory connector resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, dataControllerName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="activeDirectoryConnectorName, api-version, dataControllerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or replaces an Active Directory connector resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="activeDirectoryConnectorName, api-version, dataControllerName, resourceGroupName, subscriptionId" /> | Deletes an Active Directory connector resource |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, dataControllerName, resourceGroupName, subscriptionId" /> |  |
