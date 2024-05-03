---
title: network_function_definition_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_function_definition_versions
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
<tr><td><b>Name</b></td><td><code>network_function_definition_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.network_function_definition_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network function definition version properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a network function definition version. |
| <CopyableCode code="list_by_network_function_definition_group" /> | `SELECT` | <CopyableCode code="networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a list of network function definition versions under a network function definition group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a network function definition version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Deletes the specified network function definition version. |
| <CopyableCode code="_list_by_network_function_definition_group" /> | `EXEC` | <CopyableCode code="networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about a list of network function definition versions under a network function definition group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId" /> | Updates a network function definition version resource. |
