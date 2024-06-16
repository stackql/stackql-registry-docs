---
title: publishers
hide_title: false
hide_table_of_contents: false
keywords:
  - publishers
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>publishers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.publishers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | publisher properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information about the specified publisher. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the publishers in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the publishers in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a publisher. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Deletes the specified publisher. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Update a publisher resource. |
