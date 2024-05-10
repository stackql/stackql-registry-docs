---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - connect
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


Used to retrieve a list of <code>instances</code> in a region or to create or delete a <code>instances</code> resource, use <code>instance</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>An instanceArn is automatically generated on creation based on instanceId.</td></tr>
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
FROM aws.connect.instances
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
 "IdentityManagementType": "{{ IdentityManagementType }}",
 "Attributes": {
  "InboundCalls": "{{ InboundCalls }}",
  "OutboundCalls": "{{ OutboundCalls }}",
  "ContactflowLogs": "{{ ContactflowLogs }}",
  "ContactLens": "{{ ContactLens }}",
  "AutoResolveBestVoices": "{{ AutoResolveBestVoices }}",
  "UseCustomTTSVoices": "{{ UseCustomTTSVoices }}",
  "EarlyMedia": "{{ EarlyMedia }}"
 }
}
>>>
--required properties only
INSERT INTO aws.connect.instances (
 IdentityManagementType,
 Attributes,
 region
)
SELECT 
{{ IdentityManagementType }},
 {{ Attributes }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "IdentityManagementType": "{{ IdentityManagementType }}",
 "InstanceAlias": "{{ InstanceAlias }}",
 "DirectoryId": "{{ DirectoryId }}",
 "Attributes": {
  "InboundCalls": "{{ InboundCalls }}",
  "OutboundCalls": "{{ OutboundCalls }}",
  "ContactflowLogs": "{{ ContactflowLogs }}",
  "ContactLens": "{{ ContactLens }}",
  "AutoResolveBestVoices": "{{ AutoResolveBestVoices }}",
  "UseCustomTTSVoices": "{{ UseCustomTTSVoices }}",
  "EarlyMedia": "{{ EarlyMedia }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.connect.instances (
 IdentityManagementType,
 InstanceAlias,
 DirectoryId,
 Attributes,
 Tags,
 region
)
SELECT 
 {{ IdentityManagementType }},
 {{ InstanceAlias }},
 {{ DirectoryId }},
 {{ Attributes }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.instances
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>instances</code> resource, the following permissions are required:

### Create
```json
connect:CreateInstance,
connect:DescribeInstance,
connect:UpdateInstanceAttribute,
connect:TagResource,
ds:CheckAlias,
ds:CreateAlias,
ds:AuthorizeApplication,
ds:UnauthorizeApplication,
ds:CreateIdentityPoolDirectory,
ds:CreateDirectory,
ds:DescribeDirectories,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
logs:CreateLogGroup
```

### Delete
```json
connect:DeleteInstance,
connect:DescribeInstance,
connect:UntagResource,
ds:DeleteDirectory,
ds:UnauthorizeApplication,
ds:DescribeDirectories
```

### List
```json
connect:ListInstances,
connect:ListInstanceAttributes,
ds:DescribeDirectories
```

