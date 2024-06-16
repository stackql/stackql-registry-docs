---
title: servers_controller_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_controller_machine
  - migrate
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
<tr><td><b>Name</b></td><td><code>servers_controller_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.servers_controller_machine" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Get a Server |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Delete a Server |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Update a Server machine |
