---
title: user_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - user_tags
  - elasticache
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

Expands all tag keys and values for <code>users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElastiCache::User</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.user_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Indicates the user status. Can be "active", "modifying" or "deleting".</td></tr>
<tr><td><CopyableCode code="user_id" /></td><td><code>string</code></td><td>The ID of the user.</td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td>The username of the user.</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The target cache engine for the user.</td></tr>
<tr><td><CopyableCode code="access_string" /></td><td><code>string</code></td><td>Access permissions string used for this user account.</td></tr>
<tr><td><CopyableCode code="no_password_required" /></td><td><code>boolean</code></td><td>Indicates a password is not required for this user account.</td></tr>
<tr><td><CopyableCode code="passwords" /></td><td><code>array</code></td><td>Passwords used for this user account. You can create up to two passwords for each user.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the user account.</td></tr>
<tr><td><CopyableCode code="authentication_mode" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>users</code> in a region.
```sql
SELECT
region,
status,
user_id,
user_name,
engine,
access_string,
no_password_required,
passwords,
arn,
authentication_mode,
tag_key,
tag_value
FROM aws.elasticache.user_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>user_tags</code> resource, see <a href="/providers/aws/elasticache/users/#permissions"><code>users</code></a>

