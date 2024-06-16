---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - api_center
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.deployments" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiName, deploymentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns details of the API deployment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns a collection of API deployments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiName, deploymentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Creates new or updates existing API deployment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiName, deploymentName, resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Deletes API deployment. |
