---
title: job_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - job_tags
  - databrew
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

Expands all tag keys and values for <code>jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Job.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.job_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dataset_name" /></td><td><code>string</code></td><td>Dataset name</td></tr>
<tr><td><CopyableCode code="encryption_key_arn" /></td><td><code>string</code></td><td>Encryption Key Arn</td></tr>
<tr><td><CopyableCode code="encryption_mode" /></td><td><code>string</code></td><td>Encryption mode</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Job name</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Job type</td></tr>
<tr><td><CopyableCode code="log_subscription" /></td><td><code>string</code></td><td>Log subscription</td></tr>
<tr><td><CopyableCode code="max_capacity" /></td><td><code>integer</code></td><td>Max capacity</td></tr>
<tr><td><CopyableCode code="max_retries" /></td><td><code>integer</code></td><td>Max retries</td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_catalog_outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="database_outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="output_location" /></td><td><code>object</code></td><td>Output location</td></tr>
<tr><td><CopyableCode code="project_name" /></td><td><code>string</code></td><td>Project name</td></tr>
<tr><td><CopyableCode code="recipe" /></td><td><code>object</code></td><td>Resource schema for AWS::DataBrew::Recipe.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role arn</td></tr>
<tr><td><CopyableCode code="timeout" /></td><td><code>integer</code></td><td>Timeout</td></tr>
<tr><td><CopyableCode code="job_sample" /></td><td><code>object</code></td><td>Job Sample</td></tr>
<tr><td><CopyableCode code="profile_configuration" /></td><td><code>object</code></td><td>Profile Job configuration</td></tr>
<tr><td><CopyableCode code="validation_configurations" /></td><td><code>array</code></td><td>Data quality rules configuration</td></tr>
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
Expands tags for all <code>jobs</code> in a region.
```sql
SELECT
region,
dataset_name,
encryption_key_arn,
encryption_mode,
name,
type,
log_subscription,
max_capacity,
max_retries,
outputs,
data_catalog_outputs,
database_outputs,
output_location,
project_name,
recipe,
role_arn,
timeout,
job_sample,
profile_configuration,
validation_configurations,
tag_key,
tag_value
FROM aws.databrew.job_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>job_tags</code> resource, see <a href="/providers/aws/databrew/jobs/#permissions"><code>jobs</code></a>


