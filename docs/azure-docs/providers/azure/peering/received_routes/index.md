---
title: received_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - received_routes
  - peering
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
<tr><td><b>Name</b></td><td><code>received_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.received_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="asPath" /> | `string` | The AS path for the prefix. |
| <CopyableCode code="nextHop" /> | `string` | The next hop for the prefix. |
| <CopyableCode code="originAsValidationState" /> | `string` | The origin AS change information for the prefix. |
| <CopyableCode code="prefix" /> | `string` | The prefix. |
| <CopyableCode code="receivedTimestamp" /> | `string` | The received timestamp associated with the prefix. |
| <CopyableCode code="rpkiValidationState" /> | `string` | The RPKI validation state for the prefix and origin AS that's listed in the AS path. |
| <CopyableCode code="trustAnchor" /> | `string` | The authority which holds the Route Origin Authorization record for the prefix, if any. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_peering" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> |
