---
title: application_live_views
hide_title: false
hide_table_of_contents: false
keywords:
  - application_live_views
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>application_live_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.application_live_views" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationLiveViewName, resourceGroupName, serviceName, subscriptionId" /> | Get the Application Live  and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationLiveViewName, resourceGroupName, serviceName, subscriptionId" /> | Create the default Application Live View or update the existing Application Live View. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationLiveViewName, resourceGroupName, serviceName, subscriptionId" /> | Disable the default Application Live View. |
