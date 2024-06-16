---
title: fqdn_list_local_rulestack
hide_title: false
hide_table_of_contents: false
keywords:
  - fqdn_list_local_rulestack
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
<tr><td><b>Name</b></td><td><code>fqdn_list_local_rulestack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.fqdn_list_local_rulestack" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | fqdn object |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="localRulestackName, name, resourceGroupName, subscriptionId" /> | Get a FqdnListLocalRulestackResource |
| <CopyableCode code="list_by_local_rulestacks" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | List FqdnListLocalRulestackResource resources by LocalRulestacks |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="localRulestackName, name, resourceGroupName, subscriptionId, data__properties" /> | Create a FqdnListLocalRulestackResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="localRulestackName, name, resourceGroupName, subscriptionId" /> | Delete a FqdnListLocalRulestackResource |
