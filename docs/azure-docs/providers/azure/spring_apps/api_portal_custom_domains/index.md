---
title: api_portal_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - api_portal_custom_domains
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
<tr><td><b>Name</b></td><td><code>api_portal_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.api_portal_custom_domains" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Get the API portal custom domain. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiPortalName, resourceGroupName, serviceName, subscriptionId" /> | Handle requests to list all API portal custom domains. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Create or update the API portal custom domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Delete the API portal custom domain. |
