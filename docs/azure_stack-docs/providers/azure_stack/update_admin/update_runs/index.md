---
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
  - update_admin
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
<tr><td><b>Name</b></td><td><code>update_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.update_admin.update_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Region location of resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an update run. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, runName, subscriptionId, updateLocation, updateName" /> | Get an instance of update run using the ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Get the list of update runs. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Get the list of update runs. |
| <CopyableCode code="rerun" /> | `EXEC` | <CopyableCode code="resourceGroupName, runName, subscriptionId, updateLocation, updateName" /> | Resume a failed update. |
