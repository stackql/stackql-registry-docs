---
title: deliveries
hide_title: false
hide_table_of_contents: false
keywords:
  - deliveries
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

Creates, updates, deletes or gets a <code>delivery</code> resource or lists <code>deliveries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deliveries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This structure contains information about one delivery in your account.<br />A delivery is a connection between a logical delivery source and a logical delivery destination.<br />For more information, see &#91;CreateDelivery&#93;(https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.deliveries" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="delivery_id" /></td><td><code>string</code></td><td>The unique ID that identifies this delivery in your account.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that uniquely identifies this delivery.</td></tr>
<tr><td><CopyableCode code="delivery_source_name" /></td><td><code>string</code></td><td>The name of the delivery source that is associated with this delivery.</td></tr>
<tr><td><CopyableCode code="delivery_destination_arn" /></td><td><code>string</code></td><td>The ARN of the delivery destination that is associated with this delivery.</td></tr>
<tr><td><CopyableCode code="delivery_destination_type" /></td><td><code>string</code></td><td>Displays whether the delivery destination associated with this delivery is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags that have been assigned to this delivery.</td></tr>
<tr><td><CopyableCode code="record_fields" /></td><td><code>array</code></td><td>The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.</td></tr>
<tr><td><CopyableCode code="field_delimiter" /></td><td><code>string</code></td><td>The field delimiter to use between record fields when the final output format of a delivery is in Plain , W3C , or Raw format.</td></tr>
<tr><td><CopyableCode code="s3_suffix_path" /></td><td><code>string</code></td><td>This string allows re-configuring the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path will vary by each log source. See ConfigurationTemplate$allowedSuffixPathFields for more info on what values are supported in the suffix path for each log source.</td></tr>
<tr><td><CopyableCode code="s3_enable_hive_compatible_path" /></td><td><code>boolean</code></td><td>This parameter causes the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html"><code>AWS::Logs::Delivery</code></a>.

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
    <td><CopyableCode code="DeliverySourceName, DeliveryDestinationArn, region" /></td>
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
Gets all <code>deliveries</code> in a region.
```sql
SELECT
region,
delivery_id,
arn,
delivery_source_name,
delivery_destination_arn,
delivery_destination_type,
tags,
record_fields,
field_delimiter,
s3_suffix_path,
s3_enable_hive_compatible_path
FROM aws.logs.deliveries
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>delivery</code>.
```sql
SELECT
region,
delivery_id,
arn,
delivery_source_name,
delivery_destination_arn,
delivery_destination_type,
tags,
record_fields,
field_delimiter,
s3_suffix_path,
s3_enable_hive_compatible_path
FROM aws.logs.deliveries
WHERE region = 'us-east-1' AND data__Identifier = '<DeliveryId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>delivery</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.deliveries (
 DeliverySourceName,
 DeliveryDestinationArn,
 region
)
SELECT 
'{{ DeliverySourceName }}',
 '{{ DeliveryDestinationArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.deliveries (
 DeliverySourceName,
 DeliveryDestinationArn,
 Tags,
 RecordFields,
 FieldDelimiter,
 S3SuffixPath,
 S3EnableHiveCompatiblePath,
 region
)
SELECT 
 '{{ DeliverySourceName }}',
 '{{ DeliveryDestinationArn }}',
 '{{ Tags }}',
 '{{ RecordFields }}',
 '{{ FieldDelimiter }}',
 '{{ S3SuffixPath }}',
 '{{ S3EnableHiveCompatiblePath }}',
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
  - name: delivery
    props:
      - name: DeliverySourceName
        value: '{{ DeliverySourceName }}'
      - name: DeliveryDestinationArn
        value: '{{ DeliveryDestinationArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: RecordFields
        value:
          - '{{ RecordFields[0] }}'
      - name: FieldDelimiter
        value: '{{ FieldDelimiter }}'
      - name: S3SuffixPath
        value: '{{ S3SuffixPath }}'
      - name: S3EnableHiveCompatiblePath
        value: '{{ S3EnableHiveCompatiblePath }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.deliveries
WHERE data__Identifier = '<DeliveryId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deliveries</code> resource, the following permissions are required:

### Create
```json
logs:CreateDelivery,
logs:GetDelivery,
logs:DescribeDeliveries,
logs:ListTagsForResource,
logs:TagResource,
logs:GetDeliverySource,
logs:GetDeliveryDestination
```

### Read
```json
logs:GetDelivery,
logs:ListTagsForResource
```

### Update
```json
logs:GetDelivery,
logs:ListTagsForResource,
logs:TagResource,
logs:UntagResource
```

### Delete
```json
logs:DeleteDelivery,
logs:ListTagsForResource,
logs:UntagResource
```

### List
```json
logs:DescribeDeliveries,
logs:ListTagsForResource
```
