---
title: simple_ads
hide_title: false
hide_table_of_contents: false
keywords:
  - simple_ads
  - directoryservice
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


Used to retrieve a list of <code>simple_ads</code> in a region or to create or delete a <code>simple_ads</code> resource, use <code>simple_ad</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simple_ads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::DirectoryService::SimpleAD</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.directoryservice.simple_ads" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td>The unique identifier for a directory.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
directory_id
FROM aws.directoryservice.simple_ads
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>simple_ad</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- simple_ad.iql (required properties only)
INSERT INTO aws.directoryservice.simple_ads (
 Name,
 Size,
 VpcSettings,
 region
)
SELECT 
'{{ Name }}',
 '{{ Size }}',
 '{{ VpcSettings }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- simple_ad.iql (all properties)
INSERT INTO aws.directoryservice.simple_ads (
 CreateAlias,
 Description,
 EnableSso,
 Name,
 Password,
 ShortName,
 Size,
 VpcSettings,
 region
)
SELECT 
 '{{ CreateAlias }}',
 '{{ Description }}',
 '{{ EnableSso }}',
 '{{ Name }}',
 '{{ Password }}',
 '{{ ShortName }}',
 '{{ Size }}',
 '{{ VpcSettings }}',
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
  - name: simple_ad
    props:
      - name: CreateAlias
        value: '{{ CreateAlias }}'
      - name: Description
        value: '{{ Description }}'
      - name: EnableSso
        value: '{{ EnableSso }}'
      - name: Name
        value: '{{ Name }}'
      - name: Password
        value: '{{ Password }}'
      - name: ShortName
        value: '{{ ShortName }}'
      - name: Size
        value: '{{ Size }}'
      - name: VpcSettings
        value:
          SubnetIds:
            - '{{ SubnetIds[0] }}'
          VpcId: '{{ VpcId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.directoryservice.simple_ads
WHERE data__Identifier = '<DirectoryId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>simple_ads</code> resource, the following permissions are required:

### Create
```json
ds:CreateDirectory,
ds:CreateAlias,
ds:EnableSso,
ds:DescribeDirectories,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
ec2:CreateSecurityGroup,
ec2:CreateNetworkInterface,
ec2:DescribeNetworkInterfaces,
ec2:AuthorizeSecurityGroupIngress,
ec2:AuthorizeSecurityGroupEgress,
ec2:CreateTags
```

### Delete
```json
ds:DeleteDirectory,
ds:DescribeDirectories,
ec2:DescribeNetworkInterfaces,
ec2:DeleteSecurityGroup,
ec2:DeleteNetworkInterface,
ec2:RevokeSecurityGroupIngress,
ec2:RevokeSecurityGroupEgress,
ec2:DeleteTags
```

### List
```json
ds:DescribeDirectories
```

