---
title: sap_landscape_monitor
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_landscape_monitor
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
<tr><td><b>Name</b></td><td><code>sap_landscape_monitor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_landscape_monitor" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Gets configuration values for Single Pane Of Glass for SAP monitor for the specified subscription, resource group, and resource name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Deletes a SAP Landscape Monitor Dashboard with the specified subscription, resource group, and SAP monitor name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Patches the SAP Landscape Monitor Dashboard for the specified subscription, resource group, and SAP monitor name. |
