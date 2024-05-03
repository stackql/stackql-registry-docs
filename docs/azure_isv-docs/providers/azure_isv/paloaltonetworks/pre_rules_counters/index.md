---
title: pre_rules_counters
hide_title: false
hide_table_of_contents: false
keywords:
  - pre_rules_counters
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
<tr><td><b>Name</b></td><td><code>pre_rules_counters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.pre_rules_counters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="appSeen" /> | `object` | Data Type for App Seen |
| <CopyableCode code="firewallName" /> | `string` | firewall name |
| <CopyableCode code="hitCount" /> | `integer` | hit count |
| <CopyableCode code="lastUpdatedTimestamp" /> | `string` | last updated timestamp |
| <CopyableCode code="priority" /> | `string` | priority number |
| <CopyableCode code="requestTimestamp" /> | `string` | timestamp of request |
| <CopyableCode code="ruleListName" /> | `string` | rule list name |
| <CopyableCode code="ruleName" /> | `string` | rule name |
| <CopyableCode code="ruleStackName" /> | `string` | rule Stack Name |
| <CopyableCode code="timestamp" /> | `string` | timestamp of response |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName, priority" /> |
