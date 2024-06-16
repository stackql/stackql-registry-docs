---
title: gremlin_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - gremlin_resources
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>gremlin_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.gremlin_resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="migrate_gremlin_database_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB Gremlin database from manual throughput to autoscale |
| <CopyableCode code="migrate_gremlin_database_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB Gremlin database from autoscale to manual throughput |
| <CopyableCode code="migrate_gremlin_graph_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, databaseName, graphName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB Gremlin graph from manual throughput to autoscale |
| <CopyableCode code="migrate_gremlin_graph_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, databaseName, graphName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB Gremlin graph from autoscale to manual throughput |
| <CopyableCode code="retrieve_continuous_backup_information" /> | `EXEC` | <CopyableCode code="accountName, databaseName, graphName, resourceGroupName, subscriptionId" /> | Retrieves continuous backup information for a gremlin graph. |
