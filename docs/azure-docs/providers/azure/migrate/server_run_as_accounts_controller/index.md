---
title: server_run_as_accounts_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - server_run_as_accounts_controller
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
<tr><td><b>Name</b></td><td><code>server_run_as_accounts_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.server_run_as_accounts_controller" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, siteName, subscriptionId" /> | Get a ServerRunAsAccount |
| <CopyableCode code="list_by_server_site_resource" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List ServerRunAsAccount resources by ServerSiteResource |
