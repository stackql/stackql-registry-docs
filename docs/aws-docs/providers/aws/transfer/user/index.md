---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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


Details for a Transfer family user in a server

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Details for a Transfer family user in a server</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.user" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="data___server_id" /></td><td><code>string</code></td><td>The server id</td></tr>
<tr><td><CopyableCode code="data___user_name" /></td><td><code>string</code></td><td>The user name</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Unique Amazon Resource Name (ARN) for the user.</td></tr>
<tr><td><CopyableCode code="home_directory" /></td><td><code>string</code></td><td>The home directory of the user</td></tr>
<tr><td><CopyableCode code="home_directory_mappings" /></td><td><code>array</code></td><td>Logical directory mappings that specify what Amazon S3 paths and keys should be visible to your user and how you want to make them visible. You will need to specify the "&lt;bucket-name&gt;&#x2F;&lt;prefix&gt;" name of the Amazon S3 bucket and the "&lt;prefix&gt;" value for the Amazon S3 key in the &lt;code&gt;HomeDirectory&lt;&#x2F;code&gt; parameter. The following example will map the "&lt;prefix&gt;" value "&lt;bucket-name&gt;&#x2F;&lt;prefix&gt;" to "&lt;prefix&gt;"&gt;. The "&lt;prefix&gt;" value does not need to be specified if it is the same as the "&lt;bucket-name&gt;". The mapping will be visible to the user in the "&lt;prefix&gt;" folder of their Amazon S3 storage. This is often referred to as 'logical directory mappings'. In the example, the user will see their Amazon S3 storage as the "&lt;prefix&gt;" folder in the "&lt;bucket-name&gt;" bucket.</td></tr>
<tr><td><CopyableCode code="home_directory_type" /></td><td><code>string</code></td><td>The type of home directory to provide for the user. If you set it to &lt;code&gt;PATH&lt;&#x2F;code&gt;, the user will see the immediate contents of their Amazon S3 storage location. If you set it to &lt;code&gt;LOGICAL&lt;&#x2F;code&gt;, you will provide mappings in the &lt;code&gt;HomeDirectoryMappings&lt;&#x2F;code&gt; for what they will see at the root of their Amazon S3 storage location.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>string</code></td><td>The policy of the user</td></tr>
<tr><td><CopyableCode code="posix_profile" /></td><td><code>object</code></td><td>The full POSIX identity, including user ID (Uid), group ID (Gid), and any secondary group IDs (SecondaryGids), that controls your users' access to your Amazon EFS file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The role of the server</td></tr>
<tr><td><CopyableCode code="ssh_public_keys" /></td><td><code>array</code></td><td>The SSH public keys of the server</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags of the server</td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td>The user name</td></tr>
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
data___user_name,
arn,
home_directory,
home_directory_mappings,
home_directory_type,
policy,
posix_profile,
role,
ssh_public_keys,
tags,
user_name,
region
FROM aws.transfer.user
WHERE region = '<region>' AND data__ServerId = '<s-serverid>' AND data__UserName = '<my_user_name>';
```





