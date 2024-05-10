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


Used to retrieve a list of <code>code_signing_configs</code> in a region or to create or delete a <code>code_signing_configs</code> resource, use <code>code_signing_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>code_signing_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::CodeSigningConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.code_signing_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="code_signing_config_arn" /></td><td><code>string</code></td><td>A unique Arn for CodeSigningConfig resource</td></tr>
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
code_signing_config_arn
FROM aws.lambda.code_signing_configs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>code_signing_config</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- code_signing_config.iql (required properties only)
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
-- code_signing_config.iql (all properties)
INSERT INTO aws.lambda.code_signing_configs (
 Description,
 AllowedPublishers,
 CodeSigningPolicies,
 region
)
SELECT 
 '{{ Description }}',
 '{{ AllowedPublishers }}',
 '{{ CodeSigningPolicies }}',
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

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lambda.code_signing_configs
WHERE data__Identifier = '<CodeSigningConfigArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>code_signing_configs</code> resource, the following permissions are required:

### Create
```json
lambda:CreateCodeSigningConfig
```

### Delete
```json
lambda:DeleteCodeSigningConfig
```

### List
```json
lambda:ListCodeSigningConfigs
```

