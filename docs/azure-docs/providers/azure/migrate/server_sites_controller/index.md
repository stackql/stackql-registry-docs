---
title: server_sites_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - server_sites_controller
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
<tr><td><b>Name</b></td><td><code>server_sites_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.server_sites_controller" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of SiteResource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get a ServerSiteResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List ServerSiteResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List ServerSiteResource resources by subscription ID |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Create a ServerSiteResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Delete a ServerSiteResource |
| <CopyableCode code="compute_error_summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get the error summary for a server site. |
| <CopyableCode code="computeusage" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get a serve site usage. |
| <CopyableCode code="export_applications" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing<br />            machine and the deep discovery of the application installed in the machine. |
| <CopyableCode code="export_machine_errors" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing <br />            machine and the errors encountered during guest discovery of the machine. |
| <CopyableCode code="refresh_site" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Operation to refresh a site |
| <CopyableCode code="summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get site usage. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Update a ServerSiteResource |
