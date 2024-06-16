---
title: time_series_database_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - time_series_database_connections
  - digital_twins
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
<tr><td><b>Name</b></td><td><code>time_series_database_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digital_twins.time_series_database_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | Extension resource name. |
| <CopyableCode code="properties" /> | `object` | Properties of a time series database connection resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId, timeSeriesDatabaseConnectionName" /> | Get the description of an existing time series database connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Get all existing time series database connections for this DigitalTwins instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId, timeSeriesDatabaseConnectionName" /> | Create or update a time series database connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId, timeSeriesDatabaseConnectionName" /> | Delete a time series database connection. |
