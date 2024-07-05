---
title: access_grants_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants_locations
  - s3
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

Creates, updates, deletes or gets an <code>access_grants_location</code> resource or lists <code>access_grants_locations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessGrantsLocation resource is an Amazon S3 resource type hosted in an access grants instance which can be the target of S3 access grants.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_grants_locations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_grants_location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified Access Grants location.</td></tr>
<tr><td><CopyableCode code="access_grants_location_id" /></td><td><code>string</code></td><td>The unique identifier for the specified Access Grants location.</td></tr>
<tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the access grant location's associated IAM role.</td></tr>
<tr><td><CopyableCode code="location_scope" /></td><td><code>string</code></td><td>Descriptor for where the location actually points</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Gets all <code>access_grants_locations</code> in a region.
```sql
SELECT
region,
access_grants_location_arn,
access_grants_location_id,
iam_role_arn,
location_scope,
tags
FROM aws.s3.access_grants_locations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>access_grants_location</code>.
```sql
SELECT
region,
access_grants_location_arn,
access_grants_location_id,
iam_role_arn,
location_scope,
tags
FROM aws.s3.access_grants_locations
WHERE region = 'us-east-1' AND data__Identifier = '<AccessGrantsLocationId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_grants_location</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3.access_grants_locations (
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
INSERT INTO aws.s3.access_grants_locations (
 IamRoleArn,
 LocationScope,
 Tags,
 region
)
SELECT 
 '{{ IamRoleArn }}',
 '{{ LocationScope }}',
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
  - name: access_grants_location
    props:
      - name: IamRoleArn
        value: '{{ IamRoleArn }}'
      - name: LocationScope
        value: '{{ LocationScope }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3.access_grants_locations
WHERE data__Identifier = '<AccessGrantsLocationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_grants_locations</code> resource, the following permissions are required:

### Create
```json
s3:CreateAccessGrantsLocation,
iam:PassRole,
s3:TagResource
```

### Read
```json
s3:GetAccessGrantsLocation
```

### Delete
```json
s3:DeleteAccessGrantsLocation
```

### List
```json
s3:ListAccessGrantsLocations
```

### Update
```json
s3:UpdateAccessGrantsLocation,
s3:TagResource,
iam:PassRole
```

