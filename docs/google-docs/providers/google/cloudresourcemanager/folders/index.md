---
title: folders
hide_title: false
hide_table_of_contents: false
keywords:
  - folders
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

Creates, updates, deletes, gets or lists a <code>folders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>folders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudresourcemanager.folders" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the folder. Its format is `folders/{folder_id}`, for example: "folders/1234". |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when the folder was created. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Timestamp when the folder was requested to be deleted. |
| <CopyableCode code="displayName" /> | `string` | The folder's display name. A folder's display name must be unique amongst its siblings. For example, no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters. This is captured by the regular expression: `[\p{L}\p{N}]([\p{L}\p{N}_- ]{0,28}[\p{L}\p{N}])?`. |
| <CopyableCode code="etag" /> | `string` | Output only. A checksum computed by the server based on the current value of the folder resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="parent" /> | `string` | Required. The folder's parent's resource name. Updates to the folder's parent must be performed using MoveFolder. |
| <CopyableCode code="state" /> | `string` | Output only. The lifecycle state of the folder. Updates to the state must be performed using DeleteFolder and UndeleteFolder. |
| <CopyableCode code="tags" /> | `object` | Optional. Input only. Immutable. Tag keys/values directly bound to this folder. Each item in the map must be expressed as " : ". For example: "123/environment" : "production", "123/costCenter" : "marketing" Note: Currently this field is in Preview. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when the folder was last modified. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="foldersId" /> | Retrieves a folder identified by the supplied resource name. Valid folder resource names have the format `folders/{folder_id}` (for example, `folders/1234`). The caller must have `resourcemanager.folders.get` permission on the identified folder. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists the folders that are direct descendants of supplied parent resource. `list()` provides a strongly consistent view of the folders underneath the specified parent resource. `list()` returns folders sorted based upon the (ascending) lexical ordering of their display_name. The caller must have `resourcemanager.folders.list` permission on the identified parent. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a folder in the resource hierarchy. Returns an `Operation` which can be used to track the progress of the folder creation workflow. Upon success, the `Operation.response` field will be populated with the created Folder. In order to succeed, the addition of this new folder must not violate the folder naming, height, or fanout constraints. + The folder's `display_name` must be distinct from all other folders that share its parent. + The addition of the folder must not cause the active folder hierarchy to exceed a height of 10. Note, the full active + deleted folder hierarchy is allowed to reach a height of 20; this provides additional headroom when moving folders that contain deleted folders. + The addition of the folder must not cause the total number of folders under its parent to exceed 300. If the operation fails due to a folder constraint violation, some errors may be returned by the `CreateFolder` request, with status code `FAILED_PRECONDITION` and an error description. Other folder constraint violations will be communicated in the `Operation`, with the specific `PreconditionFailure` returned in the details list in the `Operation.error` field. The caller must have `resourcemanager.folders.create` permission on the identified parent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="foldersId" /> | Requests deletion of a folder. The folder is moved into the DELETE_REQUESTED state immediately, and is deleted approximately 30 days later. This method may only be called on an empty folder, where a folder is empty if it doesn't contain any folders or projects in the ACTIVE state. If called on a folder in DELETE_REQUESTED state the operation will result in a no-op success. The caller must have `resourcemanager.folders.delete` permission on the identified folder. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="foldersId" /> | Updates a folder, changing its `display_name`. Changes to the folder `display_name` will be rejected if they violate either the `display_name` formatting rules or the naming constraints described in the CreateFolder documentation. The folder's `display_name` must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be between 3 and 30 characters. This is captured by the regular expression: `\p{L}\p{N}{1,28}[\p{L}\p{N}]`. The caller must have `resourcemanager.folders.update` permission on the identified folder. If the update fails due to the unique name constraint then a `PreconditionFailure` explaining this violation will be returned in the Status.details field. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="foldersId" /> | Moves a folder under a new resource parent. Returns an `Operation` which can be used to track the progress of the folder move workflow. Upon success, the `Operation.response` field will be populated with the moved folder. Upon failure, a `FolderOperationError` categorizing the failure cause will be returned - if the failure occurs synchronously then the `FolderOperationError` will be returned in the `Status.details` field. If it occurs asynchronously, then the FolderOperation will be returned in the `Operation.error` field. In addition, the `Operation.metadata` field will be populated with a `FolderOperation` message as an aid to stateless clients. Folder moves will be rejected if they violate either the naming, height, or fanout constraints described in the CreateFolder documentation. The caller must have `resourcemanager.folders.move` permission on the folder's current and proposed new parent. |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="" /> | Search for folders that match specific filter criteria. `search()` provides an eventually consistent view of the folders a user has access to which meet the specified filter criteria. This will only return folders on which the caller has the permission `resourcemanager.folders.get`. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="foldersId" /> | Cancels the deletion request for a folder. This method may be called on a folder in any state. If the folder is in the ACTIVE state the result will be a no-op success. In order to succeed, the folder's parent must be in the ACTIVE state. In addition, reintroducing the folder into the tree must not violate folder naming, height, and fanout constraints described in the CreateFolder documentation. The caller must have `resourcemanager.folders.undelete` permission on the identified folder. |

## `SELECT` examples

Lists the folders that are direct descendants of supplied parent resource. `list()` provides a strongly consistent view of the folders underneath the specified parent resource. `list()` returns folders sorted based upon the (ascending) lexical ordering of their display_name. The caller must have `resourcemanager.folders.list` permission on the identified parent.

```sql
SELECT
name,
createTime,
deleteTime,
displayName,
etag,
parent,
state,
tags,
updateTime
FROM google.cloudresourcemanager.folders
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>folders</code> resource.

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
INSERT INTO google.cloudresourcemanager.folders (
,
parent,
displayName,
tags
)
SELECT 
'{{  }}',
'{{ parent }}',
'{{ displayName }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: parent
      value: '{{ parent }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: tags
      value: '{{ tags }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>folders</code> resource.

```sql
/*+ update */
UPDATE google.cloudresourcemanager.folders
SET 
parent = '{{ parent }}',
displayName = '{{ displayName }}',
tags = '{{ tags }}'
WHERE 
foldersId = '{{ foldersId }}';
```

## `DELETE` example

Deletes the specified <code>folders</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudresourcemanager.folders
WHERE foldersId = '{{ foldersId }}';
```
