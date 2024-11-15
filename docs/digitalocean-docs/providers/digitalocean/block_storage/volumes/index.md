---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - block_storage
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.block_storage.volumes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="volumes_get" /> | `SELECT` | <CopyableCode code="volume_id" /> | To show information about a block storage volume, send a GET request to `/v2/volumes/$VOLUME_ID`. |
| <CopyableCode code="volumes_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the block storage volumes available on your account, send a GET request to `/v2/volumes`. ## Filtering Results ### By Region The `region` may be provided as query parameter in order to restrict results to volumes available in a specific region. For example: `/v2/volumes?region=nyc1` ### By Name It is also possible to list volumes on your account that match a specified name. To do so, send a GET request with the volume's name as a query parameter to `/v2/volumes?name=$VOLUME_NAME`. **Note:** You can only create one volume per region with the same name. ### By Name and Region It is also possible to retrieve information about a block storage volume by name. To do so, send a GET request with the volume's name and the region slug for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`. |
| <CopyableCode code="volumes_create" /> | `INSERT` | <CopyableCode code="" /> | To create a new volume, send a POST request to `/v2/volumes`. Optionally, a `filesystem_type` attribute may be provided in order to automatically format the volume's filesystem. Pre-formatted volumes are automatically mounted when attached to Ubuntu, Debian, Fedora, Fedora Atomic, and CentOS Droplets created on or after April 26, 2018. Attaching pre-formatted volumes to Droplets without support for auto-mounting is not recommended. |
| <CopyableCode code="volumes_delete" /> | `DELETE` | <CopyableCode code="volume_id" /> | To delete a block storage volume, destroying all data and removing it from your account, send a DELETE request to `/v2/volumes/$VOLUME_ID`. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |
| <CopyableCode code="volumes_delete_by_name" /> | `DELETE` | <CopyableCode code="" /> | Block storage volumes may also be deleted by name by sending a DELETE request with the volume's **name** and the **region slug** for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`. No response body will be sent back, but the response code will indicate success. Specifically, the response code will be a 204, which means that the action was successful with no returned body data. |

## `SELECT` examples

To list all of the block storage volumes available on your account, send a GET request to `/v2/volumes`. ## Filtering Results ### By Region The `region` may be provided as query parameter in order to restrict results to volumes available in a specific region. For example: `/v2/volumes?region=nyc1` ### By Name It is also possible to list volumes on your account that match a specified name. To do so, send a GET request with the volume's name as a query parameter to `/v2/volumes?name=$VOLUME_NAME`. **Note:** You can only create one volume per region with the same name. ### By Name and Region It is also possible to retrieve information about a block storage volume by name. To do so, send a GET request with the volume's name and the region slug for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.


```sql
SELECT
column_anon
FROM digitalocean.block_storage.volumes
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volumes</code> resource.

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
INSERT INTO digitalocean.block_storage.volumes (
data__name,
data__description,
data__size_gigabytes,
data__tags,
data__snapshot_id,
data__filesystem_type,
data__region,
data__filesystem_label
)
SELECT 
'{{ name }}',
'{{ description }}',
'{{ size_gigabytes }}',
'{{ tags }}',
'{{ snapshot_id }}',
'{{ filesystem_type }}',
'{{ region }}',
'{{ filesystem_label }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.block_storage.volumes (
data__name,
data__size_gigabytes,
data__region
)
SELECT 
'{{ name }}',
'{{ size_gigabytes }}',
'{{ region }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: volumes
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: size_gigabytes
      value: integer
    - name: tags
      value: array
    - name: snapshot_id
      value: string
    - name: filesystem_type
      value: string
    - name: region
      value: string
    - name: filesystem_label
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>volumes</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.block_storage.volumes
WHERE  = '{{  }}';
```
