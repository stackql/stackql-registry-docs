---
title: advanced_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - advanced_threat_protection_settings
  - mysql
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
<tr><td><b>Name</b></td><td><code>advanced_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.advanced_threat_protection_settings" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId" /> | Get a server's Advanced Threat Protection state |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server's Advanced Threat Protection states. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="advancedThreatProtectionName, resourceGroupName, serverName, subscriptionId" /> | Updates a server's Advanced Threat Protection state. |
