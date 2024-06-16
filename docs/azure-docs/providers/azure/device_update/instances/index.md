---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - device_update
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_update.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Device Update instance properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, instanceName, resourceGroupName, subscriptionId" /> | Returns instance details for the given instance and account name. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Returns instances for the given account name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, instanceName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, instanceName, resourceGroupName, subscriptionId" /> | Deletes instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, instanceName, resourceGroupName, subscriptionId" /> | Updates instance's tags. |
