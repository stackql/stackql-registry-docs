---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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
Retrieves a list of <code>jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>jobs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.databrew.jobs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Job name</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>jobs</code> resource, the following permissions are required:

### Create
```json
databrew:CreateProfileJob,
databrew:CreateRecipeJob,
databrew:TagResource,
databrew:UntagResource,
iam:PassRole
```

### List
```json
databrew:ListJobs,
databrew:ListTagsForResource,
iam:ListRoles
```


## Example
```sql
SELECT
region,
name
FROM awscc.databrew.jobs
WHERE region = 'us-east-1'
```
