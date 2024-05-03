---
title: custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domains
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
<tr><td><b>Name</b></td><td><code>custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.custom_domains" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Get the custom domain of one lifecycle application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | List the custom domains of one lifecycle application. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Create or update custom domain of one lifecycle application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Delete the custom domain of one lifecycle application. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | List the custom domains of one lifecycle application. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="appName, domainName, resourceGroupName, serviceName, subscriptionId" /> | Update custom domain of one lifecycle application. |
