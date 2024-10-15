---
title: direct_lines
hide_title: false
hide_table_of_contents: false
keywords:
  - direct_lines
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

Creates, updates, deletes, gets or lists a <code>direct_lines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>direct_lines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.direct_lines" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="channelName, resourceGroupName, resourceName, subscriptionId, data__key, data__siteName" /> | Regenerates secret keys and returns them for the DirectLine Channel of a particular BotService resource |
