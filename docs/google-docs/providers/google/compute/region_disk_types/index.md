---
title: region_disk_types
hide_title: false
hide_table_of_contents: false
keywords:
  - region_disk_types
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

Creates, updates, deletes, gets or lists a <code>region_disk_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_disk_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_disk_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. |
| <CopyableCode code="description" /> | `string` | [Output Only] An optional description of this resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="defaultDiskSizeGb" /> | `string` | [Output Only] Server-defined default disk size in GB. |
| <CopyableCode code="deprecated" /> | `object` | Deprecation status for a public resource. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#diskType for disk types. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the disk type resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="validDiskSize" /> | `string` | [Output Only] An optional textual description of the valid disk size, such as "10GB-10TB". |
| <CopyableCode code="zone" /> | `string` | [Output Only] URL of the zone where the disk type resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskType, project, region" /> | Returns the specified regional disk type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves a list of regional disk types available to the specified project. |

## `SELECT` examples

Retrieves a list of regional disk types available to the specified project.

```sql
SELECT
id,
name,
description,
creationTimestamp,
defaultDiskSizeGb,
deprecated,
kind,
region,
selfLink,
validDiskSize,
zone
FROM google.compute.region_disk_types
WHERE project = '{{ project }}'
AND region = '{{ region }}';
```
