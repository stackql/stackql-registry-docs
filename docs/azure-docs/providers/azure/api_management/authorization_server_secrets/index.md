---
title: authorization_server_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_server_secrets
  - api_management
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
<tr><td><b>Name</b></td><td><code>authorization_server_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_server_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clientSecret" /> | `string` | oAuth Authorization Server Secrets. |
| <CopyableCode code="resourceOwnerPassword" /> | `string` | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password. |
| <CopyableCode code="resourceOwnerUsername" /> | `string` | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="authsid, resourceGroupName, serviceName, subscriptionId" /> |
