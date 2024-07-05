---
title: security_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profiles
  - connect
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

Creates, updates, deletes or gets a <code>security_profile</code> resource or lists <code>security_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::SecurityProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.security_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="allowed_access_control_tags" /></td><td><code>array</code></td><td>The list of tags that a security profile uses to restrict access to resources in Amazon Connect.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the security profile.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td>Permissions assigned to the security profile.</td></tr>
<tr><td><CopyableCode code="security_profile_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the security profile.</td></tr>
<tr><td><CopyableCode code="security_profile_name" /></td><td><code>string</code></td><td>The name of the security profile.</td></tr>
<tr><td><CopyableCode code="tag_restricted_resources" /></td><td><code>array</code></td><td>The list of resources that a security profile applies tag restrictions to in Amazon Connect.</td></tr>
<tr><td><CopyableCode code="hierarchy_restricted_resources" /></td><td><code>array</code></td><td>The list of resources that a security profile applies hierarchy restrictions to in Amazon Connect.</td></tr>
<tr><td><CopyableCode code="allowed_access_control_hierarchy_group_id" /></td><td><code>string</code></td><td>The identifier of the hierarchy group that a security profile uses to restrict access to resources in Amazon Connect.</td></tr>
<tr><td><CopyableCode code="applications" /></td><td><code>array</code></td><td>A list of third-party applications that the security profile will give access to.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags used to organize, track, or control access for this resource.</td></tr>
<tr><td><CopyableCode code="last_modified_region" /></td><td><code>string</code></td><td>The AWS Region where this resource was last modified.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>number</code></td><td>The timestamp when this resource was last modified.</td></tr>
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
    <td><CopyableCode code="InstanceArn, SecurityProfileName, region" /></td>
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
Gets all <code>security_profiles</code> in a region.
```sql
SELECT
region,
allowed_access_control_tags,
description,
instance_arn,
permissions,
security_profile_arn,
security_profile_name,
tag_restricted_resources,
hierarchy_restricted_resources,
allowed_access_control_hierarchy_group_id,
applications,
tags,
last_modified_region,
last_modified_time
FROM aws.connect.security_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>security_profile</code>.
```sql
SELECT
region,
allowed_access_control_tags,
description,
instance_arn,
permissions,
security_profile_arn,
security_profile_name,
tag_restricted_resources,
hierarchy_restricted_resources,
allowed_access_control_hierarchy_group_id,
applications,
tags,
last_modified_region,
last_modified_time
FROM aws.connect.security_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<SecurityProfileArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.security_profiles (
 InstanceArn,
 SecurityProfileName,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ SecurityProfileName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.security_profiles (
 AllowedAccessControlTags,
 Description,
 InstanceArn,
 Permissions,
 SecurityProfileName,
 TagRestrictedResources,
 HierarchyRestrictedResources,
 AllowedAccessControlHierarchyGroupId,
 Applications,
 Tags,
 region
)
SELECT 
 '{{ AllowedAccessControlTags }}',
 '{{ Description }}',
 '{{ InstanceArn }}',
 '{{ Permissions }}',
 '{{ SecurityProfileName }}',
 '{{ TagRestrictedResources }}',
 '{{ HierarchyRestrictedResources }}',
 '{{ AllowedAccessControlHierarchyGroupId }}',
 '{{ Applications }}',
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
  - name: security_profile
    props:
      - name: AllowedAccessControlTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Description
        value: '{{ Description }}'
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Permissions
        value:
          - '{{ Permissions[0] }}'
      - name: SecurityProfileName
        value: '{{ SecurityProfileName }}'
      - name: TagRestrictedResources
        value:
          - '{{ TagRestrictedResources[0] }}'
      - name: HierarchyRestrictedResources
        value:
          - null
      - name: AllowedAccessControlHierarchyGroupId
        value: '{{ AllowedAccessControlHierarchyGroupId }}'
      - name: Applications
        value:
          - ApplicationPermissions:
              - '{{ ApplicationPermissions[0] }}'
            Namespace: '{{ Namespace }}'
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.security_profiles
WHERE data__Identifier = '<SecurityProfileArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_profiles</code> resource, the following permissions are required:

### Create
```json
connect:CreateSecurityProfile,
connect:TagResource
```

### Read
```json
connect:DescribeSecurityProfile,
connect:ListSecurityProfileApplications,
connect:ListSecurityProfilePermissions
```

### Update
```json
connect:TagResource,
connect:UpdateSecurityProfile,
connect:UntagResource
```

### Delete
```json
connect:DeleteSecurityProfile,
connect:UntagResource
```

### List
```json
connect:ListSecurityProfiles
```

