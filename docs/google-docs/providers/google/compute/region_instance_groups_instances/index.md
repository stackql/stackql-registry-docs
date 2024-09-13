---
title: region_instance_groups_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_groups_instances
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

Creates, updates, deletes, gets or lists a <code>region_instance_groups_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_instance_groups_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_instance_groups_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="instance" /> | `string` | [Output Only] The URL of the instance. |
| <CopyableCode code="namedPorts" /> | `array` | [Output Only] The named ports that belong to this instance group. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of the instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_instances" /> | `SELECT` | <CopyableCode code="instanceGroup, project, region" /> | Lists the instances in the specified instance group and displays information about the named ports. Depending on the specified options, this method can list all instances or only the instances that are running. The orderBy query parameter is not supported. |

## `SELECT` examples

Lists the instances in the specified instance group and displays information about the named ports. Depending on the specified options, this method can list all instances or only the instances that are running. The orderBy query parameter is not supported.

```sql
SELECT
instance,
namedPorts,
status
FROM google.compute.region_instance_groups_instances
WHERE instanceGroup = '{{ instanceGroup }}'
AND project = '{{ project }}'
AND region = '{{ region }}'; 
```
