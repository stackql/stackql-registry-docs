---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - key_vault
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `string` | Name of the key vault resource. |
| <CopyableCode code="etag" /> | `string` | Modified whenever there is a change in the state of private endpoint connection. |
| <CopyableCode code="location" /> | `string` | Azure location of the key vault resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the private endpoint connection resource. |
| <CopyableCode code="tags" /> | `object` | Tags assigned to the key vault resource. |
| <CopyableCode code="type" /> | `string` | Resource type of the key vault resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName" /> | Gets the specified private endpoint connection associated with the key vault. |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | The List operation gets information about the private endpoint connections associated with the vault. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName" /> | Deletes the specified private endpoint connection associated with the key vault. |
| <CopyableCode code="_list_by_resource" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | The List operation gets information about the private endpoint connections associated with the vault. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName" /> | Updates the specified private endpoint connection associated with the key vault. |
