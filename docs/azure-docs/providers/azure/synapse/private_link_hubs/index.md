---
title: private_link_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_hubs
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
<tr><td><b>Name</b></td><td><code>private_link_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.private_link_hubs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | PrivateLinkHub properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets a privateLinkHub |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of privateLinkHubs in a subscription |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` |  | Returns a list of privateLinkHubs in a resource group |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates or updates a privateLinkHub |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes a privateLinkHub |
| <CopyableCode code="update" /> | `EXEC` |  | Updates a privateLinkHub |
