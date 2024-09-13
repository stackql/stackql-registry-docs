---
title: networks_effective_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - networks_effective_firewalls
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

Creates, updates, deletes, gets or lists a <code>networks_effective_firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks_effective_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.networks_effective_firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="firewallPolicys" /> | `array` | Effective firewalls from firewall policy. |
| <CopyableCode code="firewalls" /> | `array` | Effective firewalls on the network. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_effective_firewalls" /> | `SELECT` | <CopyableCode code="network, project" /> | Returns the effective firewalls on a given network. |

## `SELECT` examples

Returns the effective firewalls on a given network.

```sql
SELECT
firewallPolicys,
firewalls
FROM google.compute.networks_effective_firewalls
WHERE network = '{{ network }}'
AND project = '{{ project }}'; 
```
