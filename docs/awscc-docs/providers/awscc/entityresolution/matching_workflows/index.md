---
title: matching_workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - matching_workflows
  - entityresolution
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>matching_workflows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matching_workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>matching_workflows</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.entityresolution.matching_workflows</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workflow_name</code></td><td><code>undefined</code></td><td>The name of the MatchingWorkflow</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>matching_workflows</code> resource, the following permissions are required:

### Create
```json
entityresolution:CreateMatchingWorkflow,
entityresolution:GetMatchingWorkflow,
entityresolution:TagResource,
kms:CreateGrant,
kms:DescribeKey,
iam:PassRole
```

### List
```json
entityresolution:ListMatchingWorkflows
```


## Example
```sql
SELECT
region,
workflow_name
FROM awscc.entityresolution.matching_workflows
WHERE region = 'us-east-1'
```
