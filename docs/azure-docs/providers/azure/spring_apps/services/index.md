---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - spring_apps
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `string` | The GEO location of the resource. |
| <CopyableCode code="properties" /> | `object` | Service properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
| <CopyableCode code="tags" /> | `object` | Tags of the service which is a list of key value pairs that describe the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get a Service and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Handles requests to list all resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Handles requests to list all resources in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Create a new Service or update an exiting Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Service. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks that the resource name is valid and is not already in use. |
| <CopyableCode code="disable_apm_globally" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__resourceId" /> | Disable an APM globally. |
| <CopyableCode code="disable_test_endpoint" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Disable test endpoint functionality for a Service. |
| <CopyableCode code="enable_apm_globally" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__resourceId" /> | Enable an APM globally. |
| <CopyableCode code="enable_test_endpoint" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Enable test endpoint functionality for a Service. |
| <CopyableCode code="flush_vnet_dns_setting" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Flush Virtual Network DNS settings for a VNET injected Service. |
| <CopyableCode code="regenerate_test_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__keyType" /> | Regenerate a test key for a Service. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Start a Service. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Stop a Service. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Operation to update an exiting Service. |
