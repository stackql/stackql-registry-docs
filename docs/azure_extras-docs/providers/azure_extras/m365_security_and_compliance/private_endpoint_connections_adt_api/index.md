---
title: private_endpoint_connections_adt_api
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections_adt_api
  - m365_security_and_compliance
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections_adt_api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.m365_security_and_compliance.private_endpoint_connections_adt_api" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the PrivateEndpointConnectProperties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Gets the specified private endpoint connection associated with the service. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists all private endpoint connections for a service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Update the state of the specified private endpoint connection associated with the service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Deletes a private endpoint connection. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists all private endpoint connections for a service. |
