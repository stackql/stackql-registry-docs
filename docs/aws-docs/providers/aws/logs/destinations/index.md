---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
  - logs
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


Used to retrieve a list of <code>destinations</code> in a region or to create or delete a <code>destinations</code> resource, use <code>destination</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Logs::Destination resource specifies a CloudWatch Logs destination. A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="destination_name" /></td><td><code>string</code></td><td>The name of the destination resource</td></tr>
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
destination_name
FROM aws.logs.destinations
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
 "DestinationName": "{{ DestinationName }}",
 "RoleArn": "{{ RoleArn }}",
 "TargetArn": "{{ TargetArn }}"
}
>>>
--required properties only
INSERT INTO aws.logs.destinations (
 DestinationName,
 RoleArn,
 TargetArn,
 region
)
SELECT 
{{ DestinationName }},
 {{ RoleArn }},
 {{ TargetArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DestinationName": "{{ DestinationName }}",
 "DestinationPolicy": "{{ DestinationPolicy }}",
 "RoleArn": "{{ RoleArn }}",
 "TargetArn": "{{ TargetArn }}"
}
>>>
--all properties
INSERT INTO aws.logs.destinations (
 DestinationName,
 DestinationPolicy,
 RoleArn,
 TargetArn,
 region
)
SELECT 
 {{ DestinationName }},
 {{ DestinationPolicy }},
 {{ RoleArn }},
 {{ TargetArn }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.logs.destinations
WHERE data__Identifier = '<DestinationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>destinations</code> resource, the following permissions are required:

### Create
```json
logs:PutDestination,
logs:PutDestinationPolicy,
logs:DescribeDestinations,
iam:PassRole
```

### Delete
```json
logs:DeleteDestination
```

### List
```json
logs:DescribeDestinations
```

