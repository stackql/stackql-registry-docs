---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - purview
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the identifier. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="properties" /> | `object` | A private endpoint connection properties class. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Get a private endpoint connection |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Get private endpoint connections for account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Create or update a private endpoint connection |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Delete a private endpoint connection |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Get private endpoint connections for account |
