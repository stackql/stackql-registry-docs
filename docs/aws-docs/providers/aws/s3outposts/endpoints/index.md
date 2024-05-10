---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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


Used to retrieve a list of <code>endpoints</code> in a region or to create or delete a <code>endpoints</code> resource, use <code>endpoint</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::S3Outposts::Endpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3outposts.endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint.</td></tr>
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
FROM aws.s3outposts.endpoints
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
 "OutpostId": "{{ OutpostId }}",
 "SecurityGroupId": "{{ SecurityGroupId }}",
 "SubnetId": "{{ SubnetId }}"
}
>>>
--required properties only
INSERT INTO aws.s3outposts.endpoints (
 OutpostId,
 SecurityGroupId,
 SubnetId,
 region
)
SELECT 
{{ OutpostId }},
 {{ SecurityGroupId }},
 {{ SubnetId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "OutpostId": "{{ OutpostId }}",
 "SecurityGroupId": "{{ SecurityGroupId }}",
 "SubnetId": "{{ SubnetId }}",
 "AccessType": "{{ AccessType }}",
 "CustomerOwnedIpv4Pool": "{{ CustomerOwnedIpv4Pool }}",
 "FailedReason": {
  "ErrorCode": "{{ ErrorCode }}",
  "Message": "{{ Message }}"
 }
}
>>>
--all properties
INSERT INTO aws.s3outposts.endpoints (
 OutpostId,
 SecurityGroupId,
 SubnetId,
 AccessType,
 CustomerOwnedIpv4Pool,
 FailedReason,
 region
)
SELECT 
 {{ OutpostId }},
 {{ SecurityGroupId }},
 {{ SubnetId }},
 {{ AccessType }},
 {{ CustomerOwnedIpv4Pool }},
 {{ FailedReason }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3outposts.endpoints
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>endpoints</code> resource, the following permissions are required:

### Create
```json
s3-outposts:CreateEndpoint
```

### Delete
```json
s3-outposts:DeleteEndpoint
```

### List
```json
s3-outposts:ListEndpoints
```

