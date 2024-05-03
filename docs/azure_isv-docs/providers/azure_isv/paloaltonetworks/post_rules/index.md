---
title: post_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - post_rules
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
<tr><td><b>Name</b></td><td><code>post_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.post_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | definition of rule |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName, priority" /> | Get a PostRulesResource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | List PostRulesResource resources by Tenant |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="globalRulestackName, priority, data__properties" /> | Create a PostRulesResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="globalRulestackName, priority" /> | Delete a PostRulesResource |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="globalRulestackName" /> | List PostRulesResource resources by Tenant |
| <CopyableCode code="refresh_counters" /> | `EXEC` | <CopyableCode code="globalRulestackName, priority" /> | Refresh counters |
| <CopyableCode code="reset_counters" /> | `EXEC` | <CopyableCode code="globalRulestackName, priority" /> | Reset counters |
