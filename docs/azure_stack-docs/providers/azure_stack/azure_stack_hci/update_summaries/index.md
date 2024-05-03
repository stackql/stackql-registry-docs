---
title: update_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - update_summaries
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>update_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.update_summaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of Update summaries |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get all Update summaries under the HCI cluster |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete Update Summaries |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Put Update summaries under the HCI cluster |
