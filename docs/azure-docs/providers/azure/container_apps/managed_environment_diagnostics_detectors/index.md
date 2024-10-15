---
title: managed_environment_diagnostics_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environment_diagnostics_detectors
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

Creates, updates, deletes, gets or lists a <code>managed_environment_diagnostics_detectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_environment_diagnostics_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.managed_environment_diagnostics_detectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Diagnostics resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="detectorName, environmentName, resourceGroupName, subscriptionId" /> | Get the diagnostics data for a Managed Environment used to host container apps. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Get the list of diagnostics for a Managed Environment used to host container apps. |

## `SELECT` examples

Get the list of diagnostics for a Managed Environment used to host container apps.


```sql
SELECT
properties
FROM azure.container_apps.managed_environment_diagnostics_detectors
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```