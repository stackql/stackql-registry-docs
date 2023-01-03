---
title: public_advertised_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - public_advertised_prefixes
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
<tr><td><b>Name</b></td><td><code>public_advertised_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.public_advertised_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource type. The server generates this identifier. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `fingerprint` | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a new PublicAdvertisedPrefix. An up-to-date fingerprint must be provided in order to update the PublicAdvertisedPrefix, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a PublicAdvertisedPrefix. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `dnsVerificationIp` | `string` | The IPv4 address to be used for reverse DNS verification. |
| `ipCidrRange` | `string` | The IPv4 address range, in CIDR format, represented by this public advertised prefix. |
| `status` | `string` | The status of the public advertised prefix. Possible values include: - `INITIAL`: RPKI validation is complete. - `PTR_CONFIGURED`: User has configured the PTR. - `VALIDATED`: Reverse DNS lookup is successful. - `REVERSE_DNS_LOOKUP_FAILED`: Reverse DNS lookup failed. - `PREFIX_CONFIGURATION_IN_PROGRESS`: The prefix is being configured. - `PREFIX_CONFIGURATION_COMPLETE`: The prefix is fully configured. - `PREFIX_REMOVAL_IN_PROGRESS`: The prefix is being removed.  |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `sharedSecret` | `string` | [Output Only] The shared secret to be used for reverse DNS verification. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#publicAdvertisedPrefix for public advertised prefixes. |
| `publicDelegatedPrefixs` | `array` | [Output Only] The list of public delegated prefixes that exist for this public advertised prefix. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `publicAdvertisedPrefixes_get` | `SELECT` | `project, publicAdvertisedPrefix` | Returns the specified PublicAdvertisedPrefix resource. |
| `publicAdvertisedPrefixes_list` | `SELECT` | `project` | Lists the PublicAdvertisedPrefixes for a project. |
| `publicAdvertisedPrefixes_insert` | `INSERT` | `project` | Creates a PublicAdvertisedPrefix in the specified project using the parameters that are included in the request. |
| `publicAdvertisedPrefixes_delete` | `DELETE` | `project, publicAdvertisedPrefix` | Deletes the specified PublicAdvertisedPrefix |
| `publicAdvertisedPrefixes_patch` | `EXEC` | `project, publicAdvertisedPrefix` | Patches the specified Router resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
