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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>feature_group</code> resource, use <code>feature_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::FeatureGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.feature_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="feature_group_name" /></td><td><code>string</code></td><td>The Name of the FeatureGroup.</td></tr>
<tr><td><CopyableCode code="record_identifier_feature_name" /></td><td><code>string</code></td><td>The Record Identifier Feature Name.</td></tr>
<tr><td><CopyableCode code="event_time_feature_name" /></td><td><code>string</code></td><td>The Event Time Feature Name.</td></tr>
<tr><td><CopyableCode code="feature_definitions" /></td><td><code>array</code></td><td>An Array of Feature Definition</td></tr>
<tr><td><CopyableCode code="online_store_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="offline_store_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="throughput_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description about the FeatureGroup.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A timestamp of FeatureGroup creation time.</td></tr>
<tr><td><CopyableCode code="feature_group_status" /></td><td><code>string</code></td><td>The status of the feature group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pair to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1' AND data__Identifier = '<FeatureGroupName>';
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

