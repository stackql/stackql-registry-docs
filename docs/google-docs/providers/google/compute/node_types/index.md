---
title: node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - node_types
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

Creates, updates, deletes, gets or lists a <code>node_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.node_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. |
| <CopyableCode code="description" /> | `string` | [Output Only] An optional textual description of the resource. |
| <CopyableCode code="cpuPlatform" /> | `string` | [Output Only] The CPU platform used by this node type. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="deprecated" /> | `object` | Deprecation status for a public resource. |
| <CopyableCode code="guestCpus" /> | `integer` | [Output Only] The number of virtual CPUs that are available to the node type. |
| <CopyableCode code="kind" /> | `string` | [Output Only] The type of the resource. Always compute#nodeType for node types. |
| <CopyableCode code="localSsdGb" /> | `integer` | [Output Only] Local SSD available to the node type, defined in GB. |
| <CopyableCode code="memoryMb" /> | `integer` | [Output Only] The amount of physical memory available to the node type, defined in MB. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="zone" /> | `string` | [Output Only] The name of the zone where the node type resides, such as us-central1-a. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of node types. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="nodeType, project, zone" /> | Returns the specified node type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | Retrieves a list of node types available to the specified project. |

## `SELECT` examples

Retrieves an aggregated list of node types. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
cpuPlatform,
creationTimestamp,
deprecated,
guestCpus,
kind,
localSsdGb,
memoryMb,
selfLink,
zone
FROM google.compute.node_types
WHERE project = '{{ project }}'; 
```
