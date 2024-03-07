---
title: custom_action_types
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_action_types
  - codepipeline
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>custom_action_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_action_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>custom_action_types</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codepipeline.custom_action_types</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>category</code></td><td><code>string</code></td><td>The category of the custom action, such as a build action or a test action.</td></tr>
<tr><td><code>provider</code></td><td><code>string</code></td><td>The provider of the service used in the custom action, such as AWS CodeDeploy.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The version identifier of the custom action.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>custom_action_types</code> resource, the following permissions are required:

### Create
```json
codepipeline:CreateCustomActionType,
codepipeline:TagResource,
codepipeline:ListActionTypes
```

### List
```json
codepipeline:ListActionTypes
```


## Example
```sql
SELECT
region,
category,
provider,
version
FROM awscc.codepipeline.custom_action_types
WHERE region = 'us-east-1'
```
