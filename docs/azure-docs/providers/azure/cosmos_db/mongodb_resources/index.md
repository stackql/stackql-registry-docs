---
title: mongodb_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - mongodb_resources
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

Creates, updates, deletes, gets or lists a <code>mongodb_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mongodb_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.mongodb_resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="migrate_mongodb_collection_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, collectionName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB MongoDB collection from manual throughput to autoscale |
| <CopyableCode code="migrate_mongodb_collection_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, collectionName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB MongoDB collection from autoscale to manual throughput |
| <CopyableCode code="migrate_mongodb_database_to_autoscale" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB MongoDB database from manual throughput to autoscale |
| <CopyableCode code="migrate_mongodb_database_to_manual_throughput" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Migrate an Azure Cosmos DB MongoDB database from autoscale to manual throughput |
| <CopyableCode code="mongodb_container_redistribute_throughput" /> | `EXEC` | <CopyableCode code="accountName, collectionName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Redistribute throughput for an Azure Cosmos DB MongoDB container |
| <CopyableCode code="mongodb_container_retrieve_throughput_distribution" /> | `EXEC` | <CopyableCode code="accountName, collectionName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Retrieve throughput distribution for an Azure Cosmos DB MongoDB container |
| <CopyableCode code="mongodb_database_partition_merge" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Merges the partitions of a MongoDB database |
| <CopyableCode code="mongodb_database_redistribute_throughput" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Redistribute throughput for an Azure Cosmos DB MongoDB database |
| <CopyableCode code="mongodb_database_retrieve_throughput_distribution" /> | `EXEC` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Retrieve throughput distribution for an Azure Cosmos DB MongoDB database |
| <CopyableCode code="retrieve_continuous_backup_information" /> | `EXEC` | <CopyableCode code="accountName, collectionName, databaseName, resourceGroupName, subscriptionId" /> | Retrieves continuous backup information for a Mongodb collection. |
