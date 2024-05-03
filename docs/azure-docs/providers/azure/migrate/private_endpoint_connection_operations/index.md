---
title: private_endpoint_connection_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_operations
  - migrate
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.private_endpoint_connection_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the private endpoint connection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId" /> | Get a PrivateEndpointConnection |
| <CopyableCode code="list_by_assessment_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List PrivateEndpointConnection resources by AssessmentProject |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId" /> | Delete a PrivateEndpointConnection |
| <CopyableCode code="_list_by_assessment_project" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List PrivateEndpointConnection resources by AssessmentProject |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="privateEndpointConnectionName, projectName, resourceGroupName, subscriptionId" /> | Create a PrivateEndpointConnection |
