---
title: permission_set_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_set_tags
  - sso
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

Expands all tag keys and values for <code>permission_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_set_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO PermissionSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.permission_set_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this permission set.</td></tr>
<tr><td><CopyableCode code="permission_set_arn" /></td><td><code>string</code></td><td>The permission set that the policy will be attached to</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The permission set description.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The sso instance arn that the permission set is owned.</td></tr>
<tr><td><CopyableCode code="session_duration" /></td><td><code>string</code></td><td>The length of time that a user can be signed in to an AWS account.</td></tr>
<tr><td><CopyableCode code="relay_state_type" /></td><td><code>string</code></td><td>The relay state URL that redirect links to any service in the AWS Management Console.</td></tr>
<tr><td><CopyableCode code="managed_policies" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="inline_policy" /></td><td><code>object</code></td><td>The inline policy to put in permission set.</td></tr>
<tr><td><CopyableCode code="customer_managed_policy_references" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions_boundary" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>permission_sets</code> in a region.
```sql
SELECT
region,
name,
permission_set_arn,
description,
instance_arn,
session_duration,
relay_state_type,
managed_policies,
inline_policy,
customer_managed_policy_references,
permissions_boundary,
tag_key,
tag_value
FROM aws.sso.permission_set_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>permission_set_tags</code> resource, see <a href="/providers/aws/sso/permission_sets/#permissions"><code>permission_sets</code></a>

