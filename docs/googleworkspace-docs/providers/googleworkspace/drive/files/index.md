---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - drive
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the file. |
| `name` | `string` | The name of the file. This is not necessarily unique within a folder. Note that for immutable items such as the top level folders of shared drives, My Drive root folder, and Application Data folder the name is constant. |
| `description` | `string` | A short description of the file. |
| `hasAugmentedPermissions` | `boolean` | Whether there are permissions directly on this file. This field is only populated for items in shared drives. |
| `contentHints` | `object` | Additional information about the content of the file. These fields are never populated in responses. |
| `thumbnailVersion` | `string` | The thumbnail version for use in thumbnail cache invalidation. |
| `parents` | `array` | The IDs of the parent folders which contain the file.<br />If not specified as part of a create request, the file will be placed directly in the user's My Drive folder. If not specified as part of a copy request, the file will inherit any discoverable parents of the source file. Update requests must use the addParents and removeParents parameters to modify the parents list. |
| `copyRequiresWriterPermission` | `boolean` | Whether the options to copy, print, or download this file, should be disabled for readers and commenters. |
| `permissions` | `array` | The full list of permissions for the file. This is only available if the requesting user can share the file. Not populated for items in shared drives. |
| `driveId` | `string` | ID of the shared drive the file resides in. Only populated for items in shared drives. |
| `createdTime` | `string` | The time at which the file was created (RFC 3339 date-time). |
| `version` | `string` | A monotonically increasing version number for the file. This reflects every change made to the file on the server, even those not visible to the user. |
| `explicitlyTrashed` | `boolean` | Whether the file has been explicitly trashed, as opposed to recursively trashed from a parent folder. |
| `resourceKey` | `string` | A key needed to access the item via a shared link. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#file". |
| `owners` | `array` | The owner of this file. Only certain legacy files may have more than one owner. This field isn't populated for items in shared drives. |
| `originalFilename` | `string` | The original filename of the uploaded content if available, or else the original value of the name field. This is only available for files with binary content in Google Drive. |
| `appProperties` | `object` | A collection of arbitrary key-value pairs which are private to the requesting app.<br />Entries with null values are cleared in update and copy requests. These properties can only be retrieved using an authenticated request. An authenticated request uses an access token obtained with a OAuth 2 client ID. You cannot use an API key to retrieve private properties. |
| `contentRestrictions` | `array` | Restrictions for accessing the content of the file. Only populated if such a restriction exists. |
| `trashedTime` | `string` | The time that the item was trashed (RFC 3339 date-time). Only populated for items in shared drives. |
| `shortcutDetails` | `object` | Shortcut file details. Only populated for shortcut files, which have the mimeType field set to application/vnd.google-apps.shortcut. |
| `hasThumbnail` | `boolean` | Whether this file has a thumbnail. This does not indicate whether the requesting app has access to the thumbnail. To check access, look for the presence of the thumbnailLink field. |
| `sha1Checksum` | `string` | The SHA1 checksum associated with this file, if available. This field is only populated for files with content stored in Google Drive; it isn't populated for Docs Editors or shortcut files. |
| `imageMediaMetadata` | `object` | Additional metadata about image media, if available. |
| `quotaBytesUsed` | `string` | The number of storage quota bytes used by the file. This includes the head revision as well as previous revisions with keepForever enabled. |
| `mimeType` | `string` | The MIME type of the file.<br />Google Drive will attempt to automatically detect an appropriate value from uploaded content if no value is provided. The value cannot be changed unless a new revision is uploaded.<br />If a file is created with a Google Doc MIME type, the uploaded content will be imported if possible. The supported import formats are published in the About resource. |
| `starred` | `boolean` | Whether the user has starred the file. |
| `linkShareMetadata` | `object` | Contains details about the link URLs that clients are using to refer to this item. |
| `spaces` | `array` | The list of spaces which contain the file. The currently supported values are 'drive', 'appDataFolder' and 'photos'. |
| `modifiedTime` | `string` | The last time the file was modified by anyone (RFC 3339 date-time).<br />Note that setting modifiedTime will also update modifiedByMeTime for the user. |
| `permissionIds` | `array` | List of permission IDs for users with access to this file. |
| `sharedWithMeTime` | `string` | The time at which the file was shared with the user, if applicable (RFC 3339 date-time). |
| `headRevisionId` | `string` | The ID of the file's head revision. This is currently only available for files with binary content in Google Drive. |
| `iconLink` | `string` | A static, unauthenticated link to the file's icon. |
| `writersCanShare` | `boolean` | Whether users with only writer permission can modify the file's permissions. Not populated for items in shared drives. |
| `modifiedByMe` | `boolean` | Whether the file has been modified by this user. |
| `teamDriveId` | `string` | Deprecated - use driveId instead. |
| `exportLinks` | `object` | Links for exporting Docs Editors files to specific formats. |
| `size` | `string` | The size of the file's content in bytes. This is applicable to binary files in Google Drive and Google Docs files. |
| `viewedByMe` | `boolean` | Whether the file has been viewed by this user. |
| `shared` | `boolean` | Whether the file has been shared. Not populated for items in shared drives. |
| `viewersCanCopyContent` | `boolean` | Deprecated - use copyRequiresWriterPermission instead. |
| `labelInfo` | `object` | An overview of the labels on the file. |
| `sharingUser` | `object` | Information about a Drive user. |
| `webViewLink` | `string` | A link for opening the file in a relevant Google editor or viewer in a browser. |
| `fileExtension` | `string` | The final component of fullFileExtension. This is only available for files with binary content in Google Drive. |
| `modifiedByMeTime` | `string` | The last time the file was modified by the user (RFC 3339 date-time). |
| `trashed` | `boolean` | Whether the file has been trashed, either explicitly or from a trashed parent folder. Only the owner may trash a file. The trashed item is excluded from all files.list responses returned for any user who does not own the file. However, all users with access to the file can see the trashed item metadata in an API response. All users with access can copy, download, export, and share the file. |
| `folderColorRgb` | `string` | The color for a folder or shortcut to a folder as an RGB hex string. The supported colors are published in the folderColorPalette field of the About resource.<br />If an unsupported color is specified, the closest color in the palette will be used instead. |
| `sha256Checksum` | `string` | The SHA256 checksum associated with this file, if available. This field is only populated for files with content stored in Google Drive; it isn't populated for Docs Editors or shortcut files. |
| `viewedByMeTime` | `string` | The last time the file was viewed by the user (RFC 3339 date-time). |
| `md5Checksum` | `string` | The MD5 checksum for the content of the file. This is only applicable to files with binary content in Google Drive. |
| `webContentLink` | `string` | A link for downloading the content of the file in a browser. This is only available for files with binary content in Google Drive. |
| `fullFileExtension` | `string` | The full file extension extracted from the name field. May contain multiple concatenated extensions, such as "tar.gz". This is only available for files with binary content in Google Drive.<br />This is automatically updated when the name field changes, however it isn't cleared if the new name does not contain a valid extension. |
| `trashingUser` | `object` | Information about a Drive user. |
| `ownedByMe` | `boolean` | Whether the user owns the file. Not populated for items in shared drives. |
| `videoMediaMetadata` | `object` | Additional metadata about video media. This may not be available immediately upon upload. |
| `lastModifyingUser` | `object` | Information about a Drive user. |
| `capabilities` | `object` | Capabilities the current user has on this file. Each capability corresponds to a fine-grained action that a user may take. |
| `thumbnailLink` | `string` | A short-lived link to the file's thumbnail, if available. Typically lasts on the order of hours. Only populated when the requesting app can access the file's content. If the file isn't shared publicly, the URL returned in Files.thumbnailLink must be fetched using a credentialed request. |
| `properties` | `object` | A collection of arbitrary key-value pairs which are visible to all apps.<br />Entries with null values are cleared in update and copy requests. |
| `isAppAuthorized` | `boolean` | Whether the file was created or opened by the requesting app. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileId` | Gets a file's metadata or content by ID. |
| `list` | `SELECT` |  | Lists or searches files. |
| `create` | `INSERT` |  | Creates a file. |
| `delete` | `DELETE` | `fileId` | Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive the user must be an organizer on the parent. If the target is a folder, all descendants owned by the user are also deleted. |
| `copy` | `EXEC` | `fileId` | Creates a copy of a file and applies any requested updates with patch semantics. Folders cannot be copied. |
| `emptyTrash` | `EXEC` |  | Permanently deletes all of the user's trashed files. |
| `export` | `EXEC` | `fileId, mimeType` | Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB. |
| `generateIds` | `EXEC` |  | Generates a set of file IDs which can be provided in create or copy requests. |
| `modifyLabels` | `EXEC` | `fileId` | Modifies the set of labels on a file. |
| `update` | `EXEC` | `fileId` | Updates a file's metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might change automatically, such as modifiedDate. This method supports patch semantics. |
| `watch` | `EXEC` | `fileId` | Subscribes to changes to a file. While you can establish a channel for changes to a file on a shared drive, a change to a shared drive file won't create a notification. |
