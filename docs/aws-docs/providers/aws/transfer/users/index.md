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

Describes the properties of a user that was specified.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes the properties of a user that was specified.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.users" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="home_directory" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="home_directory_mappings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="home_directory_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="posix_profile" /></td><td><code>object</code></td><td>The full POSIX identity, including user ID (<code>Uid</code>), group ID (<code>Gid</code>), and any secondary groups IDs (<code>SecondaryGids</code>), that controls your users' access to your Amazon EFS file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ssh_public_keys" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="describe_user" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__ServerId, data__UserName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_users" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__ServerId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="create_user" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__Role, data__ServerId, data__UserName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_user" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__ServerId, data__UserName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_user" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__ServerId, data__UserName, region" /></td>
  </tr>
</tbody></table>








