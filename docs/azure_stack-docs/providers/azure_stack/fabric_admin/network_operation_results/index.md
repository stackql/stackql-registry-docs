---
title: network_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - network_operation_results
  - fabric_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>network_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.network_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Network operation result properties. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operation, resourceGroupName, subscriptionId" /> | Returns the status of a network operation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all network operation results at a location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all network operation results at a location. |
