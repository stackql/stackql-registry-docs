---
title: machine_types
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_types
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

Creates, updates, deletes, gets or lists a <code>machine_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>machine_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.machine_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. |
| <CopyableCode code="description" /> | `string` | [Output Only] An optional textual description of the resource. |
| <CopyableCode code="accelerators" /> | `array` | [Output Only] A list of accelerator configurations assigned to this machine type. |
| <CopyableCode code="architecture" /> | `string` | [Output Only] The architecture of the machine type. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="deprecated" /> | `object` | Deprecation status for a public resource. |
| <CopyableCode code="guestCpus" /> | `integer` | [Output Only] The number of virtual CPUs that are available to the instance. |
| <CopyableCode code="imageSpaceGb" /> | `integer` | [Deprecated] This property is deprecated and will never be populated with any relevant values. |
| <CopyableCode code="isSharedCpu" /> | `boolean` | [Output Only] Whether this machine type has a shared CPU. See Shared-core machine types for more information. |
| <CopyableCode code="kind" /> | `string` | [Output Only] The type of the resource. Always compute#machineType for machine types. |
| <CopyableCode code="maximumPersistentDisks" /> | `integer` | [Output Only] Maximum persistent disks allowed. |
| <CopyableCode code="maximumPersistentDisksSizeGb" /> | `string` | [Output Only] Maximum total persistent disks size (GB) allowed. |
| <CopyableCode code="memoryMb" /> | `integer` | [Output Only] The amount of physical memory available to the instance, defined in MB. |
| <CopyableCode code="scratchDisks" /> | `array` | [Output Only] A list of extended scratch disks assigned to the instance. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="zone" /> | `string` | [Output Only] The name of the zone where the machine type resides, such as us-central1-a. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of machine types. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineType, project, zone" /> | Returns the specified machine type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | Retrieves a list of machine types available to the specified project. |

## `SELECT` examples

Retrieves an aggregated list of machine types. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
accelerators,
architecture,
creationTimestamp,
deprecated,
guestCpus,
imageSpaceGb,
isSharedCpu,
kind,
maximumPersistentDisks,
maximumPersistentDisksSizeGb,
memoryMb,
scratchDisks,
selfLink,
zone
FROM google.compute.machine_types
WHERE project = '{{ project }}';
```
