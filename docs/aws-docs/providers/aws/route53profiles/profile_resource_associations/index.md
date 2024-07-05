---
title: profile_resource_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_resource_associations
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

Creates, updates, deletes or gets a <code>profile_resource_association</code> resource or lists <code>profile_resource_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_resource_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Route53Profiles::ProfileResourceAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53profiles.profile_resource_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td>The ID of the profile that you associated the resource to that is specified by ResourceArn.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Primary Identifier for Profile Resource Association</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of an association between the Profile and resource.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The arn of the resource that you associated to the Profile.</td></tr>
<tr><td><CopyableCode code="resource_properties" /></td><td><code>string</code></td><td>A JSON-formatted string with key-value pairs specifying the properties of the associated resource.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The type of the resource associated to the Profile.</td></tr>
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
    <td><CopyableCode code="ProfileId, Name, ResourceArn, region" /></td>
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
Gets all <code>profile_resource_associations</code> in a region.
```sql
SELECT
region,
profile_id,
id,
name,
resource_arn,
resource_properties,
resource_type
FROM aws.route53profiles.profile_resource_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>profile_resource_association</code>.
```sql
SELECT
region,
profile_id,
id,
name,
resource_arn,
resource_properties,
resource_type
FROM aws.route53profiles.profile_resource_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profile_resource_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53profiles.profile_resource_associations (
 ProfileId,
 Name,
 ResourceArn,
 region
)
SELECT 
'{{ ProfileId }}',
 '{{ Name }}',
 '{{ ResourceArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53profiles.profile_resource_associations (
 ProfileId,
 Name,
 ResourceArn,
 ResourceProperties,
 region
)
SELECT 
 '{{ ProfileId }}',
 '{{ Name }}',
 '{{ ResourceArn }}',
 '{{ ResourceProperties }}',
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
  - name: profile_resource_association
    props:
      - name: ProfileId
        value: '{{ ProfileId }}'
      - name: Name
        value: '{{ Name }}'
      - name: ResourceArn
        value: '{{ ResourceArn }}'
      - name: ResourceProperties
        value: '{{ ResourceProperties }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53profiles.profile_resource_associations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>profile_resource_associations</code> resource, the following permissions are required:

### Create
```json
route53profiles:AssociateResourceToProfile,
route53profiles:GetProfileResourceAssociation,
route53resolver:*,
route53:*
```

### Read
```json
route53profiles:GetProfileResourceAssociation,
route53resolver:*,
route53:*
```

### Delete
```json
route53profiles:DisassociateResourceFromProfile,
route53profiles:GetProfileResourceAssociation,
route53resolver:*,
route53:*
```

### List
```json
route53profiles:ListProfileResourceAssociations,
route53resolver:*,
route53:*
```

### Update
```json
route53profiles:UpdateProfileResourceAssociation,
route53profiles:GetProfileResourceAssociation,
route53resolver:*,
route53:*
```

