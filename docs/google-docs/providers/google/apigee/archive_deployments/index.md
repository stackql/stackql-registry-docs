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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>archive_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.archive_deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the Archive Deployment in the following format: `organizations/{org}/environments/{env}/archiveDeployments/{id}`. |
| `operation` | `string` | Output only. A reference to the LRO that created this Archive Deployment in the following format: `organizations/{org}/operations/{id}` |
| `updatedAt` | `string` | Output only. The time at which the Archive Deployment was updated in milliseconds since the epoch. |
| `createdAt` | `string` | Output only. The time at which the Archive Deployment was created in milliseconds since the epoch. |
| `gcsUri` | `string` | Input only. The Google Cloud Storage signed URL returned from GenerateUploadUrl and used to upload the Archive zip file. |
| `labels` | `object` | User-supplied key-value pairs used to organize ArchiveDeployments. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_archiveDeployments_get` | `SELECT` | `archiveDeploymentsId, environmentsId, organizationsId` | Gets the specified ArchiveDeployment. |
| `organizations_environments_archiveDeployments_list` | `SELECT` | `environmentsId, organizationsId` | Lists the ArchiveDeployments in the specified Environment. |
| `organizations_environments_archiveDeployments_create` | `INSERT` | `environmentsId, organizationsId` | Creates a new ArchiveDeployment. |
| `organizations_environments_archiveDeployments_delete` | `DELETE` | `archiveDeploymentsId, environmentsId, organizationsId` | Deletes an archive deployment. |
| `organizations_environments_archiveDeployments_generateDownloadUrl` | `EXEC` | `archiveDeploymentsId, environmentsId, organizationsId` | Generates a signed URL for downloading the original zip file used to create an Archive Deployment. The URL is only valid for a limited period and should be used within minutes after generation. Each call returns a new upload URL. |
| `organizations_environments_archiveDeployments_generateUploadUrl` | `EXEC` | `environmentsId, organizationsId` | Generates a signed URL for uploading an Archive zip file to Google Cloud Storage. Once the upload is complete, the signed URL should be passed to CreateArchiveDeployment. When uploading to the generated signed URL, please follow these restrictions: * Source file type should be a zip file. * Source file size should not exceed 1GB limit. * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL. When making a HTTP PUT request, these two headers need to be specified: * `content-type: application/zip` * `x-goog-content-length-range: 0,1073741824` And this header SHOULD NOT be specified: * `Authorization: Bearer YOUR_TOKEN` |
| `organizations_environments_archiveDeployments_patch` | `EXEC` | `archiveDeploymentsId, environmentsId, organizationsId` | Updates an existing ArchiveDeployment. Labels can modified but most of the other fields are not modifiable. |
