---
title: vm_insights_onboarding_status
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_insights_onboarding_status
  - monitor
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

Creates, updates, deletes, gets or lists a <code>vm_insights_onboarding_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vm_insights_onboarding_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.vm_insights_onboarding_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
| <CopyableCode code="type" /> | `string` | Azure resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Retrieves the VM Insights onboarding status for the specified resource or resource scope. |

## `SELECT` examples

Retrieves the VM Insights onboarding status for the specified resource or resource scope.


```sql
SELECT
id,
name,
properties,
type
FROM azure.monitor.vm_insights_onboarding_status
WHERE resourceUri = '{{ resourceUri }}';
```