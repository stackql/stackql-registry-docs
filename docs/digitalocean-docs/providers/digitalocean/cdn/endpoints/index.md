---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - cdn
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.cdn.endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference a CDN endpoint. |
| <CopyableCode code="certificate_id" /> | `string` | The ID of a DigitalOcean managed TLS certificate used for SSL when a custom subdomain is provided. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the CDN endpoint was created. |
| <CopyableCode code="custom_domain" /> | `string` | The fully qualified domain name (FQDN) of the custom subdomain used with the CDN endpoint. |
| <CopyableCode code="endpoint" /> | `string` | The fully qualified domain name (FQDN) from which the CDN-backed content is served. |
| <CopyableCode code="origin" /> | `string` | The fully qualified domain name (FQDN) for the origin server which provides the content for the CDN. This is currently restricted to a Space. |
| <CopyableCode code="ttl" /> | `integer` | The amount of time the content is cached by the CDN's edge servers in seconds. TTL must be one of 60, 600, 3600, 86400, or 604800. Defaults to 3600 (one hour) when excluded. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_endpoint" /> | `SELECT` | <CopyableCode code="cdn_id" /> | To show information about an existing CDN endpoint, send a GET request to `/v2/cdn/endpoints/$ENDPOINT_ID`. |
| <CopyableCode code="list_endpoints" /> | `SELECT` |  | To list all of the CDN endpoints available on your account, send a GET request to `/v2/cdn/endpoints`. |
| <CopyableCode code="create_endpoint" /> | `INSERT` | <CopyableCode code="data__origin" /> | To create a new CDN endpoint, send a POST request to `/v2/cdn/endpoints`. The<br />origin attribute must be set to the fully qualified domain name (FQDN) of a<br />DigitalOcean Space. Optionally, the TTL may be configured by setting the `ttl`<br />attribute.<br /><br />A custom subdomain may be configured by specifying the `custom_domain` and<br />`certificate_id` attributes.<br /> |
| <CopyableCode code="delete_endpoint" /> | `DELETE` | <CopyableCode code="cdn_id" /> | To delete a specific CDN endpoint, send a DELETE request to<br />`/v2/cdn/endpoints/$ENDPOINT_ID`.<br /><br />A status of 204 will be given. This indicates that the request was processed<br />successfully, but that no response body is needed.<br /> |
| <CopyableCode code="_get_endpoint" /> | `EXEC` | <CopyableCode code="cdn_id" /> | To show information about an existing CDN endpoint, send a GET request to `/v2/cdn/endpoints/$ENDPOINT_ID`. |
| <CopyableCode code="_list_endpoints" /> | `EXEC` |  | To list all of the CDN endpoints available on your account, send a GET request to `/v2/cdn/endpoints`. |
| <CopyableCode code="purge_cache" /> | `EXEC` | <CopyableCode code="cdn_id, data__files" /> | To purge cached content from a CDN endpoint, send a DELETE request to<br />`/v2/cdn/endpoints/$ENDPOINT_ID/cache`. The body of the request should include<br />a `files` attribute containing a list of cached file paths to be purged. A<br />path may be for a single file or may contain a wildcard (`*`) to recursively<br />purge all files under a directory. When only a wildcard is provided, all<br />cached files will be purged. There is a rate limit of 50 files per 20 seconds <br />that can be purged.<br /> |
| <CopyableCode code="update_endpoints" /> | `EXEC` | <CopyableCode code="cdn_id" /> | To update the TTL, certificate ID, or the FQDN of the custom subdomain for<br />an existing CDN endpoint, send a PUT request to<br />`/v2/cdn/endpoints/$ENDPOINT_ID`.<br /> |
