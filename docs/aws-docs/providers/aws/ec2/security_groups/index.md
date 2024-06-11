---
title: security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - security_groups
  - ec2
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

Creates, updates, deletes or gets a <code>security_group</code> resource or lists <code>security_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SecurityGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="group_description" /></td><td><code>string</code></td><td>A description for the security group.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The name of the security group.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC for the security group.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The group name or group ID depending on whether the SG is created in default or specific VPC</td></tr>
<tr><td><CopyableCode code="security_group_ingress" /></td><td><code>array</code></td><td>The inbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.</td></tr>
<tr><td><CopyableCode code="security_group_egress" /></td><td><code>array</code></td><td>&#91;VPC only&#93; The outbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the security group.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The group ID of the specified security group.</td></tr>
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
    <td><CopyableCode code="GroupDescription, region" /></td>
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
List all <code>security_groups</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.security_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>security_group</code>.
```sql
SELECT
region,
group_description,
group_name,
vpc_id,
id,
security_group_ingress,
security_group_egress,
tags,
group_id
FROM aws.ec2.security_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.security_groups (
 GroupDescription,
 region
)
SELECT 
'{{ GroupDescription }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.security_groups (
 GroupDescription,
 GroupName,
 VpcId,
 SecurityGroupIngress,
 SecurityGroupEgress,
 Tags,
 region
)
SELECT 
 '{{ GroupDescription }}',
 '{{ GroupName }}',
 '{{ VpcId }}',
 '{{ SecurityGroupIngress }}',
 '{{ SecurityGroupEgress }}',
 '{{ Tags }}',
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
  - name: security_group
    props:
      - name: GroupDescription
        value: '{{ GroupDescription }}'
      - name: GroupName
        value: '{{ GroupName }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: SecurityGroupIngress
        value:
          - CidrIp: '{{ CidrIp }}'
            CidrIpv6: '{{ CidrIpv6 }}'
            Description: '{{ Description }}'
            FromPort: '{{ FromPort }}'
            SourceSecurityGroupName: '{{ SourceSecurityGroupName }}'
            ToPort: '{{ ToPort }}'
            SourceSecurityGroupOwnerId: '{{ SourceSecurityGroupOwnerId }}'
            IpProtocol: '{{ IpProtocol }}'
            SourceSecurityGroupId: '{{ SourceSecurityGroupId }}'
            SourcePrefixListId: '{{ SourcePrefixListId }}'
      - name: SecurityGroupEgress
        value:
          - CidrIp: '{{ CidrIp }}'
            CidrIpv6: '{{ CidrIpv6 }}'
            Description: '{{ Description }}'
            FromPort: '{{ FromPort }}'
            ToPort: '{{ ToPort }}'
            IpProtocol: '{{ IpProtocol }}'
            DestinationSecurityGroupId: '{{ DestinationSecurityGroupId }}'
            DestinationPrefixListId: '{{ DestinationPrefixListId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.security_groups
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_groups</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeSecurityGroups
```

### Create
```json
ec2:CreateSecurityGroup,
ec2:DescribeSecurityGroups,
ec2:RevokeSecurityGroupEgress,
ec2:AuthorizeSecurityGroupEgress,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateTags
```

### Update
```json
ec2:RevokeSecurityGroupEgress,
ec2:RevokeSecurityGroupIngress,
ec2:DescribeSecurityGroups,
ec2:AuthorizeSecurityGroupEgress,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateTags,
ec2:DeleteTags
```

### List
```json
ec2:DescribeSecurityGroups
```

### Delete
```json
ec2:DeleteSecurityGroup,
ec2:DescribeInstances
```

