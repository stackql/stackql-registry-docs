---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
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

Creates, updates, deletes or gets a <code>pipeline</code> resource or lists <code>pipelines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CodePipeline::Pipeline resource creates a CodePipeline pipeline that describes how software changes go through a release process.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codepipeline.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="artifact_stores" /></td><td><code>array</code></td><td>A mapping of artifactStore objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.</td></tr>
<tr><td><CopyableCode code="disable_inbound_stage_transitions" /></td><td><code>array</code></td><td>Represents the input of a DisableStageTransition action.</td></tr>
<tr><td><CopyableCode code="stages" /></td><td><code>array</code></td><td>Represents information about a stage and its definition.</td></tr>
<tr><td><CopyableCode code="execution_mode" /></td><td><code>string</code></td><td>The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.</td></tr>
<tr><td><CopyableCode code="restart_execution_on_update" /></td><td><code>boolean</code></td><td>Indicates whether to rerun the CodePipeline pipeline after you update it.</td></tr>
<tr><td><CopyableCode code="triggers" /></td><td><code>array</code></td><td>The trigger configuration specifying a type of event, such as Git tags, that starts the pipeline.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the pipeline.</td></tr>
<tr><td><CopyableCode code="variables" /></td><td><code>array</code></td><td>A list that defines the pipeline variables for a pipeline resource. Variable names can have alphanumeric and underscore characters, and the values must match &#91;A-Za-z0-9@\-_&#93;+.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the pipeline.</td></tr>
<tr><td><CopyableCode code="artifact_store" /></td><td><code>object</code></td><td>The S3 bucket where artifacts for the pipeline are stored.</td></tr>
<tr><td><CopyableCode code="pipeline_type" /></td><td><code>string</code></td><td>CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Specifies the tags applied to the pipeline.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html"><code>AWS::CodePipeline::Pipeline</code></a>.

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
    <td><CopyableCode code="Stages, RoleArn, region" /></td>
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
Gets all <code>pipelines</code> in a region.
```sql
SELECT
region,
artifact_stores,
disable_inbound_stage_transitions,
stages,
execution_mode,
restart_execution_on_update,
triggers,
role_arn,
name,
variables,
version,
artifact_store,
pipeline_type,
tags
FROM aws.codepipeline.pipelines
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>pipeline</code>.
```sql
SELECT
region,
artifact_stores,
disable_inbound_stage_transitions,
stages,
execution_mode,
restart_execution_on_update,
triggers,
role_arn,
name,
variables,
version,
artifact_store,
pipeline_type,
tags
FROM aws.codepipeline.pipelines
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipeline</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.codepipeline.pipelines (
 Stages,
 RoleArn,
 region
)
SELECT 
'{{ Stages }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.codepipeline.pipelines (
 ArtifactStores,
 DisableInboundStageTransitions,
 Stages,
 ExecutionMode,
 RestartExecutionOnUpdate,
 Triggers,
 RoleArn,
 Name,
 Variables,
 ArtifactStore,
 PipelineType,
 Tags,
 region
)
SELECT 
 '{{ ArtifactStores }}',
 '{{ DisableInboundStageTransitions }}',
 '{{ Stages }}',
 '{{ ExecutionMode }}',
 '{{ RestartExecutionOnUpdate }}',
 '{{ Triggers }}',
 '{{ RoleArn }}',
 '{{ Name }}',
 '{{ Variables }}',
 '{{ ArtifactStore }}',
 '{{ PipelineType }}',
 '{{ Tags }}',
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
  - name: pipeline
    props:
      - name: ArtifactStores
        value:
          - ArtifactStore:
              Type: '{{ Type }}'
              EncryptionKey:
                Type: '{{ Type }}'
                Id: '{{ Id }}'
              Location: '{{ Location }}'
            Region: '{{ Region }}'
      - name: DisableInboundStageTransitions
        value:
          - StageName: '{{ StageName }}'
            Reason: '{{ Reason }}'
      - name: Stages
        value:
          - Blockers:
              - Name: '{{ Name }}'
                Type: '{{ Type }}'
            Actions:
              - ActionTypeId:
                  Owner: '{{ Owner }}'
                  Category: '{{ Category }}'
                  Version: '{{ Version }}'
                  Provider: '{{ Provider }}'
                Configuration: {}
                InputArtifacts:
                  - Name: '{{ Name }}'
                OutputArtifacts:
                  - Name: '{{ Name }}'
                    Files:
                      - '{{ Files[0] }}'
                Commands:
                  - '{{ Commands[0] }}'
                OutputVariables:
                  - '{{ OutputVariables[0] }}'
                Region: '{{ Region }}'
                Namespace: '{{ Namespace }}'
                RoleArn: '{{ RoleArn }}'
                RunOrder: '{{ RunOrder }}'
                Name: '{{ Name }}'
                TimeoutInMinutes: '{{ TimeoutInMinutes }}'
            Name: '{{ Name }}'
            OnFailure:
              Result: '{{ Result }}'
              RetryConfiguration:
                RetryMode: '{{ RetryMode }}'
              Conditions:
                - Result: '{{ Result }}'
                  Rules:
                    - RuleTypeId:
                        Owner: '{{ Owner }}'
                        Category: '{{ Category }}'
                        Version: '{{ Version }}'
                        Provider: '{{ Provider }}'
                      Configuration: {}
                      InputArtifacts:
                        - null
                      Region: '{{ Region }}'
                      RoleArn: '{{ RoleArn }}'
                      Name: '{{ Name }}'
            OnSuccess:
              Conditions:
                - null
            BeforeEntry:
              Conditions:
                - null
      - name: ExecutionMode
        value: '{{ ExecutionMode }}'
      - name: RestartExecutionOnUpdate
        value: '{{ RestartExecutionOnUpdate }}'
      - name: Triggers
        value:
          - GitConfiguration:
              Push:
                - FilePaths:
                    Includes:
                      - '{{ Includes[0] }}'
                    Excludes:
                      - '{{ Excludes[0] }}'
                  Branches:
                    Includes:
                      - '{{ Includes[0] }}'
                    Excludes:
                      - '{{ Excludes[0] }}'
                  Tags:
                    Includes:
                      - '{{ Includes[0] }}'
                    Excludes:
                      - '{{ Excludes[0] }}'
              SourceActionName: '{{ SourceActionName }}'
              PullRequest:
                - FilePaths: null
                  Events:
                    - '{{ Events[0] }}'
                  Branches: null
            ProviderType: '{{ ProviderType }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Variables
        value:
          - DefaultValue: '{{ DefaultValue }}'
            Description: '{{ Description }}'
            Name: '{{ Name }}'
      - name: ArtifactStore
        value: null
      - name: PipelineType
        value: '{{ PipelineType }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.codepipeline.pipelines
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pipelines</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:PassRole,
codepipeline:GetPipeline,
codepipeline:CreatePipeline,
codepipeline:DisableStageTransition,
codepipeline:GetPipelineState,
codepipeline:TagResource,
codestar-connections:PassConnection
```

### Read
```json
codepipeline:GetPipeline,
codepipeline:ListTagsForResource,
codepipeline:GetPipelineState
```

### Update
```json
iam:GetRole,
iam:PassRole,
codepipeline:EnableStageTransition,
codepipeline:StartPipelineExecution,
codepipeline:GetPipeline,
codepipeline:UpdatePipeline,
codepipeline:GetPipelineState,
codepipeline:DisableStageTransition,
codepipeline:TagResource,
codepipeline:UntagResource,
codestar-connections:PassConnection
```

### Delete
```json
codepipeline:GetPipeline,
codepipeline:DeletePipeline
```

### List
```json
codepipeline:ListPipelines
```
