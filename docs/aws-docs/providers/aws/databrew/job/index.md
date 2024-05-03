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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>job</code> resource, use <code>jobs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Job.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.job" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dataset_name" /></td><td><code>string</code></td><td>Dataset name</td></tr>
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
<tr><td><CopyableCode code="recipe" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role arn</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout" /></td><td><code>integer</code></td><td>Timeout</td></tr>
<tr><td><CopyableCode code="job_sample" /></td><td><code>object</code></td><td>Job Sample</td></tr>
<tr><td><CopyableCode code="profile_configuration" /></td><td><code>object</code></td><td>Profile Job configuration</td></tr>
<tr><td><CopyableCode code="validation_configurations" /></td><td><code>array</code></td><td>Data quality rules configuration</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>job</code> resource, the following permissions are required:

### Read
```json
databrew:DescribeJob,
databrew:ListTagsForResource,
iam:ListRoles
```

### Update
```json
databrew:UpdateProfileJob,
databrew:UpdateRecipeJob,
iam:PassRole
```

### Delete
```json
databrew:DeleteJob
```

