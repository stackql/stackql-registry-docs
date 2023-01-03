---
title: resource_record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_record_sets
  - dns
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
<tr><td><b>Name</b></td><td><code>resource_record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dns.resource_record_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | For example, www.example.com. |
| `signatureRrdatas` | `array` | As defined in RFC 4034 (section 3.2). |
| `ttl` | `integer` | Number of seconds that this ResourceRecordSet can be cached by resolvers. |
| `type` | `string` | The identifier of a supported record type. See the list of Supported DNS record types. |
| `kind` | `string` |  |
| `routingPolicy` | `object` | A RRSetRoutingPolicy represents ResourceRecordSet data that is returned dynamically with the response varying based on configured properties such as geolocation or by weighted random selection. |
| `rrdatas` | `array` | As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `resourceRecordSets_get` | `SELECT` | `managedZone, name, project, type` | Fetches the representation of an existing ResourceRecordSet. |
| `resourceRecordSets_list` | `SELECT` | `managedZone, project` | Enumerates ResourceRecordSets that you have created but not yet deleted. |
| `resourceRecordSets_create` | `INSERT` | `managedZone, project` | Creates a new ResourceRecordSet. |
| `resourceRecordSets_delete` | `DELETE` | `managedZone, name, project, type` | Deletes a previously created ResourceRecordSet. |
| `resourceRecordSets_patch` | `EXEC` | `managedZone, name, project, type` | Applies a partial update to an existing ResourceRecordSet. |
