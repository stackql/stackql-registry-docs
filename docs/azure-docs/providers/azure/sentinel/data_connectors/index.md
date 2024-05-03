---
title: data_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connectors
  - sentinel
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
<tr><td><b>Name</b></td><td><code>data_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.data_connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="kind" /> | `string` | The kind of the data connector |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataConnectorId, resourceGroupName, subscriptionId, workspaceName" /> | Gets a data connector. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all data connectors. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataConnectorId, resourceGroupName, subscriptionId, workspaceName, data__kind" /> | Creates or updates the data connector. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataConnectorId, resourceGroupName, subscriptionId, workspaceName" /> | Delete the data connector. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all data connectors. |
