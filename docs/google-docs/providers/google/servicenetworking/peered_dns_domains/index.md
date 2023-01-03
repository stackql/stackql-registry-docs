---
title: peered_dns_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - peered_dns_domains
  - servicenetworking
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
<tr><td><b>Name</b></td><td><code>peered_dns_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicenetworking.peered_dns_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | User assigned name for this resource. Must be unique within the consumer network. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes. |
| `dnsSuffix` | `string` | The DNS domain name suffix e.g. `example.com.`. Cloud DNS requires that a DNS suffix ends with a trailing dot. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `services_projects_global_networks_peeredDnsDomains_list` | `SELECT` | `networksId, projectsId, servicesId` | Lists peered DNS domains for a connection. |
| `services_projects_global_networks_peeredDnsDomains_create` | `INSERT` | `networksId, projectsId, servicesId` | Creates a peered DNS domain which sends requests for records in given namespace originating in the service producer VPC network to the consumer VPC network to be resolved. |
| `services_projects_global_networks_peeredDnsDomains_delete` | `DELETE` | `networksId, peeredDnsDomainsId, projectsId, servicesId` | Deletes a peered DNS domain. |
