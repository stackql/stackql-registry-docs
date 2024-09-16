---
title: instances_network_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_network_interface
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

Creates, updates, deletes, gets or lists a <code>instances_network_interface</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_network_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_network_interface" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update_network_interface" /> | `UPDATE` | <CopyableCode code="instance, networkInterface, project, zone" /> | Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics. |

## `UPDATE` example

Updates a <code>instances_network_interface</code> resource.

```sql
/*+ update */
UPDATE google.compute.instances_network_interface
SET 
network = '{{ network }}',
subnetwork = '{{ subnetwork }}',
networkIP = '{{ networkIP }}',
ipv6Address = '{{ ipv6Address }}',
internalIpv6PrefixLength = '{{ internalIpv6PrefixLength }}',
name = '{{ name }}',
accessConfigs = '{{ accessConfigs }}',
ipv6AccessConfigs = '{{ ipv6AccessConfigs }}',
aliasIpRanges = '{{ aliasIpRanges }}',
fingerprint = '{{ fingerprint }}',
stackType = '{{ stackType }}',
ipv6AccessType = '{{ ipv6AccessType }}',
queueCount = '{{ queueCount }}',
nicType = '{{ nicType }}',
networkAttachment = '{{ networkAttachment }}'
WHERE 
instance = '{{ instance }}'
AND networkInterface = '{{ networkInterface }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
