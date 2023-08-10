---
title: ekm_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - ekm_connections
  - cloudkms
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
<tr><td><b>Name</b></td><td><code>ekm_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.ekm_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for the EkmConnection in the format `projects/*/locations/*/ekmConnections/*`. |
| `keyManagementMode` | `string` | Optional. Describes who can perform control plane operations on the EKM. If unset, this defaults to MANUAL. |
| `serviceResolvers` | `array` | A list of ServiceResolvers where the EKM can be reached. There should be one ServiceResolver per EKM replica. Currently, only a single ServiceResolver is supported. |
| `createTime` | `string` | Output only. The time at which the EkmConnection was created. |
| `cryptoSpacePath` | `string` | Optional. Identifies the EKM Crypto Space that this EkmConnection maps to. Note: This field is required if KeyManagementMode is CLOUD_KMS. |
| `etag` | `string` | Optional. Etag of the currently stored EkmConnection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ekmConnectionsId, locationsId, projectsId` | Returns metadata for a given EkmConnection. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists EkmConnections. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new EkmConnection in a given Project and Location. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists EkmConnections. |
| `patch` | `EXEC` | `ekmConnectionsId, locationsId, projectsId` | Updates an EkmConnection's metadata. |
| `verify_connectivity` | `EXEC` | `ekmConnectionsId, locationsId, projectsId` | Verifies that Cloud KMS can successfully connect to the external key manager specified by an EkmConnection. If there is an error connecting to the EKM, this method returns a FAILED_PRECONDITION status containing structured information as described at https://cloud.google.com/kms/docs/reference/ekm_errors. |
