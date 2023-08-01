---
title: access_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - access_levels
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
<tr><td><b>Name</b></td><td><code>access_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accesscontextmanager.access_levels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name for the `AccessLevel`. Format: `accessPolicies/&#123;access_policy&#125;/accessLevels/&#123;access_level&#125;`. The `access_level` component must begin with a letter, followed by alphanumeric characters or `_`. Its maximum length is 50 characters. After you create an `AccessLevel`, you cannot change its `name`. |
| `description` | `string` | Description of the `AccessLevel` and its use. Does not affect behavior. |
| `basic` | `object` | `BasicLevel` is an `AccessLevel` using a set of recommended features. |
| `custom` | `object` | `CustomLevel` is an `AccessLevel` using the Cloud Common Expression Language to represent the necessary conditions for the level to apply to a request. See CEL spec at: https://github.com/google/cel-spec |
| `title` | `string` | Human readable title. Must be unique within the Policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accessLevelsId, accessPoliciesId` | Gets an access level based on the resource name. |
| `list` | `SELECT` | `accessPoliciesId` | Lists all access levels for an access policy. |
| `create` | `INSERT` | `accessPoliciesId` | Creates an access level. The long-running operation from this RPC has a successful status after the access level propagates to long-lasting storage. If access levels contain errors, an error response is returned for the first error encountered. |
| `delete` | `DELETE` | `accessLevelsId, accessPoliciesId` | Deletes an access level based on the resource name. The long-running operation from this RPC has a successful status after the access level has been removed from long-lasting storage. |
| `patch` | `EXEC` | `accessLevelsId, accessPoliciesId` | Updates an access level. The long-running operation from this RPC has a successful status after the changes to the access level propagate to long-lasting storage. If access levels contain errors, an error response is returned for the first error encountered. |
| `replace_all` | `EXEC` | `accessPoliciesId` | Replaces all existing access levels in an access policy with the access levels provided. This is done atomically. The long-running operation from this RPC has a successful status after all replacements propagate to long-lasting storage. If the replacement contains errors, an error response is returned for the first error encountered. Upon error, the replacement is cancelled, and existing access levels are not affected. The Operation.response field contains ReplaceAccessLevelsResponse. Removing access levels contained in existing service perimeters result in an error. |
