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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudfunctions.functions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the function. Function names must be unique globally and match pattern `projects/*/locations/*/functions/*` |
| `description` | `string` | User-provided description of a function. |
| `eventTrigger` | `object` | Describes EventTrigger, used to request events to be sent from another service. |
| `serviceConfig` | `object` | Describes the Service being deployed. Currently Supported : Cloud Run (fully managed). |
| `stateMessages` | `array` | Output only. State Messages for this Cloud Function. |
| `labels` | `object` | Labels associated with this Cloud Function. |
| `buildConfig` | `object` | Describes the Build step of the function that builds a container from the given source. |
| `satisfiesPzs` | `boolean` | Output only. Reserved for future use. |
| `updateTime` | `string` | Output only. The last update timestamp of a Cloud Function. |
| `url` | `string` | Output only. The deployed url for the function. |
| `environment` | `string` | Describe whether the function is 1st Gen or 2nd Gen. |
| `kmsKeyName` | `string` | [Preview] Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function resources. It must match the pattern `projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;key_ring&#125;/cryptoKeys/&#123;crypto_key&#125;`. |
| `state` | `string` | Output only. State of the function. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `functionsId, locationsId, projectsId` | Returns a function with the given name from the requested project. |
| `list` | `SELECT` | `locationsId, projectsId` | Returns a list of functions that belong to the requested project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error. |
| `delete` | `DELETE` | `functionsId, locationsId, projectsId` | Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function. |
| `_list` | `EXEC` | `locationsId, projectsId` | Returns a list of functions that belong to the requested project. |
| `generate_download_url` | `EXEC` | `functionsId, locationsId, projectsId` | Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: https://cloud.google.com/storage/docs/access-control/signed-urls |
| `generate_upload_url` | `EXEC` | `locationsId, projectsId` | Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: https://cloud.google.com/storage/docs/access-control/signed-urls. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code. When uploading source code to the generated signed URL, please follow these restrictions: * Source file type should be a zip file. * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL. When making a HTTP PUT request, these two headers need to be specified: * `content-type: application/zip` And this header SHOULD NOT be specified: * `Authorization: Bearer YOUR_TOKEN` |
| `patch` | `EXEC` | `functionsId, locationsId, projectsId` | Updates existing function. |
