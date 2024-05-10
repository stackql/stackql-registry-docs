---
title: user_pool_user_to_group_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_user_to_group_attachment
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>user_pool_user_to_group_attachment</code> resource, use <code>user_pool_user_to_group_attachments</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_user_to_group_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolUserToGroupAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_user_to_group_attachment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
user_pool_id,
username,
group_name
FROM aws.cognito.user_pool_user_to_group_attachment
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<GroupName>|<Username>';
```


## Permissions

To operate on the <code>user_pool_user_to_group_attachment</code> resource, the following permissions are required:

### Read
```json
cognito-idp:AdminListGroupsForUser
```

