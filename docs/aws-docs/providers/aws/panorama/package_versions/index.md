---
title: package_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - package_versions
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

Creates, updates, deletes or gets a <code>package_version</code> resource or lists <code>package_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for PackageVersion Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.package_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="owner_account" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="package_id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="package_arn" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="package_version" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="patch_version" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="mark_latest" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="is_latest_patch" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="package_name" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="status_description" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="registered_time" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_latest_patch_version" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="PackageId, PackageVersion, PatchVersion, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>package_version</code>.
```sql
SELECT
region,
owner_account,
package_id,
package_arn,
package_version,
patch_version,
mark_latest,
is_latest_patch,
package_name,
status,
status_description,
registered_time,
updated_latest_patch_version
FROM aws.panorama.package_versions
WHERE region = 'us-east-1' AND data__Identifier = '<PackageId>|<PackageVersion>|<PatchVersion>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>package_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.panorama.package_versions (
 PackageId,
 PackageVersion,
 PatchVersion,
 region
)
SELECT 
'{{ PackageId }}',
 '{{ PackageVersion }}',
 '{{ PatchVersion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.panorama.package_versions (
 OwnerAccount,
 PackageId,
 PackageVersion,
 PatchVersion,
 MarkLatest,
 UpdatedLatestPatchVersion,
 region
)
SELECT 
 '{{ OwnerAccount }}',
 '{{ PackageId }}',
 '{{ PackageVersion }}',
 '{{ PatchVersion }}',
 '{{ MarkLatest }}',
 '{{ UpdatedLatestPatchVersion }}',
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
  - name: package_version
    props:
      - name: OwnerAccount
        value: '{{ OwnerAccount }}'
      - name: PackageId
        value: '{{ PackageId }}'
      - name: PackageVersion
        value: '{{ PackageVersion }}'
      - name: PatchVersion
        value: '{{ PatchVersion }}'
      - name: MarkLatest
        value: '{{ MarkLatest }}'
      - name: UpdatedLatestPatchVersion
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.panorama.package_versions
WHERE data__Identifier = '<PackageId|PackageVersion|PatchVersion>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>package_versions</code> resource, the following permissions are required:

### Create
```json
panorama:RegisterPackageVersion,
panorama:DescribePackageVersion,
s3:ListBucket,
s3:PutObject,
s3:GetObject,
s3:GetObjectVersion
```

### Read
```json
panorama:DescribePackageVersion,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

### Update
```json
panorama:DescribePackageVersion,
panorama:RegisterPackageVersion,
s3:ListBucket,
s3:PutObject,
s3:GetObject,
s3:GetObjectVersion
```

### Delete
```json
panorama:DeregisterPackageVersion,
panorama:DescribePackageVersion,
s3:DeleteObject,
s3:DeleteObjectVersion,
s3:DeleteObjectVersionTagging,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

