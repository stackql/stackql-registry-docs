---
title: tomcat_web_applications_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - tomcat_web_applications_controller
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
<tr><td><b>Name</b></td><td><code>tomcat_web_applications_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.tomcat_web_applications_controller" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName, webApplicationName" /> | Method to get an Tomcat web application. |
| <CopyableCode code="list_by_web_app_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName" /> | Method to get all Tomcat web application. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, webAppSiteName, webApplicationName" /> | Updates the Tomcat web application tags. |
