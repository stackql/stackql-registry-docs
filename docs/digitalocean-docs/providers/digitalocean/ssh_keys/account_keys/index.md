---
title: account_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - account_keys
  - ssh_keys
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

Creates, updates, deletes, gets or lists a <code>account_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.ssh_keys.account_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="ssh_keys_get" /> | `SELECT` | <CopyableCode code="ssh_key_identifier" /> | To get information about a key, send a GET request to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`. The response will be a JSON object with the key `ssh_key` and value an ssh_key object which contains the standard ssh_key attributes. |
| <CopyableCode code="ssh_keys_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the keys in your account, send a GET request to `/v2/account/keys`. The response will be a JSON object with a key set to `ssh_keys`. The value of this will be an array of ssh_key objects, each of which contains the standard ssh_key attributes. |
| <CopyableCode code="ssh_keys_create" /> | `INSERT` | <CopyableCode code="data__name, data__public_key" /> | To add a new SSH public key to your DigitalOcean account, send a POST request to `/v2/account/keys`. Set the `name` attribute to the name you wish to use and the `public_key` attribute to the full public key you are adding. |
| <CopyableCode code="ssh_keys_delete" /> | `DELETE` | <CopyableCode code="ssh_key_identifier" /> | To destroy a public SSH key that you have in your account, send a DELETE request to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`. A 204 status will be returned, indicating that the action was successful and that the response body is empty. |
| <CopyableCode code="ssh_keys_update" /> | `EXEC` | <CopyableCode code="ssh_key_identifier" /> | To update the name of an SSH key, send a PUT request to either `/v2/account/keys/$SSH_KEY_ID` or `/v2/account/keys/$SSH_KEY_FINGERPRINT`. Set the `name` attribute to the new name you want to use. |

## `SELECT` examples

To list all of the keys in your account, send a GET request to `/v2/account/keys`. The response will be a JSON object with a key set to `ssh_keys`. The value of this will be an array of ssh_key objects, each of which contains the standard ssh_key attributes.


```sql
SELECT
column_anon
FROM digitalocean.ssh_keys.account_keys
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>account_keys</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.ssh_keys.account_keys (
data__public_key,
data__name
)
SELECT 
'{{ public_key }}',
'{{ name }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: account_keys
  props:
    - name: data__name
      value: string
    - name: data__public_key
      value: string
    - name: public_key
      value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>account_keys</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.ssh_keys.account_keys
WHERE ssh_key_identifier = '{{ ssh_key_identifier }}';
```
