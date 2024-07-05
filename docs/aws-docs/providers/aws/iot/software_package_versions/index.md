---
title: software_package_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - software_package_versions
  - iot
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

Creates, updates, deletes or gets a <code>software_package_version</code> resource or lists <code>software_package_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_package_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource definition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.software_package_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="attributes" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="error_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="package_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="package_version_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="version_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="PackageName, region" /></td>
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
Gets all <code>software_package_versions</code> in a region.
```sql
SELECT
region,
attributes,
description,
error_reason,
package_name,
package_version_arn,
status,
tags,
version_name
FROM aws.iot.software_package_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>software_package_version</code>.
```sql
SELECT
region,
attributes,
description,
error_reason,
package_name,
package_version_arn,
status,
tags,
version_name
FROM aws.iot.software_package_versions
WHERE region = 'us-east-1' AND data__Identifier = '<PackageName>|<VersionName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>software_package_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.software_package_versions (
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
/*+ create */
INSERT INTO aws.iot.software_package_versions (
 Attributes,
 Description,
 PackageName,
 Tags,
 VersionName,
 region
)
SELECT 
 '{{ Attributes }}',
 '{{ Description }}',
 '{{ PackageName }}',
 '{{ Tags }}',
 '{{ VersionName }}',
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
  - name: software_package_version
    props:
      - name: Attributes
        value: {}
      - name: Description
        value: '{{ Description }}'
      - name: PackageName
        value: '{{ PackageName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VersionName
        value: '{{ VersionName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iot.software_package_versions
WHERE data__Identifier = '<PackageName|VersionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>software_package_versions</code> resource, the following permissions are required:

### Create
```json
iot:CreatePackageVersion,
iot:GetPackageVersion,
iot:TagResource,
iot:GetIndexingConfiguration
```

### Read
```json
iot:GetPackageVersion,
iot:ListTagsForResource
```

### Update
```json
iot:UpdatePackageVersion,
iot:GetPackageVersion,
iot:ListTagsForResource,
iot:TagResource,
iot:UntagResource,
iot:GetIndexingConfiguration
```

### Delete
```json
iot:DeletePackageVersion,
iot:UpdatePackageVersion,
iot:GetPackageVersion,
iot:GetIndexingConfiguration
```

### List
```json
iot:ListPackageVersions
```

