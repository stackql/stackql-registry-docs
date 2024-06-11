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

Creates, updates, deletes or gets a <code>simple_ad</code> resource or lists <code>simple_ads</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simple_ads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::DirectoryService::SimpleAD</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.directoryservice.simple_ads" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td>The unique identifier for a directory.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>The alias for a directory.</td></tr>
<tr><td><CopyableCode code="dns_ip_addresses" /></td><td><code>array</code></td><td>The IP addresses of the DNS servers for the directory, such as &#91; "172.31.3.154", "172.31.63.203" &#93;.</td></tr>
<tr><td><CopyableCode code="create_alias" /></td><td><code>boolean</code></td><td>The name of the configuration set.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description for the directory.</td></tr>
<tr><td><CopyableCode code="enable_sso" /></td><td><code>boolean</code></td><td>Whether to enable single sign-on for a Simple Active Directory in AWS.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The fully qualified domain name for the AWS Managed Simple AD directory.</td></tr>
<tr><td><CopyableCode code="password" /></td><td><code>string</code></td><td>The password for the default administrative user named Admin.</td></tr>
<tr><td><CopyableCode code="short_name" /></td><td><code>string</code></td><td>The NetBIOS name for your domain.</td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>string</code></td><td>The size of the directory.</td></tr>
<tr><td><CopyableCode code="vpc_settings" /></td><td><code>object</code></td><td>VPC settings of the Simple AD directory server in AWS.</td></tr>
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
    <td><CopyableCode code="VpcSettings, Size, Name, region" /></td>
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
List all <code>simple_ads</code> in a region.
```sql
SELECT
region,
directory_id
FROM aws.directoryservice.simple_ads
WHERE region = 'us-east-1';
```
Gets all properties from a <code>simple_ad</code>.
```sql
SELECT
region,
directory_id,
alias,
dns_ip_addresses,
create_alias,
description,
enable_sso,
name,
password,
short_name,
size,
vpc_settings
FROM aws.directoryservice.simple_ads
WHERE region = 'us-east-1' AND data__Identifier = '<DirectoryId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>simple_ad</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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
ec2:CreateTags,
ec2:RevokeSecurityGroupIngress,
ec2:RevokeSecurityGroupEgress
```

### Read
```json
ds:DescribeDirectories
```

### Update
```json
ds:EnableSso,
ds:DisableSso,
ds:DescribeDirectories
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

