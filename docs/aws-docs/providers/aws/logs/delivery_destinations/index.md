---
title: delivery_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_destinations
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


Used to retrieve a list of <code>delivery_destinations</code> in a region or to create or delete a <code>delivery_destinations</code> resource, use <code>delivery_destination</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This structure contains information about one delivery destination in your account.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;A delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.delivery_destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this delivery destination.</td></tr>
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
name
FROM aws.logs.delivery_destinations
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
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.logs.delivery_destinations (
 Name,
 region
)
SELECT 
{{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "DestinationResourceArn": "{{ DestinationResourceArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "DeliveryDestinationPolicy": {}
}
>>>
--all properties
INSERT INTO aws.logs.delivery_destinations (
 Name,
 DestinationResourceArn,
 Tags,
 DeliveryDestinationPolicy,
 region
)
SELECT 
 {{ Name }},
 {{ DestinationResourceArn }},
 {{ Tags }},
 {{ DeliveryDestinationPolicy }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.logs.delivery_destinations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>delivery_destinations</code> resource, the following permissions are required:

### Create
```json
logs:PutDeliveryDestination,
logs:GetDeliveryDestination,
logs:ListTagsForResource,
logs:TagResource,
logs:UntagResource,
logs:PutDeliveryDestinationPolicy,
logs:GetDeliveryDestinationPolicy
```

### Delete
```json
logs:DeleteDeliveryDestination,
logs:DeleteDeliveryDestinationPolicy
```

### List
```json
logs:DescribeDeliveryDestinations,
logs:GetDeliveryDestinationPolicy
```

