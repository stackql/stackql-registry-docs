---
title: access_points
hide_title: false
hide_table_of_contents: false
keywords:
  - access_points
  - s3outposts
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


Used to retrieve a list of <code>access_points</code> in a region or to create or delete a <code>access_points</code> resource, use <code>access_point</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::S3Outposts::AccessPoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3outposts.access_points" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified AccessPoint.</td></tr>
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
arn
FROM aws.s3outposts.access_points
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>access_point</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- access_point.iql (required properties only)
INSERT INTO aws.s3outposts.access_points (
 Bucket,
 Name,
 VpcConfiguration,
 region
)
SELECT 
'{{ Bucket }}',
 '{{ Name }}',
 '{{ VpcConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- access_point.iql (all properties)
INSERT INTO aws.s3outposts.access_points (
 Bucket,
 Name,
 VpcConfiguration,
 Policy,
 region
)
SELECT 
 '{{ Bucket }}',
 '{{ Name }}',
 '{{ VpcConfiguration }}',
 '{{ Policy }}',
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
  - name: access_point
    props:
      - name: Bucket
        value: '{{ Bucket }}'
      - name: Name
        value: '{{ Name }}'
      - name: VpcConfiguration
        value:
          VpcId: '{{ VpcId }}'
      - name: Policy
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3outposts.access_points
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_points</code> resource, the following permissions are required:

### Create
```json
s3-outposts:CreateAccessPoint,
s3-outposts:GetAccessPoint,
s3-outposts:PutAccessPointPolicy,
s3-outposts:GetAccessPointPolicy
```

### Delete
```json
s3-outposts:DeleteAccessPoint,
s3-outposts:DeleteAccessPointPolicy
```

### List
```json
s3-outposts:ListAccessPoints
```

