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
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peered_dns_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicenetworking.peered_dns_domains</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `networksId, projectsId, servicesId` | Lists peered DNS domains for a connection. |
| `create` | `INSERT` | `networksId, projectsId, servicesId` | Creates a peered DNS domain which sends requests for records in given namespace originating in the service producer VPC network to the consumer VPC network to be resolved. |
| `delete` | `DELETE` | `networksId, peeredDnsDomainsId, projectsId, servicesId` | Deletes a peered DNS domain. |
