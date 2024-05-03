---
title: admin_rule_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_rule_collections
  - network
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
<tr><td><b>Name</b></td><td><code>admin_rule_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.admin_rule_collections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Defines the admin rule collection properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets a network manager security admin configuration rule collection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, subscriptionId" /> | Lists all the rule collections in a security admin configuration, in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates or updates an admin rule collection. |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes an admin rule collection. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, subscriptionId" /> | Lists all the rule collections in a security admin configuration, in a paginated format. |
