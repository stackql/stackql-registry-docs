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
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
| `unreachable` | `array` | Locations that could not be reached. |
| `dnsAuthorizations` | `array` | A list of dns authorizations for the parent resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dnsAuthorizationsId, locationsId, projectsId` | Gets details of a single DnsAuthorization. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists DnsAuthorizations in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new DnsAuthorization in a given project and location. |
| `delete` | `DELETE` | `dnsAuthorizationsId, locationsId, projectsId` | Deletes a single DnsAuthorization. |
| `patch` | `EXEC` | `dnsAuthorizationsId, locationsId, projectsId` | Updates a DnsAuthorization. |
