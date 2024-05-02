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
Gets or operates on an individual <code>subscriber</code> resource, use <code>subscribers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriber</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecurityLake::Subscriber</td></tr>
<tr><td><b>Id</b></td><td><code>aws.securitylake.subscriber</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_types</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>data_lake_arn</code></td><td><code>string</code></td><td>The ARN for the data lake.</td></tr>
<tr><td><code>subscriber_identity</code></td><td><code>object</code></td><td>The AWS identity used to access your data.</td></tr>
<tr><td><code>subscriber_name</code></td><td><code>string</code></td><td>The name of your Security Lake subscriber account.</td></tr>
<tr><td><code>subscriber_description</code></td><td><code>string</code></td><td>The description for your subscriber account in Security Lake.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</td></tr>
<tr><td><code>sources</code></td><td><code>array</code></td><td>The supported AWS services from which logs and events are collected.</td></tr>
<tr><td><code>resource_share_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_share_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subscriber_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>s3_bucket_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subscriber_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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
WHERE data__Identifier = '<SubscriberArn>';
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

### Delete
```json
securitylake:DeleteSubscriber,
iam:GetRole,
iam:ListRolePolicies,
iam:DeleteRole,
iam:DeleteRolePolicy,
glue:GetTable,
lakeformation:RevokePermissions,
lakeformation:ListPermissions,
ram:GetResourceShares,
ram:DeleteResourceShare,
events:DeleteApiDestination,
events:DeleteConnection,
events:DeleteRule,
events:ListApiDestinations,
events:ListTargetsByRule,
events:DescribeRule,
events:RemoveTargets,
sqs:DeleteQueue,
sqs:GetQueueUrl
```

