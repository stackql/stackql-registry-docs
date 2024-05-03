---
title: cassandra_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_resources
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
<tr><td><b>Name</b></td><td><code>cassandra_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.cassandra_resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="migrate_cassandra_keyspace_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB Cassandra Keyspace from manual throughput to autoscale |
| <CopyableCode code="migrate_cassandra_keyspace_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB Cassandra Keyspace from autoscale to manual throughput |
| <CopyableCode code="migrate_cassandra_table_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId, tableName" /> | Migrate an Azure Cosmos DB Cassandra table from manual throughput to autoscale |
| <CopyableCode code="migrate_cassandra_table_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId, tableName" /> | Migrate an Azure Cosmos DB Cassandra table from autoscale to manual throughput |
| <CopyableCode code="migrate_cassandra_view_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId, viewName" /> | Migrate an Azure Cosmos DB Cassandra view from manual throughput to autoscale |
| <CopyableCode code="migrate_cassandra_view_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, keyspaceName, resourceGroupName, subscriptionId, viewName" /> | Migrate an Azure Cosmos DB Cassandra view from autoscale to manual throughput |
