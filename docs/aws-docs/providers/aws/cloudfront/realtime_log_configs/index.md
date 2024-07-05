---
title: realtime_log_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - realtime_log_configs
  - cloudfront
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

Creates, updates, deletes or gets a <code>realtime_log_config</code> resource or lists <code>realtime_log_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>realtime_log_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::RealtimeLogConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.realtime_log_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="end_points" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rate" /></td><td><code>number</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, EndPoints, Fields, SamplingRate, region" /></td>
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
Gets all <code>realtime_log_configs</code> in a region.
```sql
SELECT
region,
arn,
end_points,
fields,
name,
sampling_rate
FROM aws.cloudfront.realtime_log_configs
;
```
Gets all properties from an individual <code>realtime_log_config</code>.
```sql
SELECT
region,
arn,
end_points,
fields,
name,
sampling_rate
FROM aws.cloudfront.realtime_log_configs
WHERE data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>realtime_log_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudfront.realtime_log_configs (
 EndPoints,
 Fields,
 Name,
 SamplingRate,
 region
)
SELECT 
'{{ EndPoints }}',
 '{{ Fields }}',
 '{{ Name }}',
 '{{ SamplingRate }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudfront.realtime_log_configs (
 EndPoints,
 Fields,
 Name,
 SamplingRate,
 region
)
SELECT 
 '{{ EndPoints }}',
 '{{ Fields }}',
 '{{ Name }}',
 '{{ SamplingRate }}',
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
  - name: realtime_log_config
    props:
      - name: EndPoints
        value:
          - KinesisStreamConfig:
              RoleArn: '{{ RoleArn }}'
              StreamArn: '{{ StreamArn }}'
            StreamType: '{{ StreamType }}'
      - name: Fields
        value:
          - '{{ Fields[0] }}'
      - name: Name
        value: '{{ Name }}'
      - name: SamplingRate
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudfront.realtime_log_configs
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>realtime_log_configs</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateRealtimeLogConfig,
iam:PassRole
```

### Delete
```json
cloudfront:DeleteRealtimeLogConfig,
cloudfront:GetRealtimeLogConfig
```

### List
```json
cloudfront:ListRealtimeLogConfigs
```

### Read
```json
cloudfront:GetRealtimeLogConfig
```

### Update
```json
cloudfront:UpdateRealtimeLogConfig,
cloudfront:GetRealtimeLogConfig,
iam:PassRole
```

