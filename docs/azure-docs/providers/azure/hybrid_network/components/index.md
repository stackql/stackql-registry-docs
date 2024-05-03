---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
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
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.components" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="componentName, networkFunctionName, resourceGroupName, subscriptionId" /> | Gets information about the specified application instance resource. |
| <CopyableCode code="list_by_network_function" /> | `SELECT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Lists all the component resources in a network function. |
| <CopyableCode code="_list_by_network_function" /> | `EXEC` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Lists all the component resources in a network function. |
