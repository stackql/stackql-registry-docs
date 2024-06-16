---
title: hyperv_sites_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - hyperv_sites_controller
  - migrate
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
<tr><td><b>Name</b></td><td><code>hyperv_sites_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.hyperv_sites_controller" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of VMwareSiteResource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get a HypervSite |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Create a HypervSite |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Delete a HypervSite |
| <CopyableCode code="compute_error_summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get site error summary. |
| <CopyableCode code="computeusage" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get a hyperv site usage. |
| <CopyableCode code="export_applications" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing<br />            machine and the deep discovery of the application installed in the machine. |
| <CopyableCode code="export_machine_errors" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing <br />            machine and the errors encountered during guest discovery of the machine. |
| <CopyableCode code="summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get site usage. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Update a HypervSite |
