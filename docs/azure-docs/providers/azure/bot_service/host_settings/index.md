---
title: host_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - host_settings
  - bot_service
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
<tr><td><b>Name</b></td><td><code>host_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.host_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="BotOpenIdMetadata" /> | `string` | Same as toBotFromChannelOpenIdMetadataUrl, used by SDK &lt; v4.12 |
| <CopyableCode code="OAuthUrl" /> | `string` | For in-conversation bot user authentication |
| <CopyableCode code="ToBotFromChannelOpenIdMetadataUrl" /> | `string` | For verifying incoming tokens from the channels |
| <CopyableCode code="ToBotFromChannelTokenIssuer" /> | `string` | For verifying incoming tokens from the channels |
| <CopyableCode code="ToBotFromEmulatorOpenIdMetadataUrl" /> | `string` | For verifying incoming tokens from bot emulator |
| <CopyableCode code="ToChannelFromBotLoginUrl" /> | `string` | For getting access token to channels from bot host |
| <CopyableCode code="ToChannelFromBotOAuthScope" /> | `string` | For getting access token to channels from bot host |
| <CopyableCode code="ValidateAuthority" /> | `boolean` | Per cloud OAuth setting on whether authority is validated |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
