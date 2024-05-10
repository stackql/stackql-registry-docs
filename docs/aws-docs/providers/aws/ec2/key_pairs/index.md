---
title: key_pairs
hide_title: false
hide_table_of_contents: false
keywords:
  - key_pairs
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


Used to retrieve a list of <code>key_pairs</code> in a region or to create or delete a <code>key_pairs</code> resource, use <code>key_pair</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_pairs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::KeyPair creates an SSH key pair</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.key_pairs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td>The name of the SSH key pair</td></tr>
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
key_name
FROM aws.ec2.key_pairs
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
 "KeyName": "{{ KeyName }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.key_pairs (
 KeyName,
 region
)
SELECT 
{{ KeyName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "KeyName": "{{ KeyName }}",
 "KeyType": "{{ KeyType }}",
 "KeyFormat": "{{ KeyFormat }}",
 "PublicKeyMaterial": "{{ PublicKeyMaterial }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.key_pairs (
 KeyName,
 KeyType,
 KeyFormat,
 PublicKeyMaterial,
 Tags,
 region
)
SELECT 
 {{ KeyName }},
 {{ KeyType }},
 {{ KeyFormat }},
 {{ PublicKeyMaterial }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.key_pairs
WHERE data__Identifier = '<KeyName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>key_pairs</code> resource, the following permissions are required:

### Create
```json
ec2:CreateKeyPair,
ec2:ImportKeyPair,
ec2:CreateTags,
ssm:PutParameter
```

### List
```json
ec2:DescribeKeyPairs
```

### Delete
```json
ec2:DeleteKeyPair,
ssm:DeleteParameter,
ec2:DescribeKeyPairs
```

