---
title: access_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants
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

Creates, updates, deletes or gets an <code>access_grant</code> resource or lists <code>access_grants</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessGrant resource is an Amazon S3 resource type representing permissions to a specific S3 bucket or prefix hosted in an S3 Access Grants instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_grants" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_grant_id" /></td><td><code>string</code></td><td>The ID assigned to this access grant.</td></tr>
<tr><td><CopyableCode code="access_grants_location_id" /></td><td><code>string</code></td><td>The custom S3 location to be accessed by the grantee</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="permission" /></td><td><code>string</code></td><td>The level of access to be afforded to the grantee</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the application grantees will use to access the location</td></tr>
<tr><td><CopyableCode code="s3_prefix_type" /></td><td><code>string</code></td><td>The type of S3SubPrefix.</td></tr>
<tr><td><CopyableCode code="grant_scope" /></td><td><code>string</code></td><td>The S3 path of the data to which you are granting access. It is a combination of the S3 path of the registered location and the subprefix.</td></tr>
<tr><td><CopyableCode code="access_grant_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified access grant.</td></tr>
<tr><td><CopyableCode code="grantee" /></td><td><code>object</code></td><td>The principal who will be granted permission to access S3.</td></tr>
<tr><td><CopyableCode code="access_grants_location_configuration" /></td><td><code>object</code></td><td>The configuration options of the grant location, which is the S3 path to the data to which you are granting access.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accessgrant.html"><code>AWS::S3::AccessGrant</code></a>.

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
    <td><CopyableCode code="Grantee, Permission, AccessGrantsLocationId, region" /></td>
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
Gets all <code>access_grants</code> in a region.
```sql
SELECT
region,
access_grant_id,
access_grants_location_id,
tags,
permission,
application_arn,
s3_prefix_type,
grant_scope,
access_grant_arn,
grantee,
access_grants_location_configuration
FROM aws.s3.access_grants
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>access_grant</code>.
```sql
SELECT
region,
access_grant_id,
access_grants_location_id,
tags,
permission,
application_arn,
s3_prefix_type,
grant_scope,
access_grant_arn,
grantee,
access_grants_location_configuration
FROM aws.s3.access_grants
WHERE region = 'us-east-1' AND data__Identifier = '<AccessGrantId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_grant</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3.access_grants (
 AccessGrantsLocationId,
 Permission,
 Grantee,
 region
)
SELECT 
'{{ AccessGrantsLocationId }}',
 '{{ Permission }}',
 '{{ Grantee }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.s3.access_grants (
 AccessGrantsLocationId,
 Tags,
 Permission,
 ApplicationArn,
 S3PrefixType,
 Grantee,
 AccessGrantsLocationConfiguration,
 region
)
SELECT 
 '{{ AccessGrantsLocationId }}',
 '{{ Tags }}',
 '{{ Permission }}',
 '{{ ApplicationArn }}',
 '{{ S3PrefixType }}',
 '{{ Grantee }}',
 '{{ AccessGrantsLocationConfiguration }}',
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
  - name: access_grant
    props:
      - name: AccessGrantsLocationId
        value: '{{ AccessGrantsLocationId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Permission
        value: '{{ Permission }}'
      - name: ApplicationArn
        value: '{{ ApplicationArn }}'
      - name: S3PrefixType
        value: '{{ S3PrefixType }}'
      - name: Grantee
        value:
          GranteeType: '{{ GranteeType }}'
          GranteeIdentifier: '{{ GranteeIdentifier }}'
      - name: AccessGrantsLocationConfiguration
        value:
          S3SubPrefix: '{{ S3SubPrefix }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3.access_grants
WHERE data__Identifier = '<AccessGrantId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_grants</code> resource, the following permissions are required:

### Create
```json
s3:CreateAccessGrant,
s3:TagResource
```

### Read
```json
s3:GetAccessGrant,
s3:ListTagsForResource
```

### Delete
```json
s3:DeleteAccessGrant
```

### List
```json
s3:ListAccessGrants
```

### Update
```json
s3:TagResource,
s3:UntagResource
```
