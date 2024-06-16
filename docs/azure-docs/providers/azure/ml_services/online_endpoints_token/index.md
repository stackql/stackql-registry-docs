---
title: online_endpoints_token
hide_title: false
hide_table_of_contents: false
keywords:
  - online_endpoints_token
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
<tr><td><b>Name</b></td><td><code>online_endpoints_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.online_endpoints_token" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessToken" /> | `string` | Access token for endpoint authentication. |
| <CopyableCode code="expiryTimeUtc" /> | `integer` | Access token expiry time (UTC). |
| <CopyableCode code="refreshAfterTimeUtc" /> | `integer` | Refresh access token after time (UTC). |
| <CopyableCode code="tokenType" /> | `string` | Access token type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, resourceGroupName, subscriptionId, workspaceName" /> |
