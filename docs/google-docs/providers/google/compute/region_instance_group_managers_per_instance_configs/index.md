
---
title: region_instance_group_managers_per_instance_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_group_managers_per_instance_configs
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

Creates, updates, deletes or gets an <code>region_instance_group_managers_per_instance_config</code> resource or lists <code>region_instance_group_managers_per_instance_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_instance_group_managers_per_instance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_instance_group_managers_per_instance_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of a per-instance configuration and its corresponding instance. Serves as a merge key during UpdatePerInstanceConfigs operations, that is, if a per-instance configuration with the same name exists then it will be updated, otherwise a new one will be created for the VM instance with the same name. An attempt to create a per-instance configconfiguration for a VM instance that either doesn't exist or is not part of the group will result in an error. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this per-instance config. This field can be used in optimistic locking. It is ignored when inserting a per-instance config. An up-to-date fingerprint must be provided in order to update an existing per-instance configuration or the field needs to be unset. |
| <CopyableCode code="preservedState" /> | `object` | Preserved state for a given instance. |
| <CopyableCode code="status" /> | `string` | The status of applying this per-instance configuration on the corresponding managed instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_per_instance_configs" /> | `SELECT` | <CopyableCode code="instanceGroupManager, project, region" /> | Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported. |
| <CopyableCode code="delete_per_instance_configs" /> | `DELETE` | <CopyableCode code="instanceGroupManager, project, region" /> | Deletes selected per-instance configurations for the managed instance group. |
| <CopyableCode code="update_per_instance_configs" /> | `UPDATE` | <CopyableCode code="instanceGroupManager, project, region" /> | Inserts or updates per-instance configurations for the managed instance group. perInstanceConfig.name serves as a key used to distinguish whether to perform insert or patch. |

## `SELECT` examples

Lists all of the per-instance configurations defined for the managed instance group. The orderBy query parameter is not supported.

```sql
SELECT
name,
fingerprint,
preservedState,
status
FROM google.compute.region_instance_group_managers_per_instance_configs
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `UPDATE` example

Updates a region_instance_group_managers_per_instance_config only if the necessary resources are available.

```sql
UPDATE google.compute.region_instance_group_managers_per_instance_configs
SET 
perInstanceConfigs = '{{ perInstanceConfigs }}'
WHERE 
instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified region_instance_group_managers_per_instance_config resource.

```sql
DELETE FROM google.compute.region_instance_group_managers_per_instance_configs
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
