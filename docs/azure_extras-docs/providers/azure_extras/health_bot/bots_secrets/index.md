---
title: bots_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - bots_secrets
  - health_bot
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

Creates, updates, deletes, gets or lists a <code>bots_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bots_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.health_bot.bots_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="secrets" /> | `array` | Array of Azure Health Bot Secrets. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="botName, resourceGroupName, subscriptionId" /> | List all secrets of a HealthBot. |

## `SELECT` examples

List all secrets of a HealthBot.


```sql
SELECT
secrets
FROM azure_extras.health_bot.bots_secrets
WHERE botName = '{{ botName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```