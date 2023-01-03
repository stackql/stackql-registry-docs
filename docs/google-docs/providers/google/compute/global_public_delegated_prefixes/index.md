---
title: global_public_delegated_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - global_public_delegated_prefixes
  - compute
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
<tr><td><b>Name</b></td><td><code>global_public_delegated_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.global_public_delegated_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `region` | `string` | [Output Only] URL of the region where the public delegated prefix resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `parentPrefix` | `string` | The URL of parent prefix. Either PublicAdvertisedPrefix or PublicDelegatedPrefix. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a new PublicDelegatedPrefix. An up-to-date fingerprint must be provided in order to update the PublicDelegatedPrefix, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a PublicDelegatedPrefix. |
| `ipCidrRange` | `string` | The IPv4 address range, in CIDR format, represented by this public delegated prefix. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#publicDelegatedPrefix for public delegated prefixes. |
| `status` | `string` | [Output Only] The status of the public delegated prefix, which can be one of following values: - `INITIALIZING` The public delegated prefix is being initialized and addresses cannot be created yet. - `READY_TO_ANNOUNCE` The public delegated prefix is a live migration prefix and is active. - `ANNOUNCED` The public delegated prefix is active. - `DELETING` The public delegated prefix is being deprovsioned.  |
| `isLiveMigration` | `boolean` | If true, the prefix will be live migrated. |
| `publicDelegatedSubPrefixs` | `array` | The list of sub public delegated prefixes that exist for this public delegated prefix. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `globalPublicDelegatedPrefixes_get` | `SELECT` | `project, publicDelegatedPrefix` | Returns the specified global PublicDelegatedPrefix resource. |
| `globalPublicDelegatedPrefixes_list` | `SELECT` | `project` | Lists the global PublicDelegatedPrefixes for a project. |
| `globalPublicDelegatedPrefixes_insert` | `INSERT` | `project` | Creates a global PublicDelegatedPrefix in the specified project using the parameters that are included in the request. |
| `globalPublicDelegatedPrefixes_delete` | `DELETE` | `project, publicDelegatedPrefix` | Deletes the specified global PublicDelegatedPrefix. |
| `globalPublicDelegatedPrefixes_patch` | `EXEC` | `project, publicDelegatedPrefix` | Patches the specified global PublicDelegatedPrefix resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
