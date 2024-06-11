---
title: profile_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_associations
  - route53profiles
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

Creates, updates, deletes or gets a <code>profile_association</code> resource or lists <code>profile_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Route53Profiles::ProfileAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53profiles.profile_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The resource that you associated the  profile with.</td></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td>The ID of the  profile that you associated with the resource that is specified by ResourceId.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Primary Identifier for  Profile Association</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of an association between a  Profile and a VPC.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the  profile association.</td></tr>
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
    <td><CopyableCode code="ResourceId, ProfileId, Name, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>profile_associations</code> in a region.
```sql
SELECT
region,
id
FROM aws.route53profiles.profile_associations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>profile_association</code>.
```sql
SELECT
region,
resource_id,
profile_id,
id,
name,
tags,
arn
FROM aws.route53profiles.profile_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profile_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53profiles.profile_associations (
 ResourceId,
 ProfileId,
 Name,
 region
)
SELECT 
'{{ ResourceId }}',
 '{{ ProfileId }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53profiles.profile_associations (
 ResourceId,
 ProfileId,
 Name,
 Tags,
 Arn,
 region
)
SELECT 
 '{{ ResourceId }}',
 '{{ ProfileId }}',
 '{{ Name }}',
 '{{ Tags }}',
 '{{ Arn }}',
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
  - name: profile_association
    props:
      - name: ResourceId
        value: '{{ ResourceId }}'
      - name: ProfileId
        value: '{{ ProfileId }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Arn
        value: '{{ Arn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53profiles.profile_associations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>profile_associations</code> resource, the following permissions are required:

### Create
```json
route53profiles:AssociateProfile,
route53profiles:GetProfileAssociation,
ec2:DescribeVpcs,
route53profiles:TagResource
```

### Update
```json
route53profiles:GetProfileAssociation,
route53profiles:TagResource,
route53profiles:UntagResource,
route53profiles:ListTagsForResource
```

### Read
```json
route53profiles:GetProfileAssociation,
route53profiles:ListTagsForResource
```

### Delete
```json
route53profiles:DisassociateProfile,
route53profiles:GetProfileAssociation,
route53profiles:UntagResource
```

### List
```json
route53profiles:ListProfileAssociations,
route53profiles:ListTagsForResource
```

