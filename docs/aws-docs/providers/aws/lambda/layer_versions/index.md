---
title: layer_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - layer_versions
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


Used to retrieve a list of <code>layer_versions</code> in a region or to create or delete a <code>layer_versions</code> resource, use <code>layer_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>layer_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::LayerVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.layer_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="layer_version_arn" /></td><td><code>string</code></td><td></td></tr>
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
layer_version_arn
FROM aws.lambda.layer_versions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>layer_version</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- layer_version.iql (required properties only)
INSERT INTO aws.lambda.layer_versions (
 Content,
 region
)
SELECT 
'{{ Content }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- layer_version.iql (all properties)
INSERT INTO aws.lambda.layer_versions (
 CompatibleRuntimes,
 LicenseInfo,
 Description,
 LayerName,
 Content,
 CompatibleArchitectures,
 region
)
SELECT 
 '{{ CompatibleRuntimes }}',
 '{{ LicenseInfo }}',
 '{{ Description }}',
 '{{ LayerName }}',
 '{{ Content }}',
 '{{ CompatibleArchitectures }}',
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
  - name: layer_version
    props:
      - name: CompatibleRuntimes
        value:
          - '{{ CompatibleRuntimes[0] }}'
      - name: LicenseInfo
        value: '{{ LicenseInfo }}'
      - name: Description
        value: '{{ Description }}'
      - name: LayerName
        value: '{{ LayerName }}'
      - name: Content
        value:
          S3ObjectVersion: '{{ S3ObjectVersion }}'
          S3Bucket: '{{ S3Bucket }}'
          S3Key: '{{ S3Key }}'
      - name: CompatibleArchitectures
        value:
          - '{{ CompatibleArchitectures[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lambda.layer_versions
WHERE data__Identifier = '<LayerVersionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>layer_versions</code> resource, the following permissions are required:

### Create
```json
lambda:PublishLayerVersion,
s3:GetObject,
s3:GetObjectVersion
```

### Delete
```json
lambda:GetLayerVersion,
lambda:DeleteLayerVersion
```

### List
```json
lambda:ListLayerVersions
```

