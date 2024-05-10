---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
  - xray
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


Used to retrieve a list of <code>resource_policies</code> in a region or to create or delete a <code>resource_policies</code> resource, use <code>resource_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay Resource Policy resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.resource_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the resource policy. Must be unique within a specific AWS account.</td></tr>
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
policy_name
FROM aws.xray.resource_policies
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
 "PolicyName": "{{ PolicyName }}",
 "PolicyDocument": "{{ PolicyDocument }}"
}
>>>
--required properties only
INSERT INTO aws.xray.resource_policies (
 PolicyName,
 PolicyDocument,
 region
)
SELECT 
{{ .PolicyName }},
 {{ .PolicyDocument }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PolicyName": "{{ PolicyName }}",
 "PolicyDocument": "{{ PolicyDocument }}",
 "BypassPolicyLockoutCheck": "{{ BypassPolicyLockoutCheck }}"
}
>>>
--all properties
INSERT INTO aws.xray.resource_policies (
 PolicyName,
 PolicyDocument,
 BypassPolicyLockoutCheck,
 region
)
SELECT 
 {{ .PolicyName }},
 {{ .PolicyDocument }},
 {{ .BypassPolicyLockoutCheck }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.xray.resource_policies
WHERE data__Identifier = '<PolicyName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_policies</code> resource, the following permissions are required:

### Create
```json
xray:PutResourcePolicy,
xray:ListResourcePolicies
```

### Delete
```json
xray:DeleteResourcePolicy
```

### List
```json
xray:ListResourcePolicies
```

