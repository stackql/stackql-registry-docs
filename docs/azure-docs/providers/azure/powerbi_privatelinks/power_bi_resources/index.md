---
title: power_bi_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - power_bi_resources
  - powerbi_privatelinks
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
<tr><td><b>Name</b></td><td><code>power_bi_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_privatelinks.power_bi_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the resource. |
| <CopyableCode code="location" /> | `string` | Specifies the location of the resource. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Specifies the tags of the resource. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_resource_name" /> | `SELECT` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Gets all the private link resources for the given Azure resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Creates or updates a Private Link Service Resource for Power BI. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Deletes a Private Link Service Resource for Power BI. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Creates or updates a Private Link Service Resource for Power BI. |
