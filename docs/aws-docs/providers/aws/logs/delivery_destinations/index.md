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

Creates, updates, deletes or gets a <code>delivery_destination</code> resource or lists <code>delivery_destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This structure contains information about one delivery destination in your account.<br />A delivery destination is an AWS resource that represents an AWS service that logs can be sent to CloudWatch Logs, Amazon S3, are supported as Kinesis Data Firehose delivery destinations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.delivery_destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this delivery destination.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.</td></tr>
<tr><td><CopyableCode code="destination_resource_arn" /></td><td><code>string</code></td><td>The ARN of the AWS resource that will receive the logs.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags that have been assigned to this delivery destination.</td></tr>
<tr><td><CopyableCode code="delivery_destination_type" /></td><td><code>string</code></td><td>Displays whether this delivery destination is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.</td></tr>
<tr><td><CopyableCode code="delivery_destination_policy" /></td><td><code>object</code></td><td>IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.<br />The policy must be in JSON string format.<br />Length Constraints: Maximum length of 51200</td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>delivery_destinations</code> in a region.
```sql
SELECT
region,
name,
arn,
destination_resource_arn,
tags,
delivery_destination_type,
delivery_destination_policy
FROM aws.logs.delivery_destinations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>delivery_destination</code>.
```sql
SELECT
region,
name,
arn,
destination_resource_arn,
tags,
delivery_destination_type,
delivery_destination_policy
FROM aws.logs.delivery_destinations
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>delivery_destination</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.logs.delivery_destinations (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.delivery_destinations (
 Name,
 DestinationResourceArn,
 Tags,
 DeliveryDestinationPolicy,
 region
)
SELECT 
 '{{ Name }}',
 '{{ DestinationResourceArn }}',
 '{{ Tags }}',
 '{{ DeliveryDestinationPolicy }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: delivery_destination
    props:
      - name: Name
        value: '{{ Name }}'
      - name: DestinationResourceArn
        value: '{{ DestinationResourceArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: DeliveryDestinationPolicy
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
logs:GetDeliveryDestination,
logs:ListTagsForResource,
logs:GetDeliveryDestinationPolicy
```

### Update
```json
logs:PutDeliveryDestination,
logs:GetDeliveryDestination,
logs:ListTagsForResource,
logs:TagResource,
logs:UntagResource,
logs:DeleteDeliveryDestinationPolicy,
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

