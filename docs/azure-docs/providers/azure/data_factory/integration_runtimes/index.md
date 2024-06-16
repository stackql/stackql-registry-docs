---
title: integration_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes
  - data_factory
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
<tr><td><b>Name</b></td><td><code>integration_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.integration_runtimes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | Azure Data Factory nested object which serves as a compute resource for activities. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Gets an integration runtime. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Lists integration runtimes. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an integration runtime. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Deletes an integration runtime. |
| <CopyableCode code="regenerate_auth_key" /> | `EXEC` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Regenerates the authentication key for an integration runtime. |
| <CopyableCode code="remove_links" /> | `EXEC` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId, data__factoryName" /> | Remove all linked integration runtimes under specific data factory in a self-hosted integration runtime. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Starts a ManagedReserved type integration runtime. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Stops a ManagedReserved type integration runtime. |
| <CopyableCode code="sync_credentials" /> | `EXEC` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Force the integration runtime to synchronize credentials across integration runtime nodes, and this will override the credentials across all worker nodes with those available on the dispatcher node. If you already have the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime node than using this API directly. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Updates an integration runtime. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Upgrade self-hosted integration runtime to latest version if availability. |
