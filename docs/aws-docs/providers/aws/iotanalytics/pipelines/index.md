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


Used to retrieve a list of <code>pipelines</code> in a region or to create or delete a <code>pipelines</code> resource, use <code>pipeline</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoTAnalytics::Pipeline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotanalytics.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="pipeline_name" /></td><td><code>string</code></td><td></td></tr>
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
pipeline_name
FROM aws.iotanalytics.pipelines
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
 "PipelineActivities": [
  {
   "SelectAttributes": {
    "Next": "{{ Next }}",
    "Attributes": [
     "{{ Attributes[0] }}"
    ],
    "Name": "{{ Name }}"
   },
   "Datastore": {
    "DatastoreName": "{{ DatastoreName }}",
    "Name": "{{ Name }}"
   },
   "Filter": {
    "Filter": "{{ Filter }}",
    "Next": "{{ Next }}",
    "Name": "{{ Name }}"
   },
   "AddAttributes": {
    "Next": "{{ Next }}",
    "Attributes": {},
    "Name": "{{ Name }}"
   },
   "Channel": {
    "ChannelName": "{{ ChannelName }}",
    "Next": "{{ Next }}",
    "Name": "{{ Name }}"
   },
   "DeviceShadowEnrich": {
    "Attribute": "{{ Attribute }}",
    "Next": "{{ Next }}",
    "ThingName": "{{ ThingName }}",
    "RoleArn": "{{ RoleArn }}",
    "Name": "{{ Name }}"
   },
   "Math": {
    "Attribute": "{{ Attribute }}",
    "Next": "{{ Next }}",
    "Math": "{{ Math }}",
    "Name": "{{ Name }}"
   },
   "Lambda": {
    "BatchSize": "{{ BatchSize }}",
    "Next": "{{ Next }}",
    "LambdaName": "{{ LambdaName }}",
    "Name": "{{ Name }}"
   },
   "DeviceRegistryEnrich": {
    "Attribute": "{{ Attribute }}",
    "Next": "{{ Next }}",
    "ThingName": "{{ ThingName }}",
    "RoleArn": "{{ RoleArn }}",
    "Name": "{{ Name }}"
   },
   "RemoveAttributes": {
    "Next": "{{ Next }}",
    "Attributes": [
     "{{ Attributes[0] }}"
    ],
    "Name": "{{ Name }}"
   }
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.iotanalytics.pipelines (
 PipelineActivities,
 region
)
SELECT 
{{ PipelineActivities }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PipelineName": "{{ PipelineName }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "PipelineActivities": [
  {
   "SelectAttributes": {
    "Next": "{{ Next }}",
    "Attributes": [
     "{{ Attributes[0] }}"
    ],
    "Name": "{{ Name }}"
   },
   "Datastore": {
    "DatastoreName": "{{ DatastoreName }}",
    "Name": "{{ Name }}"
   },
   "Filter": {
    "Filter": "{{ Filter }}",
    "Next": "{{ Next }}",
    "Name": "{{ Name }}"
   },
   "AddAttributes": {
    "Next": "{{ Next }}",
    "Attributes": {},
    "Name": "{{ Name }}"
   },
   "Channel": {
    "ChannelName": "{{ ChannelName }}",
    "Next": "{{ Next }}",
    "Name": "{{ Name }}"
   },
   "DeviceShadowEnrich": {
    "Attribute": "{{ Attribute }}",
    "Next": "{{ Next }}",
    "ThingName": "{{ ThingName }}",
    "RoleArn": "{{ RoleArn }}",
    "Name": "{{ Name }}"
   },
   "Math": {
    "Attribute": "{{ Attribute }}",
    "Next": "{{ Next }}",
    "Math": "{{ Math }}",
    "Name": "{{ Name }}"
   },
   "Lambda": {
    "BatchSize": "{{ BatchSize }}",
    "Next": "{{ Next }}",
    "LambdaName": "{{ LambdaName }}",
    "Name": "{{ Name }}"
   },
   "DeviceRegistryEnrich": {
    "Attribute": "{{ Attribute }}",
    "Next": "{{ Next }}",
    "ThingName": "{{ ThingName }}",
    "RoleArn": "{{ RoleArn }}",
    "Name": "{{ Name }}"
   },
   "RemoveAttributes": {
    "Next": "{{ Next }}",
    "Attributes": [
     "{{ Attributes[0] }}"
    ],
    "Name": "{{ Name }}"
   }
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iotanalytics.pipelines (
 PipelineName,
 Tags,
 PipelineActivities,
 region
)
SELECT 
 {{ PipelineName }},
 {{ Tags }},
 {{ PipelineActivities }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
iotanalytics:DeletePipeline
```

### List
```json
iotanalytics:ListPipelines
```

