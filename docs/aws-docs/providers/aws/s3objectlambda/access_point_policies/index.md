---
title: access_point_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point_policies
  - s3objectlambda
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


Used to retrieve a list of <code>access_point_policies</code> in a region or to create or delete a <code>access_point_policies</code> resource, use <code>access_point_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::S3ObjectLambda::AccessPointPolicy resource is an Amazon S3ObjectLambda policy type that you can use to control permissions for your S3ObjectLambda</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3objectlambda.access_point_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="object_lambda_access_point" /></td><td><code>string</code></td><td>The name of the Amazon S3 ObjectLambdaAccessPoint to which the policy applies.</td></tr>
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
object_lambda_access_point
FROM aws.s3objectlambda.access_point_policies
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ObjectLambdaAccessPoint": "{{ ObjectLambdaAccessPoint }}",
 "PolicyDocument": {}
}
>>>
--required properties only
INSERT INTO aws.s3objectlambda.access_point_policies (
 ObjectLambdaAccessPoint,
 PolicyDocument,
 region
)
SELECT 
{{ .ObjectLambdaAccessPoint }},
 {{ .PolicyDocument }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ObjectLambdaAccessPoint": "{{ ObjectLambdaAccessPoint }}",
 "PolicyDocument": {}
}
>>>
--all properties
INSERT INTO aws.s3objectlambda.access_point_policies (
 ObjectLambdaAccessPoint,
 PolicyDocument,
 region
)
SELECT 
 {{ .ObjectLambdaAccessPoint }},
 {{ .PolicyDocument }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3objectlambda.access_point_policies
WHERE data__Identifier = '<ObjectLambdaAccessPoint>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_point_policies</code> resource, the following permissions are required:

### Create
```json
s3:PutAccessPointPolicyForObjectLambda,
s3:GetAccessPointPolicyForObjectLambda
```

### Delete
```json
s3:DeleteAccessPointPolicyForObjectLambda,
s3:GetAccessPointPolicyForObjectLambda
```

