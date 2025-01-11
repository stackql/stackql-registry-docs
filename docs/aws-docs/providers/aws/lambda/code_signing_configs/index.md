---
title: code_signing_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - code_signing_configs
  - lambda
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

Creates, updates, deletes or gets a <code>code_signing_config</code> resource or lists <code>code_signing_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>code_signing_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::CodeSigningConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.code_signing_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the CodeSigningConfig</td></tr>
<tr><td><CopyableCode code="allowed_publishers" /></td><td><code>object</code></td><td>When the CodeSigningConfig is later on attached to a function, the function code will be expected to be signed by profiles from this list</td></tr>
<tr><td><CopyableCode code="code_signing_policies" /></td><td><code>object</code></td><td>Policies to control how to act if a signature is invalid</td></tr>
<tr><td><CopyableCode code="code_signing_config_id" /></td><td><code>string</code></td><td>A unique identifier for CodeSigningConfig resource</td></tr>
<tr><td><CopyableCode code="code_signing_config_arn" /></td><td><code>string</code></td><td>A unique Arn for CodeSigningConfig resource</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to CodeSigningConfig resource</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html"><code>AWS::Lambda::CodeSigningConfig</code></a>.

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
    <td><CopyableCode code="AllowedPublishers, region" /></td>
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
Gets all <code>code_signing_configs</code> in a region.
```sql
SELECT
region,
description,
allowed_publishers,
code_signing_policies,
code_signing_config_id,
code_signing_config_arn,
tags
FROM aws.lambda.code_signing_configs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>code_signing_config</code>.
```sql
SELECT
region,
description,
allowed_publishers,
code_signing_policies,
code_signing_config_id,
code_signing_config_arn,
tags
FROM aws.lambda.code_signing_configs
WHERE region = 'us-east-1' AND data__Identifier = '<CodeSigningConfigArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>code_signing_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lambda.code_signing_configs (
 AllowedPublishers,
 region
)
SELECT 
'{{ AllowedPublishers }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lambda.code_signing_configs (
 Description,
 AllowedPublishers,
 CodeSigningPolicies,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ AllowedPublishers }}',
 '{{ CodeSigningPolicies }}',
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
  - name: code_signing_config
    props:
      - name: Description
        value: '{{ Description }}'
      - name: AllowedPublishers
        value:
          SigningProfileVersionArns:
            - '{{ SigningProfileVersionArns[0] }}'
      - name: CodeSigningPolicies
        value:
          UntrustedArtifactOnDeployment: '{{ UntrustedArtifactOnDeployment }}'
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
DELETE FROM aws.lambda.code_signing_configs
WHERE data__Identifier = '<CodeSigningConfigArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>code_signing_configs</code> resource, the following permissions are required:

### Create
```json
lambda:CreateCodeSigningConfig,
lambda:TagResource
```

### Read
```json
lambda:GetCodeSigningConfig,
lambda:ListTags
```

### Update
```json
lambda:UpdateCodeSigningConfig,
lambda:ListTags,
lambda:TagResource,
lambda:UntagResource
```

### Delete
```json
lambda:DeleteCodeSigningConfig
```

### List
```json
lambda:ListCodeSigningConfigs
```
