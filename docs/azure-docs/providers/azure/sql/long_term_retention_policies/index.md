---
title: long_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_policies
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
<tr><td><b>Name</b></td><td><code>long_term_retention_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_policies" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, policyName, resourceGroupName, serverName, subscriptionId" /> | Gets a database's long term retention policy. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a database's long term retention policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, policyName, resourceGroupName, serverName, subscriptionId" /> | Set or update a database's long term retention policy. |
