---
title: dns_record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_record_sets
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
<tr><td><b>Name</b></td><td><code>dns_record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicenetworking.dns_record_sets</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `services_dnsRecordSets_add` | `INSERT` | `servicesId` | Service producers can use this method to add DNS record sets to private DNS zones in the shared producer host project. |
| `services_dnsRecordSets_remove` | `DELETE` | `servicesId` | Service producers can use this method to remove DNS record sets from private DNS zones in the shared producer host project. |
| `services_dnsRecordSets_update` | `EXEC` | `servicesId` | Service producers can use this method to update DNS record sets from private DNS zones in the shared producer host project. |
