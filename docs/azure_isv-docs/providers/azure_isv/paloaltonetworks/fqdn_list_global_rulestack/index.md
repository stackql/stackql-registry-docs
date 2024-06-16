---
title: fqdn_list_global_rulestack
hide_title: false
hide_table_of_contents: false
keywords:
  - fqdn_list_global_rulestack
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
<tr><td><b>Name</b></td><td><code>fqdn_list_global_rulestack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.fqdn_list_global_rulestack" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | fqdn object |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName, name" /> | Get a FqdnListGlobalRulestackResource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | List FqdnListGlobalRulestackResource resources by Tenant |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="globalRulestackName, name, data__properties" /> | Create a FqdnListGlobalRulestackResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="globalRulestackName, name" /> | Delete a FqdnListGlobalRulestackResource |
