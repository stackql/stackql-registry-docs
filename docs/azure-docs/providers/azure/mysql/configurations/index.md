---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.configurations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, resourceGroupName, serverName, subscriptionId" /> | Gets information about a configuration of server. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the configurations in a given server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationName, resourceGroupName, serverName, subscriptionId" /> | Updates a configuration of a server. |
| <CopyableCode code="batch_update" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Update a list of configurations in a given server. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="configurationName, resourceGroupName, serverName, subscriptionId" /> | Updates a configuration of a server. |
