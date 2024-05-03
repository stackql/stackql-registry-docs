---
title: sap_database_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_database_instances
  - sap_workloads
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
<tr><td><b>Name</b></td><td><code>sap_database_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_database_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the Database properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Gets the SAP Database Instance resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Lists the Database resources associated with a Virtual Instance for SAP solutions resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Creates the Database resource corresponding to the Virtual Instance for SAP solutions resource. &lt;br&gt;&lt;br&gt;This will be used by service only. PUT by end user will return a Bad Request error. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Deletes the Database resource corresponding to a Virtual Instance for SAP solutions resource. &lt;br&gt;&lt;br&gt;This will be used by service only. Delete by end user will return a Bad Request error. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Lists the Database resources associated with a Virtual Instance for SAP solutions resource. |
| <CopyableCode code="start_instance" /> | `EXEC` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Starts the database instance of the SAP system. |
| <CopyableCode code="stop_instance" /> | `EXEC` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Stops the database instance of the SAP system. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="databaseInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Updates the Database resource. |
