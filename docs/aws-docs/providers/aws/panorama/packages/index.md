---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
  - panorama
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


Used to retrieve a list of <code>packages</code> in a region or to create or delete a <code>packages</code> resource, use <code>package</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for Package CloudFormation Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.packages" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="package_id" /></td><td><code>undefined</code></td><td></td></tr>
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
package_id
FROM aws.panorama.packages
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>package</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- package.iql (required properties only)
INSERT INTO aws.panorama.packages (
 PackageName,
 region
)
SELECT 
'{{ PackageName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- package.iql (all properties)
INSERT INTO aws.panorama.packages (
 PackageName,
 StorageLocation,
 Tags,
 region
)
SELECT 
 '{{ PackageName }}',
 '{{ StorageLocation }}',
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
  - name: package
    props:
      - name: PackageName
        value: '{{ PackageName }}'
      - name: StorageLocation
        value:
          Bucket: '{{ Bucket }}'
          RepoPrefixLocation: '{{ RepoPrefixLocation }}'
          GeneratedPrefixLocation: '{{ GeneratedPrefixLocation }}'
          BinaryPrefixLocation: '{{ BinaryPrefixLocation }}'
          ManifestPrefixLocation: '{{ ManifestPrefixLocation }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.panorama.packages
WHERE data__Identifier = '<PackageId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>packages</code> resource, the following permissions are required:

### Create
```json
panorama:CreatePackage,
panorama:ListTagsForResource,
panorama:TagResource,
panorama:DescribePackage,
s3:ListBucket,
s3:PutObject,
s3:GetObject,
s3:GetObjectVersion
```

### List
```json
panorama:ListPackages,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

### Delete
```json
panorama:DeletePackage,
panorama:DescribePackage,
s3:DeleteObject,
s3:DeleteObjectVersion,
s3:DeleteObjectVersionTagging,
s3:ListObjects,
s3:ListObjectsV2,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

