---
title: canary_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - canary_tags
  - synthetics
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

Expands all tag keys and values for <code>canaries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canary_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Synthetics::Canary</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.synthetics.canary_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the canary.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the canary</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>State of the canary</td></tr>
<tr><td><CopyableCode code="code" /></td><td><code>object</code></td><td>Provide the canary script source</td></tr>
<tr><td><CopyableCode code="artifact_s3_location" /></td><td><code>string</code></td><td>Provide the s3 bucket output location for test results</td></tr>
<tr><td><CopyableCode code="artifact_config" /></td><td><code>object</code></td><td>Provide artifact configuration</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>Frequency to run your canaries</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>Lambda Execution role used to run your canaries</td></tr>
<tr><td><CopyableCode code="runtime_version" /></td><td><code>string</code></td><td>Runtime version of Synthetics Library</td></tr>
<tr><td><CopyableCode code="success_retention_period" /></td><td><code>integer</code></td><td>Retention period of successful canary runs represented in number of days</td></tr>
<tr><td><CopyableCode code="failure_retention_period" /></td><td><code>integer</code></td><td>Retention period of failed canary runs represented in number of days</td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td>Provide VPC Configuration if enabled.</td></tr>
<tr><td><CopyableCode code="run_config" /></td><td><code>object</code></td><td>Provide canary run configuration</td></tr>
<tr><td><CopyableCode code="start_canary_after_creation" /></td><td><code>boolean</code></td><td>Runs canary if set to True. Default is False</td></tr>
<tr><td><CopyableCode code="visual_reference" /></td><td><code>object</code></td><td>Visual reference configuration for visual testing</td></tr>
<tr><td><CopyableCode code="delete_lambda_resources_on_canary_deletion" /></td><td><code>boolean</code></td><td>Deletes associated lambda resources created by Synthetics if set to True. Default is False</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>canaries</code> in a region.
```sql
SELECT
region,
name,
id,
state,
code,
artifact_s3_location,
artifact_config,
schedule,
execution_role_arn,
runtime_version,
success_retention_period,
failure_retention_period,
vpc_config,
run_config,
start_canary_after_creation,
visual_reference,
delete_lambda_resources_on_canary_deletion,
tag_key,
tag_value
FROM aws.synthetics.canary_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>canary_tags</code> resource, see <a href="/providers/aws/synthetics/canaries/#permissions"><code>canaries</code></a>


