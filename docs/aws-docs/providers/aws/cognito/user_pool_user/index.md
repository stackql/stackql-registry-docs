---
title: user_pool_user
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_user
  - cognito
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

Gets or operates on an individual <code>user_pool_user</code> resource, use <code>user_pool_users</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolUser</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_user" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="desired_delivery_mediums" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="force_alias_creation" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="user_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="message_action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="validation_data" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="client_metadata" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
desired_delivery_mediums,
force_alias_creation,
user_attributes,
message_action,
username,
user_pool_id,
validation_data,
client_metadata
FROM aws.cognito.user_pool_user
WHERE data__Identifier = '<UserPoolId>|<Username>';
```

## Permissions

To operate on the <code>user_pool_user</code> resource, the following permissions are required:

### Read
```json
cognito-idp:AdminGetUser
```

### Delete
```json
cognito-idp:AdminDeleteUser
```

