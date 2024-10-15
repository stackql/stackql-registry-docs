---
title: bots_check_name_availabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - bots_check_name_availabilities
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

Creates, updates, deletes, gets or lists a <code>bots_check_name_availabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bots_check_name_availabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.bots_check_name_availabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="absCode" /> | `string` | response code from ABS |
| <CopyableCode code="message" /> | `string` | additional message from the bot management api showing why a bot name is not available |
| <CopyableCode code="valid" /> | `boolean` | indicates if the bot name is valid. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Check whether a bot name is available. |

## `SELECT` examples

Check whether a bot name is available.


```sql
SELECT
absCode,
message,
valid
FROM azure.bot_service.bots_check_name_availabilities
;
```