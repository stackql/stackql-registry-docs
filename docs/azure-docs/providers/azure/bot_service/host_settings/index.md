---
title: host_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - host_settings
  - bot_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>host_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.host_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="BotOpenIdMetadata" /> | `string` | Same as toBotFromChannelOpenIdMetadataUrl, used by SDK < v4.12 |
| <CopyableCode code="OAuthUrl" /> | `string` | For in-conversation bot user authentication |
| <CopyableCode code="ToBotFromChannelOpenIdMetadataUrl" /> | `string` | For verifying incoming tokens from the channels |
| <CopyableCode code="ToBotFromChannelTokenIssuer" /> | `string` | For verifying incoming tokens from the channels |
| <CopyableCode code="ToBotFromEmulatorOpenIdMetadataUrl" /> | `string` | For verifying incoming tokens from bot emulator |
| <CopyableCode code="ToChannelFromBotLoginUrl" /> | `string` | For getting access token to channels from bot host |
| <CopyableCode code="ToChannelFromBotOAuthScope" /> | `string` | For getting access token to channels from bot host |
| <CopyableCode code="ValidateAuthority" /> | `boolean` | Per cloud OAuth setting on whether authority is validated |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get per subscription settings needed to host bot in compute resource such as Azure App Service |

## `SELECT` examples

Get per subscription settings needed to host bot in compute resource such as Azure App Service


```sql
SELECT
BotOpenIdMetadata,
OAuthUrl,
ToBotFromChannelOpenIdMetadataUrl,
ToBotFromChannelTokenIssuer,
ToBotFromEmulatorOpenIdMetadataUrl,
ToChannelFromBotLoginUrl,
ToChannelFromBotOAuthScope,
ValidateAuthority
FROM azure.bot_service.host_settings
WHERE subscriptionId = '{{ subscriptionId }}';
```