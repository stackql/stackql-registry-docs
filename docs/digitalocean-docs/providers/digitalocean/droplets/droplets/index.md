---
title: droplets
hide_title: false
hide_table_of_contents: false
keywords:
  - droplets
  - droplets
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

Creates, updates, deletes, gets or lists a <code>droplets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>droplets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.droplets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_get" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To show information about an individual Droplet, send a GET request to `/v2/droplets/$DROPLET_ID`. |
| <CopyableCode code="droplets_list" /> | `SELECT` | <CopyableCode code="" /> | To list all Droplets in your account, send a GET request to `/v2/droplets`. The response body will be a JSON object with a key of `droplets`. This will be set to an array containing objects each representing a Droplet. These will contain the standard Droplet attributes. ### Filtering Results by Tag It's possible to request filtered results by including certain query parameters. To only list Droplets assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/droplets?tag_name=$TAG_NAME`. ### GPU Droplets By default, only non-GPU Droplets are returned. To list only GPU Droplets, set the `type` query parameter to `gpus`. For example, `/v2/droplets?type=gpus`. |
| <CopyableCode code="droplets_create" /> | `INSERT` | <CopyableCode code="" /> | To create a new Droplet, send a POST request to `/v2/droplets` setting the required attributes. A Droplet will be created using the provided information. The response body will contain a JSON object with a key called `droplet`. The value will be an object containing the standard attributes for your new Droplet. The response code, 202 Accepted, does not indicate the success or failure of the operation, just that the request has been accepted for processing. The `actions` returned as part of the response's `links` object can be used to check the status of the Droplet create event. ### Create Multiple Droplets Creating multiple Droplets is very similar to creating a single Droplet. Instead of sending `name` as a string, send `names` as an array of strings. A Droplet will be created for each name you send using the associated information. Up to ten Droplets may be created this way at a time. Rather than returning a single Droplet, the response body will contain a JSON array with a key called `droplets`. This will be set to an array of JSON objects, each of which will contain the standard Droplet attributes. The response code, 202 Accepted, does not indicate the success or failure of any operation, just that the request has been accepted for processing. The array of `actions` returned as part of the response's `links` object can be used to check the status of each individual Droplet create event. |
| <CopyableCode code="droplets_destroy" /> | `DELETE` | <CopyableCode code="droplet_id" /> | To delete a Droplet, send a DELETE request to `/v2/droplets/$DROPLET_ID`. A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. |
| <CopyableCode code="droplets_destroy_by_tag" /> | `DELETE` | <CopyableCode code="tag_name" /> | To delete **all** Droplets assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your DELETE request. For example, `/v2/droplets?tag_name=$TAG_NAME`. A successful request will receive a 204 status code with no body in response. This indicates that the request was processed successfully. |
| <CopyableCode code="droplets_destroy_retry_with_associated_resources" /> | `EXEC` | <CopyableCode code="droplet_id" /> | If the status of a request to destroy a Droplet with its associated resources reported any errors, it can be retried by sending a POST request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/retry` endpoint. Only one destroy can be active at a time per Droplet. If a retry is issued while another destroy is in progress for the Droplet a 409 status code will be returned. A successful response will include a 202 response code and no content. |
| <CopyableCode code="droplets_destroy_with_associated_resources_dangerous" /> | `EXEC` | <CopyableCode code="X-Dangerous, droplet_id" /> | To destroy a Droplet along with all of its associated resources, send a DELETE request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/dangerous` endpoint. The headers of this request must include an `X-Dangerous` key set to `true`. To preview which resources will be destroyed, first query the Droplet's associated resources. This operation _can not_ be reverse and should be used with caution. A successful response will include a 202 response code and no content. Use the status endpoint to check on the success or failure of the destruction of the individual resources. |
| <CopyableCode code="droplets_destroy_with_associated_resources_selective" /> | `EXEC` | <CopyableCode code="droplet_id" /> | To destroy a Droplet along with a sub-set of its associated resources, send a DELETE request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/selective` endpoint. The JSON body of the request should include `reserved_ips`, `snapshots`, `volumes`, or `volume_snapshots` keys each set to an array of IDs for the associated resources to be destroyed. The IDs can be found by querying the Droplet's associated resources. Any associated resource not included in the request will remain and continue to accrue changes on your account. A successful response will include a 202 response code and no content. Use the status endpoint to check on the success or failure of the destruction of the individual resources. |

## `SELECT` examples

To list all Droplets in your account, send a GET request to `/v2/droplets`. The response body will be a JSON object with a key of `droplets`. This will be set to an array containing objects each representing a Droplet. These will contain the standard Droplet attributes. ### Filtering Results by Tag It's possible to request filtered results by including certain query parameters. To only list Droplets assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/droplets?tag_name=$TAG_NAME`. ### GPU Droplets By default, only non-GPU Droplets are returned. To list only GPU Droplets, set the `type` query parameter to `gpus`. For example, `/v2/droplets?type=gpus`.


```sql
SELECT
column_anon
FROM digitalocean.droplets.droplets
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>droplets</code> resource.

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
INSERT INTO digitalocean.droplets.droplets (
data__name,
data__region,
data__size,
data__image,
data__ssh_keys,
data__backups,
data__backup_policy,
data__ipv6,
data__monitoring,
data__tags,
data__user_data,
data__private_networking,
data__volumes,
data__vpc_uuid,
data__with_droplet_agent
)
SELECT 
'{{ name }}',
'{{ region }}',
'{{ size }}',
'{{ image }}',
'{{ ssh_keys }}',
'{{ backups }}',
'{{ backup_policy }}',
'{{ ipv6 }}',
'{{ monitoring }}',
'{{ tags }}',
'{{ user_data }}',
'{{ private_networking }}',
'{{ volumes }}',
'{{ vpc_uuid }}',
'{{ with_droplet_agent }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.droplets.droplets (
data__size,
data__image
)
SELECT 
'{{ size }}',
'{{ image }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: droplets
  props:
    - name: name
      value: string
    - name: region
      value: string
    - name: size
      value: string
    - name: image
      value: string
    - name: ssh_keys
      value: array
    - name: backups
      value: boolean
    - name: backup_policy
      props:
        - name: plan
          value: string
        - name: weekday
          value: string
        - name: hour
          value: integer
    - name: ipv6
      value: boolean
    - name: monitoring
      value: boolean
    - name: tags
      value: array
    - name: user_data
      value: string
    - name: private_networking
      value: boolean
    - name: volumes
      value: array
    - name: vpc_uuid
      value: string
    - name: with_droplet_agent
      value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>droplets</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.droplets.droplets
WHERE tag_name = '{{ tag_name }}';
```
