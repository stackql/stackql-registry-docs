---
title: racks
hide_title: false
hide_table_of_contents: false
keywords:
  - racks
  - nexus
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
<tr><td><b>Name</b></td><td><code>racks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.racks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="rackName, resourceGroupName, subscriptionId" /> | Get properties of the provided rack. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of racks in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of racks in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="rackName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new rack or update properties of the existing one.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="rackName, resourceGroupName, subscriptionId" /> | Delete the provided rack.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="rackName, resourceGroupName, subscriptionId" /> | Patch properties of the provided rack, or update the tags associated with the rack. Properties and tag updates can be done independently. |
