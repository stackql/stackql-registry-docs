---
title: applications_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_tokens
  - managed_applications
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
<tr><td><b>Name</b></td><td><code>applications_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.applications_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessToken" /> | `string` | The requested access token. |
| <CopyableCode code="authorizationAudience" /> | `string` | The aud (audience) the access token was request for. This is the same as what was provided in the listTokens request. |
| <CopyableCode code="expiresIn" /> | `string` | The number of seconds the access token will be valid. |
| <CopyableCode code="expiresOn" /> | `string` | The timespan when the access token expires. This is represented as the number of seconds from epoch. |
| <CopyableCode code="notBefore" /> | `string` | The timespan when the access token takes effect. This is represented as the number of seconds from epoch. |
| <CopyableCode code="resourceId" /> | `string` | The Azure resource ID for the issued token. This is either the managed application ID or the user-assigned identity ID. |
| <CopyableCode code="tokenType" /> | `string` | The type of the token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> |
