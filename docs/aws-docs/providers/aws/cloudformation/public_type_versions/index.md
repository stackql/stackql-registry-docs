---
title: public_type_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - public_type_versions
  - cloudformation
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


Used to retrieve a list of <code>public_type_versions</code> in a region or to create or delete a <code>public_type_versions</code> resource, use <code>public_type_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_type_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Test and Publish a resource that has been registered in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.public_type_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="public_type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) assigned to the public extension upon publication</td></tr>
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
public_type_arn
FROM aws.cloudformation.public_type_versions
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
 "Arn": "{{ Arn }}",
 "PublicVersionNumber": "{{ PublicVersionNumber }}",
 "TypeName": "{{ TypeName }}",
 "LogDeliveryBucket": "{{ LogDeliveryBucket }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.cloudformation.public_type_versions (
 Arn,
 PublicVersionNumber,
 TypeName,
 LogDeliveryBucket,
 Type,
 region
)
SELECT 
{{ Arn }},
 {{ PublicVersionNumber }},
 {{ TypeName }},
 {{ LogDeliveryBucket }},
 {{ Type }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Arn": "{{ Arn }}",
 "PublicVersionNumber": "{{ PublicVersionNumber }}",
 "TypeName": "{{ TypeName }}",
 "LogDeliveryBucket": "{{ LogDeliveryBucket }}",
 "Type": "{{ Type }}"
}
>>>
--all properties
INSERT INTO aws.cloudformation.public_type_versions (
 Arn,
 PublicVersionNumber,
 TypeName,
 LogDeliveryBucket,
 Type,
 region
)
SELECT 
 {{ Arn }},
 {{ PublicVersionNumber }},
 {{ TypeName }},
 {{ LogDeliveryBucket }},
 {{ Type }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudformation.public_type_versions
WHERE data__Identifier = '<PublicTypeArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>public_type_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:TestType,
cloudformation:DescribeType,
cloudformation:PublishType,
cloudformation:DescribePublisher,
s3:GetObject,
s3:PutObject
```

### List
```json
cloudformation:ListTypes
```

