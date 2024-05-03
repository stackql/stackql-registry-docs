---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - communication
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | A class that describes the properties of the CommunicationService. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communicationServiceName, resourceGroupName, subscriptionId" /> | Get the CommunicationService and its properties. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Handles requests to list all resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Handles requests to list all resources in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="communicationServiceName, resourceGroupName, subscriptionId" /> | Create a new CommunicationService or update an existing CommunicationService. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="communicationServiceName, resourceGroupName, subscriptionId" /> | Operation to delete a CommunicationService. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Handles requests to list all resources in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Handles requests to list all resources in a subscription. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks that the CommunicationService name is valid and is not already in use. |
| <CopyableCode code="link_notification_hub" /> | `EXEC` | <CopyableCode code="communicationServiceName, resourceGroupName, subscriptionId, data__connectionString, data__resourceId" /> | Links an Azure Notification Hub to this communication service. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="communicationServiceName, resourceGroupName, subscriptionId" /> | Regenerate CommunicationService access key. PrimaryKey and SecondaryKey cannot be regenerated at the same time. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="communicationServiceName, resourceGroupName, subscriptionId" /> | Operation to update an existing CommunicationService. |
