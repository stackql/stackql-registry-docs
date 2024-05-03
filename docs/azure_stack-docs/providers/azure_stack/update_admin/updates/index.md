---
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
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
<tr><td><b>Name</b></td><td><code>updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.update_admin.updates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Region location of resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an update. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Get a specific update at an update location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation" /> | Get the list of updates at an update locations |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation" /> | Get the list of updates at an update locations |
| <CopyableCode code="apply" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Apply a specific update at an update location. |
| <CopyableCode code="health_check" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Run health check for a specified update at an update location. |
| <CopyableCode code="prepare" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Prepare a specified update at an update location. |
