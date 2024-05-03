---
title: move_collections_move_collections_by_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - move_collections_move_collections_by_subscription
  - resource_mover
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
<tr><td><b>Name</b></td><td><code>move_collections_move_collections_by_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_mover.move_collections_move_collections_by_subscription" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource Id for the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | The etag of the resource. |
| <CopyableCode code="identity" /> | `object` | Defines the MSI properties of the Move Collection. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives. |
| <CopyableCode code="properties" /> | `object` | Defines the move collection properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> |
