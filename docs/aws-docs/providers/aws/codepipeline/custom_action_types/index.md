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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>custom_action_types</code> in a region or to create or delete a <code>custom_action_types</code> resource, use <code>custom_action_type</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_action_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CodePipeline::CustomActionType resource creates a custom action for activities that aren't included in the CodePipeline default actions, such as running an internally developed build process or a test suite. You can use these custom actions in the stage of a pipeline.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codepipeline.custom_action_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="category" /></td><td><code>string</code></td><td>The category of the custom action, such as a build action or a test action.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the service used in the custom action, such as AWS CodeDeploy.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version identifier of the custom action.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
category,
provider,
version
FROM aws.codepipeline.custom_action_types
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Category": "{{ Category }}",
 "InputArtifactDetails": {
  "MaximumCount": "{{ MaximumCount }}",
  "MinimumCount": "{{ MinimumCount }}"
 },
 "OutputArtifactDetails": null,
 "Provider": "{{ Provider }}",
 "Version": "{{ Version }}"
}
>>>
--required properties only
INSERT INTO aws.codepipeline.custom_action_types (
 Category,
 InputArtifactDetails,
 OutputArtifactDetails,
 Provider,
 Version,
 region
)
SELECT 
{{ .Category }},
 {{ .InputArtifactDetails }},
 {{ .OutputArtifactDetails }},
 {{ .Provider }},
 {{ .Version }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Category": "{{ Category }}",
 "ConfigurationProperties": [
  {
   "Description": "{{ Description }}",
   "Key": "{{ Key }}",
   "Name": "{{ Name }}",
   "Queryable": "{{ Queryable }}",
   "Required": "{{ Required }}",
   "Secret": "{{ Secret }}",
   "Type": "{{ Type }}"
  }
 ],
 "InputArtifactDetails": {
  "MaximumCount": "{{ MaximumCount }}",
  "MinimumCount": "{{ MinimumCount }}"
 },
 "OutputArtifactDetails": null,
 "Provider": "{{ Provider }}",
 "Settings": {
  "EntityUrlTemplate": "{{ EntityUrlTemplate }}",
  "ExecutionUrlTemplate": "{{ ExecutionUrlTemplate }}",
  "RevisionUrlTemplate": "{{ RevisionUrlTemplate }}",
  "ThirdPartyConfigurationUrl": "{{ ThirdPartyConfigurationUrl }}"
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Version": "{{ Version }}"
}
>>>
--all properties
INSERT INTO aws.codepipeline.custom_action_types (
 Category,
 ConfigurationProperties,
 InputArtifactDetails,
 OutputArtifactDetails,
 Provider,
 Settings,
 Tags,
 Version,
 region
)
SELECT 
 {{ .Category }},
 {{ .ConfigurationProperties }},
 {{ .InputArtifactDetails }},
 {{ .OutputArtifactDetails }},
 {{ .Provider }},
 {{ .Settings }},
 {{ .Tags }},
 {{ .Version }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.codepipeline.custom_action_types
WHERE data__Identifier = '<Category|Provider|Version>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>custom_action_types</code> resource, the following permissions are required:

### Create
```json
codepipeline:CreateCustomActionType,
codepipeline:TagResource,
codepipeline:ListActionTypes
```

### Delete
```json
codepipeline:DeleteCustomActionType,
codepipeline:ListActionTypes
```

### List
```json
codepipeline:ListActionTypes
```

