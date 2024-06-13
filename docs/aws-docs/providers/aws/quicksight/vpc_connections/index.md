---
title: vpc_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connections
  - quicksight
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

Creates, updates, deletes or gets a <code>vpc_connection</code> resource or lists <code>vpc_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::VPCConnection Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.vpc_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the VPC connection.</p></td></tr>
<tr><td><CopyableCode code="availability_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The time that the VPC connection was created.</p></td></tr>
<tr><td><CopyableCode code="dns_resolvers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The time that the VPC connection was last updated.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_interfaces" /></td><td><code>array</code></td><td><p>A list of network interfaces.</p></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_connection_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td><p>The Amazon EC2 VPC ID associated with the VPC connection.</p></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>vpc_connections</code> in a region.
```sql
SELECT
region,
aws_account_id,
vpc_connection_id
FROM aws.quicksight.vpc_connections
WHERE region = 'us-east-1';
```
Gets all properties from a <code>vpc_connection</code>.
```sql
SELECT
region,
arn,
availability_status,
aws_account_id,
created_time,
dns_resolvers,
last_updated_time,
name,
network_interfaces,
role_arn,
security_group_ids,
status,
subnet_ids,
tags,
vpc_connection_id,
vpc_id
FROM aws.quicksight.vpc_connections
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<VPCConnectionId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_connection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.quicksight.vpc_connections (
 AvailabilityStatus,
 AwsAccountId,
 DnsResolvers,
 Name,
 RoleArn,
 SecurityGroupIds,
 SubnetIds,
 Tags,
 VPCConnectionId,
 region
)
SELECT 
'{{ AvailabilityStatus }}',
 '{{ AwsAccountId }}',
 '{{ DnsResolvers }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ SecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ Tags }}',
 '{{ VPCConnectionId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.quicksight.vpc_connections (
 AvailabilityStatus,
 AwsAccountId,
 DnsResolvers,
 Name,
 RoleArn,
 SecurityGroupIds,
 SubnetIds,
 Tags,
 VPCConnectionId,
 region
)
SELECT 
 '{{ AvailabilityStatus }}',
 '{{ AwsAccountId }}',
 '{{ DnsResolvers }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ SecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ Tags }}',
 '{{ VPCConnectionId }}',
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
  - name: vpc_connection
    props:
      - name: AvailabilityStatus
        value: '{{ AvailabilityStatus }}'
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: DnsResolvers
        value:
          - '{{ DnsResolvers[0] }}'
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VPCConnectionId
        value: '{{ VPCConnectionId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.quicksight.vpc_connections
WHERE data__Identifier = '<AwsAccountId|VPCConnectionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_connections</code> resource, the following permissions are required:

### Create
```json
quicksight:CreateVPCConnection,
quicksight:DescribeVPCConnection,
quicksight:ListTagsForResource,
quicksight:TagResource,
iam:PassRole
```

### Read
```json
quicksight:DescribeVPCConnection,
quicksight:ListTagsForResource
```

### Update
```json
quicksight:DescribeVPCConnection,
quicksight:UpdateVPCConnection,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource,
iam:PassRole
```

### Delete
```json
quicksight:DescribeVPCConnection,
quicksight:DeleteVPCConnection,
quicksight:ListTagsForResource,
iam:PassRole
```

### List
```json
quicksight:ListVPCConnections
```

