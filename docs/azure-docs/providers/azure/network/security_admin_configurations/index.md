---
title: security_admin_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - security_admin_configurations
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
<tr><td><b>Name</b></td><td><code>security_admin_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.security_admin_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Defines the security admin configuration properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Retrieves a network manager security admin configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Lists all the network manager security admin configurations in a network manager, in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates or updates a network manager security admin configuration. |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes a network manager security admin configuration. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Lists all the network manager security admin configurations in a network manager, in a paginated format. |
