---
title: local_rulestacks
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rulestacks
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>local_rulestacks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.local_rulestacks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | PAN Rulestack Describe Object |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Get a LocalRulestackResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List LocalRulestackResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List LocalRulestackResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId, data__properties" /> | Create a LocalRulestackResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Delete a LocalRulestackResource |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List LocalRulestackResource resources by resource group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List LocalRulestackResource resources by subscription ID |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Commit rulestack configuration |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Revert rulestack configuration |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | Update a LocalRulestackResource |
