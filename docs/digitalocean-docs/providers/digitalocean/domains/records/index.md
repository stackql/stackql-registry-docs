---
title: records
hide_title: false
hide_table_of_contents: false
keywords:
  - records
  - domains
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.domains.records</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique identifier for each domain record. |
| `name` | `string` | The host name, alias, or service being defined by the record. |
| `priority` | `integer` | The priority for SRV and MX records. |
| `data` | `string` | Variable data depending on record type. For example, the "data" value for an A record would be the IPv4 address to which the domain will be mapped. For a CAA record, it would contain the domain name of the CA being granted permission to issue certificates. |
| `type` | `string` | The type of the DNS record. For example: A, CNAME, TXT, ... |
| `flags` | `integer` | An unsigned integer between 0-255 used for CAA records. |
| `ttl` | `integer` | This value is the time to live for the record, in seconds. This defines the time frame that clients can cache queried information before a refresh should be requested. |
| `tag` | `string` | The parameter tag for CAA records. Valid values are "issue", "issuewild", or "iodef" |
| `weight` | `integer` | The weight for SRV records. |
| `port` | `integer` | The port for SRV records. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_record` | `SELECT` | `domain_name, domain_record_id` | To retrieve a specific domain record, send a GET request to `/v2/domains/$DOMAIN_NAME/records/$RECORD_ID`. |
| `list_records` | `SELECT` | `domain_name` | To get a listing of all records configured for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records`.<br />The list of records returned can be filtered by using the `name` and `type` query parameters. For example, to only include A records for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records?type=A`. `name` must be a fully qualified record name. For example, to only include records matching `sub.example.com`, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. Both name and type may be used together.<br /><br /> |
| `create_record` | `INSERT` | `domain_name` | To create a new record to a domain, send a POST request to<br />`/v2/domains/$DOMAIN_NAME/records`.<br /><br />The request must include all of the required fields for the domain record type<br />being added.<br /><br />See the [attribute table](#tag/Domain-Records) for details regarding record<br />types and their respective required attributes.<br /> |
| `delete_record` | `DELETE` | `domain_name, domain_record_id` | To delete a record for a domain, send a DELETE request to<br />`/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`.<br /><br />The record will be deleted and the response status will be a 204. This<br />indicates a successful request with no body returned.<br /> |
| `_get_record` | `EXEC` | `domain_name, domain_record_id` | To retrieve a specific domain record, send a GET request to `/v2/domains/$DOMAIN_NAME/records/$RECORD_ID`. |
| `_list_records` | `EXEC` | `domain_name` | To get a listing of all records configured for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records`.<br />The list of records returned can be filtered by using the `name` and `type` query parameters. For example, to only include A records for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records?type=A`. `name` must be a fully qualified record name. For example, to only include records matching `sub.example.com`, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. Both name and type may be used together.<br /><br /> |
| `patch_record` | `EXEC` | `domain_name, domain_record_id, data__type` | To update an existing record, send a PATCH request to<br />`/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`. Any attribute valid for<br />the record type can be set to a new value for the record.<br /><br />See the [attribute table](#tag/Domain-Records) for details regarding record<br />types and their respective attributes.<br /> |
| `update_record` | `EXEC` | `domain_name, domain_record_id, data__type` | To update an existing record, send a PUT request to<br />`/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`. Any attribute valid for<br />the record type can be set to a new value for the record.<br /><br />See the [attribute table](#tag/Domain-Records) for details regarding record<br />types and their respective attributes.<br /> |
