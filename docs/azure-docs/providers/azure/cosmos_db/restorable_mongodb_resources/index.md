---
title: restorable_mongodb_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_mongodb_resources
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>restorable_mongodb_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.restorable_mongodb_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="collectionNames" /> | `array` | The names of the collections available for restore. |
| <CopyableCode code="databaseName" /> | `string` | The name of the database available for restore. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instanceId, location, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="instanceId, location, subscriptionId" /> |
