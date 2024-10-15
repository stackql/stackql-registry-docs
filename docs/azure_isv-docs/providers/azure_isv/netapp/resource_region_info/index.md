---
title: resource_region_info
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_region_info
  - netapp
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

Creates, updates, deletes, gets or lists a <code>resource_region_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_region_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.resource_region_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Provides region specific information. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Provides storage to network proximity and logical zone mapping information. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Provides region specific information. |

## `SELECT` examples

Provides storage to network proximity and logical zone mapping information.


```sql
SELECT
properties
FROM azure_isv.netapp.resource_region_info
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```