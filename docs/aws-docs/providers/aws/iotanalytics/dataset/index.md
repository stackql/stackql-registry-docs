---
title: dataset
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset
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
Gets an individual <code>dataset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoTAnalytics::Dataset</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotanalytics.dataset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>late_data_rules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>dataset_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>content_delivery_rules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>triggers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>versioning_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>retention_period</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
actions,
late_data_rules,
dataset_name,
content_delivery_rules,
triggers,
versioning_configuration,
id,
retention_period,
tags
FROM aws.iotanalytics.dataset
WHERE data__Identifier = '<DatasetName>';
```

## Permissions

To operate on the <code>dataset</code> resource, the following permissions are required:

### Read
```json
iotanalytics:DescribeDataset,
iotanalytics:ListTagsForResource
```

### Update
```json
iotanalytics:UpdateDataset,
iotanalytics:TagResource,
iotanalytics:UntagResource
```

### Delete
```json
iotanalytics:DeleteDataset
```

