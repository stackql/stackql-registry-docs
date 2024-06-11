---
title: subscribers
hide_title: false
hide_table_of_contents: false
keywords:
  - subscribers
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

Creates, updates, deletes or gets a <code>subscriber</code> resource or lists <code>subscribers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscribers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecurityLake::Subscriber</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securitylake.subscribers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_types" /></td><td><code>The Amazon S3 or AWS Lake Formation access type.</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="AccessTypes, DataLakeArn, Sources, SubscriberIdentity, SubscriberName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>subscribers</code> in a region.
```sql
SELECT
region,
subscriber_arn
FROM aws.securitylake.subscribers
WHERE region = 'us-east-1';
```
Gets all properties from a <code>subscriber</code>.
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
FROM aws.securitylake.subscribers
WHERE region = 'us-east-1' AND data__Identifier = '<SubscriberArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscriber</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.securitylake.subscribers (
 AccessTypes,
 DataLakeArn,
 SubscriberIdentity,
 SubscriberName,
 Sources,
 region
)
SELECT 
'{{ AccessTypes }}',
 '{{ DataLakeArn }}',
 '{{ SubscriberIdentity }}',
 '{{ SubscriberName }}',
 '{{ Sources }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securitylake.subscribers (
 AccessTypes,
 DataLakeArn,
 SubscriberIdentity,
 SubscriberName,
 SubscriberDescription,
 Tags,
 Sources,
 region
)
SELECT 
 '{{ AccessTypes }}',
 '{{ DataLakeArn }}',
 '{{ SubscriberIdentity }}',
 '{{ SubscriberName }}',
 '{{ SubscriberDescription }}',
 '{{ Tags }}',
 '{{ Sources }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: subscriber
    props:
      - name: AccessTypes
        value:
          - '{{ AccessTypes[0] }}'
      - name: DataLakeArn
        value: '{{ DataLakeArn }}'
      - name: SubscriberIdentity
        value:
          ExternalId: '{{ ExternalId }}'
          Principal: '{{ Principal }}'
      - name: SubscriberName
        value: '{{ SubscriberName }}'
      - name: SubscriberDescription
        value: '{{ SubscriberDescription }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Sources
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securitylake.subscribers
WHERE data__Identifier = '<SubscriberArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subscribers</code> resource, the following permissions are required:

### Create
```json
securitylake:CreateSubscriber,
securitylake:CreateCustomLogSource,
securitylake:CreateDataLake,
securitylake:TagResource,
securitylake:GetSubscriber,
securitylake:ListTagsForResource,
iam:GetRole,
iam:GetRolePolicy,
iam:PutRolePolicy,
iam:CreateRole,
iam:CreateServiceLinkedRole,
glue:GetDatabase,
glue:GetTable,
lakeformation:RegisterResource,
lakeformation:GrantPermissions,
lakeformation:RevokePermissions,
lakeformation:ListPermissions,
ram:GetResourceShareAssociations,
ram:CreateResourceShare,
ram:UpdateResourceShare,
ram:GetResourceShares
```

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

### List
```json
securitylake:ListSubscribers
```

