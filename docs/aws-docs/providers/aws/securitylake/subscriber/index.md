---
title: subscriber
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriber
  - securitylake
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


Gets or updates an individual <code>subscriber</code> resource, use <code>subscribers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriber</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecurityLake::Subscriber</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securitylake.subscriber" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_types" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_lake_arn" /></td><td><code>string</code></td><td>The ARN for the data lake.</td></tr>
<tr><td><CopyableCode code="subscriber_identity" /></td><td><code>object</code></td><td>The AWS identity used to access your data.</td></tr>
<tr><td><CopyableCode code="subscriber_name" /></td><td><code>string</code></td><td>The name of your Security Lake subscriber account.</td></tr>
<tr><td><CopyableCode code="subscriber_description" /></td><td><code>string</code></td><td>The description for your subscriber account in Security Lake.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>The supported AWS services from which logs and events are collected.</td></tr>
<tr><td><CopyableCode code="resource_share_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_share_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subscriber_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="s3_bucket_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subscriber_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
access_types,
data_lake_arn,
subscriber_identity,
subscriber_name,
subscriber_description,
tags,
sources,
resource_share_arn,
resource_share_name,
subscriber_role_arn,
s3_bucket_arn,
subscriber_arn
FROM aws.securitylake.subscriber
WHERE region = 'us-east-1' AND data__Identifier = '<SubscriberArn>';
```


## Permissions

To operate on the <code>subscriber</code> resource, the following permissions are required:

### Read
```json
securitylake:GetSubscriber,
securitylake:ListTagsForResource
```

### Update
```json
securitylake:UpdateSubscriber,
securitylake:GetSubscriber,
securitylake:TagResource,
securitylake:UntagResource,
securitylake:ListTagsForResource,
glue:GetDatabase,
glue:GetTable,
lakeformation:ListPermissions,
lakeformation:GrantPermissions,
lakeformation:RevokePermissions,
ram:CreateResourceShare,
ram:GetResourceShares,
ram:GetResourceShareAssociations,
ram:UpdateResourceShare,
ram:DeleteResourceShare,
iam:CreateRole,
iam:GetRole,
iam:DeleteRole,
iam:PutRolePolicy,
iam:DeleteRolePolicy,
iam:ListRolePolicies,
events:CreateApiDestination,
events:CreateConnection,
events:ListApiDestinations,
events:ListConnections,
events:PutRule,
events:UpdateApiDestination,
events:UpdateConnection,
events:DeleteApiDestination,
events:DeleteConnection,
events:DeleteRule,
events:RemoveTargets,
events:ListTargetsByRule,
events:DescribeRule,
events:PutTargets
```

