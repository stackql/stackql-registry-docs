---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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


List of Transfer family users in a server

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of Transfer family users in a server</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.users" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="data___server_id" /></td><td><code>string</code></td><td>The server id</td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td>The user name</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Unique Amazon Resource Name (ARN) for the user.</td></tr>
<tr><td><CopyableCode code="home_directory_type" /></td><td><code>string</code></td><td>The home directory type for the user</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The role of the server</td></tr>
<tr><td><CopyableCode code="ssh_public_key_count" /></td><td><code>integer</code></td><td>The SSH public key count of the server</td></tr>
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
data___server_id,
user_name,
arn,
home_directory_type,
role,
ssh_public_key_count,
region
FROM aws.transfer.users
WHERE region = '<region>' AND data__ServerId = '<s-serverid>';
```





