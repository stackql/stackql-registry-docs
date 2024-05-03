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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>custom_action_type</code> resource, use <code>custom_action_types</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_action_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CodePipeline::CustomActionType resource creates a custom action for activities that aren't included in the CodePipeline default actions, such as running an internally developed build process or a test suite. You can use these custom actions in the stage of a pipeline.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codepipeline.custom_action_type" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="category" /></td><td><code>string</code></td><td>The category of the custom action, such as a build action or a test action.</td></tr>
<tr><td><CopyableCode code="configuration_properties" /></td><td><code>array</code></td><td>The configuration properties for the custom action.</td></tr>
<tr><td><CopyableCode code="input_artifact_details" /></td><td><code>object</code></td><td>The details of the input artifact for the action, such as its commit ID.</td></tr>
<tr><td><CopyableCode code="output_artifact_details" /></td><td><code>object</code></td><td>The details of the output artifact of the action, such as its commit ID.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the service used in the custom action, such as AWS CodeDeploy.</td></tr>
<tr><td><CopyableCode code="settings" /></td><td><code>object</code></td><td>URLs that provide users information about this custom action.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the custom action.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version identifier of the custom action.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
category,
configuration_properties,
input_artifact_details,
output_artifact_details,
provider,
settings,
tags,
version,
id
FROM aws.codepipeline.custom_action_type
WHERE data__Identifier = '<Category>|<Provider>|<Version>';
```

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

