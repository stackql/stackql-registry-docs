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

Creates, updates, deletes or gets a <code>custom_action_type</code> resource or lists <code>custom_action_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_action_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CodePipeline::CustomActionType resource creates a custom action for activities that aren't included in the CodePipeline default actions, such as running an internally developed build process or a test suite. You can use these custom actions in the stage of a pipeline.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codepipeline.custom_action_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="category" /></td><td><code>string</code></td><td>The category of the custom action, such as a build action or a test action.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Category, InputArtifactDetails, OutputArtifactDetails, Provider, Version, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>custom_action_types</code> in a region.
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
FROM aws.codepipeline.custom_action_types
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>custom_action_type</code>.
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
FROM aws.codepipeline.custom_action_types
WHERE region = 'us-east-1' AND data__Identifier = '<Category>|<Provider>|<Version>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_action_type</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.codepipeline.custom_action_types (
 Category,
 InputArtifactDetails,
 OutputArtifactDetails,
 Provider,
 Version,
 region
)
SELECT 
'{{ Category }}',
 '{{ InputArtifactDetails }}',
 '{{ OutputArtifactDetails }}',
 '{{ Provider }}',
 '{{ Version }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Category }}',
 '{{ ConfigurationProperties }}',
 '{{ InputArtifactDetails }}',
 '{{ OutputArtifactDetails }}',
 '{{ Provider }}',
 '{{ Settings }}',
 '{{ Tags }}',
 '{{ Version }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: custom_action_type
    props:
      - name: Category
        value: '{{ Category }}'
      - name: ConfigurationProperties
        value:
          - Description: '{{ Description }}'
            Key: '{{ Key }}'
            Name: '{{ Name }}'
            Queryable: '{{ Queryable }}'
            Required: '{{ Required }}'
            Secret: '{{ Secret }}'
            Type: '{{ Type }}'
      - name: InputArtifactDetails
        value:
          MaximumCount: '{{ MaximumCount }}'
          MinimumCount: '{{ MinimumCount }}'
      - name: OutputArtifactDetails
        value: null
      - name: Provider
        value: '{{ Provider }}'
      - name: Settings
        value:
          EntityUrlTemplate: '{{ EntityUrlTemplate }}'
          ExecutionUrlTemplate: '{{ ExecutionUrlTemplate }}'
          RevisionUrlTemplate: '{{ RevisionUrlTemplate }}'
          ThirdPartyConfigurationUrl: '{{ ThirdPartyConfigurationUrl }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Version
        value: '{{ Version }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### List
```json
codepipeline:ListActionTypes
```

