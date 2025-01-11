---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - iotanalytics
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

Creates, updates, deletes or gets a <code>pipeline</code> resource or lists <code>pipelines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoTAnalytics::Pipeline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotanalytics.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pipeline_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="pipeline_activities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html"><code>AWS::IoTAnalytics::Pipeline</code></a>.

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
    <td><CopyableCode code="PipelineActivities, region" /></td>
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
Gets all <code>pipelines</code> in a region.
```sql
SELECT
region,
id,
pipeline_name,
tags,
pipeline_activities
FROM aws.iotanalytics.pipelines
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>pipeline</code>.
```sql
SELECT
region,
id,
pipeline_name,
tags,
pipeline_activities
FROM aws.iotanalytics.pipelines
WHERE region = 'us-east-1' AND data__Identifier = '<PipelineName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipeline</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotanalytics.pipelines (
 PipelineActivities,
 region
)
SELECT 
'{{ PipelineActivities }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotanalytics.pipelines (
 PipelineName,
 Tags,
 PipelineActivities,
 region
)
SELECT 
 '{{ PipelineName }}',
 '{{ Tags }}',
 '{{ PipelineActivities }}',
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
  - name: pipeline
    props:
      - name: PipelineName
        value: '{{ PipelineName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: PipelineActivities
        value:
          - SelectAttributes:
              Next: '{{ Next }}'
              Attributes:
                - '{{ Attributes[0] }}'
              Name: '{{ Name }}'
            Datastore:
              DatastoreName: '{{ DatastoreName }}'
              Name: '{{ Name }}'
            Filter:
              Filter: '{{ Filter }}'
              Next: '{{ Next }}'
              Name: '{{ Name }}'
            AddAttributes:
              Next: '{{ Next }}'
              Attributes: {}
              Name: '{{ Name }}'
            Channel:
              ChannelName: '{{ ChannelName }}'
              Next: '{{ Next }}'
              Name: '{{ Name }}'
            DeviceShadowEnrich:
              Attribute: '{{ Attribute }}'
              Next: '{{ Next }}'
              ThingName: '{{ ThingName }}'
              RoleArn: '{{ RoleArn }}'
              Name: '{{ Name }}'
            Math:
              Attribute: '{{ Attribute }}'
              Next: '{{ Next }}'
              Math: '{{ Math }}'
              Name: '{{ Name }}'
            Lambda:
              BatchSize: '{{ BatchSize }}'
              Next: '{{ Next }}'
              LambdaName: '{{ LambdaName }}'
              Name: '{{ Name }}'
            DeviceRegistryEnrich:
              Attribute: '{{ Attribute }}'
              Next: '{{ Next }}'
              ThingName: '{{ ThingName }}'
              RoleArn: '{{ RoleArn }}'
              Name: '{{ Name }}'
            RemoveAttributes:
              Next: '{{ Next }}'
              Attributes:
                - '{{ Attributes[0] }}'
              Name: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotanalytics.pipelines
WHERE data__Identifier = '<PipelineName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pipelines</code> resource, the following permissions are required:

### Create
```json
iotanalytics:CreatePipeline
```

### Read
```json
iotanalytics:DescribePipeline,
iotanalytics:ListTagsForResource
```

### Update
```json
iotanalytics:UpdatePipeline,
iotanalytics:TagResource,
iotanalytics:UntagResource
```

### Delete
```json
iotanalytics:DeletePipeline
```

### List
```json
iotanalytics:ListPipelines
```
