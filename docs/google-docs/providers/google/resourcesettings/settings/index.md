---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - resourcesettings
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.resourcesettings.settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the setting. Must be in one of the following forms: * `projects/{project_number}/settings/{setting_name}` * `folders/{folder_id}/settings/{setting_name}` * `organizations/{organization_id}/settings/{setting_name}` For example, "/projects/123/settings/gcp-enableMyFeature" |
| <CopyableCode code="effectiveValue" /> | `object` | The data in a setting value. |
| <CopyableCode code="etag" /> | `string` | A fingerprint used for optimistic concurrency. See UpdateSetting for more details. |
| <CopyableCode code="localValue" /> | `object` | The data in a setting value. |
| <CopyableCode code="metadata" /> | `object` | Metadata about a setting which is not editable by the end user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_settings_get" /> | `SELECT` | <CopyableCode code="foldersId, settingsId" /> | Returns a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. |
| <CopyableCode code="folders_settings_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists all the settings that are available on the Cloud resource `parent`. |
| <CopyableCode code="organizations_settings_get" /> | `SELECT` | <CopyableCode code="organizationsId, settingsId" /> | Returns a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. |
| <CopyableCode code="organizations_settings_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all the settings that are available on the Cloud resource `parent`. |
| <CopyableCode code="projects_settings_get" /> | `SELECT` | <CopyableCode code="projectsId, settingsId" /> | Returns a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. |
| <CopyableCode code="projects_settings_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all the settings that are available on the Cloud resource `parent`. |
| <CopyableCode code="folders_settings_patch" /> | `UPDATE` | <CopyableCode code="foldersId, settingsId" /> | Updates a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if the setting is flagged as read only. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the setting value. On success, the response will contain only `name`, `local_value` and `etag`. The `metadata` and `effective_value` cannot be updated through this API. Note: the supplied setting will perform a full overwrite of the `local_value` field. |
| <CopyableCode code="organizations_settings_patch" /> | `UPDATE` | <CopyableCode code="organizationsId, settingsId" /> | Updates a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if the setting is flagged as read only. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the setting value. On success, the response will contain only `name`, `local_value` and `etag`. The `metadata` and `effective_value` cannot be updated through this API. Note: the supplied setting will perform a full overwrite of the `local_value` field. |
| <CopyableCode code="projects_settings_patch" /> | `UPDATE` | <CopyableCode code="projectsId, settingsId" /> | Updates a specified setting. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the setting does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.FAILED_PRECONDITION` if the setting is flagged as read only. Returns a `google.rpc.Status` with `google.rpc.Code.ABORTED` if the etag supplied in the request does not match the persisted etag of the setting value. On success, the response will contain only `name`, `local_value` and `etag`. The `metadata` and `effective_value` cannot be updated through this API. Note: the supplied setting will perform a full overwrite of the `local_value` field. |

## `SELECT` examples

Lists all the settings that are available on the Cloud resource `parent`.

```sql
SELECT
name,
effectiveValue,
etag,
localValue,
metadata
FROM google.resourcesettings.settings
WHERE foldersId = '{{ foldersId }}';
```

## `UPDATE` example

Updates a <code>settings</code> resource.

```sql
/*+ update */
UPDATE google.resourcesettings.settings
SET 
localValue = '{{ localValue }}',
etag = '{{ etag }}',
name = '{{ name }}'
WHERE 
foldersId = '{{ foldersId }}'
AND settingsId = '{{ settingsId }}';
```
