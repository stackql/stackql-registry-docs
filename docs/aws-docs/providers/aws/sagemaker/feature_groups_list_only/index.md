---
title: feature_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_groups_list_only
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

Lists <code>feature_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/feature_groups/"><code>feature_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::FeatureGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.feature_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="feature_group_name" /></td><td><code>string</code></td><td>The Name of the FeatureGroup.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>feature_groups</code> in a region.
```sql
SELECT
region,
feature_group_name
FROM aws.sagemaker.feature_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>feature_groups_list_only</code> resource, see <a href="/providers/aws/sagemaker/feature_groups/#permissions"><code>feature_groups</code></a>


