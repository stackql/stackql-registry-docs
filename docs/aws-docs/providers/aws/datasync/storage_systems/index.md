---
title: storage_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_systems
  - datasync
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


Used to retrieve a list of <code>storage_systems</code> in a region or to create or delete a <code>storage_systems</code> resource, use <code>storage_system</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::StorageSystem.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.storage_systems" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="storage_system_arn" /></td><td><code>string</code></td><td>The ARN of the on-premises storage system added to DataSync Discovery.</td></tr>
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
storage_system_arn
FROM aws.datasync.storage_systems
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
 "ServerConfiguration": {
  "ServerHostname": "{{ ServerHostname }}",
  "ServerPort": "{{ ServerPort }}"
 },
 "SystemType": "{{ SystemType }}",
 "AgentArns": [
  "{{ AgentArns[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.datasync.storage_systems (
 ServerConfiguration,
 SystemType,
 AgentArns,
 region
)
SELECT 
{{ ServerConfiguration }},
 {{ SystemType }},
 {{ AgentArns }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ServerConfiguration": {
  "ServerHostname": "{{ ServerHostname }}",
  "ServerPort": "{{ ServerPort }}"
 },
 "ServerCredentials": {
  "Username": "{{ Username }}",
  "Password": "{{ Password }}"
 },
 "SystemType": "{{ SystemType }}",
 "AgentArns": [
  "{{ AgentArns[0] }}"
 ],
 "CloudWatchLogGroupArn": "{{ CloudWatchLogGroupArn }}",
 "Name": "{{ Name }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.datasync.storage_systems (
 ServerConfiguration,
 ServerCredentials,
 SystemType,
 AgentArns,
 CloudWatchLogGroupArn,
 Name,
 Tags,
 region
)
SELECT 
 {{ ServerConfiguration }},
 {{ ServerCredentials }},
 {{ SystemType }},
 {{ AgentArns }},
 {{ CloudWatchLogGroupArn }},
 {{ Name }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.datasync.storage_systems
WHERE data__Identifier = '<StorageSystemArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>storage_systems</code> resource, the following permissions are required:

### Create
```json
datasync:AddStorageSystem,
datasync:DescribeStorageSystem,
datasync:ListTagsForResource,
datasync:TagResource,
secretsmanager:CreateSecret,
secretsmanager:DescribeSecret,
iam:CreateServiceLinkedRole
```

### Delete
```json
datasync:DescribeStorageSystem,
datasync:RemoveStorageSystem,
secretsmanager:DescribeSecret,
secretsmanager:DeleteSecret
```

### List
```json
datasync:ListStorageSystems
```

