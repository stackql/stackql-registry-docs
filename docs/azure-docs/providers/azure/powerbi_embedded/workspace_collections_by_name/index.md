---
title: workspace_collections_by_name
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_collections_by_name
  - powerbi_embedded
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
<tr><td><b>Name</b></td><td><code>workspace_collections_by_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_embedded.workspace_collections_by_name" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource id |
| <CopyableCode code="name" /> | `string` | Workspace collection name |
| <CopyableCode code="location" /> | `string` | Azure location |
| <CopyableCode code="properties" /> | `object` | Properties |
| <CopyableCode code="sku" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceCollectionName" /> |
