---
title: sql_discovery_site_data_source_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_discovery_site_data_source_controller
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
<tr><td><b>Name</b></td><td><code>sql_discovery_site_data_source_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_discovery_site_data_source_controller" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Get a SqlDiscoverySiteDataSource |
| <CopyableCode code="list_by_sql_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | List SqlDiscoverySiteDataSource resources by SqlSite |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Create a SqlDiscoverySiteDataSource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, sqlSiteName, subscriptionId" /> | Delete a SqlDiscoverySiteDataSource |
