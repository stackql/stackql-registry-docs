---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - grants
  - licensemanager
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

Creates, updates, deletes or gets a <code>grant</code> resource or lists <code>grants</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.licensemanager.grants" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="grant_arn" /></td><td><code>string</code></td><td>Arn of the grant.</td></tr>
<tr><td><CopyableCode code="grant_name" /></td><td><code>string</code></td><td>Name for the created Grant.</td></tr>
<tr><td><CopyableCode code="license_arn" /></td><td><code>string</code></td><td>License Arn for the grant.</td></tr>
<tr><td><CopyableCode code="home_region" /></td><td><code>string</code></td><td>Home region for the created grant.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the grant.</td></tr>
<tr><td><CopyableCode code="allowed_operations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="principals" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html"><code>AWS::LicenseManager::Grant</code></a>.

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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>grants</code> in a region.
```sql
SELECT
region,
grant_arn,
grant_name,
license_arn,
home_region,
version,
allowed_operations,
principals,
status
FROM aws.licensemanager.grants
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>grant</code>.
```sql
SELECT
region,
grant_arn,
grant_name,
license_arn,
home_region,
version,
allowed_operations,
principals,
status
FROM aws.licensemanager.grants
WHERE region = 'us-east-1' AND data__Identifier = '<GrantArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>grant</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.licensemanager.grants (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.licensemanager.grants (
 GrantName,
 LicenseArn,
 HomeRegion,
 AllowedOperations,
 Principals,
 Status,
 region
)
SELECT 
 '{{ GrantName }}',
 '{{ LicenseArn }}',
 '{{ HomeRegion }}',
 '{{ AllowedOperations }}',
 '{{ Principals }}',
 '{{ Status }}',
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
  - name: grant
    props:
      - name: GrantName
        value: '{{ GrantName }}'
      - name: LicenseArn
        value: '{{ LicenseArn }}'
      - name: HomeRegion
        value: '{{ HomeRegion }}'
      - name: AllowedOperations
        value:
          - '{{ AllowedOperations[0] }}'
      - name: Principals
        value:
          - null
      - name: Status
        value: '{{ Status }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.licensemanager.grants
WHERE data__Identifier = '<GrantArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>grants</code> resource, the following permissions are required:

### Create
```json
license-manager:CreateGrant
```

### Read
```json
license-manager:GetGrant
```

### Update
```json
license-manager:CreateGrantVersion
```

### Delete
```json
license-manager:DeleteGrant
```

### List
```json
license-manager:ListDistributedGrants
```
