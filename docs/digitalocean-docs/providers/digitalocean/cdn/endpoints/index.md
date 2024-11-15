---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - cdn
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.cdn.endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="cdn_get_endpoint" /> | `SELECT` | <CopyableCode code="cdn_id" /> | To show information about an existing CDN endpoint, send a GET request to `/v2/cdn/endpoints/$ENDPOINT_ID`. |
| <CopyableCode code="cdn_list_endpoints" /> | `SELECT` | <CopyableCode code="" /> | To list all of the CDN endpoints available on your account, send a GET request to `/v2/cdn/endpoints`. |
| <CopyableCode code="cdn_create_endpoint" /> | `INSERT` | <CopyableCode code="data__origin" /> | To create a new CDN endpoint, send a POST request to `/v2/cdn/endpoints`. The origin attribute must be set to the fully qualified domain name (FQDN) of a DigitalOcean Space. Optionally, the TTL may be configured by setting the `ttl` attribute. A custom subdomain may be configured by specifying the `custom_domain` and `certificate_id` attributes. |
| <CopyableCode code="cdn_delete_endpoint" /> | `DELETE` | <CopyableCode code="cdn_id" /> | To delete a specific CDN endpoint, send a DELETE request to `/v2/cdn/endpoints/$ENDPOINT_ID`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
| <CopyableCode code="cdn_purge_cache" /> | `EXEC` | <CopyableCode code="cdn_id, data__files" /> | To purge cached content from a CDN endpoint, send a DELETE request to `/v2/cdn/endpoints/$ENDPOINT_ID/cache`. The body of the request should include a `files` attribute containing a list of cached file paths to be purged. A path may be for a single file or may contain a wildcard (`*`) to recursively purge all files under a directory. When only a wildcard is provided, all cached files will be purged. There is a rate limit of 50 files per 20 seconds that can be purged. CDN endpoints have a rate limit of 5 requests per 10 seconds. Purging files using a wildcard path counts as a single request against the API's rate limit. Two identical purge requests cannot be sent at the same time. |
| <CopyableCode code="cdn_update_endpoints" /> | `EXEC` | <CopyableCode code="cdn_id" /> | To update the TTL, certificate ID, or the FQDN of the custom subdomain for an existing CDN endpoint, send a PUT request to `/v2/cdn/endpoints/$ENDPOINT_ID`. |

## `SELECT` examples

To list all of the CDN endpoints available on your account, send a GET request to `/v2/cdn/endpoints`.


```sql
SELECT
column_anon
FROM digitalocean.cdn.endpoints
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoints</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.cdn.endpoints (
data__origin,
data__ttl,
data__certificate_id,
data__custom_domain
)
SELECT 
'{{ origin }}',
'{{ ttl }}',
'{{ certificate_id }}',
'{{ custom_domain }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.cdn.endpoints (
data__origin
)
SELECT 
'{{ origin }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: endpoints
  props:
    - name: data__origin
      value: string
    - name: origin
      value: string
    - name: ttl
      value: integer
    - name: certificate_id
      value: string
    - name: custom_domain
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.cdn.endpoints
WHERE cdn_id = '{{ cdn_id }}';
```
