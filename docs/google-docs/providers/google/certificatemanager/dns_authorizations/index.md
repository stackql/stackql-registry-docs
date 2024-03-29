---
title: dns_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_authorizations
  - certificatemanager
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
<tr><td><b>Name</b></td><td><code>dns_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.dns_authorizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the dns authorization. DnsAuthorization names must be unique globally and match pattern `projects/*/locations/*/dnsAuthorizations/*`. |
| `description` | `string` | One or more paragraphs of text description of a DnsAuthorization. |
| `updateTime` | `string` | Output only. The last update timestamp of a DnsAuthorization. |
| `createTime` | `string` | Output only. The creation timestamp of a DnsAuthorization. |
| `dnsResourceRecord` | `object` | The structure describing the DNS Resource Record that needs to be added to DNS configuration for the authorization to be usable by certificate. |
| `domain` | `string` | Required. Immutable. A domain that is being authorized. A DnsAuthorization resource covers a single domain and its wildcard, e.g. authorization for `example.com` can be used to issue certificates for `example.com` and `*.example.com`. |
| `labels` | `object` | Set of labels associated with a DnsAuthorization. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dnsAuthorizationsId, locationsId, projectsId` | Gets details of a single DnsAuthorization. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists DnsAuthorizations in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new DnsAuthorization in a given project and location. |
| `delete` | `DELETE` | `dnsAuthorizationsId, locationsId, projectsId` | Deletes a single DnsAuthorization. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists DnsAuthorizations in a given project and location. |
| `patch` | `EXEC` | `dnsAuthorizationsId, locationsId, projectsId` | Updates a DnsAuthorization. |
