---
title: application_inference_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - application_inference_profiles
  - bedrock
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

Creates, updates, deletes or gets an <code>application_inference_profile</code> resource or lists <code>application_inference_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_inference_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::ApplicationInferenceProfile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.application_inference_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the inference profile</td></tr>
<tr><td><CopyableCode code="inference_profile_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="inference_profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="inference_profile_identifier" /></td><td><code>string</code></td><td>Inference profile identifier. Supports both system-defined inference profile ids, and inference profile ARNs.</td></tr>
<tr><td><CopyableCode code="inference_profile_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_source" /></td><td><code>undefined</code></td><td>Various ways to encode a list of models in a CreateInferenceProfile request</td></tr>
<tr><td><CopyableCode code="models" /></td><td><code>array</code></td><td>List of model configuration</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Status of the Inference Profile</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>List of Tags</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Type of the Inference Profile</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-applicationinferenceprofile.html"><code>AWS::Bedrock::ApplicationInferenceProfile</code></a>.

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
    <td><CopyableCode code="InferenceProfileName, region" /></td>
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
Gets all <code>application_inference_profiles</code> in a region.
```sql
SELECT
region,
created_at,
description,
inference_profile_arn,
inference_profile_id,
inference_profile_identifier,
inference_profile_name,
model_source,
models,
status,
tags,
type,
updated_at
FROM aws.bedrock.application_inference_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application_inference_profile</code>.
```sql
SELECT
region,
created_at,
description,
inference_profile_arn,
inference_profile_id,
inference_profile_identifier,
inference_profile_name,
model_source,
models,
status,
tags,
type,
updated_at
FROM aws.bedrock.application_inference_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<InferenceProfileIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_inference_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.bedrock.application_inference_profiles (
 InferenceProfileName,
 region
)
SELECT 
'{{ InferenceProfileName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.bedrock.application_inference_profiles (
 Description,
 InferenceProfileName,
 ModelSource,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ InferenceProfileName }}',
 '{{ ModelSource }}',
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
  - name: application_inference_profile
    props:
      - name: Description
        value: '{{ Description }}'
      - name: InferenceProfileName
        value: '{{ InferenceProfileName }}'
      - name: ModelSource
        value: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.bedrock.application_inference_profiles
WHERE data__Identifier = '<InferenceProfileIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>application_inference_profiles</code> resource, the following permissions are required:

### Create
```json
bedrock:CreateInferenceProfile,
bedrock:GetInferenceProfile,
bedrock:TagResource,
bedrock:ListTagsForResource
```

### Read
```json
bedrock:GetInferenceProfile,
bedrock:ListTagsForResource
```

### Update
```json
bedrock:GetInferenceProfile,
bedrock:ListTagsForResource,
bedrock:TagResource,
bedrock:UntagResource
```

### Delete
```json
bedrock:DeleteInferenceProfile,
bedrock:GetInferenceProfile
```

### List
```json
bedrock:ListInferenceProfiles
```
