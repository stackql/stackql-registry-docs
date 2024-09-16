---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - dns
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dns.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the resource; defined by the server (output only). |
| <CopyableCode code="name" /> | `string` | User-assigned name for this policy. |
| <CopyableCode code="description" /> | `string` | A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the policy's function. |
| <CopyableCode code="alternativeNameServerConfig" /> | `object` |  |
| <CopyableCode code="enableInboundForwarding" /> | `boolean` | Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When enabled, a virtual IP address is allocated from each of the subnetworks that are bound to this policy. |
| <CopyableCode code="enableLogging" /> | `boolean` | Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set. |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="networks" /> | `array` | List of network names specifying networks to which this policy is applied. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policy, project" /> | Fetches the representation of an existing Policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Enumerates all Policies associated with a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="project" /> | Creates a new Policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policy, project" /> | Deletes a previously created Policy. Fails if the policy is still being referenced by a network. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="policy, project" /> | Applies a partial update to an existing Policy. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="policy, project" /> | Updates an existing Policy. |

## `SELECT` examples

Enumerates all Policies associated with a project.

```sql
SELECT
id,
name,
description,
alternativeNameServerConfig,
enableInboundForwarding,
enableLogging,
kind,
networks
FROM google.dns.policies
WHERE project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies</code> resource.

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
INSERT INTO google.dns.policies (
project,
id,
name,
enableInboundForwarding,
description,
networks,
alternativeNameServerConfig,
enableLogging,
kind
)
SELECT 
'{{ project }}',
'{{ id }}',
'{{ name }}',
true|false,
'{{ description }}',
'{{ networks }}',
'{{ alternativeNameServerConfig }}',
true|false,
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: '{{ id }}'
    - name: name
      value: '{{ name }}'
    - name: enableInboundForwarding
      value: '{{ enableInboundForwarding }}'
    - name: description
      value: '{{ description }}'
    - name: networks
      value: '{{ networks }}'
    - name: alternativeNameServerConfig
      value: '{{ alternativeNameServerConfig }}'
    - name: enableLogging
      value: '{{ enableLogging }}'
    - name: kind
      value: '{{ kind }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>policies</code> resource.

```sql
/*+ update */
UPDATE google.dns.policies
SET 
id = '{{ id }}',
name = '{{ name }}',
enableInboundForwarding = true|false,
description = '{{ description }}',
networks = '{{ networks }}',
alternativeNameServerConfig = '{{ alternativeNameServerConfig }}',
enableLogging = true|false,
kind = '{{ kind }}'
WHERE 
policy = '{{ policy }}'
AND project = '{{ project }}';
```

## `UPDATE` example

Replaces all fields in the specified <code>policies</code> resource.

```sql
/*+ update */
REPLACE google.dns.policies
SET 
id = '{{ id }}',
name = '{{ name }}',
enableInboundForwarding = true|false,
description = '{{ description }}',
networks = '{{ networks }}',
alternativeNameServerConfig = '{{ alternativeNameServerConfig }}',
enableLogging = true|false,
kind = '{{ kind }}'
WHERE 
policy = '{{ policy }}'
AND project = '{{ project }}';
```

## `DELETE` example

Deletes the specified <code>policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.dns.policies
WHERE policy = '{{ policy }}'
AND project = '{{ project }}';
```
