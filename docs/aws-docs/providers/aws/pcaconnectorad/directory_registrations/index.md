---
title: directory_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_registrations
  - pcaconnectorad
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

Creates, updates, deletes or gets a <code>directory_registration</code> resource or lists <code>directory_registrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::DirectoryRegistration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.directory_registrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="directory_registration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="DirectoryId, region" /></td>
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
Gets all <code>directory_registrations</code> in a region.
```sql
SELECT
region,
directory_id,
directory_registration_arn,
tags
FROM aws.pcaconnectorad.directory_registrations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>directory_registration</code>.
```sql
SELECT
region,
directory_id,
directory_registration_arn,
tags
FROM aws.pcaconnectorad.directory_registrations
WHERE region = 'us-east-1' AND data__Identifier = '<DirectoryRegistrationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>directory_registration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.pcaconnectorad.directory_registrations (
 DirectoryId,
 region
)
SELECT 
'{{ DirectoryId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pcaconnectorad.directory_registrations (
 DirectoryId,
 Tags,
 region
)
SELECT 
 '{{ DirectoryId }}',
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
  - name: directory_registration
    props:
      - name: DirectoryId
        value: '{{ DirectoryId }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.pcaconnectorad.directory_registrations
WHERE data__Identifier = '<DirectoryRegistrationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>directory_registrations</code> resource, the following permissions are required:

### Create
```json
pca-connector-ad:GetDirectoryRegistration,
pca-connector-ad:CreateDirectoryRegistration,
ds:AuthorizeApplication,
ds:DescribeDirectories
```

### Read
```json
pca-connector-ad:ListTagsForResource,
pca-connector-ad:GetDirectoryRegistration
```

### Delete
```json
pca-connector-ad:GetDirectoryRegistration,
pca-connector-ad:DeleteDirectoryRegistration,
ds:DescribeDirectories,
ds:UnauthorizeApplication,
ds:UpdateAuthorizedApplication
```

### List
```json
pca-connector-ad:ListDirectoryRegistrations
```

### Update
```json
pca-connector-ad:ListTagsForResource,
pca-connector-ad:TagResource,
pca-connector-ad:UntagResource
```

