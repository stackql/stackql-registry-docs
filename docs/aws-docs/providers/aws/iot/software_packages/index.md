---
title: software_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - software_packages
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


Used to retrieve a list of <code>software_packages</code> in a region or to create or delete a <code>software_packages</code> resource, use <code>software_package</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource definition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.software_packages" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="package_name" /></td><td><code>string</code></td><td></td></tr>
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
package_name
FROM aws.iot.software_packages
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>software_package</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- software_package.iql (required properties only)
INSERT INTO aws.iot.software_packages (
 Description,
 PackageName,
 Tags,
 region
)
SELECT 
'{{ Description }}',
 '{{ PackageName }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- software_package.iql (all properties)
INSERT INTO aws.iot.software_packages (
 Description,
 PackageName,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ PackageName }}',
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
  - name: software_package
    props:
      - name: Description
        value: '{{ Description }}'
      - name: PackageName
        value: '{{ PackageName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.software_packages
WHERE data__Identifier = '<PackageName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>software_packages</code> resource, the following permissions are required:

### Create
```json
iot:CreatePackage,
iot:GetPackage,
iot:TagResource,
iot:GetIndexingConfiguration
```

### Delete
```json
iot:DeletePackage,
iot:DeletePackageVersion,
iot:GetPackage,
iot:GetPackageVersion,
iot:UpdatePackage,
iot:UpdatePackageVersion,
iot:GetIndexingConfiguration,
iot:ListPackageVersions
```

### List
```json
iot:ListPackages
```

