---
title: firewalls_log_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls_log_profile
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
<tr><td><b>Name</b></td><td><code>firewalls_log_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.firewalls_log_profile" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applicationInsights" /> | `object` | Application Insights key |
| <CopyableCode code="commonDestination" /> | `object` | Log Destination |
| <CopyableCode code="decryptLogDestination" /> | `object` | Log Destination |
| <CopyableCode code="logOption" /> | `string` | Log options possible |
| <CopyableCode code="logType" /> | `string` | Possible log types |
| <CopyableCode code="threatLogDestination" /> | `object` | Log Destination |
| <CopyableCode code="trafficLogDestination" /> | `object` | Log Destination |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> |
