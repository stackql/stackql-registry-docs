---
title: archive_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - archive_deployments
  - apigee
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

Creates, updates, deletes, gets or lists a <code>archive_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>archive_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.archive_deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the Archive Deployment in the following format: `organizations/{org}/environments/{env}/archiveDeployments/{id}`. |
| <CopyableCode code="createdAt" /> | `string` | Output only. The time at which the Archive Deployment was created in milliseconds since the epoch. |
| <CopyableCode code="gcsUri" /> | `string` | Input only. The Google Cloud Storage signed URL returned from GenerateUploadUrl and used to upload the Archive zip file. |
| <CopyableCode code="labels" /> | `object` | User-supplied key-value pairs used to organize ArchiveDeployments. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
| <CopyableCode code="operation" /> | `string` | Output only. A reference to the LRO that created this Archive Deployment in the following format: `organizations/{org}/operations/{id}` |
| <CopyableCode code="updatedAt" /> | `string` | Output only. The time at which the Archive Deployment was updated in milliseconds since the epoch. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_archive_deployments_get" /> | `SELECT` | <CopyableCode code="archiveDeploymentsId, environmentsId, organizationsId" /> | Gets the specified ArchiveDeployment. |
| <CopyableCode code="organizations_environments_archive_deployments_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Lists the ArchiveDeployments in the specified Environment. |
| <CopyableCode code="organizations_environments_archive_deployments_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a new ArchiveDeployment. |
| <CopyableCode code="organizations_environments_archive_deployments_delete" /> | `DELETE` | <CopyableCode code="archiveDeploymentsId, environmentsId, organizationsId" /> | Deletes an archive deployment. |
| <CopyableCode code="organizations_environments_archive_deployments_patch" /> | `UPDATE` | <CopyableCode code="archiveDeploymentsId, environmentsId, organizationsId" /> | Updates an existing ArchiveDeployment. Labels can modified but most of the other fields are not modifiable. |
| <CopyableCode code="organizations_environments_archive_deployments_generate_download_url" /> | `EXEC` | <CopyableCode code="archiveDeploymentsId, environmentsId, organizationsId" /> | Generates a signed URL for downloading the original zip file used to create an Archive Deployment. The URL is only valid for a limited period and should be used within minutes after generation. Each call returns a new upload URL. |
| <CopyableCode code="organizations_environments_archive_deployments_generate_upload_url" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Generates a signed URL for uploading an Archive zip file to Google Cloud Storage. Once the upload is complete, the signed URL should be passed to CreateArchiveDeployment. When uploading to the generated signed URL, please follow these restrictions: * Source file type should be a zip file. * Source file size should not exceed 1GB limit. * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL. When making a HTTP PUT request, these two headers need to be specified: * `content-type: application/zip` * `x-goog-content-length-range: 0,1073741824` And this header SHOULD NOT be specified: * `Authorization: Bearer YOUR_TOKEN` |

## `SELECT` examples

Lists the ArchiveDeployments in the specified Environment.

```sql
SELECT
name,
createdAt,
gcsUri,
labels,
operation,
updatedAt
FROM google.apigee.archive_deployments
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>archive_deployments</code> resource.

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
INSERT INTO google.apigee.archive_deployments (
environmentsId,
organizationsId,
gcsUri,
name,
labels
)
SELECT 
'{{ environmentsId }}',
'{{ organizationsId }}',
'{{ gcsUri }}',
'{{ name }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
createdAt: string
gcsUri: string
name: string
operation: string
updatedAt: string
labels: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>archive_deployments</code> resource.

```sql
/*+ update */
UPDATE google.apigee.archive_deployments
SET 
gcsUri = '{{ gcsUri }}',
name = '{{ name }}',
labels = '{{ labels }}'
WHERE 
archiveDeploymentsId = '{{ archiveDeploymentsId }}'
AND environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>archive_deployments</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.archive_deployments
WHERE archiveDeploymentsId = '{{ archiveDeploymentsId }}'
AND environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
