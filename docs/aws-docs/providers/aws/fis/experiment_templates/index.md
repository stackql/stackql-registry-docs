---
title: experiment_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment_templates
  - fis
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

Creates, updates, deletes or gets an <code>experiment_template</code> resource or lists <code>experiment_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::FIS::ExperimentTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fis.experiment_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>A description for the experiment template.</code></td><td></td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>The targets for the experiment.</code></td><td></td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>The actions for the experiment.</code></td><td></td></tr>
<tr><td><CopyableCode code="stop_conditions" /></td><td><code>One or more stop conditions.</code></td><td></td></tr>
<tr><td><CopyableCode code="log_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>The Amazon Resource Name (ARN) of an IAM role that grants the AWS FIS service permission to perform service actions on your behalf.</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="experiment_options" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="Description, StopConditions, Targets, RoleArn, Tags, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>experiment_templates</code> in a region.
```sql
SELECT
region,
id
FROM aws.fis.experiment_templates
WHERE region = 'us-east-1';
```
Gets all properties from an <code>experiment_template</code>.
```sql
SELECT
region,
id,
description,
targets,
actions,
stop_conditions,
log_configuration,
role_arn,
tags,
experiment_options
FROM aws.fis.experiment_templates
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>experiment_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.fis.experiment_templates (
 Description,
 Targets,
 StopConditions,
 RoleArn,
 Tags,
 region
)
SELECT 
'{{ Description }}',
 '{{ Targets }}',
 '{{ StopConditions }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.fis.experiment_templates (
 Description,
 Targets,
 Actions,
 StopConditions,
 LogConfiguration,
 RoleArn,
 Tags,
 ExperimentOptions,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Targets }}',
 '{{ Actions }}',
 '{{ StopConditions }}',
 '{{ LogConfiguration }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ ExperimentOptions }}',
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
  - name: experiment_template
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Targets
        value: {}
      - name: Actions
        value: {}
      - name: StopConditions
        value:
          - Source: '{{ Source }}'
            Value: '{{ Value }}'
      - name: LogConfiguration
        value:
          CloudWatchLogsConfiguration:
            LogGroupArn: '{{ LogGroupArn }}'
          S3Configuration:
            BucketName: '{{ BucketName }}'
            Prefix: '{{ Prefix }}'
          LogSchemaVersion: '{{ LogSchemaVersion }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value: {}
      - name: ExperimentOptions
        value:
          AccountTargeting: '{{ AccountTargeting }}'
          EmptyTargetResolutionMode: '{{ EmptyTargetResolutionMode }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.fis.experiment_templates
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>experiment_templates</code> resource, the following permissions are required:

### Create
```json
fis:CreateExperimentTemplate,
fis:TagResource,
iam:PassRole
```

### Read
```json
fis:GetExperimentTemplate,
fis:ListTagsForResource
```

### Update
```json
fis:UpdateExperimentTemplate,
fis:TagResource,
fis:UntagResource,
iam:PassRole
```

### Delete
```json
fis:DeleteExperimentTemplate
```

### List
```json
fis:ListExperimentTemplates,
fis:ListTagsForResource
```

