---
title: tag_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_rules
  - newrelic
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
<tr><td><b>Name</b></td><td><code>tag_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.newrelic.tag_rules" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subscriptionId" /> | Get a TagRule |
| <CopyableCode code="list_by_new_relic_monitor_resource" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | List TagRule resources by NewRelicMonitorResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subscriptionId, data__properties" /> | Create a TagRule |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subscriptionId" /> | Delete a TagRule |
| <CopyableCode code="_list_by_new_relic_monitor_resource" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | List TagRule resources by NewRelicMonitorResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, ruleSetName, subscriptionId" /> | Update a TagRule |
