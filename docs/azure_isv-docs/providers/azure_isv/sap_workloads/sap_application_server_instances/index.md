---
title: sap_application_server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_application_server_instances
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
<tr><td><b>Name</b></td><td><code>sap_application_server_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_application_server_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the SAP Application Server instance properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Gets the SAP Application Server Instance corresponding to the Virtual Instance for SAP solutions resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Lists the SAP Application Server Instance resources for a given Virtual Instance for SAP solutions resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Puts the SAP Application Server Instance resource. &lt;br&gt;&lt;br&gt;This will be used by service only. PUT by end user will return a Bad Request error. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Deletes the SAP Application Server Instance resource. &lt;br&gt;&lt;br&gt;This operation will be used by service only. Delete by end user will return a Bad Request error. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Lists the SAP Application Server Instance resources for a given Virtual Instance for SAP solutions resource. |
| <CopyableCode code="start_instance" /> | `EXEC` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Starts the SAP Application Server Instance. |
| <CopyableCode code="stop_instance" /> | `EXEC` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Stops the SAP Application Server Instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="applicationInstanceName, resourceGroupName, sapVirtualInstanceName, subscriptionId" /> | Puts the SAP Application Server Instance resource. |
