---
title: custom_action_type
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_action_type
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
Gets an individual <code>custom_action_type</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_action_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>custom_action_type</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codepipeline.custom_action_type</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>category</code></td><td><code>string</code></td><td>The category of the custom action, such as a build action or a test action.</td></tr>
<tr><td><code>configuration_properties</code></td><td><code>array</code></td><td>The configuration properties for the custom action.</td></tr>
<tr><td><code>input_artifact_details</code></td><td><code>object</code></td><td>The details of the input artifact for the action, such as its commit ID.</td></tr>
<tr><td><code>output_artifact_details</code></td><td><code>object</code></td><td>The details of the output artifact of the action, such as its commit ID.</td></tr>
<tr><td><code>provider</code></td><td><code>string</code></td><td>The provider of the service used in the custom action, such as AWS CodeDeploy.</td></tr>
<tr><td><code>settings</code></td><td><code>object</code></td><td>URLs that provide users information about this custom action.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Any tags assigned to the custom action.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The version identifier of the custom action.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>custom_action_type</code> resource, the following permissions are required:

### Read
```json
codepipeline:ListActionTypes,
codepipeline:ListTagsForResource
```

### Update
```json
codepipeline:ListActionTypes,
codepipeline:TagResource,
codepipeline:UntagResource
```

### Delete
```json
codepipeline:DeleteCustomActionType,
codepipeline:ListActionTypes
```


## Example
```sql
SELECT
region,
category,
configuration_properties,
input_artifact_details,
output_artifact_details,
provider,
settings,
tags,
version,
id
FROM awscc.codepipeline.custom_action_type
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Category&gt;'
AND data__Identifier = '&lt;Provider&gt;'
AND data__Identifier = '&lt;Version&gt;'
```
