
---
title: routers_nat_mapping_info
hide_title: false
hide_table_of_contents: false
keywords:
  - routers_nat_mapping_info
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

Creates, updates, deletes or gets an <code>routers_nat_mapping_info</code> resource or lists <code>routers_nat_mapping_info</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routers_nat_mapping_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.routers_nat_mapping_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="instanceName" /> | `string` | Name of the VM instance which the endpoint belongs to |
| <CopyableCode code="interfaceNatMappings" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_nat_mapping_info" /> | `SELECT` | <CopyableCode code="project, region, router" /> | Retrieves runtime Nat mapping information of VM endpoints. |

## `SELECT` examples

Retrieves runtime Nat mapping information of VM endpoints.

```sql
SELECT
instanceName,
interfaceNatMappings
FROM google.compute.routers_nat_mapping_info
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND router = '{{ router }}'; 
```
