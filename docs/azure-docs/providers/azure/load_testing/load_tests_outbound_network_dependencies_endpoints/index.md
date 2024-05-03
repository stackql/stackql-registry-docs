---
title: load_tests_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - load_tests_outbound_network_dependencies_endpoints
  - load_testing
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
<tr><td><b>Name</b></td><td><code>load_tests_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.load_testing.load_tests_outbound_network_dependencies_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="category" /> | `string` | The type of service that Azure Load Testing connects to. |
| <CopyableCode code="endpoints" /> | `array` | The endpoints for this service to which the Batch service makes outbound calls. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> |
