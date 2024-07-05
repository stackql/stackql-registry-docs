---
title: module_default_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - module_default_versions
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

Creates, updates, deletes or gets a <code>module_default_version</code> resource or lists <code>module_default_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>module_default_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A module that has been registered in the CloudFormation registry as the default version</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.module_default_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the module version to set as the default version.</td></tr>
<tr><td><CopyableCode code="module_name" /></td><td><code>string</code></td><td>The name of a module existing in the registry.</td></tr>
<tr><td><CopyableCode code="version_id" /></td><td><code>string</code></td><td>The ID of an existing version of the named module to set as the default.</td></tr>
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
Gets all <code>module_default_versions</code> in a region.
```sql
SELECT
region,
arn,
module_name,
version_id
FROM aws.cloudformation.module_default_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>module_default_version</code>.
```sql
SELECT
region,
arn,
module_name,
version_id
FROM aws.cloudformation.module_default_versions
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>module_default_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudformation.module_default_versions (
 Arn,
 ModuleName,
 VersionId,
 region
)
SELECT 
'{{ Arn }}',
 '{{ ModuleName }}',
 '{{ VersionId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudformation.module_default_versions (
 Arn,
 ModuleName,
 VersionId,
 region
)
SELECT 
 '{{ Arn }}',
 '{{ ModuleName }}',
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
  - name: module_default_version
    props:
      - name: Arn
        value: '{{ Arn }}'
      - name: ModuleName
        value: '{{ ModuleName }}'
      - name: VersionId
        value: '{{ VersionId }}'

```
</TabItem>
</Tabs>

## Permissions

To operate on the <code>module_default_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:DescribeType,
cloudformation:SetTypeDefaultVersion
```

### Read
```json
cloudformation:DescribeType
```

### List
```json
cloudformation:ListTypes
```

