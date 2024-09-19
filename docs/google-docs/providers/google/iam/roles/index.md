---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - iam
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the role. When `Role` is used in `CreateRole`, the role name must not be set. When `Role` is used in output and other input such as `UpdateRole`, the role name is the complete path. For example, `roles/logging.viewer` for predefined roles, `organizations/{ORGANIZATION_ID}/roles/myRole` for organization-level custom roles, and `projects/{PROJECT_ID}/roles/myRole` for project-level custom roles. |
| <CopyableCode code="description" /> | `string` | Optional. A human-readable description for the role. |
| <CopyableCode code="deleted" /> | `boolean` | The current deleted state of the role. This field is read only. It will be ignored in calls to CreateRole and UpdateRole. |
| <CopyableCode code="etag" /> | `string` | Used to perform a consistent read-modify-write. |
| <CopyableCode code="includedPermissions" /> | `array` | The names of the permissions this role grants when bound in an IAM policy. |
| <CopyableCode code="stage" /> | `string` | The current launch stage of the role. If the `ALPHA` launch stage has been selected for a role, the `stage` field will not be included in the returned definition for the role. |
| <CopyableCode code="title" /> | `string` | Optional. A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="rolesId" /> | Gets the definition of a Role. |
| <CopyableCode code="get_org_roles" /> | `SELECT` | <CopyableCode code="organizationsId, rolesId" /> | Gets the definition of a Role. |
| <CopyableCode code="get_project_roles" /> | `SELECT` | <CopyableCode code="projectsId, rolesId" /> | Gets the definition of a Role. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists every predefined Role that IAM supports, or every custom role that is defined for an organization or project. |
| <CopyableCode code="list_org_roles" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists every predefined Role that IAM supports, or every custom role that is defined for an organization or project. |
| <CopyableCode code="list_project_roles" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists every predefined Role that IAM supports, or every custom role that is defined for an organization or project. |
| <CopyableCode code="create_org_roles" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a new custom Role. |
| <CopyableCode code="create_project_roles" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new custom Role. |
| <CopyableCode code="delete_org_roles" /> | `DELETE` | <CopyableCode code="organizationsId, rolesId" /> | Deletes a custom Role. When you delete a custom role, the following changes occur immediately: * You cannot bind a principal to the custom role in an IAM Policy. * Existing bindings to the custom role are not changed, but they have no effect. * By default, the response from ListRoles does not include the custom role. A deleted custom role still counts toward the [custom role limit](https://cloud.google.com/iam/help/limits) until it is permanently deleted. You have 7 days to undelete the custom role. After 7 days, the following changes occur: * The custom role is permanently deleted and cannot be recovered. * If an IAM policy contains a binding to the custom role, the binding is permanently removed. * The custom role no longer counts toward your custom role limit. |
| <CopyableCode code="delete_project_roles" /> | `DELETE` | <CopyableCode code="projectsId, rolesId" /> | Deletes a custom Role. When you delete a custom role, the following changes occur immediately: * You cannot bind a principal to the custom role in an IAM Policy. * Existing bindings to the custom role are not changed, but they have no effect. * By default, the response from ListRoles does not include the custom role. A deleted custom role still counts toward the [custom role limit](https://cloud.google.com/iam/help/limits) until it is permanently deleted. You have 7 days to undelete the custom role. After 7 days, the following changes occur: * The custom role is permanently deleted and cannot be recovered. * If an IAM policy contains a binding to the custom role, the binding is permanently removed. * The custom role no longer counts toward your custom role limit. |
| <CopyableCode code="patch_org_roles" /> | `UPDATE` | <CopyableCode code="organizationsId, rolesId" /> | Updates the definition of a custom Role. |
| <CopyableCode code="patch_project_roles" /> | `UPDATE` | <CopyableCode code="projectsId, rolesId" /> | Updates the definition of a custom Role. |
| <CopyableCode code="query_grantable_roles" /> | `EXEC` | <CopyableCode code="" /> | Lists roles that can be granted on a Google Cloud resource. A role is grantable if the IAM policy for the resource can contain bindings to the role. |
| <CopyableCode code="undelete_org_roles" /> | `EXEC` | <CopyableCode code="organizationsId, rolesId" /> | Undeletes a custom Role. |
| <CopyableCode code="undelete_project_roles" /> | `EXEC` | <CopyableCode code="projectsId, rolesId" /> | Undeletes a custom Role. |

## `SELECT` examples

Lists every predefined Role that IAM supports, or every custom role that is defined for an organization or project.

```sql
SELECT
name,
description,
deleted,
etag,
includedPermissions,
stage,
title
FROM google.iam.roles
;
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>roles</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.iam.roles (
projectsId,
roleId,
role
)
SELECT 
'{{ projectsId }}',
'{{ roleId }}',
'{{ role }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: roleId
      value: string
    - name: role
      value:
        - name: name
          value: string
        - name: title
          value: string
        - name: description
          value: string
        - name: includedPermissions
          value:
            - string
        - name: stage
          value: string
        - name: etag
          value: string
        - name: deleted
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>roles</code> resource.

```sql
/*+ update */
UPDATE google.iam.roles
SET 
name = '{{ name }}',
title = '{{ title }}',
description = '{{ description }}',
includedPermissions = '{{ includedPermissions }}',
stage = '{{ stage }}',
etag = '{{ etag }}',
deleted = true|false
WHERE 
projectsId = '{{ projectsId }}'
AND rolesId = '{{ rolesId }}';
```

## `DELETE` example

Deletes the specified <code>roles</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.roles
WHERE projectsId = '{{ projectsId }}'
AND rolesId = '{{ rolesId }}';
```
