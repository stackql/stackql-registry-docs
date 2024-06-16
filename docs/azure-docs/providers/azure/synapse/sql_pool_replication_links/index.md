---
title: sql_pool_replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_replication_links
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_replication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_replication_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Location of the workspace that contains this firewall rule. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of a Sql pool replication link. |
| <CopyableCode code="type" /> | `string` | Type of resource this is. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Lists a Sql pool's replication links. |
| <CopyableCode code="get_by_name" /> | `EXEC` | <CopyableCode code="linkId, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get SQL pool replication link by name. |
