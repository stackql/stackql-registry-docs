---
title: hook_default_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_default_versions
  - cloudformation
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

Creates, updates, deletes or gets a <code>hook_default_version</code> resource or lists <code>hook_default_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_default_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Set a version as default version for a hook in CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.hook_default_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type version.</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.<br/><br/>We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type. This is used to uniquely identify a HookDefaultVersion</td></tr>
<tr><td><CopyableCode code="version_id" /></td><td><code>string</code></td><td>The ID of an existing version of the hook to set as the default.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>hook_default_versions</code> in a region.
```sql
SELECT
region,
arn
FROM aws.cloudformation.hook_default_versions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>hook_default_version</code>.
```sql
SELECT
region,
type_version_arn,
type_name,
arn,
version_id
FROM aws.cloudformation.hook_default_versions
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hook_default_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudformation.hook_default_versions (
 TypeVersionArn,
 TypeName,
 VersionId,
 region
)
SELECT 
'{{ TypeVersionArn }}',
 '{{ TypeName }}',
 '{{ VersionId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudformation.hook_default_versions (
 TypeVersionArn,
 TypeName,
 VersionId,
 region
)
SELECT 
 '{{ TypeVersionArn }}',
 '{{ TypeName }}',
 '{{ VersionId }}',
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
  - name: hook_default_version
    props:
      - name: TypeVersionArn
        value: '{{ TypeVersionArn }}'
      - name: TypeName
        value: '{{ TypeName }}'
      - name: VersionId
        value: '{{ VersionId }}'

```
</TabItem>
</Tabs>

## Permissions

To operate on the <code>hook_default_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:SetTypeDefaultVersion
```

### Read
```json
cloudformation:DescribeType
```

### Update
```json
cloudformation:SetTypeDefaultVersion
```

### List
```json
cloudformation:ListTypes
```

