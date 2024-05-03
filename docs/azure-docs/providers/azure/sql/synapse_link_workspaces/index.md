---
title: synapse_link_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - synapse_link_workspaces
  - sql
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
<tr><td><b>Name</b></td><td><code>synapse_link_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.synapse_link_workspaces" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> |
| <CopyableCode code="_list_by_database" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> |
