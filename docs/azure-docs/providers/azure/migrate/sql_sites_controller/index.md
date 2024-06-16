---
title: sql_sites_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_sites_controller
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
<tr><td><b>Name</b></td><td><code>sql_sites_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_sites_controller" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Method to get a site. |
| <CopyableCode code="list_by_master_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Method to get all sites. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Method to create a SQL site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Deletes the SQL site. |
| <CopyableCode code="error_summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Method to get error summary from SQL site. |
| <CopyableCode code="export_sql_server_errors" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Method to generate report containing SQL servers. |
| <CopyableCode code="export_sql_servers" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Method to generate report containing SQL servers. |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Method to refresh a site. |
| <CopyableCode code="summary" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Method to get site usage/summary. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Method to update an existing site. |
