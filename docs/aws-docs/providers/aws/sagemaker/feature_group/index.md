---
title: feature_group
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_group
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>feature_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::FeatureGroup</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.feature_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>feature_group_name</code></td><td><code>string</code></td><td>The Name of the FeatureGroup.</td></tr>
<tr><td><code>record_identifier_feature_name</code></td><td><code>string</code></td><td>The Record Identifier Feature Name.</td></tr>
<tr><td><code>event_time_feature_name</code></td><td><code>string</code></td><td>The Event Time Feature Name.</td></tr>
<tr><td><code>feature_definitions</code></td><td><code>array</code></td><td>An Array of Feature Definition</td></tr>
<tr><td><code>online_store_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>offline_store_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>throughput_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description about the FeatureGroup.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>A timestamp of FeatureGroup creation time.</td></tr>
<tr><td><code>feature_group_status</code></td><td><code>string</code></td><td>The status of the feature group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pair to apply to this resource.</td></tr>
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
feature_group_name,
record_identifier_feature_name,
event_time_feature_name,
feature_definitions,
online_store_config,
offline_store_config,
throughput_config,
role_arn,
description,
creation_time,
feature_group_status,
tags
FROM aws.sagemaker.feature_group
WHERE data__Identifier = '<FeatureGroupName>';
```

## Permissions

To operate on the <code>feature_group</code> resource, the following permissions are required:

### Update
```json
sagemaker:UpdateFeatureGroup,
sagemaker:DescribeFeatureGroup,
sagemaker:AddTags,
sagemaker:ListTags,
sagemaker:DeleteTags
```

### Read
```json
sagemaker:DescribeFeatureGroup,
sagemaker:ListTags
```

### Delete
```json
sagemaker:DeleteFeatureGroup,
sagemaker:DescribeFeatureGroup
```

