---
title: available_workload_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - available_workload_profiles
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>available_workload_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_workload_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.available_workload_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Region of the workload profile. |
| <CopyableCode code="properties" /> | `object` | Revision resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get all available workload profiles for a location. |

## `SELECT` examples

Get all available workload profiles for a location.


```sql
SELECT
location,
properties
FROM azure.container_apps.available_workload_profiles
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```