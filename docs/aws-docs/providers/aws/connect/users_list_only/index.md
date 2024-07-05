---
title: users_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - users_list_only
  - connect
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

Lists <code>users</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/users/"><code>users</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::User</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.users_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="directory_user_id" /></td><td><code>string</code></td><td>The identifier of the user account in the directory used for identity management.</td></tr>
<tr><td><CopyableCode code="hierarchy_group_arn" /></td><td><code>string</code></td><td>The identifier of the hierarchy group for the user.</td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td>The user name for the account.</td></tr>
<tr><td><CopyableCode code="password" /></td><td><code>string</code></td><td>The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.</td></tr>
<tr><td><CopyableCode code="routing_profile_arn" /></td><td><code>string</code></td><td>The identifier of the routing profile for the user.</td></tr>
<tr><td><CopyableCode code="identity_info" /></td><td><code>object</code></td><td>The information about the identity of the user.</td></tr>
<tr><td><CopyableCode code="phone_config" /></td><td><code>object</code></td><td>The phone settings for the user.</td></tr>
<tr><td><CopyableCode code="security_profile_arns" /></td><td><code>array</code></td><td>One or more security profile arns for the user</td></tr>
<tr><td><CopyableCode code="user_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the user.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="user_proficiencies" /></td><td><code>array</code></td><td>One or more predefined attributes assigned to a user, with a level that indicates how skilled they are.</td></tr>
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
Lists all <code>users</code> in a region.
```sql
SELECT
region,
user_arn
FROM aws.connect.users_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>users_list_only</code> resource, see <a href="/providers/aws/connect/users/#permissions"><code>users</code></a>


