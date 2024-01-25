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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.bot_service.host_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `BotOpenIdMetadata` | `string` | Same as toBotFromChannelOpenIdMetadataUrl, used by SDK &lt; v4.12 |
| `OAuthUrl` | `string` | For in-conversation bot user authentication |
| `ToBotFromChannelOpenIdMetadataUrl` | `string` | For verifying incoming tokens from the channels |
| `ToBotFromChannelTokenIssuer` | `string` | For verifying incoming tokens from the channels |
| `ToBotFromEmulatorOpenIdMetadataUrl` | `string` | For verifying incoming tokens from bot emulator |
| `ToChannelFromBotLoginUrl` | `string` | For getting access token to channels from bot host |
| `ToChannelFromBotOAuthScope` | `string` | For getting access token to channels from bot host |
| `ValidateAuthority` | `boolean` | Per cloud OAuth setting on whether authority is validated |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `subscriptionId` |
