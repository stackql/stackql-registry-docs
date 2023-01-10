---
title: authorized_orgs_descs
hide_title: false
hide_table_of_contents: false
keywords:
  - authorized_orgs_descs
  - accesscontextmanager
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
<tr><td><b>Name</b></td><td><code>authorized_orgs_descs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accesscontextmanager.authorized_orgs_descs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by [RFC 3986 Section 2.3](https://tools.ietf.org/html/rfc3986#section-2.3)). Should not be specified by the client during creation. Example: "accessPolicies/122256/authorizedOrgs/b3-BhcX_Ud5N" |
| `orgs` | `array` | The list of organization ids in this AuthorizedOrgsDesc. |
| `assetType` | `string` | The asset type of this authorized orgs desc. e.g. device, credential strength. |
| `authorizationDirection` | `string` | Authorization direction of this authorization relationship. i.e. Whether to allow specified orgs to evaluate this org's traffic, or allow specified orgs' traffic to be evaluated by this org. Orgs specified as `AUTHORIZATION_DIRECTION_TO` in this AuthorizedOrgsDesc[com.google.identity.accesscontextmanager.v1.AuthorizedOrgsDesc] must also specify this org as the `AUTHORIZATION_DIRECTION_FROM` in their own AuthorizedOrgsDesc in order for this relationship to take effect. Orgs specified as `AUTHORIZATION_DIRECTION_FROM` in this AuthorizedOrgsDesc[com.google.identity.accesscontextmanager.v1.AuthorizedOrgsDesc] must also specify this org as the `AUTHORIZATION_DIRECTION_TO` in their own AuthorizedOrgsDesc in order for this relationship to take effect. |
| `authorizationType` | `string` | The authorization type of this authorized orgs desc. e.g.authorization, troubleshooting or logging. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accessPolicies_authorizedOrgsDescs_get` | `SELECT` | `accessPoliciesId, authorizedOrgsDescsId` | Gets a authorized orgs desc based on the resource name. |
| `accessPolicies_authorizedOrgsDescs_list` | `SELECT` | `accessPoliciesId` | Lists all authorized orgs descs for an access policy. |
| `accessPolicies_authorizedOrgsDescs_create` | `INSERT` | `accessPoliciesId` | Creates a authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. The name of this `AuthorizedOrgsDesc` will be assigned during creation. |
| `accessPolicies_authorizedOrgsDescs_delete` | `DELETE` | `accessPoliciesId, authorizedOrgsDescsId` | Deletes a authorized orgs desc based on the resource name. The long-running operation from this RPC has a successful status after the authorized orgs desc is removed from long-lasting storage. |
| `accessPolicies_authorizedOrgsDescs_patch` | `EXEC` | `accessPoliciesId, authorizedOrgsDescsId` | Updates a authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. Only the organization list in `AuthorizedOrgsDesc` can be updated. The name, authorization_type, asset_type and authorization_direction cannot be updated. |
