---
title: ipam_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_scopes
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

Creates, updates, deletes or gets an <code>ipam_scope</code> resource or lists <code>ipam_scopes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMScope Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_scopes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ipam_scope_id" /></td><td><code>string</code></td><td>Id of the IPAM scope.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM scope.</td></tr>
<tr><td><CopyableCode code="ipam_id" /></td><td><code>string</code></td><td>The Id of the IPAM this scope is a part of.</td></tr>
<tr><td><CopyableCode code="ipam_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM this scope is a part of.</td></tr>
<tr><td><CopyableCode code="ipam_scope_type" /></td><td><code>string</code></td><td>Determines whether this scope contains publicly routable space or space for a private network</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>Is this one of the default scopes created with the IPAM.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pool_count" /></td><td><code>integer</code></td><td>The number of pools that currently exist in this scope.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipamscope.html"><code>AWS::EC2::IPAMScope</code></a>.

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
    <td><CopyableCode code="IpamId, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>ipam_scopes</code> in a region.
```sql
SELECT
region,
ipam_scope_id,
arn,
ipam_id,
ipam_arn,
ipam_scope_type,
is_default,
description,
pool_count,
tags
FROM aws.ec2.ipam_scopes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ipam_scope</code>.
```sql
SELECT
region,
ipam_scope_id,
arn,
ipam_id,
ipam_arn,
ipam_scope_type,
is_default,
description,
pool_count,
tags
FROM aws.ec2.ipam_scopes
WHERE region = 'us-east-1' AND data__Identifier = '<IpamScopeId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ipam_scope</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.ipam_scopes (
 IpamId,
 region
)
SELECT 
'{{ IpamId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.ipam_scopes (
 IpamId,
 Description,
 Tags,
 region
)
SELECT 
 '{{ IpamId }}',
 '{{ Description }}',
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
  - name: ipam_scope
    props:
      - name: IpamId
        value: '{{ IpamId }}'
      - name: Description
        value: '{{ Description }}'
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
DELETE FROM aws.ec2.ipam_scopes
WHERE data__Identifier = '<IpamScopeId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ipam_scopes</code> resource, the following permissions are required:

### Create
```json
ec2:CreateIpamScope,
ec2:DescribeIpamScopes,
ec2:CreateTags
```

### Read
```json
ec2:DescribeIpamScopes
```

### Update
```json
ec2:ModifyIpamScope,
ec2:DescribeIpamScopes,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteIpamScope,
ec2:DescribeIpamScopes,
ec2:DeleteTags
```

### List
```json
ec2:DescribeIpamScopes
```
