---
title: sql_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_resources
  - cosmos_db
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>sql_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.sql_resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="migrate_sql_container_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB SQL container from manual throughput to autoscale |
| <CopyableCode code="migrate_sql_container_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB SQL container from autoscale to manual throughput |
| <CopyableCode code="migrate_sql_database_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB SQL database from manual throughput to autoscale |
| <CopyableCode code="migrate_sql_database_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB SQL database from autoscale to manual throughput |
| <CopyableCode code="retrieve_continuous_backup_information" /> | `EXEC` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, subscriptionId" /> | Retrieves continuous backup information for a container resource. |
| <CopyableCode code="sql_container_redistribute_throughput" /> | `EXEC` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Redistribute throughput for an Azure Cosmos DB SQL container |
| <CopyableCode code="sql_container_retrieve_throughput_distribution" /> | `EXEC` | <CopyableCode code="accountName, containerName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Retrieve throughput distribution for an Azure Cosmos DB SQL container |
| <CopyableCode code="sql_database_partition_merge" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Merges the partitions of a SQL database |
| <CopyableCode code="sql_database_redistribute_throughput" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Redistribute throughput for an Azure Cosmos DB SQL database |
| <CopyableCode code="sql_database_retrieve_throughput_distribution" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Retrieve throughput distribution for an Azure Cosmos DB SQL database |
