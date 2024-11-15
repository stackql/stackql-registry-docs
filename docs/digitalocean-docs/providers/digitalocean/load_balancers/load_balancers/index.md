---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - load_balancers
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

Creates, updates, deletes, gets or lists a <code>load_balancers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.load_balancers.load_balancers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="load_balancers_get" /> | `SELECT` | <CopyableCode code="lb_id" /> | To show information about a load balancer instance, send a GET request to `/v2/load_balancers/$LOAD_BALANCER_ID`. |
| <CopyableCode code="load_balancers_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the load balancer instances on your account, send a GET request to `/v2/load_balancers`. |
| <CopyableCode code="load_balancers_create" /> | `INSERT` | <CopyableCode code="" /> | To create a new load balancer instance, send a POST request to `/v2/load_balancers`. You can specify the Droplets that will sit behind the load balancer using one of two methods: * Set `droplet_ids` to a list of specific Droplet IDs. * Set `tag` to the name of a tag. All Droplets with this tag applied will be assigned to the load balancer. Additional Droplets will be automatically assigned as they are tagged. These methods are mutually exclusive. |
| <CopyableCode code="load_balancers_delete" /> | `DELETE` | <CopyableCode code="lb_id" /> | To delete a load balancer instance, disassociating any Droplets assigned to it and removing it from your account, send a DELETE request to `/v2/load_balancers/$LOAD_BALANCER_ID`. A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. |
| <CopyableCode code="load_balancers_update" /> | `EXEC` | <CopyableCode code="lb_id" /> | To update a load balancer's settings, send a PUT request to `/v2/load_balancers/$LOAD_BALANCER_ID`. The request should contain a full representation of the load balancer including existing attributes. It may contain _one of_ the `droplets_ids` or `tag` attributes as they are mutually exclusive. **Note that any attribute that is not provided will be reset to its default value.** |

## `SELECT` examples

To list all of the load balancer instances on your account, send a GET request to `/v2/load_balancers`.


```sql
SELECT
column_anon
FROM digitalocean.load_balancers.load_balancers
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>load_balancers</code> resource.

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
INSERT INTO digitalocean.load_balancers.load_balancers (
data__droplet_ids,
data__region,
data__name,
data__project_id,
data__size_unit,
data__size,
data__algorithm,
data__forwarding_rules,
data__health_check,
data__sticky_sessions,
data__redirect_http_to_https,
data__enable_proxy_protocol,
data__enable_backend_keepalive,
data__http_idle_timeout_seconds,
data__vpc_uuid,
data__disable_lets_encrypt_dns_records,
data__firewall,
data__network
)
SELECT 
'{{ droplet_ids }}',
'{{ region }}',
'{{ name }}',
'{{ project_id }}',
'{{ size_unit }}',
'{{ size }}',
'{{ algorithm }}',
'{{ forwarding_rules }}',
'{{ health_check }}',
'{{ sticky_sessions }}',
'{{ redirect_http_to_https }}',
'{{ enable_proxy_protocol }}',
'{{ enable_backend_keepalive }}',
'{{ http_idle_timeout_seconds }}',
'{{ vpc_uuid }}',
'{{ disable_lets_encrypt_dns_records }}',
'{{ firewall }}',
'{{ network }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.load_balancers.load_balancers (
data__forwarding_rules
)
SELECT 
'{{ forwarding_rules }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: load_balancers
  props:
    - name: droplet_ids
      value: array
    - name: region
      value: string
    - name: name
      value: string
    - name: project_id
      value: string
    - name: size_unit
      value: integer
    - name: size
      value: string
    - name: algorithm
      value: string
    - name: forwarding_rules
      value: array
      props:
        - name: entry_protocol
          value: string
        - name: entry_port
          value: integer
        - name: target_protocol
          value: string
        - name: target_port
          value: integer
        - name: certificate_id
          value: string
        - name: tls_passthrough
          value: boolean
    - name: health_check
      props:
        - name: protocol
          value: string
        - name: port
          value: integer
        - name: path
          value: string
        - name: check_interval_seconds
          value: integer
        - name: response_timeout_seconds
          value: integer
        - name: unhealthy_threshold
          value: integer
        - name: healthy_threshold
          value: integer
    - name: sticky_sessions
      props:
        - name: type
          value: string
        - name: cookie_name
          value: string
        - name: cookie_ttl_seconds
          value: integer
    - name: redirect_http_to_https
      value: boolean
    - name: enable_proxy_protocol
      value: boolean
    - name: enable_backend_keepalive
      value: boolean
    - name: http_idle_timeout_seconds
      value: integer
    - name: vpc_uuid
      value: string
    - name: disable_lets_encrypt_dns_records
      value: boolean
    - name: firewall
      props:
        - name: deny
          value: array
        - name: allow
          value: array
    - name: network
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>load_balancers</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.load_balancers.load_balancers
WHERE lb_id = '{{ lb_id }}';
```
