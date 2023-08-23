---
title: contact_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_centers
  - contactcenteraiplatform
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
<tr><td><b>Name</b></td><td><code>contact_centers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenteraiplatform.contact_centers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | name of resource |
| `instanceConfig` | `object` | Message storing the instance configuration. |
| `createTime` | `string` | Output only. [Output only] Create time stamp |
| `kmsKey` | `string` | Immutable. The KMS key name to encrypt the user input (`ContactCenter`). |
| `updateTime` | `string` | Output only. [Output only] Update time stamp |
| `customerDomainPrefix` | `string` | Required. Immutable. At least 2 and max 16 char long, must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). |
| `state` | `string` | Output only. The state of this contact center. |
| `displayName` | `string` | Required. A user friendly name for the ContactCenter. |
| `userEmail` | `string` | Optional. Email address of the first admin user. |
| `adminUser` | `object` | Message storing info about the first admin user. Next ID: 3 |
| `labels` | `object` | Labels as key value pairs |
| `samlParams` | `object` | Message storing SAML params to enable Google as IDP. |
| `ccaipManagedUsers` | `boolean` | Optional. Whether to enable users to be created in the CCAIP-instance concurrently to having users in Cloud identity |
| `uris` | `object` | Message storing the URIs of the ContactCenter. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `contactCentersId, locationsId, projectsId` | Gets details of a single ContactCenter. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ContactCenters in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ContactCenter in a given project and location. |
| `delete` | `DELETE` | `contactCentersId, locationsId, projectsId` | Deletes a single ContactCenter. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists ContactCenters in a given project and location. |
| `patch` | `EXEC` | `contactCentersId, locationsId, projectsId` | Updates the parameters of a single ContactCenter. |
