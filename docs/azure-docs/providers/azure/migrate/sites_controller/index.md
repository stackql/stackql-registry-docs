---
title: sites_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_controller
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
<tr><td><b>Name</b></td><td><code>sites_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sites_controller" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of SiteResource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Get a VmwareSite |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the vmware sites in the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the vmware sites in the subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Create a VmwareSite |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Delete a VmwareSite |
| <CopyableCode code="compute_error_summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get site error summary. |
| <CopyableCode code="computeusage" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get site error summary. |
| <CopyableCode code="export_applications" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing<br />            machine and the deep discovery of the application installed in the machine. |
| <CopyableCode code="export_machine_errors" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing <br />            machine and the errors encountered during guest discovery of the machine. |
| <CopyableCode code="export_machines" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to generate report containing <br />            machine and the deep discovery of the application installed in the machine. |
| <CopyableCode code="summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get site usage/summary. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Update a VmwareSite |
