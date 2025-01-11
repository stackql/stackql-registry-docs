---
title: sinks
hide_title: false
hide_table_of_contents: false
keywords:
  - sinks
  - oam
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

Creates, updates, deletes or gets a <code>sink</code> resource or lists <code>sinks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Oam::Sink</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.oam.sinks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the ObservabilityAccessManager Sink</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the ObservabilityAccessManager Sink.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>The policy of this ObservabilityAccessManager Sink.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Tags to apply to the sink</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-oam-sink.html"><code>AWS::Oam::Sink</code></a>.

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
Gets all <code>sinks</code> in a region.
```sql
SELECT
region,
arn,
name,
policy,
tags
FROM aws.oam.sinks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>sink</code>.
```sql
SELECT
region,
arn,
name,
policy,
tags
FROM aws.oam.sinks
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sink</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.oam.sinks (
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
INSERT INTO aws.oam.sinks (
 Name,
 Policy,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Policy }}',
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
  - name: sink
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Policy
        value: {}
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.oam.sinks
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>sinks</code> resource, the following permissions are required:

### Create
```json
oam:CreateSink,
oam:PutSinkPolicy,
oam:GetSinkPolicy,
oam:GetSink,
oam:TagResource,
oam:ListTagsForResource
```

### Delete
```json
oam:DeleteSink,
oam:GetSinkPolicy,
oam:GetSink
```

### List
```json
oam:ListSinks
```

### Read
```json
oam:GetSinkPolicy,
oam:GetSink,
oam:ListTagsForResource
```

### Update
```json
oam:PutSinkPolicy,
oam:GetSinkPolicy,
oam:GetSink,
oam:TagResource,
oam:UntagResource,
oam:ListTagsForResource
```
