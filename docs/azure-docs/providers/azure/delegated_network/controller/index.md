---
title: controller
hide_title: false
hide_table_of_contents: false
keywords:
  - controller
  - delegated_network
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
<tr><td><b>Name</b></td><td><code>controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.delegated_network.controller" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a dnc controller |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes the DNC controller |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Update dnc controller |
