---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - transfer
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


List of Transfer family servers in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of Transfer family servers in a region</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.servers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Unique Amazon Resource Name (ARN) for the server.</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The domain of the server</td></tr>
<tr><td><CopyableCode code="endpoint_type" /></td><td><code>string</code></td><td>The endpoint type of the server</td></tr>
<tr><td><CopyableCode code="identity_provider_type" /></td><td><code>string</code></td><td>The mode of authentication for a server. The default</td></tr>
<tr><td><CopyableCode code="logging_role" /></td><td><code>string</code></td><td>The logging role of the server</td></tr>
<tr><td><CopyableCode code="server_id" /></td><td><code>string</code></td><td>The server id</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Describes the condition of a file transfer protocol-enabled server with respect to its ability to perform file operations. There are six possible states: OFFLINE, ONLINE, STARTING, STOPPING, START_FAILED, and STOP_FAILED. OFFLINE indicates that the server exists, but that it is not available for file operations. ONLINE indicates that the server is available to perform file operations. STARTING indicates that the server's was instantiated, but the server is not yet available to perform file operations. Under normal conditions, it can take a couple of minutes for the server to be completely operational. Both START_FAILED and STOP_FAILED are error conditions.</td></tr>
<tr><td><CopyableCode code="user_count" /></td><td><code>integer</code></td><td>The user count of the server</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="view" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
domain,
endpoint_type,
identity_provider_type,
logging_role,
server_id,
state,
user_count,
region
FROM aws.transfer.servers
WHERE region = '<region>';
```





