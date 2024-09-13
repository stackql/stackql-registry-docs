---
title: instances_display_device
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_display_device
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

Creates, updates, deletes, gets or lists a <code>instances_display_device</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_display_device</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_display_device" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update_display_device" /> | `UPDATE` | <CopyableCode code="instance, project, zone" /> | Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |

## `UPDATE` example

Updates a <code>instances_display_device</code> resource.

```sql
/*+ update */
UPDATE google.compute.instances_display_device
SET 
enableDisplay = true|false
WHERE 
instance = '{{ instance }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
