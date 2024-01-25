---
title: kafka_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - kafka_configurations
  - purview
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kafka_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.purview.kafka_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the identifier. |
| `name` | `string` | Gets or sets the name. |
| `properties` | `object` | The kafka configuration properties of the event streaming service attached to the Purview account for kafka notifications. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Gets or sets the type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, kafkaConfigurationName, resourceGroupName, subscriptionId` | Gets the kafka configuration for the account |
| `list_by_account` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Kafka configurations in the Account |
| `create_or_update` | `INSERT` | `accountName, api-version, kafkaConfigurationName, resourceGroupName, subscriptionId` | Create or update Kafka Configuration |
| `delete` | `DELETE` | `accountName, api-version, kafkaConfigurationName, resourceGroupName, subscriptionId` | Deletes a KafkaConfiguration resource. |
| `_list_by_account` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Kafka configurations in the Account |
