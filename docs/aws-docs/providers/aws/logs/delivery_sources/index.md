---
title: delivery_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_sources
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

Creates, updates, deletes or gets a <code>delivery_source</code> resource or lists <code>delivery_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.<br />Only some AWS services support being configured as a delivery source. These services are listed as Supported &#91;V2 Permissions&#93; in the table at &#91;Enabling logging from AWS services&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.delivery_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name of the Log source.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that uniquely identifies this delivery source.</td></tr>
<tr><td><CopyableCode code="resource_arns" /></td><td><code>array</code></td><td>This array contains the ARN of the AWS resource that sends logs and is represented by this delivery source. Currently, only one ARN can be in the array.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The ARN of the resource that will be sending the logs.</td></tr>
<tr><td><CopyableCode code="service" /></td><td><code>string</code></td><td>The AWS service that is sending logs.</td></tr>
<tr><td><CopyableCode code="log_type" /></td><td><code>string</code></td><td>The type of logs being delivered. Only mandatory when the resourceArn could match more than one. In such a case, the error message will contain all the possible options.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags that have been assigned to this delivery source.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html"><code>AWS::Logs::DeliverySource</code></a>.

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
Gets all <code>delivery_sources</code> in a region.
```sql
SELECT
region,
name,
arn,
resource_arns,
resource_arn,
service,
log_type,
tags
FROM aws.logs.delivery_sources
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>delivery_source</code>.
```sql
SELECT
region,
name,
arn,
resource_arns,
resource_arn,
service,
log_type,
tags
FROM aws.logs.delivery_sources
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>delivery_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.delivery_sources (
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
INSERT INTO aws.logs.delivery_sources (
 Name,
 ResourceArn,
 LogType,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ ResourceArn }}',
 '{{ LogType }}',
 '{{ Tags }}',
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
  - name: delivery_source
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ResourceArn
        value: '{{ ResourceArn }}'
      - name: LogType
        value: '{{ LogType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.delivery_sources
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>delivery_sources</code> resource, the following permissions are required:

### Create
```json
logs:PutDeliverySource,
logs:GetDeliverySource,
logs:ListTagsForResource,
logs:TagResource,
logs:AllowVendedLogDeliveryForResource,
codewhisperer:AllowVendedLogDeliveryForResource,
autoloop:AllowVendedLogDeliveryForResource,
workmail:AllowVendedLogDeliveryForResource
```

### Read
```json
logs:GetDeliverySource,
logs:ListTagsForResource
```

### Update
```json
logs:PutDeliverySource,
logs:GetDeliverySource,
logs:ListTagsForResource,
logs:TagResource,
logs:UntagResource
```

### Delete
```json
logs:DeleteDeliverySource
```

### List
```json
logs:DescribeDeliverySources
```
