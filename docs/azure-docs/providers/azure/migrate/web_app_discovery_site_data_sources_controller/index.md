---
title: web_app_discovery_site_data_sources_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - web_app_discovery_site_data_sources_controller
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
<tr><td><b>Name</b></td><td><code>web_app_discovery_site_data_sources_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.web_app_discovery_site_data_sources_controller" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get a Web app data source in site. |
| <CopyableCode code="list_by_web_app_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get all Web app data sources in site. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to create or update a Web app data source in site. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="discoverySiteDataSourceName, resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to delete a Web app data source in site. |
