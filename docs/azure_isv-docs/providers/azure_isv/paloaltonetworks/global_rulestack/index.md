---
title: global_rulestack
hide_title: false
hide_table_of_contents: false
keywords:
  - global_rulestack
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
<tr><td><b>Name</b></td><td><code>global_rulestack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.global_rulestack" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="location" /> | `string` | Global Location |
| <CopyableCode code="properties" /> | `object` | PAN Rulestack Describe Object |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | Get a GlobalRulestackResource |
| <CopyableCode code="list" /> | `SELECT` |  | List GlobalRulestackResource resources by Tenant |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="globalRulestackName, data__location, data__properties" /> | Create a GlobalRulestackResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="globalRulestackName" /> | Delete a GlobalRulestackResource |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="globalRulestackName" /> | Commit rulestack configuration |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="globalRulestackName" /> | Revert rulestack configuration |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="globalRulestackName" /> | Update a GlobalRulestackResource |
