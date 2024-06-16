---
title: big_data_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - big_data_pools
  - synapse
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
<tr><td><b>Name</b></td><td><code>big_data_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.big_data_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a Big Data pool powered by Apache Spark |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bigDataPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Get a Big Data pool. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List Big Data pools in a workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bigDataPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Create a new Big Data pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bigDataPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Delete a Big Data pool from the workspace. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="bigDataPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Patch a Big Data pool. |
