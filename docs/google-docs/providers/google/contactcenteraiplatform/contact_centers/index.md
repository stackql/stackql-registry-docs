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
| `labels` | `object` | Labels as key value pairs |
| `displayName` | `string` | Required. A user friendly name for the ContactCenter. |
| `createTime` | `string` | Output only. [Output only] Create time stamp |
| `updateTime` | `string` | Output only. [Output only] Update time stamp |
| `ccaipManagedUsers` | `boolean` | Optional. Whether to enable users to be created in the CCAIP-instance concurrently to having users in Cloud identity |
| `state` | `string` | Output only. The state of this contact center. |
| `userEmail` | `string` | Optional. Email address of the first admin users. |
| `customerDomainPrefix` | `string` | Required. Immutable. At least 2 and max 16 char long, must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). |
| `instanceConfig` | `object` | Message storing the instance configuration. |
| `uris` | `object` | Message storing the URIs of the ContactCenter. |
| `samlParams` | `object` | Message storing SAML params to enable Google as IDP. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_contactCenters_get` | `SELECT` | `contactCentersId, locationsId, projectsId` | Gets details of a single ContactCenter. |
| `projects_locations_contactCenters_list` | `SELECT` | `locationsId, projectsId` | Lists ContactCenters in a given project and location. |
| `projects_locations_contactCenters_create` | `INSERT` | `locationsId, projectsId` | Creates a new ContactCenter in a given project and location. |
| `projects_locations_contactCenters_delete` | `DELETE` | `contactCentersId, locationsId, projectsId` | Deletes a single ContactCenter. |
| `projects_locations_contactCenters_patch` | `EXEC` | `contactCentersId, locationsId, projectsId` | Updates the parameters of a single ContactCenter. |
