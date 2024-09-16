---
title: instances_access_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_access_config
  - compute
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

Creates, updates, deletes, gets or lists a <code>instances_access_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_access_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_access_config" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_access_config" /> | `INSERT` | <CopyableCode code="instance, networkInterface, project, zone" /> | Adds an access config to an instance's network interface. |
| <CopyableCode code="delete_access_config" /> | `DELETE` | <CopyableCode code="accessConfig, instance, networkInterface, project, zone" /> | Deletes an access config from an instance's network interface. |
| <CopyableCode code="update_access_config" /> | `UPDATE` | <CopyableCode code="instance, networkInterface, project, zone" /> | Updates the specified access config from an instance's network interface with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances_access_config</code> resource.

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
INSERT INTO google.compute.instances_access_config (
instance,
networkInterface,
project,
zone,
type,
name,
natIP,
externalIpv6,
externalIpv6PrefixLength,
setPublicPtr,
publicPtrDomainName,
networkTier,
securityPolicy
)
SELECT 
'{{ instance }}',
'{{ networkInterface }}',
'{{ project }}',
'{{ zone }}',
'{{ type }}',
'{{ name }}',
'{{ natIP }}',
'{{ externalIpv6 }}',
'{{ externalIpv6PrefixLength }}',
true|false,
'{{ publicPtrDomainName }}',
'{{ networkTier }}',
'{{ securityPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: type
      value: '{{ type }}'
    - name: name
      value: '{{ name }}'
    - name: natIP
      value: '{{ natIP }}'
    - name: externalIpv6
      value: '{{ externalIpv6 }}'
    - name: externalIpv6PrefixLength
      value: '{{ externalIpv6PrefixLength }}'
    - name: setPublicPtr
      value: '{{ setPublicPtr }}'
    - name: publicPtrDomainName
      value: '{{ publicPtrDomainName }}'
    - name: networkTier
      value: '{{ networkTier }}'
    - name: securityPolicy
      value: '{{ securityPolicy }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instances_access_config</code> resource.

```sql
/*+ update */
UPDATE google.compute.instances_access_config
SET 
type = '{{ type }}',
name = '{{ name }}',
natIP = '{{ natIP }}',
externalIpv6 = '{{ externalIpv6 }}',
externalIpv6PrefixLength = '{{ externalIpv6PrefixLength }}',
setPublicPtr = true|false,
publicPtrDomainName = '{{ publicPtrDomainName }}',
networkTier = '{{ networkTier }}',
securityPolicy = '{{ securityPolicy }}'
WHERE 
instance = '{{ instance }}'
AND networkInterface = '{{ networkInterface }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```

## `DELETE` example

Deletes the specified <code>instances_access_config</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.instances_access_config
WHERE accessConfig = '{{ accessConfig }}'
AND instance = '{{ instance }}'
AND networkInterface = '{{ networkInterface }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
