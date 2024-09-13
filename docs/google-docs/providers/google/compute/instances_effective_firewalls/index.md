
---
title: instances_effective_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_effective_firewalls
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

Creates, updates, deletes or gets an <code>instances_effective_firewall</code> resource or lists <code>instances_effective_firewalls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_effective_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_effective_firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="firewallPolicys" /> | `array` | Effective firewalls from firewall policies. |
| <CopyableCode code="firewalls" /> | `array` | Effective firewalls on the instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_effective_firewalls" /> | `SELECT` | <CopyableCode code="instance, networkInterface, project, zone" /> | Returns effective firewalls applied to an interface of the instance. |

## `SELECT` examples

Returns effective firewalls applied to an interface of the instance.

```sql
SELECT
firewallPolicys,
firewalls
FROM google.compute.instances_effective_firewalls
WHERE instance = '{{ instance }}'
AND networkInterface = '{{ networkInterface }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```
