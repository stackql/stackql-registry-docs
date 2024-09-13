---
title: storage_pool_types
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_pool_types
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

Creates, updates, deletes, gets or lists a <code>storage_pool_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_pool_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.storage_pool_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. |
| <CopyableCode code="description" /> | `string` | [Output Only] An optional description of this resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="deprecated" /> | `object` | Deprecation status for a public resource. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#storagePoolType for storage pool types. |
| <CopyableCode code="maxPoolProvisionedCapacityGb" /> | `string` | [Output Only] Maximum storage pool size in GB. |
| <CopyableCode code="maxPoolProvisionedIops" /> | `string` | [Output Only] Maximum provisioned IOPS. |
| <CopyableCode code="maxPoolProvisionedThroughput" /> | `string` | [Output Only] Maximum provisioned throughput. |
| <CopyableCode code="minPoolProvisionedCapacityGb" /> | `string` | [Output Only] Minimum storage pool size in GB. |
| <CopyableCode code="minPoolProvisionedIops" /> | `string` | [Output Only] Minimum provisioned IOPS. |
| <CopyableCode code="minPoolProvisionedThroughput" /> | `string` | [Output Only] Minimum provisioned throughput. |
| <CopyableCode code="minSizeGb" /> | `string` | [Deprecated] This field is deprecated. Use minPoolProvisionedCapacityGb instead. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="selfLinkWithId" /> | `string` | [Output Only] Server-defined URL for this resource with the resource id. |
| <CopyableCode code="supportedDiskTypes" /> | `array` | [Output Only] The list of disk types supported in this storage pool type. |
| <CopyableCode code="zone" /> | `string` | [Output Only] URL of the zone where the storage pool type resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of storage pool types. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, storagePoolType, zone" /> | Returns the specified storage pool type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | Retrieves a list of storage pool types available to the specified project. |

## `SELECT` examples

Retrieves an aggregated list of storage pool types. To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

```sql
SELECT
id,
name,
description,
creationTimestamp,
deprecated,
kind,
maxPoolProvisionedCapacityGb,
maxPoolProvisionedIops,
maxPoolProvisionedThroughput,
minPoolProvisionedCapacityGb,
minPoolProvisionedIops,
minPoolProvisionedThroughput,
minSizeGb,
selfLink,
selfLinkWithId,
supportedDiskTypes,
zone
FROM google.compute.storage_pool_types
WHERE project = '{{ project }}'; 
```
