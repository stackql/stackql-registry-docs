---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - powerbi_privatelinks
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_privatelinks.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the id of the resource. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the resource. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureResourceName, privateEndpointName, resourceGroupName, subscriptionId" /> | Get a specific private endpoint connection for Power BI by private endpoint name. |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Gets private endpoint connection for Power BI. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="azureResourceName, privateEndpointName, resourceGroupName, subscriptionId" /> | Updates the status of Private Endpoint Connection object. Used to approve or reject a connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureResourceName, privateEndpointName, resourceGroupName, subscriptionId" /> | Deletes a private endpoint connection for Power BI by private endpoint name. |
