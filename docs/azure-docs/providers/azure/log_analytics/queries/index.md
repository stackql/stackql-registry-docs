---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.queries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Properties that define an Log Analytics QueryPack-Query resource. |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, queryPackName, resourceGroupName, subscriptionId" /> | Gets a specific Log Analytics Query defined within a Log Analytics QueryPack. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="queryPackName, resourceGroupName, subscriptionId" /> | Gets a list of Queries defined within a Log Analytics QueryPack. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, queryPackName, resourceGroupName, subscriptionId" /> | Deletes a specific Query defined within an Log Analytics QueryPack. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="id, queryPackName, resourceGroupName, subscriptionId" /> | Adds or Updates a specific Query within a Log Analytics QueryPack. |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="queryPackName, resourceGroupName, subscriptionId" /> | Search a list of Queries defined within a Log Analytics QueryPack according to given search properties. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="id, queryPackName, resourceGroupName, subscriptionId" /> | Adds or Updates a specific Query within a Log Analytics QueryPack. |
