---
title: experiment
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment
  - evidently
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>experiment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Experiment.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.evidently.experiment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>project</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>running_status</code></td><td><code>object</code></td><td>Start Experiment. Default is False</td></tr>
<tr><td><code>randomization_salt</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>treatments</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>metric_goals</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>sampling_rate</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>online_ab_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>segment</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>remove_segment</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
name,
project,
description,
running_status,
randomization_salt,
treatments,
metric_goals,
sampling_rate,
online_ab_config,
segment,
remove_segment,
tags
FROM aws.evidently.experiment
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>experiment</code> resource, the following permissions are required:

### Read
```json
evidently:GetExperiment,
evidently:ListTagsForResource
```

### Update
```json
evidently:UpdateExperiment,
evidently:TagResource,
evidently:UntagResource,
evidently:GetExperiment,
evidently:StartExperiment,
evidently:StopExperiment
```

### Delete
```json
evidently:DeleteExperiment,
evidently:UntagResource,
evidently:GetExperiment
```

