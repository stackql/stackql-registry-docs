---
title: workspaces_notebook_access_token
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_notebook_access_token
  - ml_services
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
<tr><td><b>Name</b></td><td><code>workspaces_notebook_access_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.workspaces_notebook_access_token" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="accessToken" /> | `string` |
| <CopyableCode code="expiresIn" /> | `integer` |
| <CopyableCode code="hostName" /> | `string` |
| <CopyableCode code="notebookResourceId" /> | `string` |
| <CopyableCode code="publicDns" /> | `string` |
| <CopyableCode code="refreshToken" /> | `string` |
| <CopyableCode code="scope" /> | `string` |
| <CopyableCode code="tokenType" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
