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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kafka_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.kafka_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the identifier. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="properties" /> | `object` | The kafka configuration properties of the event streaming service attached to the Purview account for kafka notifications. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, kafkaConfigurationName, resourceGroupName, subscriptionId" /> | Gets the kafka configuration for the account |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists the Kafka configurations in the Account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, api-version, kafkaConfigurationName, resourceGroupName, subscriptionId" /> | Create or update Kafka Configuration |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, kafkaConfigurationName, resourceGroupName, subscriptionId" /> | Deletes a KafkaConfiguration resource. |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists the Kafka configurations in the Account |
