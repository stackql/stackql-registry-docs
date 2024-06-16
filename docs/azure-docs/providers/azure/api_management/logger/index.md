---
title: logger
hide_title: false
hide_table_of_contents: false
keywords:
  - logger
  - api_management
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
<tr><td><b>Name</b></td><td><code>logger</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.logger" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loggerId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the logger specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of loggers in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="loggerId, resourceGroupName, serviceName, subscriptionId" /> | Creates or Updates a logger. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, loggerId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified logger. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, loggerId, resourceGroupName, serviceName, subscriptionId" /> | Updates an existing logger. |
