---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - transfer
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

Creates, updates, deletes or gets a <code>workflow</code> resource or lists <code>workflows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Workflow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.workflows" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="on_exception_steps" /></td><td><code>array</code></td><td>Specifies the steps (actions) to take if any errors are encountered during execution of the workflow.</td></tr>
<tr><td><CopyableCode code="steps" /></td><td><code>array</code></td><td>Specifies the details for the steps that are in the specified workflow.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A textual description for the workflow.</td></tr>
<tr><td><CopyableCode code="workflow_id" /></td><td><code>string</code></td><td>A unique identifier for the workflow.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the workflow.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html"><code>AWS::Transfer::Workflow</code></a>.

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
    <td><CopyableCode code="Steps, region" /></td>
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
Gets all <code>workflows</code> in a region.
```sql
SELECT
region,
on_exception_steps,
steps,
tags,
description,
workflow_id,
arn
FROM aws.transfer.workflows
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>workflow</code>.
```sql
SELECT
region,
on_exception_steps,
steps,
tags,
description,
workflow_id,
arn
FROM aws.transfer.workflows
WHERE region = 'us-east-1' AND data__Identifier = '<WorkflowId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workflow</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.transfer.workflows (
 Steps,
 region
)
SELECT 
'{{ Steps }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.transfer.workflows (
 OnExceptionSteps,
 Steps,
 Tags,
 Description,
 region
)
SELECT 
 '{{ OnExceptionSteps }}',
 '{{ Steps }}',
 '{{ Tags }}',
 '{{ Description }}',
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
  - name: workflow
    props:
      - name: OnExceptionSteps
        value:
          - CopyStepDetails:
              DestinationFileLocation:
                S3FileLocation:
                  Bucket: '{{ Bucket }}'
                  Key: '{{ Key }}'
              Name: '{{ Name }}'
              OverwriteExisting: '{{ OverwriteExisting }}'
              SourceFileLocation: '{{ SourceFileLocation }}'
            CustomStepDetails:
              Name: '{{ Name }}'
              Target: '{{ Target }}'
              TimeoutSeconds: '{{ TimeoutSeconds }}'
              SourceFileLocation: '{{ SourceFileLocation }}'
            DecryptStepDetails:
              DestinationFileLocation:
                S3FileLocation: null
                EfsFileLocation:
                  FileSystemId: '{{ FileSystemId }}'
                  Path: '{{ Path }}'
              Name: '{{ Name }}'
              Type: '{{ Type }}'
              OverwriteExisting: '{{ OverwriteExisting }}'
              SourceFileLocation: '{{ SourceFileLocation }}'
            DeleteStepDetails:
              Name: '{{ Name }}'
              SourceFileLocation: '{{ SourceFileLocation }}'
            TagStepDetails:
              Name: '{{ Name }}'
              Tags:
                - Key: '{{ Key }}'
                  Value: '{{ Value }}'
              SourceFileLocation: '{{ SourceFileLocation }}'
            Type: '{{ Type }}'
      - name: Steps
        value:
          - null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Description
        value: '{{ Description }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.transfer.workflows
WHERE data__Identifier = '<WorkflowId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>workflows</code> resource, the following permissions are required:

### Create
```json
transfer:CreateWorkflow,
transfer:TagResource
```

### Read
```json
transfer:DescribeWorkflow
```

### Delete
```json
transfer:DeleteWorkflow
```

### List
```json
transfer:ListWorkflows
```

### Update
```json
transfer:UnTagResource,
transfer:TagResource
```
