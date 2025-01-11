---
title: scripts_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts_list_only
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>scripts</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/scripts/"><code>scripts</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scripts_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Script resource creates a new script record for your Realtime Servers script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.scripts_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A unique identifier for the Realtime script</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>scripts</code> in a region.
```sql
SELECT
region,
id
FROM aws.gamelift.scripts_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>scripts_list_only</code> resource, see <a href="/providers/aws/gamelift/scripts/#permissions"><code>scripts</code></a>

