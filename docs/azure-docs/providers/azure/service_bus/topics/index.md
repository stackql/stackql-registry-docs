---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - service_bus
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_bus.topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The Topic Properties definition. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, topicName" /> | Returns a description for the specified topic. |
| <CopyableCode code="list_by_namespace" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Gets all the topics in a namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, topicName" /> | Creates a topic in the specified namespace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, topicName" /> | Deletes a topic from the specified namespace and resource group. |
| <CopyableCode code="_list_by_namespace" /> | `EXEC` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Gets all the topics in a namespace. |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, topicName, data__keyType" /> | Regenerates primary or secondary connection strings for the topic. |
