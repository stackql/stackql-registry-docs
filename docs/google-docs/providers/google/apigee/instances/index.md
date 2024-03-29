---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Resource ID of the instance. Values must match the regular expression `^a-z&#123;0,30&#125;[a-z\d]$`. |
| `description` | `string` | Optional. Description of the instance. |
| `ipRange` | `string` | Optional. Comma-separated list of CIDR blocks of length 22 and/or 28 used to create the Apigee instance. Providing CIDR ranges is optional. You can provide just /22 or /28 or both (or neither). Ranges you provide should be freely available as part of a larger named range you have allocated to the Service Networking peering. If this parameter is not provided, Apigee automatically requests an available /22 and /28 CIDR block from Service Networking. Use the /22 CIDR block for configuring your firewall needs to allow traffic from Apigee. Input formats: `a.b.c.d/22` or `e.f.g.h/28` or `a.b.c.d/22,e.f.g.h/28` |
| `peeringCidrRange` | `string` | Optional. Size of the CIDR block range that will be reserved by the instance. PAID organizations support `SLASH_16` to `SLASH_20` and defaults to `SLASH_16`. Evaluation organizations support only `SLASH_23`. |
| `host` | `string` | Output only. Internal hostname or IP address of the Apigee endpoint used by clients to connect to the service. |
| `state` | `string` | Output only. State of the instance. Values other than `ACTIVE` means the resource is not ready to use. |
| `consumerAcceptList` | `array` | Optional. Customer accept list represents the list of projects (id/number) on customer side that can privately connect to the service attachment. It is an optional field which the customers can provide during the instance creation. By default, the customer project associated with the Apigee organization will be included to the list. |
| `displayName` | `string` | Optional. Display name for the instance. |
| `runtimeVersion` | `string` | Output only. Version of the runtime system running in the instance. The runtime system is the set of components that serve the API Proxy traffic in your Environments. |
| `lastModifiedAt` | `string` | Output only. Time the instance was last modified in milliseconds since epoch. |
| `createdAt` | `string` | Output only. Time the instance was created in milliseconds since epoch. |
| `port` | `string` | Output only. Port number of the exposed Apigee endpoint. |
| `diskEncryptionKeyName` | `string` | Customer Managed Encryption Key (CMEK) used for disk and volume encryption. Required for Apigee paid subscriptions only. Use the following format: `projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)` |
| `location` | `string` | Required. Compute Engine location where the instance resides. |
| `serviceAttachment` | `string` | Output only. Resource name of the service attachment created for the instance in the format: `projects/*/regions/*/serviceAttachments/*` Apigee customers can privately forward traffic to this service attachment using the PSC endpoints. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_instances_get` | `SELECT` | `instancesId, organizationsId` | Gets the details for an Apigee runtime instance. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_list` | `SELECT` | `organizationsId` | Lists all Apigee runtime instances for the organization. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_create` | `INSERT` | `organizationsId` | Creates an Apigee runtime instance. The instance is accessible from the authorized network configured on the organization. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_delete` | `DELETE` | `instancesId, organizationsId` | Deletes an Apigee runtime instance. The instance stops serving requests and the runtime data is deleted. **Note:** Not supported for Apigee hybrid. |
| `_organizations_instances_list` | `EXEC` | `organizationsId` | Lists all Apigee runtime instances for the organization. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_patch` | `EXEC` | `instancesId, organizationsId` | Updates an Apigee runtime instance. You can update the fields described in NodeConfig. No other fields will be updated. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_report_status` | `EXEC` | `instancesId, organizationsId` | Reports the latest status for a runtime instance. |
