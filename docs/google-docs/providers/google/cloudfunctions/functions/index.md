---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
  - cloudfunctions
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

Creates, updates, deletes, gets or lists a <code>functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudfunctions.functions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A user-defined name of the function. Function names must be unique globally and match pattern `projects/*/locations/*/functions/*` |
| <CopyableCode code="description" /> | `string` | User-provided description of a function. |
| <CopyableCode code="buildConfig" /> | `object` | Describes the Build step of the function that builds a container from the given source. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create timestamp of a Cloud Function. This is only applicable to 2nd Gen functions. |
| <CopyableCode code="environment" /> | `string` | Describe whether the function is 1st Gen or 2nd Gen. |
| <CopyableCode code="eventTrigger" /> | `object` | Describes EventTrigger, used to request events to be sent from another service. |
| <CopyableCode code="kmsKeyName" /> | `string` | Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function resources. It must match the pattern `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`. |
| <CopyableCode code="labels" /> | `object` | Labels associated with this Cloud Function. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="serviceConfig" /> | `object` | Describes the Service being deployed. Currently Supported : Cloud Run (fully managed). |
| <CopyableCode code="state" /> | `string` | Output only. State of the function. |
| <CopyableCode code="stateMessages" /> | `array` | Output only. State Messages for this Cloud Function. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a Cloud Function. |
| <CopyableCode code="upgradeInfo" /> | `object` | Information related to: * A function's eligibility for 1st Gen to 2nd Gen migration * Current state of migration for function undergoing migration. |
| <CopyableCode code="url" /> | `string` | Output only. The deployed url for the function. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Returns a function with the given name from the requested project. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns a list of functions that belong to the requested project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Updates existing function. |
| <CopyableCode code="abort_function_upgrade" /> | `EXEC` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Aborts generation upgrade process for a function with the given name from the specified project. Deletes all 2nd Gen copy related configuration and resources which were created during the upgrade process. |
| <CopyableCode code="commit_function_upgrade" /> | `EXEC` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Finalizes the upgrade after which function upgrade can not be rolled back. This is the last step of the multi step process to upgrade 1st Gen functions to 2nd Gen. Deletes all original 1st Gen related configuration and resources. |
| <CopyableCode code="generate_download_url" /> | `EXEC` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: https://cloud.google.com/storage/docs/access-control/signed-urls |
| <CopyableCode code="generate_upload_url" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: https://cloud.google.com/storage/docs/access-control/signed-urls. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code. When uploading source code to the generated signed URL, please follow these restrictions: * Source file type should be a zip file. * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL. When making a HTTP PUT request, specify this header: * `content-type: application/zip` Do not specify this header: * `Authorization: Bearer YOUR_TOKEN` |
| <CopyableCode code="redirect_function_upgrade_traffic" /> | `EXEC` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Changes the traffic target of a function from the original 1st Gen function to the 2nd Gen copy. This is the second step of the multi step process to upgrade 1st Gen functions to 2nd Gen. After this operation, all new traffic will be served by 2nd Gen copy. |
| <CopyableCode code="rollback_function_upgrade_traffic" /> | `EXEC` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Reverts the traffic target of a function from the 2nd Gen copy to the original 1st Gen function. After this operation, all new traffic would be served by the 1st Gen. |
| <CopyableCode code="setup_function_upgrade_config" /> | `EXEC` | <CopyableCode code="functionsId, locationsId, projectsId" /> | Creates a 2nd Gen copy of the function configuration based on the 1st Gen function with the given name. This is the first step of the multi step process to upgrade 1st Gen functions to 2nd Gen. Only 2nd Gen configuration is setup as part of this request and traffic continues to be served by 1st Gen. |

## `SELECT` examples

Returns a list of functions that belong to the requested project.

```sql
SELECT
name,
description,
buildConfig,
createTime,
environment,
eventTrigger,
kmsKeyName,
labels,
satisfiesPzs,
serviceConfig,
state,
stateMessages,
updateTime,
upgradeInfo,
url
FROM google.cloudfunctions.functions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>functions</code> resource.

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
INSERT INTO google.cloudfunctions.functions (
locationsId,
projectsId,
name,
description,
buildConfig,
serviceConfig,
eventTrigger,
state,
updateTime,
labels,
stateMessages,
environment,
upgradeInfo,
url,
kmsKeyName,
satisfiesPzs,
createTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ buildConfig }}',
'{{ serviceConfig }}',
'{{ eventTrigger }}',
'{{ state }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ stateMessages }}',
'{{ environment }}',
'{{ upgradeInfo }}',
'{{ url }}',
'{{ kmsKeyName }}',
true|false,
'{{ createTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: buildConfig
      value: '{{ buildConfig }}'
    - name: serviceConfig
      value: '{{ serviceConfig }}'
    - name: eventTrigger
      value: '{{ eventTrigger }}'
    - name: state
      value: '{{ state }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: stateMessages
      value: '{{ stateMessages }}'
    - name: environment
      value: '{{ environment }}'
    - name: upgradeInfo
      value: '{{ upgradeInfo }}'
    - name: url
      value: '{{ url }}'
    - name: kmsKeyName
      value: '{{ kmsKeyName }}'
    - name: satisfiesPzs
      value: '{{ satisfiesPzs }}'
    - name: createTime
      value: '{{ createTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>functions</code> resource.

```sql
/*+ update */
UPDATE google.cloudfunctions.functions
SET 
name = '{{ name }}',
description = '{{ description }}',
buildConfig = '{{ buildConfig }}',
serviceConfig = '{{ serviceConfig }}',
eventTrigger = '{{ eventTrigger }}',
state = '{{ state }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
stateMessages = '{{ stateMessages }}',
environment = '{{ environment }}',
upgradeInfo = '{{ upgradeInfo }}',
url = '{{ url }}',
kmsKeyName = '{{ kmsKeyName }}',
satisfiesPzs = true|false,
createTime = '{{ createTime }}'
WHERE 
functionsId = '{{ functionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>functions</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudfunctions.functions
WHERE functionsId = '{{ functionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
