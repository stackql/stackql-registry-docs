---
title: security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_settings
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
<tr><td><b>Name</b></td><td><code>security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.security_settings" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, securitySettingsName, subscriptionId" /> | Get a SecuritySetting |
| <CopyableCode code="list_by_clusters" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List SecuritySetting resources by Clusters |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, securitySettingsName, subscriptionId" /> | Create a security setting |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, securitySettingsName, subscriptionId" /> | Delete a SecuritySetting |
