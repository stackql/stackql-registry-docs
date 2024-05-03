---
title: update_strategies
hide_title: false
hide_table_of_contents: false
keywords:
  - update_strategies
  - fleet
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
<tr><td><b>Name</b></td><td><code>update_strategies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fleet.update_strategies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="properties" /> | `object` | The properties of the UpdateStrategy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateStrategyName" /> | Get a FleetUpdateStrategy |
| <CopyableCode code="list_by_fleet" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | List FleetUpdateStrategy resources by Fleet |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateStrategyName" /> | Create a FleetUpdateStrategy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateStrategyName" /> | Delete a FleetUpdateStrategy |
| <CopyableCode code="_list_by_fleet" /> | `EXEC` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | List FleetUpdateStrategy resources by Fleet |
