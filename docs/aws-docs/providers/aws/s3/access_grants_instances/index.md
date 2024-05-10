---
title: access_grants_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants_instances
  - s3
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


Used to retrieve a list of <code>access_grants_instances</code> in a region or to create or delete a <code>access_grants_instances</code> resource, use <code>access_grants_instance</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessGrantsInstance resource is an Amazon S3 resource type that hosts Access Grants and their associated locations</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_grants_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_grants_instance_arn" /></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the specified Access Grants instance.</td></tr>
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
access_grants_instance_arn
FROM aws.s3.access_grants_instances
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
{}
>>>
--required properties only
INSERT INTO aws.s3.access_grants_instances (
 ,
 region
)
SELECT 
{{ . }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "IdentityCenterArn": "{{ IdentityCenterArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.s3.access_grants_instances (
 IdentityCenterArn,
 Tags,
 region
)
SELECT 
 {{ .IdentityCenterArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3.access_grants_instances
WHERE data__Identifier = '<AccessGrantsInstanceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_grants_instances</code> resource, the following permissions are required:

### Create
```json
s3:CreateAccessGrantsInstance,
s3:TagResource
```

### Delete
```json
s3:DeleteAccessGrantsInstance
```

### List
```json
s3:ListAccessGrantsInstances
```

