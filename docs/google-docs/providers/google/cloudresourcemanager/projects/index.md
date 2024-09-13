
---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - cloudresourcemanager
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

Creates, updates, deletes or gets an <code>project</code> resource or lists <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The unique resource name of the project. It is an int64 generated number prefixed by "projects/". Example: `projects/415104041262` |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The time at which this resource was requested for deletion. |
| <CopyableCode code="displayName" /> | `string` | Optional. A user-assigned display name of the project. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. Example: `My Project` |
| <CopyableCode code="etag" /> | `string` | Output only. A checksum computed by the server based on the current value of the Project resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels associated with this project. Label keys must be between 1 and 63 characters long and must conform to the following regular expression: \[a-z\](\[-a-z0-9\]*\[a-z0-9\])?. Label values must be between 0 and 63 characters long and must conform to the regular expression (\[a-z\](\[-a-z0-9\]*\[a-z0-9\])?)?. No more than 64 labels can be associated with a given resource. Clients should store labels in a representation such as JSON that does not depend on specific characters being disallowed. Example: `"myBusinessDimension" : "businessValue"` |
| <CopyableCode code="parent" /> | `string` | Optional. A reference to a parent Resource. eg., `organizations/123` or `folders/876`. |
| <CopyableCode code="projectId" /> | `string` | Immutable. The unique, user-assigned id of the project. It must be 6 to 30 lowercase ASCII letters, digits, or hyphens. It must start with a letter. Trailing hyphens are prohibited. Example: `tokyo-rain-123` |
| <CopyableCode code="state" /> | `string` | Output only. The project lifecycle state. |
| <CopyableCode code="tags" /> | `object` | Optional. Input only. Immutable. Tag keys/values directly bound to this project. Each item in the map must be expressed as " : ". For example: "123/environment" : "production", "123/costCenter" : "marketing" Note: Currently this field is in Preview. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time this resource was modified. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectsId" /> | Retrieves the project identified by the specified `name` (for example, `projects/415104041262`). The caller must have `resourcemanager.projects.get` permission for this project. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists projects that are direct children of the specified folder or organization resource. `list()` provides a strongly consistent view of the projects underneath the specified parent resource. `list()` returns projects sorted based upon the (ascending) lexical ordering of their `display_name`. The caller must have `resourcemanager.projects.list` permission on the identified parent. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Request that a new project be created. The result is an `Operation` which can be used to track the creation process. This process usually takes a few seconds, but can sometimes take much longer. The tracking `Operation` is automatically deleted after a few hours, so there is no need to call `DeleteOperation`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectsId" /> | Marks the project identified by the specified `name` (for example, `projects/415104041262`) for deletion. This method will only affect the project if it has a lifecycle state of ACTIVE. This method changes the Project's lifecycle state from ACTIVE to DELETE_REQUESTED. The deletion starts at an unspecified time, at which point the Project is no longer accessible. Until the deletion completes, you can check the lifecycle state checked by retrieving the project with GetProject, and the project remains visible to ListProjects. However, you cannot update the project. After the deletion completes, the project is not retrievable by the GetProject, ListProjects, and SearchProjects methods. This method behaves idempotently, such that deleting a `DELETE_REQUESTED` project will not cause an error, but also won't do anything. The caller must have `resourcemanager.projects.delete` permissions for this project. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="projectsId" /> | Updates the `display_name` and labels of the project identified by the specified `name` (for example, `projects/415104041262`). Deleting all labels requires an update mask for labels field. The caller must have `resourcemanager.projects.update` permission for this project. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="projectsId" /> | Move a project to another place in your resource hierarchy, under a new resource parent. Returns an operation which can be used to track the process of the project move workflow. Upon success, the `Operation.response` field will be populated with the moved project. The caller must have `resourcemanager.projects.move` permission on the project, on the project's current and proposed new parent. If project has no current parent, or it currently does not have an associated organization resource, you will also need the `resourcemanager.projects.setIamPolicy` permission in the project.  |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="" /> | Search for projects that the caller has the `resourcemanager.projects.get` permission on, and also satisfy the specified query. This method returns projects in an unspecified order. This method is eventually consistent with project mutations; this means that a newly created project may not appear in the results or recent updates to an existing project may not be reflected in the results. To retrieve the latest state of a project, use the GetProject method. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="projectsId" /> | Restores the project identified by the specified `name` (for example, `projects/415104041262`). You can only use this method for a project that has a lifecycle state of DELETE_REQUESTED. After deletion starts, the project cannot be restored. The caller must have `resourcemanager.projects.undelete` permission for this project. |

## `SELECT` examples

Lists projects that are direct children of the specified folder or organization resource. `list()` provides a strongly consistent view of the projects underneath the specified parent resource. `list()` returns projects sorted based upon the (ascending) lexical ordering of their `display_name`. The caller must have `resourcemanager.projects.list` permission on the identified parent.

```sql
SELECT
name,
createTime,
deleteTime,
displayName,
etag,
labels,
parent,
projectId,
state,
tags,
updateTime
FROM google.cloudresourcemanager.projects
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>projects</code> resource.

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
INSERT INTO google.cloudresourcemanager.projects (
,
name,
parent,
projectId,
state,
displayName,
createTime,
updateTime,
deleteTime,
etag,
labels,
tags
)
SELECT 
'{{  }}',
'{{ name }}',
'{{ parent }}',
'{{ projectId }}',
'{{ state }}',
'{{ displayName }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ etag }}',
'{{ labels }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: parent
        value: '{{ parent }}'
      - name: projectId
        value: '{{ projectId }}'
      - name: state
        value: '{{ state }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: etag
        value: '{{ etag }}'
      - name: labels
        value: '{{ labels }}'
      - name: tags
        value: '{{ tags }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a project only if the necessary resources are available.

```sql
UPDATE google.cloudresourcemanager.projects
SET 
name = '{{ name }}',
parent = '{{ parent }}',
projectId = '{{ projectId }}',
state = '{{ state }}',
displayName = '{{ displayName }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
deleteTime = '{{ deleteTime }}',
etag = '{{ etag }}',
labels = '{{ labels }}',
tags = '{{ tags }}'
WHERE 
projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified project resource.

```sql
DELETE FROM google.cloudresourcemanager.projects
WHERE projectsId = '{{ projectsId }}';
```
