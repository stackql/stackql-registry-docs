---
title: config_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - config_servers
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
<tr><td><b>Name</b></td><td><code>config_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.config_servers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Get the config server and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all config server resources in a Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Disable the default Config Server, only available in Enterprise Plan. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Check if the config server settings are valid. |
