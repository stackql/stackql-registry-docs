---
title: permissions_for_resource_group
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions_for_resource_group
  - authorization
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
<tr><td><b>Name</b></td><td><code>permissions_for_resource_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.permissions_for_resource_group" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actions" /> | `array` | Allowed actions. |
| <CopyableCode code="condition" /> | `string` | The conditions on the role definition. This limits the resources it can be assigned to. e.g.: @Resource[Microsoft.Storage/storageAccounts/blobServices/containers:ContainerName] StringEqualsIgnoreCase 'foo_storage_container' |
| <CopyableCode code="conditionVersion" /> | `string` | Version of the condition. Currently the only accepted value is '2.0' |
| <CopyableCode code="dataActions" /> | `array` | Allowed Data actions. |
| <CopyableCode code="notActions" /> | `array` | Denied actions. |
| <CopyableCode code="notDataActions" /> | `array` | Denied Data actions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
