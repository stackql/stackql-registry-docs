---
title: keys_ip_override
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_ip_override
  - recaptchaenterprise
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>keys_ip_override</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_ip_override</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.keys_ip_override" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_ip_override" /> | `INSERT` | <CopyableCode code="keysId, projectsId" /> | Adds an IP override to a key. The following restrictions hold: * The maximum number of IP overrides per key is 100. * For any conflict (such as IP already exists or IP part of an existing IP range), an error is returned. |
| <CopyableCode code="remove_ip_override" /> | `DELETE` | <CopyableCode code="keysId, projectsId" /> | Removes an IP override from a key. The following restrictions hold: * If the IP isn't found in an existing IP override, a `NOT_FOUND` error is returned. * If the IP is found in an existing IP override, but the override type does not match, a `NOT_FOUND` error is returned. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>keys_ip_override</code> resource.

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
INSERT INTO google.recaptchaenterprise.keys_ip_override (
keysId,
projectsId,
ipOverrideData
)
SELECT 
'{{ keysId }}',
'{{ projectsId }}',
'{{ ipOverrideData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: ipOverrideData
      value:
        - name: overrideType
          value: string
        - name: ip
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>keys_ip_override</code> resource.

```sql
/*+ delete */
DELETE FROM google.recaptchaenterprise.keys_ip_override
WHERE keysId = '{{ keysId }}'
AND projectsId = '{{ projectsId }}';
```
