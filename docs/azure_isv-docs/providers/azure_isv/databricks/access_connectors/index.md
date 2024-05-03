---
title: access_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - access_connectors
  - databricks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>access_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.databricks.access_connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectorName, resourceGroupName, subscriptionId" /> | Gets an azure databricks accessConnector. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the azure databricks accessConnectors within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the azure databricks accessConnectors within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectorName, resourceGroupName, subscriptionId" /> | Creates or updates azure databricks accessConnector. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectorName, resourceGroupName, subscriptionId" /> | Deletes the azure databricks accessConnector. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the azure databricks accessConnectors within a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets all the azure databricks accessConnectors within a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="connectorName, resourceGroupName, subscriptionId" /> | Updates an azure databricks accessConnector. |
