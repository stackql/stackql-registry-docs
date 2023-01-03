---
title: domain_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_mappings
  - appengine
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
<tr><td><b>Name</b></td><td><code>domain_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.domain_mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Relative name of the domain serving the application. Example: example.com. |
| `name` | `string` | Full path to the DomainMapping resource in the API. Example: apps/myapp/domainMapping/example.com.@OutputOnly |
| `resourceRecords` | `array` | The resource records required to configure this domain mapping. These records must be added to the domain's DNS configuration in order to serve the application via this domain mapping.@OutputOnly |
| `sslSettings` | `object` | SSL configuration for a DomainMapping resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `apps_domainMappings_get` | `SELECT` | `appsId, domainMappingsId` | Gets the specified domain mapping. |
| `apps_domainMappings_list` | `SELECT` | `appsId` | Lists the domain mappings on an application. |
| `apps_domainMappings_create` | `INSERT` | `appsId` | Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see AuthorizedDomains.ListAuthorizedDomains. |
| `apps_domainMappings_delete` | `DELETE` | `appsId, domainMappingsId` | Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a DomainMapping resource. |
| `apps_domainMappings_patch` | `EXEC` | `appsId, domainMappingsId` | Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update certificate_id to point to an AuthorizedCertificate resource. A user must be authorized to administer the associated domain in order to update a DomainMapping resource. |
