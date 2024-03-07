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
<tr><td><b>Description</b></td><td>feature_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.feature_group</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.sagemaker.feature_group
WHERE region = 'us-east-1'
AND data__Identifier = '{FeatureGroupName}';
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

