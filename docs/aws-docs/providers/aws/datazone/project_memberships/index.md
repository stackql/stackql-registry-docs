---
title: project_memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - project_memberships
  - datazone
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

Creates, updates, deletes or gets a <code>project_membership</code> resource or lists <code>project_memberships</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project_memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::ProjectMembership Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.project_memberships" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="project_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="designation" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="member" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Designation, DomainIdentifier, ProjectIdentifier, Member, region" /></td>
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
Gets all <code>project_memberships</code> in a region.
```sql
SELECT
region,
project_identifier,
designation,
member,
domain_identifier
FROM aws.datazone.project_memberships
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>project_membership</code>.
```sql
SELECT
region,
project_identifier,
designation,
member,
domain_identifier
FROM aws.datazone.project_memberships
WHERE region = 'us-east-1' AND data__Identifier = '<DomainIdentifier>|<MemberIdentifier>|<MemberIdentifierType>|<ProjectIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>project_membership</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datazone.project_memberships (
 ProjectIdentifier,
 Designation,
 Member,
 DomainIdentifier,
 region
)
SELECT 
'{{ ProjectIdentifier }}',
 '{{ Designation }}',
 '{{ Member }}',
 '{{ DomainIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datazone.project_memberships (
 ProjectIdentifier,
 Designation,
 Member,
 DomainIdentifier,
 region
)
SELECT 
 '{{ ProjectIdentifier }}',
 '{{ Designation }}',
 '{{ Member }}',
 '{{ DomainIdentifier }}',
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
  - name: project_membership
    props:
      - name: ProjectIdentifier
        value: '{{ ProjectIdentifier }}'
      - name: Designation
        value: '{{ Designation }}'
      - name: Member
        value: null
      - name: DomainIdentifier
        value: '{{ DomainIdentifier }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datazone.project_memberships
WHERE data__Identifier = '<DomainIdentifier|MemberIdentifier|MemberIdentifierType|ProjectIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>project_memberships</code> resource, the following permissions are required:

### Read
```json
datazone:ListProjectMemberships
```

### Create
```json
datazone:CreateProjectMembership,
datazone:ListProjectMemberships,
iam:GetRole,
datazone:GetGroupProfile,
datazone:GetUserProfile
```

### Update
```json
datazone:CreateProjectMembership,
datazone:DeleteProjectMembership
```

### List
```json
datazone:ListProjectMemberships
```

### Delete
```json
datazone:DeleteProjectMembership
```

