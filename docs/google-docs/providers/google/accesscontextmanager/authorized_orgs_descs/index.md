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
| `name` | `string` | Resource name for the `AuthorizedOrgsDesc`. Format: `accessPolicies/&#123;access_policy&#125;/authorizedOrgsDescs/&#123;authorized_orgs_desc&#125;`. The `authorized_orgs_desc` component must begin with a letter, followed by alphanumeric characters or `_`. After you create an `AuthorizedOrgsDesc`, you cannot change its `name`. |
| `authorizationDirection` | `string` | The direction of the authorization relationship between this organization and the organizations listed in the `orgs` field. The valid values for this field include the following: `AUTHORIZATION_DIRECTION_FROM`: Allows this organization to evaluate traffic in the organizations listed in the `orgs` field. `AUTHORIZATION_DIRECTION_TO`: Allows the organizations listed in the `orgs` field to evaluate the traffic in this organization. For the authorization relationship to take effect, all of the organizations must authorize and specify the appropriate relationship direction. For example, if organization A authorized organization B and C to evaluate its traffic, by specifying `AUTHORIZATION_DIRECTION_TO` as the authorization direction, organizations B and C must specify `AUTHORIZATION_DIRECTION_FROM` as the authorization direction in their `AuthorizedOrgsDesc` resource. |
| `authorizationType` | `string` | A granular control type for authorization levels. Valid value is `AUTHORIZATION_TYPE_TRUST`. |
| `orgs` | `array` | The list of organization ids in this AuthorizedOrgsDesc. Format: `organizations/` Example: `organizations/123456` |
| `assetType` | `string` | The asset type of this authorized orgs desc. Valid values are `ASSET_TYPE_DEVICE`, and `ASSET_TYPE_CREDENTIAL_STRENGTH`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accessPoliciesId, authorizedOrgsDescsId` | Gets an authorized orgs desc based on the resource name. |
| `list` | `SELECT` | `accessPoliciesId` | Lists all authorized orgs descs for an access policy. |
| `create` | `INSERT` | `accessPoliciesId` | Creates an authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. The name of this `AuthorizedOrgsDesc` will be assigned during creation. |
| `delete` | `DELETE` | `accessPoliciesId, authorizedOrgsDescsId` | Deletes an authorized orgs desc based on the resource name. The long-running operation from this RPC has a successful status after the authorized orgs desc is removed from long-lasting storage. |
| `_list` | `EXEC` | `accessPoliciesId` | Lists all authorized orgs descs for an access policy. |
| `patch` | `EXEC` | `accessPoliciesId, authorizedOrgsDescsId` | Updates an authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. Only the organization list in `AuthorizedOrgsDesc` can be updated. The name, authorization_type, asset_type and authorization_direction cannot be updated. |
