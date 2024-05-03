---
title: test_lines
hide_title: false
hide_table_of_contents: false
keywords:
  - test_lines
  - voice_services
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
<tr><td><b>Name</b></td><td><code>test_lines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.voice_services.test_lines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the TestLine resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId, testLineName" /> | Get a TestLine |
| <CopyableCode code="list_by_communications_gateway" /> | `SELECT` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId" /> | List TestLine resources by CommunicationsGateway |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId, testLineName" /> | Create a TestLine |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId, testLineName" /> | Delete a TestLine |
| <CopyableCode code="_list_by_communications_gateway" /> | `EXEC` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId" /> | List TestLine resources by CommunicationsGateway |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="communicationsGatewayName, resourceGroupName, subscriptionId, testLineName" /> | Update a TestLine |
