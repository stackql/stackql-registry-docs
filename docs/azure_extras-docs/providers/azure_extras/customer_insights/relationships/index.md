---
title: relationships
hide_title: false
hide_table_of_contents: false
keywords:
  - relationships
  - customer_insights
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>relationships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.relationships" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The definition of Relationship. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, relationshipName, resourceGroupName, subscriptionId" /> | Gets information about the specified relationship. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all relationships in the hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, relationshipName, resourceGroupName, subscriptionId" /> | Creates a relationship or updates an existing relationship within a hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, relationshipName, resourceGroupName, subscriptionId" /> | Deletes a relationship within a hub. |
| <CopyableCode code="_list_by_hub" /> | `EXEC` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all relationships in the hub. |
