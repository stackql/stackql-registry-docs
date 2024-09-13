
---
title: instances_shielded_instance_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_shielded_instance_config
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

Creates, updates, deletes or gets an <code>instances_shielded_instance_config</code> resource or lists <code>instances_shielded_instance_config</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_shielded_instance_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_shielded_instance_config" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update_shielded_instance_config" /> | `UPDATE` | <CopyableCode code="instance, project, zone" /> | Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |

## `UPDATE` example

Updates a instances_shielded_instance_config only if the necessary resources are available.

```sql
UPDATE google.compute.instances_shielded_instance_config
SET 
enableSecureBoot = true|false,
enableVtpm = true|false,
enableIntegrityMonitoring = true|false
WHERE 
instance = '{{ instance }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```
