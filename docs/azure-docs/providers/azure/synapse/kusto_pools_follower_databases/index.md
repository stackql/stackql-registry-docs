---
title: kusto_pools_follower_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pools_follower_databases
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
<tr><td><b>Name</b></td><td><code>kusto_pools_follower_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pools_follower_databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attachedDatabaseConfigurationName" /> | `string` | Resource name of the attached database configuration in the follower cluster. |
| <CopyableCode code="clusterResourceId" /> | `string` | Resource id of the cluster that follows a database owned by this cluster. |
| <CopyableCode code="databaseName" /> | `string` | The database name owned by this cluster that was followed. * in case following all databases. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> |
