---
title: managed_instance_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_private_endpoint_connections
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_instance_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets a private endpoint connection. |
| <CopyableCode code="list_by_managed_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets all private endpoint connections on a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Approve or reject a private endpoint connection with a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedInstanceName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes a private endpoint connection with a given name. |
