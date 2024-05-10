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


Used to retrieve a list of <code>package_versions</code> in a region or to create or delete a <code>package_versions</code> resource, use <code>package_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for PackageVersion Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.package_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="package_id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="package_version" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="patch_version" /></td><td><code>undefined</code></td><td></td></tr>
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
package_id,
package_version,
patch_version
FROM aws.panorama.package_versions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>package_version</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- package_version.iql (required properties only)
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
-- package_version.iql (all properties)
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

## `DELETE` Example

```sql
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

