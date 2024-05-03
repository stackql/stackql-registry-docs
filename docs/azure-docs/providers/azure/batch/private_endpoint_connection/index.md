---
title: private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection
  - batch
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.private_endpoint_connection" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="properties" /> | `object` | Private endpoint connection properties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets information about the specified private endpoint connection. |
| <CopyableCode code="list_by_batch_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all of the private endpoint connections in the specified account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes the specified private endpoint connection. |
| <CopyableCode code="_list_by_batch_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all of the private endpoint connections in the specified account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing private endpoint connection. |
