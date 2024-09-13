
---
title: routers_router_status
hide_title: false
hide_table_of_contents: false
keywords:
  - routers_router_status
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

Creates, updates, deletes or gets an <code>routers_router_status</code> resource or lists <code>routers_router_status</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routers_router_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.routers_router_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Type of resource. |
| <CopyableCode code="result" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_router_status" /> | `SELECT` | <CopyableCode code="project, region, router" /> | Retrieves runtime information of the specified router. |

## `SELECT` examples

Retrieves runtime information of the specified router.

```sql
SELECT
kind,
result
FROM google.compute.routers_router_status
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND router = '{{ router }}'; 
```
