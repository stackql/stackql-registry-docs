---
title: web_pub_sub_replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub_replicas
  - web_pubsub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub_replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.web_pub_sub_replicas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="sku" /> | `object` | The billing information of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Get the replica and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List all replicas belong to this resource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Create or update a replica. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Operation to delete a replica. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Operation to restart a replica. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Operation to update an exiting replica. |
