---
title: buckets_storage_layout
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets_storage_layout
  - storage
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

Creates, updates, deletes, gets or lists a <code>buckets_storage_layout</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets_storage_layout</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.buckets_storage_layout" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bucket" /> | `string` | The name of the bucket. |
| <CopyableCode code="customPlacementConfig" /> | `object` | The bucket's custom placement configuration for Custom Dual Regions. |
| <CopyableCode code="hierarchicalNamespace" /> | `object` | The bucket's hierarchical namespace configuration. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For storage layout, this is always storage#storageLayout. |
| <CopyableCode code="location" /> | `string` | The location of the bucket. |
| <CopyableCode code="locationType" /> | `string` | The type of the bucket location. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_storage_layout" /> | `SELECT` | <CopyableCode code="bucket" /> | Returns the storage layout configuration for the specified bucket. Note that this operation requires storage.objects.list permission. |

## `SELECT` examples

Returns the storage layout configuration for the specified bucket. Note that this operation requires storage.objects.list permission.

```sql
SELECT
bucket,
customPlacementConfig,
hierarchicalNamespace,
kind,
location,
locationType
FROM google.storage.buckets_storage_layout
WHERE bucket = '{{ bucket }}';
```
