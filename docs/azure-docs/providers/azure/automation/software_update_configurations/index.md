---
title: software_update_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configurations
  - automation
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
<tr><td><b>Name</b></td><td><code>software_update_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.software_update_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id of the software update configuration |
| <CopyableCode code="name" /> | `string` | Name of the software update configuration. |
| <CopyableCode code="properties" /> | `object` | Software update configuration collection item properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Get all software update configurations for the account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId, data__properties" /> | Create a new software update configuration with the name given in the URI. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId" /> | delete a specific software update configuration. |
| <CopyableCode code="get_by_name" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId" /> | Get a single software update configuration by name. |
