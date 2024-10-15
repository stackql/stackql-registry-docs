---
title: required_aml_fs_subnets_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - required_aml_fs_subnets_sizes
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>required_aml_fs_subnets_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>required_aml_fs_subnets_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.required_aml_fs_subnets_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="filesystemSubnetSize" /> | `integer` | The number of available IP addresses that are required for the AML file system. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the number of available IP addresses needed for the AML file system information provided. |

## `SELECT` examples

Get the number of available IP addresses needed for the AML file system information provided.


```sql
SELECT
filesystemSubnetSize
FROM azure.storage_cache.required_aml_fs_subnets_sizes
WHERE subscriptionId = '{{ subscriptionId }}';
```