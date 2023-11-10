---
title: job
hide_title: false
hide_table_of_contents: false
keywords:
  - job
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
Gets an individual <code>job</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>job</td></tr>
<tr><td><b>Id</b></td><td><code>aws.databrew.job</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dataset_name</code></td><td><code>string</code></td><td>Dataset name</td></tr>
<tr><td><code>encryption_key_arn</code></td><td><code>string</code></td><td>Encryption Key Arn</td></tr>
<tr><td><code>encryption_mode</code></td><td><code>string</code></td><td>Encryption mode</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Job name</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>Job type</td></tr>
<tr><td><code>log_subscription</code></td><td><code>string</code></td><td>Log subscription</td></tr>
<tr><td><code>max_capacity</code></td><td><code>integer</code></td><td>Max capacity</td></tr>
<tr><td><code>max_retries</code></td><td><code>integer</code></td><td>Max retries</td></tr>
<tr><td><code>outputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>data_catalog_outputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>database_outputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>output_location</code></td><td><code>object</code></td><td>Output location</td></tr>
<tr><td><code>project_name</code></td><td><code>string</code></td><td>Project name</td></tr>
<tr><td><code>recipe</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>Role arn</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>timeout</code></td><td><code>integer</code></td><td>Timeout</td></tr>
<tr><td><code>job_sample</code></td><td><code>object</code></td><td>Job Sample</td></tr>
<tr><td><code>profile_configuration</code></td><td><code>object</code></td><td>Profile Job configuration</td></tr>
<tr><td><code>validation_configurations</code></td><td><code>array</code></td><td>Data quality rules configuration</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
tags,
timeout,
job_sample,
profile_configuration,
validation_configurations
FROM aws.databrew.job
WHERE region = 'us-east-1'
AND data__Identifier = '<Name>'
```
